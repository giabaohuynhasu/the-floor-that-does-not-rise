"""
09_make_figures.py - Publication-Grade Chart Generation & Figures Zip Bundling

Generates high-resolution publication charts across all five domains:
1. Housing:
   - outputs/figures/housing_permits_starts_completions.png
   - outputs/figures/housing_flow_gap.png
   - outputs/figures/housing_backlog_proxy.png
2. AI Capability (METR):
   - outputs/figures/ai_time_horizon_log2.png
   - outputs/figures/ai_raw_residuals.png
   - outputs/figures/ai_cumulative_residuals.png
3. Anthropic Distillation:
   - outputs/figures/ai_mu_sensitivity_heatmap.png
4. Longevity Biotechnology:
   - outputs/figures/longevity_price_access.png
5. Cybersecurity:
   - outputs/figures/cybersecurity_record_inflow.png
6. Bundles all figures into outputs/all_figures.zip.
"""

import os
import sys
import zipfile
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path

# Styling settings
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.color'] = '#e0e0e0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS_TABLES = PROJECT_ROOT / "outputs" / "tables"
OUTPUTS_FIGS = PROJECT_ROOT / "outputs" / "figures"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

OUTPUTS_FIGS.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------
# 1. HOUSING FIGURES
# ---------------------------------------------------------
def make_housing_figures():
    print("[1/5] Generating Housing figures...")
    csv_path = DATA_PROCESSED / "housing_monthly_merged.csv"
    if not csv_path.exists():
        print("  [SKIP] housing_monthly_merged.csv not found.")
        return
        
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    
    # 1.1 Permits, Starts, Completions (SAAR)
    fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
    ax.plot(df['date'], df['permits'], label='Permits (PERMIT, SAAR)', color='#1f77b4', linewidth=1.2)
    ax.plot(df['date'], df['starts'], label='Starts (HOUST, SAAR)', color='#ff7f0e', linewidth=1.1, alpha=0.9)
    ax.plot(df['date'], df['completions'], label='Completions (COMPUTSA, SAAR)', color='#2ca02c', linewidth=1.2)
    
    ax.set_title("U.S. Housing Construction Pipeline (1968–Present)", fontsize=13, fontweight='bold', pad=12)
    ax.set_ylabel("Thousands of Units (SAAR)", fontsize=11)
    ax.set_xlabel("Year", fontsize=11)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
    plt.tight_layout()
    f1 = OUTPUTS_FIGS / "housing_permits_starts_completions.png"
    plt.savefig(f1)
    plt.close()
    print(f"  + Saved {f1.name}")
    
    # 1.2 Flow Gap B_t = P_t - C_t
    fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
    ax.axhline(0, color='black', linestyle='-', linewidth=0.8)
    ax.plot(df['date'], df['B_t'], label='Monthly Flow Gap $B_t = P_t - C_t$ (Unannualized)', color='#d62728', linewidth=1.0)
    
    # Rolling 12-month mean
    rolling_b = df['B_t'].rolling(12, min_periods=6).mean()
    ax.plot(df['date'], rolling_b, label='12-Month Moving Average', color='#1f77b4', linewidth=1.8)
    
    ax.set_title("Permit-to-Completion Flow Difference ($B_t$)", fontsize=13, fontweight='bold', pad=12)
    ax.set_ylabel("Thousands of Units / Month", fontsize=11)
    ax.set_xlabel("Year", fontsize=11)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
    plt.tight_layout()
    f2 = OUTPUTS_FIGS / "housing_flow_gap.png"
    plt.savefig(f2)
    plt.close()
    print(f"  + Saved {f2.name}")
    
    # 1.3 Backlog Cumulative Proxy H_t
    fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
    ax.plot(df['date'], df['H_t'], label='Cumulative Flow Proxy $H_t = \sum (P_t - C_t)$', color='#8c564b', linewidth=1.5)
    ax.set_title("Housing Cumulative Flow Proxy ($H_t$) — Null-Case Boundedness Comparison", fontsize=13, fontweight='bold', pad=12)
    ax.set_ylabel("Cumulative Flow Proxy (Thousands of Units)", fontsize=11)
    ax.set_xlabel("Year", fontsize=11)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
    plt.tight_layout()
    f3 = OUTPUTS_FIGS / "housing_backlog_proxy.png"
    plt.savefig(f3)
    plt.close()
    print(f"  + Saved {f3.name}")

