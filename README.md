# The Floor That Does Not Rise: Reset Events, Queueing Instability, and the Hard–Soft Floor Distinction

### A General Theory, Tested Against Five Empirical Domains

**Author**: Gia Bao Huynh  
*Independent Researcher, Ho Chi Minh City, Vietnam*  
*Email: huynhbao@asu.edu · ORCID: [0009-0008-2372-5852](https://orcid.org/0009-0008-2372-5852)*  
*Collaborator: Claude Sonnet 5 & Gemini Spark*

**Repositories**:
- 🌐 **GitHub**: [https://github.com/giabaohuynhasu/the-floor-that-does-not-rise](https://github.com/giabaohuynhasu/the-floor-that-does-not-rise)
- 🌐 **Hugging Face Hub**: [https://huggingface.co/datasets/giabaohuynhasu/the-floor-that-does-not-rise](https://huggingface.co/datasets/giabaohuynhasu/the-floor-that-does-not-rise)

---

## 📌 Overview & Abstract

Some technologies generate their own inequality faster than they can resolve it, because the very engine that creates a new advantage is also, in principle, the only mechanism that could ever spread it evenly — and the engine now compounds faster than the spreading mechanism can move.

This paper formalizes this structure as a **workload process** $V(t)$ in queueing theory:
$$\rho(t) = \frac{\lambda(t) \cdot \mathbb{E}[\delta]}{\mu}$$
where:
- $\lambda(t)$ is the arrival rate of **reset events** (discrete frontier capability advances).
- $\delta$ is the jump size of each advance.
- $\mu$ is the bounded service capacity of the **general-access floor** (diffusion rate).

When $\rho(t) < 1$, the system is locally stable and the gap $\Delta(t)$ oscillates around a bounded mean. When $\rho(t) > 1$, the system is **structurally unstable**: the backlog of unabsorbed advances grows without bound, producing a widening frontier–floor chasm.

We test this formalization against raw, primary data across **five empirical domains**:
1. **U.S. Housing Construction Pipeline (Null Comparator)**: FRED and Census Bureau time series (Permits, Starts, Completions from 1968 to 2026).
2. **AI Capability Growth (METR Benchmark)**: 24,008 task-level evaluation runs across 21 frontier models from METR's `eval-analysis-public` repository.
3. **AI Distillation Extraction Economy (Anthropic Disclosures)**: Empirical exchange volumes (15M exchanges / 90 days) and effective throughput sensitivity modeling ($\mu_{\text{eff}}$).
4. **Longevity Biotechnology**: CALERIE trial epigenetic biomarker outcomes (DunedinPACE, PhenoAge, GrimAge) versus economic price/access stratification.
5. **Cybersecurity Vulnerabilities**: 28-year CVE inflow (1999–2026), CNA authority decentralization (HHI), and CISA KEV remediation administrative pacing.

---

## 📊 Key Empirical Findings

| Domain | Key Metric | Value / Estimate | Statistical Status / Evidence | Classification |
| :--- | :--- | :--- | :--- | :--- |
| **Housing** | Backlog ADF test ($B_t = P_t - C_t$) | $\text{ADF} = -7.49$, $p < 10^{-10}$ | Rejects unit root; mean-reverting ($t_{1/2} = 5.09$ mo) | `observed` / `derived` (Null case) |
| **Housing** | Under-construction ADF ($Q_t = S_t - C_t$) | $\text{ADF} = -7.03$, $p < 10^{-10}$ | Rejects unit root; mean-reverting | `observed` / `derived` |
| **AI (METR)** | $T_{50}$ capability doubling time | $7.2$ months | 95% CI: [5.4, 10.8] months, $R^2 = 0.81$ | `derived` |
| **AI (METR)** | Quadratic curvature test ($p$-value) | $p = 0.28$ | Linear model preferred; no robust monotonic acceleration | `derived` |
| **AI (METR)** | Chronological negative residual run | 6 consecutive models | March–October 2024 growth lull | `observed` |
| **Anthropic** | Primary distillation exchange volume | 166,667 exchanges/day | 15M exchanges / 24k accounts / 90 days | `reported_attribution` |
| **Anthropic** | Effective throughput ($\mu_{\text{eff}}$) | $[0.015, 150.0]$ units/day | Sensitivity grid across $r, u, v, h$ parameters | `scenario` |
| **Longevity** | DunedinPACE aging rate change | $-0.02$ /year | $[-0.035, -0.005]$, $p = 0.008$ (CALERIE) | `observed` |
| **Longevity** | Generic Metformin Affordability | $0.98$ ($4.00/mo) | Widely affordable, but lacks validated longevity indication | `derived` |
| **Longevity** | Concierge Clinic Affordability | $0.00$ ($1,250.00/mo) | Cash-pay tier, 3 orders of magnitude cost gap | `derived` |
| **Cybersecurity** | CVE inflow growth (2018–2024) | $+139.3\%$ | 16,508 $\to$ 39,500 CVEs/year | `observed` |
| **Cybersecurity** | CNA concentration (HHI) | $710$ | Decentralized from 1,500 in 2018 | `derived` |
| **Cybersecurity** | BOD 22-01 remediation deadlines | 14–21 days | Administrative mandate; technical remediation unresolved | `observed` / `unresolved` |

---

## 📁 Repository Structure

```text
the-floor-that-does-not-rise/
├── README.md                           # Comprehensive documentation & replication guide
├── LICENSE                             # MIT License
├── requirements.txt                    # Pinned Python dependencies
├── environment.yml                     # Conda/Mamba environment definition
├── run_pipeline.bat                    # One-click execution script for Windows
├── generate_enhanced_paper.py          # Script generating publication-quality DOCX
├── data/
│   ├── raw/                            # Primary raw data files
│   │   ├── housing/census/             # Census Bureau / FRED PERMIT, HOUST, COMPUTSA CSVs
│   │   ├── ai_metr/                    # METR raw_runs.jsonl and time-horizon evaluations
│   │   ├── anthropic/                  # Threat intelligence disclosure reports
│   │   ├── longevity/                  # CALERIE trial extracts (PMC11552646)
│   │   └── cybersecurity/              # CISA KEV JSON and CVE time series
│   ├── interim/                        # Cleaned intermediate extracts
│   └── processed/                      # Analysis-ready datasets (e.g. ai_clean_runs.csv)
├── metadata/
│   ├── source_ledger.csv               # Complete inventory of primary sources and tiers
│   ├── retrieval_log.csv               # HTTP headers, status codes, and timestamps
│   ├── exclusion_log.csv               # Row-level audit of excluded observations
│   ├── variable_dictionary.csv         # Variable definitions, units, and evidence labels
│   └── checksum_manifest.csv           # Authoritative SHA-256 checksums
├── scripts/
│   ├── 00_download_all.py              # Automated retrieval pipeline
│   ├── 01_validate_sources.py          # SHA-256 and structural validation
│   ├── 02_process_housing.py           # Housing pipeline & unit root tests (ADF/KPSS)
│   ├── 03_process_ai_metr.py           # METR task horizon logistic regressions
│   ├── 04_process_anthropic.py         # Distillation input rates & throughput grid
│   ├── 05_process_longevity.py         # CALERIE biomarker & affordability index
│   ├── 06_process_cybersecurity.py     # CVE inflow, CNA HHI, and KEV policy break
│   ├── 07_run_all_models.py            # Master econometrics & queueing model runner
│   ├── 08_make_tables.py               # Formats publication-ready CSV & LaTeX tables
│   └── 09_make_figures.py              # Generates publication figures (PNG/PDF)
├── tests/
│   └── test_pipeline.py                # 6 automated validation tests (pytest)
├── outputs/
│   ├── The_Floor_That_Does_Not_Rise_REWRITTEN_FINAL.docx # Completely rewritten manuscript
│   ├── research_data_audit.pdf          # Full research data audit report
│   ├── all_figures.zip                 # All publication figures
│   ├── tables/                         # Generated CSV and LaTeX tables
│   ├── figures/                        # High-resolution charts (Housing, AI, Cyber)
│   └── paper_insertions_final/         # Machine-readable textual summaries
└── knowledge_graph/                    # Zotero-Obsidian Citation Network & Dialectic Mindmap
    ├── 00_Master_Mindmap_and_Cite_Network.md # Master Mermaid mindmap & topological index
    ├── 01_NotebookLM_Interrogation_Dossier.md# Grounding protocol, 5 Epistemic Gates, 20 Task Classes
    ├── thinkers/                       # Dialectic cards (Foundational Pillars vs. Refuted Fallacies)
    ├── monographs/                     # Author's 6 foundational monographs (Zenodo DOIs & Zotero keys)
    └── claims/                         # Core theorems, queueing thresholds & Rule Zero invariant
```

---

## 🧠 Zotero-Obsidian Citation Network & Dialectic Mindmap

This repository includes a publication-grade, fully interconnected **Zotero-Obsidian Citation Network** located in [`knowledge_graph/`](knowledge_graph/00_Master_Mindmap_and_Cite_Network.md), which can be opened directly as an Obsidian Vault or navigated via GitHub markdown.

### Dialectical Structure:
1. **Foundational & Mathematical Pillars**:
   - **Ward Whitt (2002)**: Heavy-traffic limits, $M_t/G/1$ approximations, and non-stationary backlog divergence.
   - **Leonard Kleinrock (1975) & William Massey (1985)**: The workload process $V(t)$ and time-dependent arrival queues.
   - **Philippe Aghion & Peter Howitt (1992)**: Creative destruction and non-equilibrium growth microfoundations.
   - **Fred Hirsch (1977)**: Positional goods and the social limits to growth.
   - **Nick Bostrom (2002)**: Differential technological development and the unilateral acceleration dilemma.
   - **Leigh Van Valen (1973)**: The Red Queen hypothesis adapted to asymmetric technological competition.
   - **Raj Chetty et al. (2016) & David Cutler et al. (2006)**: Empirical documentation of income-stratified mortality divergence.
2. **Refuted Counter-Paradigms**:
   - **Everett Rogers (2003) & Donald Berwick (2003)**: Refuting the *Diffusion Convergence Fallacy* (the dogma of inevitable S-curve democratization).
   - **Ray Kurzweil & Peter Diamandis**: Refuting *The Smartphone Fallacy* (conflating 2D silicon scaling with live human biological time).
   - **In Silico Trialists & Digital Twin Proponents**: Exposing the fallacy that neural simulations can replace live human longitudinal Phase III endpoints.
   - **Patent Cliff & Biosimilar Commoditization Theorists**: Proving that generic price collapses cannot close relative gaps against an exponential frontier.
3. **Author's Foundational Monograph Series (Gia Bao Huynh 2026)**:
   - *Till Death Tear Us Apart* (DOI: `10.5281/zenodo.20777406`, Zotero: `GI2ASFMG`)
   - *The Unfalsifiable Critic* (DOI: `10.5281/zenodo.20776160`, Zotero: `TDKDGZHA`)
   - *The Biological Zero-Day Mechanism* (DOI: `10.5281/zenodo.20780733`, Zotero: `EIKTRBGH`)
   - *The Closing Window* (DOI: `10.5281/zenodo.20785465`, Zotero: `FFWLB6YX`)
   - *The Two Biases That Blind Governance* (DOI: `10.5281/zenodo.20792546`, Zotero: `GUNS4C6I`)
   - *The Floor That Does Not Rise* (DOI: `10.5281/zenodo.21335914`)

---

## 🚀 Reproduction Instructions

### Prerequisites
- Python 3.10+ (tested on Python 3.11 & 3.12)
- Git

### Quick Setup

```bash
# 1. Clone repository
git clone https://github.com/giabaohuynhasu/the-floor-that-does-not-rise.git
cd the-floor-that-does-not-rise

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Run Full Pipeline
To re-run all data ingestion, transformations, econometric models, table generation, and figure plotting from scratch:

```bash
# Windows
run_pipeline.bat

# Linux / macOS
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
```

### Run Audit Tests
```bash
pytest -v tests/
```
All 6 tests verify data integrity, ADF stationary conditions, METR parameter bounds, and table outputs with 0 failures.

---

## 📜 Citation

```bibtex
@article{huynh2026thefloorthatdoesnotrise,
  author    = {Gia Bao Huynh},
  title     = {The Floor That Does Not Rise: Reset Events, Queueing Instability, and the Hard--Soft Floor Distinction},
  year      = {2026},
  note      = {Working Draft},
  url       = {https://github.com/giabaohuynhasu/the-floor-that-does-not-rise}
}
```

---

## ⚖️ License
This project is licensed under the [MIT License](LICENSE).
