"""
03_process_ai_metr.py - AI Task Evaluation Data Cleaning & Time Horizon Reconstruction

1. Ingests raw runs from time-horizon-1-1_runs.jsonl (and time-horizon-1-0).
2. Applies explicit exclusion criteria, logging every excluded row in metadata/exclusion_log.csv:
   - missing task duration
   - impossible duration (<= 0)
   - duplicate exact run
   - missing model identity
3. Fits weighted logistic regression for each model:
   logit(P(Y_i=1)) = alpha_m + beta_m * log2(T_i)
4. Solves for 50% and 80% time horizons:
   log2(T_50) = -alpha_m / beta_m
   log2(T_80) = (logit(0.8) - alpha_m) / beta_m
5. Computes confidence intervals via:
   - bootstrap by task
   - bootstrap by run
   - clustered bootstrap by task family
6. Saves:
   - data/processed/ai_clean_runs.csv
   - data/processed/ai_model_horizons.csv
   - outputs/tables/ai_model_horizons.csv
   - outputs/tables/ai_model_horizon_confidence_intervals.csv
"""

import os
import sys
import json
import csv
import math
import numpy as np
import pandas as pd
import statsmodels.api as sm
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw" / "ai_metr"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS_TABLES = PROJECT_ROOT / "outputs" / "tables"
METADATA_DIR = PROJECT_ROOT / "metadata"

EXCLUSION_LOG = METADATA_DIR / "exclusion_log.csv"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
OUTPUTS_TABLES.mkdir(parents=True, exist_ok=True)

