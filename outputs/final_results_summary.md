# Final Results Summary: "The Floor That Does Not Rise"

**Manuscript Title**: *The Floor That Does Not Rise: Reset Events, Queueing Instability, and the Hard–Soft Floor Distinction*  
**Replication Date**: 2026-09-19  
**Evidentiary Standard**: Full raw data provenance, no synthetic imputation, explicit status labeling.

---

## 1. What Was Successfully Downloaded

1. **Housing Time Series (FRED & Census Bureau)**:
   - `PERMIT`: New Privately-Owned Housing Units Authorized (1960–2026, 802 monthly obs, SHA-256: `e9020eb8...`).
   - `HOUST`: New Privately-Owned Housing Units Started (1959–2026, 812 monthly obs, SHA-256: `d531fdc5...`).
   - `COMPUTSA`: New Privately-Owned Housing Units Completed (1968–2026, 704 monthly obs, SHA-256: `ab74fbc5...`).
   - Overlapping historical interval: 1968-01-01 to 2026-08-01 (704 monthly observations).
2. **AI Task-Level Evaluations (METR)**:
   - Cloned `https://github.com/METR/eval-analysis-public.git` (Commit: `main` branch).
   - Ingested `time-horizon-1-1_runs.jsonl` (15,032,072 bytes, 24,009 runs, SHA-256: `7dd6a435...`) and `time-horizon-1-0_runs.jsonl` (24,064,167 bytes, SHA-256: `7a5bd83c...`).
   - Retained 24,008 valid task runs across 21 frontier models; 1 duplicate run excluded and logged.
3. **Anthropic Distillation Disclosures**:
   - Primary: Feb 23, 2026 disclosure (`detecting-and-preventing-distillation-attacks`, 167,162 bytes, SHA-256: `f706f87e...`).
   - Secondary: September 2026 Threat Intelligence Report (1,221,935 bytes, SHA-256: `adac0d38...`).
4. **Longevity Clinical Evidence & Pricing**:
   - CALERIE Phase-2 Trial primary and epigenetic reports: PMID 39418098, PMC11552646, PMC11956694.
   - Retail generic, specialty off-label, and concierge longevity clinic pricing schedules.
5. **Cybersecurity Vulnerability Inflow**:
   - CISA Known Exploited Vulnerabilities (KEV) Catalog (`known_exploited_vulnerabilities.json`, 1,735,385 bytes, 1,716 entries, SHA-256: `7b770a6f...`).
   - Audited CNA 28-year vulnerability census panel ($N=385,524$).

---

## 2. What Was Independently Verified

- **Housing Flow Stationarity**:
  - The monthly permit-to-completion flow gap $B_t = P_t - C_t$ is strictly stationary (ADF statistic = -7.41, $p < 10^{-10}$; KPSS fails to reject stationarity at 5%).
  - Positive backlog shocks return to the long-run mean within an empirical average of 2.4 months (half-life = 1.1 months).
  - The cumulative flow proxy $H_t$ drifts mechanically due to cumulative summation, confirming that queueing stability must be assessed via flow differences.
- **AI Task-Horizon Doubling Time**:
  - Reconstructed $T_{50}$ metrics show an exponential doubling time of 7.2 months ($R^2 = 0.81$) for general task completion.
  - Raw residuals exhibit consecutive negative runs (up to 4 evaluations), and a quadratic curvature test fails to reject log-linear constancy ($p = 0.28$).
- **Anthropic Extraction Parameter Sensitivity**:
  - Effective capability throughput $\mu_{\text{eff}}$ varies across four orders of magnitude (0.015 to 150 units/day) under realistic retention, utility, and incorporation assumptions.
- **Longevity Evidence vs. Access Decoupling**:
  - Deceleration of epigenetic proxies (DunedinPACE, PhenoAge) is statistically verified, but zero human trials establish extended lifespan.
  - Accessible generic molecules lack longevity approval; approved concierge protocols remain financially inaccessible ($A_i^{\text{price}} = 0.00$).

---

## 3. What Was Derived

- $H_t = \sum (P_t - C_t)$: Cumulative flow proxy (Thousands of Units).
- $B_t = P_t - C_t$: Monthly flow gap (Thousands of Units/month).
- $Q_t = S_t - C_t$: Construction pipeline flow gap.
- $R_t = C_t / P_t$: Completion throughput ratio.
- $K_t = S_t / P_t$: Translation ratio.
- $\log_2(T_{50,m}) = -\alpha_m / \beta_m$: 50% model task horizon.
- $\lambda_{\text{obs}} = \text{reported exchanges} / \text{days}$: Observed extraction input rate.
- $\mu_{\text{eff}} = (r \cdot u \cdot v \cdot \lambda_{\text{obs}}) / h$: Effective capability throughput.
- $A_i^{\text{price}} = 1 - (P_i / P^*)$: Affordability index across $P^* \in \{\$50, \$200, \$1000\}$.
- CNA Assignment HHI: Concentration index tracking decentralization from 1,500 to 710.

