"""
02_process_housing.py - Housing Data Processing & Alignment

Merges FRED series (PERMIT, HOUST, COMPUTSA) on overlapping dates.
Constructs:
  - SAAR and unannualized monthly-flow (/12) series
  - H_t = H_{t-1} + P_t - C_t (cumulative flow proxy)
  - B_t = P_t - C_t (permit-to-completion flow gap)
  - Q_t = S_t - C_t (starts-to-completion flow gap)
  - R_t = C_t / P_t (throughput ratio)
  - K_t = S_t / P_t (translation ratio)
Outputs:
  - data/processed/housing_monthly_merged.csv
  - outputs/diagnostics/housing_vintage_alignment.json
"""

import os
import sys
import json
import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw" / "housing"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS_DIAG = PROJECT_ROOT / "outputs" / "diagnostics"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIAG.mkdir(parents=True, exist_ok=True)

def load_fred_series(filepath, col_name):
    """Loads a standard FRED CSV (DATE or OBSERVATION_DATE, VALUE)."""
    df = pd.read_csv(filepath)
    df.columns = [c.strip().upper() for c in df.columns]
    date_col = 'OBSERVATION_DATE' if 'OBSERVATION_DATE' in df.columns else 'DATE'
    df.rename(columns={date_col: 'DATE'}, inplace=True)
    df[col_name] = pd.to_numeric(df[col_name].replace('.', np.nan), errors='coerce')
    df['DATE'] = pd.to_datetime(df['DATE'])
    df = df.dropna(subset=['DATE', col_name]).sort_values('DATE').reset_index(drop=True)
    return df

def main():
    print("=" * 60)
    print("Processing Housing Data (02_process_housing.py)")
    print("=" * 60)
    
    permit_file = DATA_RAW / "fred_PERMIT.csv"
    houst_file = DATA_RAW / "fred_HOUST.csv"
    computsa_file = DATA_RAW / "fred_COMPUTSA.csv"
    
    df_p = load_fred_series(permit_file, 'PERMIT')
    df_s = load_fred_series(houst_file, 'HOUST')
    df_c = load_fred_series(computsa_file, 'COMPUTSA')
    
    # Vintage alignment diagnostics
    p_start, p_end = df_p['DATE'].min().strftime('%Y-%m-%d'), df_p['DATE'].max().strftime('%Y-%m-%d')
    s_start, s_end = df_s['DATE'].min().strftime('%Y-%m-%d'), df_s['DATE'].max().strftime('%Y-%m-%d')
    c_start, c_end = df_c['DATE'].min().strftime('%Y-%m-%d'), df_c['DATE'].max().strftime('%Y-%m-%d')
    
    # Common overlapping interval
    common_start = max(df_p['DATE'].min(), df_s['DATE'].min(), df_c['DATE'].min())
    common_end = min(df_p['DATE'].max(), df_s['DATE'].max(), df_c['DATE'].max())
    
    alignment_diag = {
        "series_metadata": {
            "PERMIT": {"start": p_start, "end": p_end, "total_obs": len(df_p), "unit": "Thousands of Units, SAAR"},
            "HOUST": {"start": s_start, "end": s_end, "total_obs": len(df_s), "unit": "Thousands of Units, SAAR"},
            "COMPUTSA": {"start": c_start, "end": c_end, "total_obs": len(df_c), "unit": "Thousands of Units, SAAR"}
        },
        "overlapping_interval": {
            "start": common_start.strftime('%Y-%m-%d'),
            "end": common_end.strftime('%Y-%m-%d'),
            "common_months_count": 0
        },
        "transformation_rules": {
            "monthly_flow": "SAAR / 12",
            "cumulative_flow_proxy": "H_t = H_{t-1} + P_t - C_t (anchored at 0 at start of common interval)",
            "flow_gap_B_t": "P_t - C_t",
            "pipeline_gap_Q_t": "S_t - C_t",
            "throughput_ratio_R_t": "C_t / P_t",
            "translation_ratio_K_t": "S_t / P_t"
        },
        "evidentiary_status": {
            "permits": "observed",
            "starts": "observed",
            "completions": "observed",
            "flows_and_proxies": "derived"
        }
    }
    
    # Merge on exact DATE
    df_merged = df_p.merge(df_s, on='DATE', how='inner').merge(df_c, on='DATE', how='inner')
    df_merged = df_merged.sort_values('DATE').reset_index(drop=True)
    alignment_diag["overlapping_interval"]["common_months_count"] = len(df_merged)
    
    # Add metadata columns
    df_merged['permit_source'] = 'FRED_PERMIT'
    df_merged['starts_source'] = 'FRED_HOUST'
    df_merged['completion_source'] = 'FRED_COMPUTSA'
    df_merged['seasonal_adjustment'] = 'SAAR'
    df_merged['annualization_factor'] = 12.0
    
    # Monthly flow (/12)
    df_merged['permits_flow'] = df_merged['PERMIT'] / 12.0
    df_merged['starts_flow'] = df_merged['HOUST'] / 12.0
    df_merged['completions_flow'] = df_merged['COMPUTSA'] / 12.0
    
    # Flow differences (SAAR basis and monthly-flow basis)
    df_merged['B_t_saar'] = df_merged['PERMIT'] - df_merged['COMPUTSA']
    df_merged['Q_t_saar'] = df_merged['HOUST'] - df_merged['COMPUTSA']
    
    df_merged['B_t'] = df_merged['permits_flow'] - df_merged['completions_flow']
    df_merged['Q_t'] = df_merged['starts_flow'] - df_merged['completions_flow']
    
    # Ratios
    df_merged['R_t'] = df_merged['COMPUTSA'] / df_merged['PERMIT']
    df_merged['K_t'] = df_merged['HOUST'] / df_merged['PERMIT']
    
    # Cumulative flow proxy H_t (anchored at 0 at start of overlapping interval)
    df_merged['H_t'] = df_merged['B_t'].cumsum()
    df_merged['H_t_label'] = 'cumulative flow proxy'
    
    # Reorder columns
    out_cols = [
        'DATE', 'PERMIT', 'HOUST', 'COMPUTSA',
        'permits_flow', 'starts_flow', 'completions_flow',
        'B_t', 'Q_t', 'B_t_saar', 'Q_t_saar',
        'R_t', 'K_t', 'H_t', 'H_t_label',
        'permit_source', 'starts_source', 'completion_source',
        'seasonal_adjustment', 'annualization_factor'
    ]
    df_out = df_merged[out_cols].copy()
    df_out.rename(columns={'DATE': 'date', 'PERMIT': 'permits', 'HOUST': 'starts', 'COMPUTSA': 'completions'}, inplace=True)
    
    out_csv = DATA_PROCESSED / "housing_monthly_merged.csv"
    df_out.to_csv(out_csv, index=False)
    print(f"[HOUSING PROCESSED] Saved {len(df_out)} monthly observations to {out_csv}")
    print(f"  Overlap: {df_out['date'].min().strftime('%Y-%m-%d')} to {df_out['date'].max().strftime('%Y-%m-%d')}")
    
    out_json = OUTPUTS_DIAG / "housing_vintage_alignment.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(alignment_diag, f, indent=2)
    print(f"[DIAGNOSTICS] Saved vintage alignment to {out_json}")

if __name__ == "__main__":
    main()
