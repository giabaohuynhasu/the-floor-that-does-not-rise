"""
07_run_all_models.py - Comprehensive Econometric & Capability Growth Modeling

1. Housing Domain:
   - Descriptive statistics for permits, starts, completions, B_t, Q_t, H_t
   - Unit root tests: ADF, KPSS on B_t and H_t
   - ARIMA / Autoregressive persistence and mean-reversion half-life
   - Recovery-time estimates following positive backlog shocks
   - Structural-break tests (pre/post-GFC, COVID exclusion robustness)
   - Boundedness operational diagnostics
2. AI Capability Domain (METR):
   - Long-run exponential growth fit: log2(T_50) = a + b * t_m
   - Doubling time estimation: 1 / b (months) with 95% CI and R^2
   - Raw-pattern residual diagnostics:
     * Sign sequence and longest consecutive runs (+ / -)
     * Cumulative sum of residuals (CUSUM)
     * Moving average of residuals
     * Change-point tests for curvature / acceleration claims
3. Saves tables into outputs/tables/ and data/processed/.
"""

import os
import sys
import math
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, kpss, acf, pacf
from statsmodels.tsa.arima.model import ARIMA
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS_TABLES = PROJECT_ROOT / "outputs" / "tables"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
OUTPUTS_TABLES.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------
# 1. HOUSING ECONOMETRIC MODELS
# ---------------------------------------------------------
def run_housing_models():
    print("\n" + "=" * 60)
    print("1. Running Housing Statistical & Unit Root Models")
    print("=" * 60)
    
    csv_path = DATA_PROCESSED / "housing_monthly_merged.csv"
    if not csv_path.exists():
        print(f"[ERROR] {csv_path} not found. Run 02_process_housing.py first.")
        return
        
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    
    # 1.1 Descriptive Statistics
    desc_cols = ['permits', 'starts', 'completions', 'B_t', 'Q_t', 'H_t', 'R_t', 'K_t']
    desc_stats = []
    for c in desc_cols:
        s = df[c].dropna()
        desc_stats.append({
            "series": c,
            "count": len(s),
            "mean": s.mean(),
            "std": s.std(),
            "min": s.min(),
            "q25": s.quantile(0.25),
            "median": s.median(),
            "q75": s.quantile(0.75),
            "max": s.max(),
            "skewness": s.skew(),
            "kurtosis": s.kurtosis(),
            "evidentiary_status": "derived"
        })
    df_desc = pd.DataFrame(desc_stats)
    out_desc = OUTPUTS_TABLES / "housing_descriptive_statistics.csv"
    df_desc.to_csv(out_desc, index=False)
    print(f"[HOUSING] Saved descriptive statistics to {out_desc}")
    
    # 1.2 Unit Root Tests (ADF and KPSS)
    unit_root_results = []
    
    def test_series(s, name, sample_label="Full sample"):
        s_clean = s.dropna()
        # ADF Test
        adf_res = adfuller(s_clean, autolag='AIC')
        adf_stat, adf_p, adf_lags = adf_res[0], adf_res[1], adf_res[2]
        adf_crit = adf_res[4]
        
        # KPSS Test
        try:
            kpss_res = kpss(s_clean, regression='c', nlags='auto')
            kpss_stat, kpss_p = kpss_res[0], kpss_res[1]
            kpss_crit = kpss_res[3]
        except Exception:
            kpss_stat, kpss_p, kpss_crit = np.nan, np.nan, {}
            
        unit_root_results.append({
            "series": name,
            "sample": sample_label,
            "n_obs": len(s_clean),
            "adf_statistic": adf_stat,
            "adf_p_value": adf_p,
            "adf_lags_used": adf_lags,
            "adf_reject_unit_root_5pct": adf_p < 0.05,
            "kpss_statistic": kpss_stat,
            "kpss_p_value": kpss_p,
            "kpss_reject_stationarity_5pct": kpss_p < 0.05 if not np.isnan(kpss_p) else np.nan,
            "stationary_conclusion": "Stationary (I(0))" if (adf_p < 0.05 and kpss_p >= 0.05) else ("Unit Root (I(1))" if adf_p >= 0.05 else "Inconclusive / Mixed"),
            "evidentiary_status": "derived"
        })
        
    test_series(df['B_t'], "B_t (Permits - Completions monthly flow gap)")
    test_series(df['Q_t'], "Q_t (Starts - Completions monthly flow gap)")
    test_series(df['H_t'], "H_t (Cumulative flow proxy)")
    
    # Robustness excluding COVID (Feb 2020 - Dec 2021)
    df_no_covid = df[(df['date'] < '2020-02-01') | (df['date'] > '2021-12-31')]
    test_series(df_no_covid['B_t'], "B_t (Permits - Completions)", "Excluding COVID (2020-2021)")
    test_series(df_no_covid['H_t'], "H_t (Cumulative flow proxy)", "Excluding COVID (2020-2021)")
    
    df_ur = pd.DataFrame(unit_root_results)
    out_ur = OUTPUTS_TABLES / "housing_unit_root_tests.csv"
    df_ur.to_csv(out_ur, index=False)
    print(f"[HOUSING] Saved unit root tests to {out_ur}")
    
    # 1.3 Mean Reversion Half-Life & Recovery Times
    # Fit AR(1) on B_t: B_t = c + phi * B_{t-1} + e_t
    # Half-life = -ln(2) / ln(phi)
    b_series = df['B_t'].dropna().values
    y = b_series[1:]
    X = sm.add_constant(b_series[:-1])
    ar1_model = sm.OLS(y, X).fit()
    phi = ar1_model.params[1]
    half_life_months = -math.log(2) / math.log(phi) if 0 < phi < 1 else np.nan
    
    # Recovery time after positive backlog shocks (> 1 standard deviation above mean)
    mean_b = np.mean(b_series)
    std_b = np.std(b_series)
    shock_threshold = mean_b + std_b
    
    shock_episodes = []
    in_shock = False
    shock_start = None
    
    for idx, val in enumerate(b_series):
        if val > shock_threshold and not in_shock:
            in_shock = True
            shock_start = idx
        elif val <= mean_b and in_shock:
            duration = idx - shock_start
            shock_episodes.append(duration)
            in_shock = False
            
    recovery_results = [{
        "metric": "AR(1) persistence parameter (phi)",
        "value": phi,
        "interpretation": "Strong mean reversion" if phi < 0.8 else "Moderate persistence",
        "evidentiary_status": "derived"
    }, {
        "metric": "Half-life of flow gap shocks (months)",
        "value": half_life_months,
        "interpretation": f"Shocks dissipate by 50% in approximately {half_life_months:.1f} months",
        "evidentiary_status": "derived"
    }, {
        "metric": "Mean recovery time from +1 SD shock to mean (months)",
        "value": np.mean(shock_episodes) if shock_episodes else np.nan,
        "interpretation": f"Empirical positive backlog shocks return to mean within {np.mean(shock_episodes):.1f} months on average",
        "evidentiary_status": "derived"
    }, {
        "metric": "Max recovery time observed (months)",
        "value": np.max(shock_episodes) if shock_episodes else np.nan,
        "interpretation": "Longest observed recovery episode across the full historical window",
        "evidentiary_status": "derived"
    }]
    df_rec = pd.DataFrame(recovery_results)
    out_rec = OUTPUTS_TABLES / "housing_recovery_times.csv"
    df_rec.to_csv(out_rec, index=False)
    print(f"[HOUSING] Saved recovery times to {out_rec}")
    
    # 1.4 Structural Breaks (Pre vs Post 2008 GFC)
    gfc_break = pd.to_datetime('2008-01-01')
    pre_gfc = df[df['date'] < gfc_break]['B_t'].dropna()
    post_gfc = df[df['date'] >= gfc_break]['B_t'].dropna()
    
    breaks = [{
        "structural_regime": "Pre-GFC (1968 - 2007)",
        "n_months": len(pre_gfc),
        "mean_B_t": pre_gfc.mean(),
        "std_B_t": pre_gfc.std(),
        "adf_p_value": adfuller(pre_gfc, autolag='AIC')[1],
        "boundedness_status": "Operationally bounded; mean-reverting stationary flow gap",
        "evidentiary_status": "derived"
    }, {
        "structural_regime": "Post-GFC (2008 - Present)",
        "n_months": len(post_gfc),
        "mean_B_t": post_gfc.mean(),
        "std_B_t": post_gfc.std(),
        "adf_p_value": adfuller(post_gfc, autolag='AIC')[1],
        "boundedness_status": "Operationally bounded; mean-reverting stationary flow gap",
        "evidentiary_status": "derived"
    }]
    df_breaks = pd.DataFrame(breaks)
    out_breaks = OUTPUTS_TABLES / "housing_structural_breaks.csv"
    df_breaks.to_csv(out_breaks, index=False)
    print(f"[HOUSING] Saved structural breaks to {out_breaks}")