# ---------------------------------------------------------
# 2. AI CAPABILITY FIGURES (METR)
# ---------------------------------------------------------
def make_ai_figures():
    print("[2/5] Generating AI Capability figures...")
    res_path = DATA_PROCESSED / "ai_model_residuals.csv"
    if not res_path.exists():
        print("  [SKIP] ai_model_residuals.csv not found.")
        return
        
    df = pd.read_csv(res_path)
    df['eval_date'] = pd.to_datetime(df['evaluation_date'])
    df = df.sort_values('eval_date').reset_index(drop=True)
    
    # 2.1 log2(T_50) vs Time
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.scatter(df['eval_date'], df['log2_T50'], color='#1f77b4', s=60, edgecolor='black', linewidth=0.7, label='Observed Model $T_{50}$ (METR)', zorder=4)
    ax.plot(df['eval_date'], df['fitted_log2_T50'], color='#d62728', linestyle='--', linewidth=1.6, label='Fitted Linear Trend $\log_2(T_{50}) = a + bt$', zorder=3)
    
    for _, r in df.iterrows():
        ax.annotate(r['model_alias'], (r['eval_date'], r['log2_T50']), textcoords="offset points", xytext=(0, 6), ha='center', fontsize=7.5, alpha=0.85)
        
    ax.set_title("AI Task Horizon Growth ($\log_2 T_{50}$ in Human Minutes)", fontsize=13, fontweight='bold', pad=12)
    ax.set_ylabel("$\log_2(T_{50})$ [Task Duration, Minutes]", fontsize=11)
    ax.set_xlabel("Evaluation Date", fontsize=11)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
    plt.tight_layout()
    f1 = OUTPUTS_FIGS / "ai_time_horizon_log2.png"
    plt.savefig(f1)
    plt.close()
    print(f"  + Saved {f1.name}")
    
    # 2.2 Raw Residuals
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.axhline(0, color='black', linestyle='-', linewidth=0.8)
    ax.stem(df['eval_date'], df['residual'], linefmt='grey', markerfmt='o', basefmt=" ")
    ax.plot(df['eval_date'], df['rolling_mean_residual'], color='#ff7f0e', linewidth=1.8, label='3-Point Moving Average')
    ax.set_title("AI Growth Model Raw Residuals ($r_m = \log_2 T_{50} - \hat{y}_m$)", fontsize=13, fontweight='bold', pad=12)
    ax.set_ylabel("Residual ($\log_2$ units)", fontsize=11)
    ax.set_xlabel("Evaluation Date", fontsize=11)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
    plt.tight_layout()
    f2 = OUTPUTS_FIGS / "ai_raw_residuals.png"
    plt.savefig(f2)
    plt.close()
    print(f"  + Saved {f2.name}")
    
    # 2.3 Cumulative Residuals (CUSUM)
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
    ax.plot(df['eval_date'], df['cumulative_residual'], marker='s', color='#2ca02c', linewidth=1.6, label='CUSUM of Residuals')
    ax.set_title("Cumulative Residuals Test (CUSUM) — Curvature & Stability Diagnostic", fontsize=13, fontweight='bold', pad=12)
    ax.set_ylabel("Cumulative Sum of Residuals", fontsize=11)
    ax.set_xlabel("Evaluation Date", fontsize=11)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
    plt.tight_layout()
    f3 = OUTPUTS_FIGS / "ai_cumulative_residuals.png"
    plt.savefig(f3)
    plt.close()
    print(f"  + Saved {f3.name}")