def log_exclusion(row_id, source_file, orig_id, reason):
    import datetime
    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    fields = ["row_id", "domain", "source_file", "original_identifier", "exclusion_reason", "status_label", "timestamp_utc"]
    row = {
        "row_id": str(row_id),
        "domain": "ai_metr",
        "source_file": source_file,
        "original_identifier": str(orig_id),
        "exclusion_reason": reason,
        "status_label": "excluded",
        "timestamp_utc": now_utc
    }
    file_exists = os.path.exists(EXCLUSION_LOG) and os.path.getsize(EXCLUSION_LOG) > 0
    with open(EXCLUSION_LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if not file_exists:
            w.writeheader()
        w.writerow(row)

def load_and_clean_runs():
    print("[1/4] Loading and cleaning METR runs...")
    target_file = DATA_RAW / "time-horizon-1-1_runs.jsonl"
    if not target_file.exists():
        target_file = DATA_RAW / "time-horizon-1-0_runs.jsonl"
        
    print(f" -> Using primary source: {target_file.name}")
    
    clean_rows = []
    seen_runs = set()
    
    with open(target_file, "r", encoding="utf-8") as f:
        for line_idx, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception as e:
                log_exclusion(line_idx, target_file.name, line_idx, f"malformed JSON: {str(e)}")
                continue
                
            model = r.get("model") or r.get("model_name")
            alias = r.get("alias") or r.get("model_alias") or model
            task_id = r.get("task_id") or r.get("task")
            task_family = r.get("task_family") or r.get("family") or "default_family"
            dur = r.get("human_minutes") or r.get("human_duration_minutes")
            score_bin = r.get("score_binarized")
            score_cont = r.get("score_cont") if "score_cont" in r else r.get("score")
            weight = r.get("invsqrt_task_weight") or r.get("weight") or 1.0
            run_id = r.get("run_id") or f"{model}_{task_id}_{line_idx}"
            eval_date = str(r.get("evaluation_date") or r.get("date") or "")[:10]
            
            # Exclusions
            if not model:
                log_exclusion(line_idx, target_file.name, run_id, "missing model identity")
                continue
            if dur is None:
                log_exclusion(line_idx, target_file.name, run_id, "missing task duration")
                continue
            try:
                dur = float(dur)
            except ValueError:
                log_exclusion(line_idx, target_file.name, run_id, f"non-numeric duration: {dur}")
                continue
            if dur <= 0:
                log_exclusion(line_idx, target_file.name, run_id, f"impossible duration (<= 0): {dur}")
                continue
            if score_bin is None and score_cont is None:
                log_exclusion(line_idx, target_file.name, run_id, "missing task score")
                continue
                
            # Duplicate check
            exact_key = (model, task_id, dur, score_bin, run_id)
            if exact_key in seen_runs:
                log_exclusion(line_idx, target_file.name, run_id, "duplicate exact run")
                continue
            seen_runs.add(exact_key)
            
            # Binarize score if needed
            if score_bin is None:
                score_bin = 1 if float(score_cont) >= 0.5 else 0
            else:
                score_bin = int(score_bin)
                
            clean_rows.append({
                "model": model,
                "model_alias": alias,
                "task_id": str(task_id),
                "task_family": str(task_family),
                "human_minutes": dur,
                "log_human_minutes": math.log2(dur),
                "score_binarized": score_bin,
                "score_cont": float(score_cont) if score_cont is not None else float(score_bin),
                "weight": float(weight),
                "evaluation_date": eval_date,
                "source_file": target_file.name
            })
            
    df_clean = pd.DataFrame(clean_rows)
    out_clean_csv = DATA_PROCESSED / "ai_clean_runs.csv"
    df_clean.to_csv(out_clean_csv, index=False)
    print(f" -> Retained {len(df_clean)} valid runs across {df_clean['model'].nunique()} models.")
    print(f" -> Saved to {out_clean_csv}")
    return df_clean

def fit_logistic_horizon(df_sub):
    """Fits weighted logistic regression and solves for T_50 and T_80."""
    X = sm.add_constant(df_sub['log_human_minutes'])
    y = df_sub['score_binarized']
    w = df_sub['weight']
    
    # Check if there is variation in y
    if len(np.unique(y)) < 2:
        return None
        
    try:
        glm_binom = sm.GLM(y, X, family=sm.families.Binomial(), freq_weights=w)
        res = glm_binom.fit(disp=False, maxiter=100)
        alpha, beta = res.params.iloc[0], res.params.iloc[1]
        
        # Beta must be negative (longer tasks -> lower success)
        # If beta is near zero or positive, horizon is unidentifiable
        if beta >= 0:
            return None
            
        log2_T50 = -alpha / beta
        T50 = 2.0 ** log2_T50
        
        # 80% threshold: logit(0.8) = log(4) = 1.386294
        logit_80 = math.log(0.8 / 0.2)
        log2_T80 = (logit_80 - alpha) / beta
        T80 = 2.0 ** log2_T80 if log2_T80 > 0 else np.nan
        
        return {
            "alpha": alpha,
            "beta": beta,
            "log2_T50": log2_T50,
            "T50_minutes": T50,
            "log2_T80": log2_T80,
            "T80_minutes": T80,
            "aic": res.aic,
            "n_obs": len(df_sub)
        }
    except Exception:
        return None

def run_bootstrap_ci(df_sub, n_boot=100):
    """Computes bootstrap CIs by task, by run, and clustered by task family."""
    tasks = df_sub['task_id'].unique()
    families = df_sub['task_family'].unique()
    n_rows = len(df_sub)
    
    # Pre-index for ultra-fast sampling
    task_indices = df_sub.groupby('task_id').indices
    family_indices = df_sub.groupby('task_family').indices
    
    boot_t50_task = []
    boot_t50_run = []
    boot_t50_fam = []
    
    np.random.seed(42)
    
    # 1. By run
    for _ in range(n_boot):
        sample_idx = np.random.choice(n_rows, size=n_rows, replace=True)
        sample_runs = df_sub.iloc[sample_idx]
        fit = fit_logistic_horizon(sample_runs)
        if fit and 0 < fit["log2_T50"] < 30:
            boot_t50_run.append(fit["log2_T50"])
            
    # 2. By task
    for _ in range(n_boot):
        sampled_tasks = np.random.choice(tasks, size=len(tasks), replace=True)
        sample_idx = np.concatenate([task_indices[t] for t in sampled_tasks])
        sample_df = df_sub.iloc[sample_idx]
        fit = fit_logistic_horizon(sample_df)
        if fit and 0 < fit["log2_T50"] < 30:
            boot_t50_task.append(fit["log2_T50"])
            
    # 3. Clustered by family
    if len(families) > 2:
        for _ in range(n_boot):
            sampled_fam = np.random.choice(families, size=len(families), replace=True)
            sample_idx = np.concatenate([family_indices[fam] for fam in sampled_fam])
            sample_df = df_sub.iloc[sample_idx]
            fit = fit_logistic_horizon(sample_df)
            if fit and 0 < fit["log2_T50"] < 30:
                boot_t50_fam.append(fit["log2_T50"])

    def get_ci(arr):
        if len(arr) >= 20:
            return np.percentile(arr, 2.5), np.percentile(arr, 97.5)
        return np.nan, np.nan

    run_lo, run_hi = get_ci(boot_t50_run)
    task_lo, task_hi = get_ci(boot_t50_task)
    fam_lo, fam_hi = get_ci(boot_t50_fam)
    
    return {
        "ci_run_lo": run_lo, "ci_run_hi": run_hi,
        "ci_task_lo": task_lo, "ci_task_hi": task_hi,
        "ci_family_lo": fam_lo, "ci_family_hi": fam_hi
    }

def main():
    print("=" * 60)
    print("AI METR Time Horizon Modeling (03_process_ai_metr.py)")
    print("=" * 60)
    
    df_clean = load_and_clean_runs()
    
    print("\n[2/4] Estimating model task horizons (T_50, T_80)...")
    models = df_clean['model'].unique()
    
    horizon_results = []
    ci_results = []
    
    for m in sorted(models):
        sub = df_clean[df_clean['model'] == m].copy()
        fit = fit_logistic_horizon(sub)
        if not fit:
            print(f"  [SKIP] Model {m} (insufficient variation or non-negative slope)")
            continue
            
        alias = sub['model_alias'].iloc[0]
        eval_date = sub['evaluation_date'].max()
        
        row = {
            "model": m,
            "model_alias": alias,
            "evaluation_date": eval_date,
            "n_runs": fit["n_obs"],
            "alpha": fit["alpha"],
            "beta": fit["beta"],
            "log2_T50": fit["log2_T50"],
            "T50_minutes": fit["T50_minutes"],
            "log2_T80": fit["log2_T80"],
            "T80_minutes": fit["T80_minutes"],
            "aic": fit["aic"],
            "evidentiary_status": "derived"
        }
        horizon_results.append(row)
        print(f"  Model {m:25s} | log2(T50): {fit['log2_T50']:6.2f} ({fit['T50_minutes']:8.1f} min) | N={fit['n_obs']}")
        
        # Bootstrap CI
        ci = run_bootstrap_ci(sub, n_boot=150)
        ci_row = {
            "model": m,
            "model_alias": alias,
            "log2_T50": fit["log2_T50"],
            "ci_run_95_lo": ci["ci_run_lo"],
            "ci_run_95_hi": ci["ci_run_hi"],
            "ci_task_95_lo": ci["ci_task_lo"],
            "ci_task_95_hi": ci["ci_task_hi"],
            "ci_family_95_lo": ci["ci_family_lo"],
            "ci_family_95_hi": ci["ci_family_hi"],
            "evidentiary_status": "derived"
        }
        ci_results.append(ci_row)
        
    df_horizons = pd.DataFrame(horizon_results).sort_values("log2_T50", ascending=False).reset_index(drop=True)
    df_cis = pd.DataFrame(ci_results)
    
    # Save processed outputs
    out_h1 = DATA_PROCESSED / "ai_model_horizons.csv"
    out_h2 = OUTPUTS_TABLES / "ai_model_horizons.csv"
    out_ci = OUTPUTS_TABLES / "ai_model_horizon_confidence_intervals.csv"
    
    df_horizons.to_csv(out_h1, index=False)
    df_horizons.to_csv(out_h2, index=False)
    df_cis.to_csv(out_ci, index=False)
    
    print(f"\n[3/4] Successfully estimated horizons for {len(df_horizons)} models.")
    print(f" -> Saved to {out_h1}")
    print(f" -> Saved to {out_ci}")

if __name__ == "__main__":
    main()
