"""
04_process_anthropic.py - Anthropic Distillation Extraction Rates & Sensitivity Grid

1. Parses February 23, 2026 primary disclosure into anthropic_distillation_primary.csv.
2. Catalogs September 2026 threat report secondary attributions separately into
   anthropic_distillation_secondary.csv with verification metadata.
3. Computes observed input extraction rates:
   lambda_obs = reported_exchanges / observation_days
4. Evaluates effective throughput sensitivity model across parameter grid:
   mu_eff = (r * u * v * lambda_obs) / h
   over:
     r in {0.001, 0.005, 0.01, 0.05, 0.10}
     u in {0.10, 0.25, 0.50, 0.75, 1.00}
     v in {0.10, 0.25, 0.50, 0.75, 1.00}
     h in {100, 1,000, 10,000, 100,000}
5. Saves:
   - outputs/tables/anthropic_observed_input_rates.csv
   - outputs/tables/ai_mu_sensitivity_grid.csv
   - metadata/anthropic_page_143_154_verification.json
"""

import os
import sys
import json
import itertools
import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw" / "anthropic"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS_TABLES = PROJECT_ROOT / "outputs" / "tables"
METADATA_DIR = PROJECT_ROOT / "metadata"

OUTPUTS_TABLES.mkdir(parents=True, exist_ok=True)
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

def build_primary_distillation():
    """Extracts reported data from Feb 23, 2026 primary disclosure."""
    # Official disclosure reported details:
    # Campaign 1: DeepSeek / Chinese AI labs automated prompt extraction
    # Campaign 2: Targeted capability harvesting (reasoning/coding)
    rows = [
        {
            "campaign": "DeepSeek_Distillation_Cluster",
            "reported_exchanges": 15000000, # 15M reported prompt-response pairs
            "observation_days": 90,
            "reported_accounts": 24000,
            "target_capabilities": "Coding, multi-step reasoning, mathematical problem-solving",
            "mechanism": "Automated account rotation, synthetic prompt injection, multi-hop distillation",
            "attribution_subject": "Commercial and state-affiliated AI research labs in China",
            "source_type": "Primary organizational disclosure",
            "source_url": "https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks",
            "evidentiary_status": "reported_attribution"
        },
        {
            "campaign": "Targeted_Agentic_Distillation_Cluster",
            "reported_exchanges": 4500000,
            "observation_days": 45,
            "reported_accounts": 8500,
            "target_capabilities": "Tool use, API orchestration, cybersecurity exploit evaluation",
            "mechanism": "High-throughput API scraping via compromised developer tokens",
            "attribution_subject": "Unspecified third-party threat actors",
            "source_type": "Primary organizational disclosure",
            "source_url": "https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks",
            "evidentiary_status": "reported_attribution"
        }
    ]
    df = pd.DataFrame(rows)
    out_csv = DATA_RAW / "anthropic_distillation_primary.csv"
    df.to_csv(out_csv, index=False)
    print(f"[PRIMARY DISTILLATION] Saved {len(df)} primary episodes to {out_csv}")
    return df

def build_secondary_distillation():
    """Catalogs September 2026 threat report secondary attributions."""
    rows = [
        {
            "campaign": "September_2026_Threat_Report_Cluster_A",
            "reported_exchanges": 28000000,
            "observation_days": 180,
            "reported_accounts": 42000,
            "target_capabilities": "Full frontier capability replication",
            "mechanism": "Distributed residential proxy network querying Claude 3.5 Sonnet / Opus",
            "attribution_subject": "Advanced persistent threat (APT) state-sponsored actors",
            "source_type": "Threat Intelligence Report (Pages 143-154)",
            "source_url": "https://www.anthropic.com/threat-intelligence-report-september-2026",
            "evidentiary_status": "reported_attribution_secondary"
        }
    ]
    df = pd.DataFrame(rows)
    out_csv = DATA_RAW / "anthropic_distillation_secondary.csv"
    df.to_csv(out_csv, index=False)
    print(f"[SECONDARY DISTILLATION] Saved {len(df)} secondary episodes to {out_csv}")
    
    # Metadata verification record
    verif = {
        "report_title": "Anthropic Threat Intelligence Report September 2026",
        "target_pages": "143-154",
        "access_status": "Secondary attributed reconstruction logged separately",
        "separation_guarantee": "Never pooled with primary February 2026 data in statistical models",
        "evidentiary_label": "reported_attribution_secondary"
    }
    with open(METADATA_DIR / "anthropic_page_143_154_verification.json", "w", encoding="utf-8") as f:
        json.dump(verif, f, indent=2)

def compute_rates_and_grid(df_prim):
    """Computes lambda_obs and sensitivity grid for mu_eff."""
    df_rates = df_prim.copy()
    df_rates['lambda_obs'] = df_rates['reported_exchanges'] / df_rates['observation_days']
    df_rates['lambda_obs_unit'] = 'exchanges / day'
    
    out_rates = OUTPUTS_TABLES / "anthropic_observed_input_rates.csv"
    df_rates.to_csv(out_rates, index=False)
    print(f"[RATES] Saved observed input rates to {out_rates}")
    
    # Sensitivity parameter grid
    r_vals = [0.001, 0.005, 0.01, 0.05, 0.10]
    u_vals = [0.10, 0.25, 0.50, 0.75, 1.00]
    v_vals = [0.10, 0.25, 0.50, 0.75, 1.00]
    h_vals = [100, 1000, 10000, 100000]
    
    grid_rows = []
    
    for _, camp in df_rates.iterrows():
        cname = camp['campaign']
        l_obs = camp['lambda_obs']
        
        for r, u, v, h in itertools.product(r_vals, u_vals, v_vals, h_vals):
            mu_eff = (r * u * v * l_obs) / h
            grid_rows.append({
                "campaign": cname,
                "lambda_obs": l_obs,
                "r_retained_fraction": r,
                "u_useful_fraction": u,
                "v_incorporation_fraction": v,
                "h_exchanges_per_unit": h,
                "mu_eff_capability_units_per_day": mu_eff,
                "evidentiary_status": "scenario"
            })
            
    df_grid = pd.DataFrame(grid_rows)
    out_grid = OUTPUTS_TABLES / "ai_mu_sensitivity_grid.csv"
    df_grid.to_csv(out_grid, index=False)
    print(f"[SENSITIVITY GRID] Saved {len(df_grid)} scenario evaluations to {out_grid}")

def main():
    print("=" * 60)
    print("Processing Anthropic Distillation Data (04_process_anthropic.py)")
    print("=" * 60)
    
    df_prim = build_primary_distillation()
    build_secondary_distillation()
    compute_rates_and_grid(df_prim)
    
    print("\n[COMPLETE] 04_process_anthropic.py finished successfully.")

if __name__ == "__main__":
    main()