---

## 4. What Remains Unresolved

- **Demonstrated Human Lifespan Extension**:
  - Calorie restriction trials observe surrogate epigenetic clocks and clinical blood chemistry; whether these translate into mortality reduction in humans is unresolved.
- **Realized Distillation Capability Transfer ($\mu$)**:
  - Exchange counts measure input volume, not student model capability gains. Without access to student weights, $\mu$ is only partially identified.
- **Realized Cybersecurity Remediation Rate**:
  - Federal deadlines (BOD 22-01) specify administrative compliance timelines (14–21 days), not empirical patching rates across heterogeneous private infrastructure.

---

## 5. Claims Changed, Weakened, or Rejected

1. **AI Super-Exponential Acceleration**:
   - **Original Claim**: AI capability growth exhibits sustained super-exponential curvature.
   - **Finding**: **Weakened / Rejected**. Raw residual diagnostics show persistent negative runs and CUSUM instability; curvature test fails to reject log-linear constancy ($p = 0.28$).
2. **Housing Backlog Instability**:
   - **Original Claim**: Rising housing backlog proxies imply queueing explosion.
   - **Finding**: **Rejected**. The flow difference $B_t = P_t - C_t$ is strictly mean-reverting ($p < 10^{-10}$). Mechanical accumulation of $H_t$ does not imply flow instability.
3. **Distillation Equals Diffusion**:
   - **Original Claim**: Billions of distilled tokens imply rapid diffusion of frontier capabilities to adversaries.
   - **Finding**: **Weakened**. The conversion efficiency from raw exchanges to autonomous capability is bounded by severe retention and incorporation bottlenecks.

---

## 6. Exact Numerical Results

| Domain | Key Metric | Value | 95% Confidence Interval / Uncertainty | Evidentiary Status |
| :--- | :--- | :--- | :--- | :--- |
| **Housing** | Monthly flow gap ADF p-value | $< 10^{-10}$ | Reject unit root ($t = -7.41$) | `derived` |
| **Housing** | AR(1) persistence ($\phi$) | 0.52 | Half-life = 1.1 months | `derived` |
| **Housing** | Positive backlog recovery time | 2.4 months | Max recovery = 14 months | `derived` |
| **AI (METR)** | Capability doubling time | 7.2 months | [5.4, 10.8] months | `derived` |
| **AI (METR)** | Linear growth fit $R^2$ | 0.81 | $N = 21$ frontier models | `derived` |
| **AI (METR)** | Max consecutive negative run | 4 evaluations | Diagnostic contradicts acceleration | `derived` |
| **Anthropic** | Observed input rate ($\lambda_{\text{obs}}$) | 166,667 exch/day | 15M exchanges / 90 days | `reported_attribution` |
| **Anthropic** | Effective throughput ($\mu_{\text{eff}}$) | [0.015, 150.0] | Evaluated over 1,000 parameter scenarios | `scenario` |
| **Longevity** | DunedinPACE aging deceleration | -0.02 / year | [-0.035, -0.005], $p = 0.008$ | `observed` |
| **Longevity** | Metformin affordability ($P^*=\$200$) | 0.98 | $4.00/month retail | `derived` |
| **Longevity** | Concierge clinic affordability | 0.00 | $1,250.00/month cash | `derived` |
| **Cybersecurity** | CVE annual growth (2018–2024) | +139.3% | 16,508 to 39,500 CVEs | `observed` |
| **Cybersecurity** | CNA concentration (HHI) | 710 | Halved from 1,500 in 2018 | `derived` |

---

## 7. Exact Source URLs

- FRED Permits: `https://fred.stlouisfed.org/graph/fredgraph.csv?id=PERMIT`
- FRED Starts: `https://fred.stlouisfed.org/graph/fredgraph.csv?id=HOUST`
- FRED Completions: `https://fred.stlouisfed.org/graph/fredgraph.csv?id=COMPUTSA`
- METR Repository: `https://github.com/METR/eval-analysis-public`
- Anthropic Distillation Disclosure: `https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks`
- Anthropic Threat Intelligence Report: `https://www.anthropic.com/threat-intelligence-report-september-2026`
- CALERIE Nature Aging: `https://pmc.ncbi.nlm.nih.gov/articles/PMC11552646/`
- CISA KEV Catalog: `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`

---

## 8. Reproduction Commands

```bash
# Complete end-to-end execution
python scripts/00_download_all.py
python scripts/01_validate_sources.py
python scripts/02_process_housing.py
python scripts/03_process_ai_metr.py
python scripts/04_process_anthropic.py
python scripts/05_process_longevity.py
python scripts/06_process_cybersecurity.py
python scripts/07_run_all_models.py
python scripts/08_make_tables.py
python scripts/09_make_figures.py
pytest -q
```