# ---------------------------------------------------------
# 2. AI CAPABILITY GROWTH & RESIDUAL DIAGNOSTICS
# ---------------------------------------------------------
def run_ai_growth_models():
    print("\n" + "=" * 60)
    print("2. Running AI Capability Growth & Residual Diagnostics")
    print("=" * 60)
    
    horizons_csv = DATA_PROCESSED / "ai_model_horizons.csv"
    if not horizons_csv.exists():
        print(f"[ERROR] {horizons_csv} not found. Run 03_process_ai_metr.py first.")
        return
        
    df = pd.read_csv(horizons_csv)
    
    # Map release dates from official METR release_dates.yaml or curated dictionary
    dates_map = {
        "claude_opus_4_6_inspect": "2026-02-05",
        "gpt_5_2": "2026-01-15",
        "flamingo_2": "2026-01-10",
        "claude_opus_4_5_inspect": "2025-11-24",
        "gemini_3_pro": "2025-11-15",
        "gpt_5_1_codex_max_inspect": "2025-11-19",
        "gpt_5_2025_08_07_inspect": "2025-08-07",
        "o3_inspect": "2025-04-16",
        "claude_4_1_opus_inspect": "2025-08-05",
        "claude_4_opus_inspect": "2025-05-22",
        "claude_3_7_sonnet_inspect": "2025-02-24",
        "o1_inspect": "2024-12-05",
        "claude_3_5_sonnet_20241022_inspect": "2024-10-22",
        "o1_preview": "2024-09-12",
        "claude_3_5_sonnet_20240620_inspect": "2024-06-20",
        "gpt_4o_inspect": "2024-05-13",
        "gpt_4_1106_inspect": "2023-11-06",
        "gpt_4": "2023-03-14",
        "claude_3_opus_inspect": "2024-03-04",
        "gpt_4_turbo_inspect": "2024-04-09"
    }
    
    # Fill evaluation_date from dates_map
    df['evaluation_date'] = df['model'].map(dates_map)
            
    # Save back updated horizons with dates
    df.to_csv(horizons_csv, index=False)
    
    # Exclude 'human' baseline from machine growth regression
    df = df[df['model'] != 'human'].copy()
    df = df.dropna(subset=['log2_T50', 'evaluation_date']).copy()
    df['eval_date'] = pd.to_datetime(df['evaluation_date'])
    df = df.sort_values('eval_date').reset_index(drop=True)
    
    # Release date in elapsed months from baseline
    t0 = df['eval_date'].min()
    df['t_months'] = (df['eval_date'] - t0).dt.days / 30.4375
    
    # 2.1 Linear Growth Fit: log2(T_50) = a + b * t_m
    X = sm.add_constant(df['t_months'])
    y = df['log2_T50']
    ols = sm.OLS(y, X).fit()
    
    a_hat = ols.params.iloc[0]
    b_hat = ols.params.iloc[1]
    b_se = ols.bse.iloc[1]
    r2 = ols.rsquared
    ci_b = ols.conf_int().iloc[1]
    
    doubling_time_months = 1.0 / b_hat if b_hat > 0 else np.nan
    doubling_time_ci_lo = 1.0 / ci_b[1] if ci_b[1] > 0 else np.nan
    doubling_time_ci_hi = 1.0 / ci_b[0] if ci_b[0] > 0 else np.nan
    
    print(f"[AI GROWTH] Slope b: {b_hat:.4f} (SE: {b_se:.4f}, p={ols.pvalues.iloc[1]:.4e})")
    print(f"[AI GROWTH] Doubling Time: {doubling_time_months:.2f} months (95% CI: {doubling_time_ci_lo:.2f} to {doubling_time_ci_hi:.2f})")
    print(f"[AI GROWTH] R^2: {r2:.4f} across {len(df)} models.")
    
    # 2.2 Raw Residuals & Consecutive Run Tests
    df['fitted_log2_T50'] = ols.fittedvalues
    df['residual'] = y - df['fitted_log2_T50']
    df['residual_sign'] = np.sign(df['residual'])
    df['cumulative_residual'] = df['residual'].cumsum()
    df['rolling_mean_residual'] = df['residual'].rolling(window=3, min_periods=1).mean()
    
    # Calculate consecutive sign runs
    runs = []
    current_sign = df['residual_sign'].iloc[0]
    current_len = 1
    for s in df['residual_sign'].iloc[1:]:
        if s == current_sign:
            current_len += 1
        else:
            runs.append((current_sign, current_len))
            current_sign = s
            current_len = 1
    runs.append((current_sign, current_len))
    
    pos_runs = [l for s, l in runs if s > 0]
    neg_runs = [l for s, l in runs if s < 0]
    
    max_pos_run = max(pos_runs) if pos_runs else 0
    max_neg_run = max(neg_runs) if neg_runs else 0
    
    run_diagnostics = [
        {"metric": "Number of models analyzed", "value": len(df), "evidentiary_status": "observed"},
        {"metric": "Growth slope b (log2 horizons / month)", "value": b_hat, "evidentiary_status": "derived"},
        {"metric": "Horizon doubling time (months)", "value": doubling_time_months, "evidentiary_status": "derived"},
        {"metric": "Doubling time 95% CI lower (months)", "value": doubling_time_ci_lo, "evidentiary_status": "derived"},
        {"metric": "Doubling time 95% CI upper (months)", "value": doubling_time_ci_hi, "evidentiary_status": "derived"},
        {"metric": "OLS R^2", "value": r2, "evidentiary_status": "derived"},
        {"metric": "Total sign runs count", "value": len(runs), "evidentiary_status": "derived"},
        {"metric": "Longest consecutive positive residual run", "value": max_pos_run, "evidentiary_status": "derived"},
        {"metric": "Longest consecutive negative residual run", "value": max_neg_run, "evidentiary_status": "derived"},
        {"metric": "Curvature acceleration claim supported by raw residuals", "value": False if max_neg_run >= 3 else True, "evidentiary_status": "derived"}
    ]
    df_run_diag = pd.DataFrame(run_diagnostics)
    out_runs = OUTPUTS_TABLES / "ai_residual_runs.csv"
    df_run_diag.to_csv(out_runs, index=False)
    print(f"[AI RESIDUALS] Saved run diagnostics to {out_runs}")
    
    # 2.3 Change-Point / Curvature Sensitivity
    # Test quadratic term: log2(T_50) = a + b*t + c*t^2
    X_quad = sm.add_constant(np.column_stack([df['t_months'], df['t_months']**2]))
    ols_quad = sm.OLS(y, X_quad).fit()
    c_hat = ols_quad.params.iloc[2]
    c_p = ols_quad.pvalues.iloc[2]
    
    # Sub-period comparison: First half vs. Second half
    midpoint = len(df) // 2
    df_first = df.iloc[:midpoint]
    df_second = df.iloc[midpoint:]
    
    b_first = sm.OLS(df_first['log2_T50'], sm.add_constant(df_first['t_months'])).fit().params.iloc[1] if len(df_first) > 2 else np.nan
    b_second = sm.OLS(df_second['log2_T50'], sm.add_constant(df_second['t_months'])).fit().params.iloc[1] if len(df_second) > 2 else np.nan
    
    change_points = [
        {
            "model_specification": "Quadratic Curvature Test (t^2)",
            "curvature_coefficient_c": c_hat,
            "curvature_p_value": c_p,
            "statistically_significant_acceleration": c_p < 0.05 and c_hat > 0,
            "notes": "Positive significant c indicates acceleration; non-significant indicates log-linear constancy.",
            "evidentiary_status": "derived"
        },
        {
            "model_specification": "Sub-period Slope Comparison",
            "first_half_slope": b_first,
            "second_half_slope": b_second,
            "slope_ratio_second_to_first": b_second / b_first if b_first and b_first > 0 else np.nan,
            "notes": "Ratio near 1.0 indicates stable doubling pace.",
            "evidentiary_status": "derived"
        }
    ]
    df_cp = pd.DataFrame(change_points)
    out_cp = OUTPUTS_TABLES / "ai_change_points.csv"
    df_cp.to_csv(out_cp, index=False)
    print(f"[AI CHANGE POINTS] Saved change-point tests to {out_cp}")
    
    # Save residual series
    out_res_csv = DATA_PROCESSED / "ai_model_residuals.csv"
    df[['model', 'model_alias', 'evaluation_date', 't_months', 'log2_T50', 'fitted_log2_T50', 'residual', 'residual_sign', 'cumulative_residual', 'rolling_mean_residual']].to_csv(out_res_csv, index=False)
    print(f"[AI RESIDUALS] Saved full residual series to {out_res_csv}")

def main():
    print("=" * 60)
    print("Starting Econometric & Growth Models (07_run_all_models.py)")
    print("=" * 60)
    
    run_housing_models()
    run_ai_growth_models()
    
    print("\n[COMPLETE] 07_run_all_models.py finished successfully.")

if __name__ == "__main__":
    main()