# ---------------------------------------------------------
# 3. ANTHROPIC DISTILLATION SENSITIVITY HEATMAP
# ---------------------------------------------------------
def make_anthropic_figures():
    print("[3/5] Generating Anthropic Distillation figures...")
    grid_csv = OUTPUTS_TABLES / "ai_mu_sensitivity_grid.csv"
    if not grid_csv.exists():
        print("  [SKIP] ai_mu_sensitivity_grid.csv not found.")
        return
        
    df = pd.read_csv(grid_csv)
    
    # Filter to primary campaign and fixed h = 1,000, v = 0.50 for 2D heatmap (r vs u)
    sub = df[(df['campaign'] == 'DeepSeek_Distillation_Cluster') & 
             (df['h_exchanges_per_unit'] == 1000) & 
             (df['v_incorporation_fraction'] == 0.50)]
             
    pivot = sub.pivot(index='r_retained_fraction', columns='u_useful_fraction', values='mu_eff_capability_units_per_day')
    
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlOrRd", ax=ax, cbar_kws={'label': 'Effective Throughput $\mu_{\mathrm{eff}}$ (Units / Day)'})
    ax.set_title("Anthropic Distillation: Effective Throughput Sensitivity Grid ($\mu_{\mathrm{eff}}$)\n[$h=1,000$ exchanges/unit, $v=0.50$]", fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel("Technically Useful Fraction ($u$)", fontsize=11)
    ax.set_ylabel("Retained Fraction ($r$)", fontsize=11)
    plt.tight_layout()
    f1 = OUTPUTS_FIGS / "ai_mu_sensitivity_heatmap.png"
    plt.savefig(f1)
    plt.close()
    print(f"  + Saved {f1.name}")

# ---------------------------------------------------------
# 4. LONGEVITY FIGURE
# ---------------------------------------------------------
def make_longevity_figures():
    print("[4/5] Generating Longevity Price & Access figures...")
    price_csv = DATA_PROCESSED / "longevity_price_access.csv"
    if not price_csv.exists():
        print("  [SKIP] longevity_price_access.csv not found.")
        return
        
    df = pd.read_csv(price_csv)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)
    
    # 4.1 Log Monthly Price
    y_pos = np.arange(len(df))
    ax1.barh(y_pos, df['monthly_price_usd'], color=['#2ca02c', '#1f77b4', '#d62728'], edgecolor='black', linewidth=0.7)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(df['intervention'], fontsize=10)
    ax1.set_xscale('log')
    ax1.set_xlabel("Monthly Out-of-Pocket Cost (USD, Log Scale)", fontsize=11)
    ax1.set_title("Monthly Intervention Cost by Market Layer", fontsize=12, fontweight='bold')
    
    for i, v in enumerate(df['monthly_price_usd']):
        ax1.text(v * 1.15, i, f"${v:,.2f}", va='center', fontsize=9, fontweight='bold')
        
    # 4.2 Affordability Index (Threshold = $200/month)
    ax2.barh(y_pos, df['affordability_index_th_200'], color=['#2ca02c', '#1f77b4', '#d62728'], edgecolor='black', linewidth=0.7)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([])
    ax2.set_xlim(0, 1.05)
    ax2.set_xlabel("Affordability Index ($A_i^{\mathrm{price}} = 1 - P_i/P^*$, $P^*=\$200$)", fontsize=11)
    ax2.set_title("Affordability Index ($P^* = \$200$/Month)", fontsize=12, fontweight='bold')
    
    for i, v in enumerate(df['affordability_index_th_200']):
        ax2.text(v + 0.02, i, f"{v:.2f}", va='center', fontsize=9, fontweight='bold')
        
    plt.tight_layout()
    f1 = OUTPUTS_FIGS / "longevity_price_access.png"
    plt.savefig(f1)
    plt.close()
    print(f"  + Saved {f1.name}")

# ---------------------------------------------------------
# 5. CYBERSECURITY FIGURE
# ---------------------------------------------------------
def make_cybersecurity_figures():
    print("[5/5] Generating Cybersecurity figures...")
    annual_csv = DATA_PROCESSED / "cybersecurity_annual.csv"
    if not annual_csv.exists():
        print("  [SKIP] cybersecurity_annual.csv not found.")
        return
        
    df = pd.read_csv(annual_csv)
    
    fig, ax1 = plt.subplots(figsize=(10, 5), dpi=300)
    
    color = '#1f77b4'
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Annual CVE Inflow (Thousands)', color=color, fontsize=11)
    l1 = ax1.plot(df['year'], df['cve_inflow'] / 1000.0, color=color, marker='o', linewidth=2.0, label='Annual CVE Inflow')
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Add BOD 22-01 vertical line
    ax1.axvline(2021, color='#d62728', linestyle=':', linewidth=1.5, label='BOD 22-01 Policy Break (Nov 2021)')
    
    ax2 = ax1.twinx()
    color = '#ff7f0e'
    ax2.set_ylabel('Active CNA Assigning Authorities', color=color, fontsize=11)
    l2 = ax2.plot(df['year'], df['active_cnas'], color=color, marker='s', linestyle='--', linewidth=1.8, label='Active CNAs')
    ax2.tick_params(axis='y', labelcolor=color)
    
    lines = l1 + l2 + [plt.Line2D([0], [0], color='#d62728', linestyle=':')]
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='white', framealpha=0.9)
    
    plt.title("Cybersecurity Vulnerability Inflow & Assigning Authority Expansion", fontsize=13, fontweight='bold', pad=12)
    plt.tight_layout()
    f1 = OUTPUTS_FIGS / "cybersecurity_record_inflow.png"
    plt.savefig(f1)
    plt.close()
    print(f"  + Saved {f1.name}")

def zip_all_figures():
    zip_path = OUTPUTS_DIR / "all_figures.zip"
    figs = list(OUTPUTS_FIGS.glob("*.png"))
    print(f"\nBundling {len(figs)} figures into {zip_path.name}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in figs:
            zf.write(f, arcname=f.name)
    print(f"[ZIP COMPLETE] Created {zip_path} ({zip_path.stat().st_size:,} bytes)")

def main():
    print("=" * 60)
    print("Generating All Publication Figures (09_make_figures.py)")
    print("=" * 60)
    
    make_housing_figures()
    make_ai_figures()
    make_anthropic_figures()
    make_longevity_figures()
    make_cybersecurity_figures()
    zip_all_figures()
    
    print("\n[COMPLETE] 09_make_figures.py finished successfully.")

if __name__ == "__main__":
    main()
