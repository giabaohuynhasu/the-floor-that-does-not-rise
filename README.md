# The Floor That Does Not Rise: Reset Events, Queueing Instability, and the Hard–Soft Floor Distinction

### A General Theory, Tested Against Five Empirical Domains

**Author**: Gia Bao Huynh  
*Independent Researcher, Ho Chi Minh City, Vietnam*  
*Email: huynhbao@asu.edu · ORCID: [0009-0008-2372-5852](https://orcid.org/0009-0008-2372-5852)*  
*Research Stance: Challenging the unchecked power, epistemic asymmetries, and monopolized governance of non-state actors across frontier technologies.*  
*Collaborator: Claude (Anthropic)*

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

We test this formalization against raw, primary data across **four core empirical domains** in the primary paper, complemented by a dedicated quantitative module on longevity biotechnology:
1. **U.S. Housing Construction Pipeline (Null Comparator)**: FRED and Census Bureau time series (Permits, Starts, Completions from 1968 to 2026).
2. **AI Capability Growth (METR Benchmark)**: 24,008 task-level evaluation runs across 21 frontier models from METR's `eval-analysis-public` repository ($T_{50} = 7.2$ months).
3. **AI Distillation Extraction Economy (Anthropic Disclosures)**: Empirical exchange volumes (15M exchanges / 90 days) and effective throughput sensitivity modeling ($\mu_{\text{eff}}$).
4. **Cybersecurity Vulnerabilities**: 28-year CVE inflow (1999–2026), CNA authority decentralization (HHI), and CISA KEV remediation administrative pacing.
5. **Companion Empirical Module — Longevity Biotechnology Access**: A dedicated companion manuscript (*The Queue Behind the Frontier*) analyzing Tufts CSDD 50-year drug development latency, CALERIE trial epigenetic clock corrections, Anthropic export-control pause natural experiments, tiered access economics, and COVAX ceilings.

---

## 📄 Manuscripts in this Release

This repository contains the authoritative PDFs and empirical replication data for two complementary manuscripts:

### 1. Primary Formal Paper: *The Floor That Does Not Rise: Reset Events, Queueing Instability, and the Hard–Soft Floor Distinction*
- **File**: [`The_Floor_That_Does_Not_Rise_FINAL.pdf`](The_Floor_That_Does_Not_Rise_FINAL.pdf) (11 pages)
- **Zenodo DOI**: [10.5281/zenodo.22941167](https://doi.org/10.5281/zenodo.22941167) (Version 2.0.0) · [Concept DOI: 10.5281/zenodo.21335913](https://doi.org/10.5281/zenodo.21335913) (Resolves to latest version)
- **Focus**: Workload process $V(t)$, queueing instability condition $\rho(t) > 1$, reset event arrivals $\lambda(t)$, jump sizes $\delta$, service rate $\mu$, and the analytical distinction between hard floors (physical throughput limits) and soft floors (contractual/distillation concessions). Tested against Housing (null control), AI capability (METR), AI distillation (Anthropic), and Cybersecurity (CVE/CNA/KEV).
- **Scope Note**: To preserve strict queueing domain validity, the biotechnology access domain drafted earlier in the project history was decoupled from the primary paper and established as its own dedicated quantitative companion module.

### 2. Quantitative Companion Module: *The Queue Behind the Frontier: A Quantitative Module on Longevity-Biotechnology Access, Extending the Political Economy of Volume IV*
- **File**: [`Queue_Behind_the_Frontier.pdf`](Queue_Behind_the_Frontier.pdf) (7 pages)
- **Data Source**: [`biotech_module_sourced_facts.xlsx`](biotech_module_sourced_facts.xlsx)
- **Focus**: Quantitative delivery-latency model formalizing the conflict between the **Delivery Clock** (Tufts CSDD 50-year data: Phase I-to-approval takes 7.3 years, adding +4.8 months in 2014-18, approval rate 12%) and the **Discovery Clock** (METR 4.0-month doubling scenario). Features:
  - *Epigenetic calibration*: CALERIE trial corrections (DunedinPACE rate reduction $d=0.3$, $-0.02$/yr or $2.5\%$; PhenoAge and GrimAge non-significant).
  - *Export-control natural experiment*: Anthropic Claude 3.5 / 3.7 Fable 5 & Mythos 5 pause (June 12–30, 2026: 18-day pause = 14.8% of doubling interval, yielding 1.11x capability advance while foreign access was 0).
  - *Tiered access economics*: Generic metformin ($4/mo), off-label rapamycin ($30–$150/mo), to concierge biological monitoring ($10,500–$85,000/yr).
  - *Global distribution ceiling*: COVAX benchmark (600M doses delivered against 2B target in Year 1).
  - *Falsification conditions G1–G5*: Precise empirical tests under which the model is refuted.

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
| **Cybersecurity** | CVE inflow growth (2018–2024) | $+139.3\%$ | 16,508 $\to$ 39,500 CVEs/year | `observed` |
| **Cybersecurity** | CNA concentration (HHI) | $710$ | Decentralized from 1,500 in 2018 | `derived` |
| **Cybersecurity** | BOD 22-01 remediation deadlines | 14–21 days | Administrative mandate; technical remediation unresolved | `observed` / `unresolved` |
| **Longevity (Companion)** | Drug development delivery latency | $7.3$ years ($+4.8$ mo) | Tufts CSDD 50-year data; no structural acceleration | `observed` |
| **Longevity (Companion)** | Phase I-to-Approval success rate | $12\%$ | Bounded biological pipeline capacity | `observed` |
| **Longevity (Companion)** | DunedinPACE aging rate change | $-0.02$ /year ($d=0.3$) | $p = 0.008$ (CALERIE); PhenoAge & GrimAge null | `observed` |
| **Longevity (Companion)** | Export control pause capability ratio | $1.11\times$ | 18-day pause / 4.0-mo doubling; foreign access = 0 | `derived` |
| **Longevity (Companion)** | Cash-pay concierge clinic pricing | $\$10,500 - \$85,000$/yr | Fountain Life 2026; 3–4 orders of magnitude gap | `observed` |

---

## 📁 Repository Structure

```text
the-floor-that-does-not-rise/
├── README.md                           # Comprehensive documentation & replication guide
├── The_Floor_That_Does_Not_Rise_FINAL.pdf # Master formal manuscript (11 pages, Zenodo DOI: 10.5281/zenodo.21335914)
├── Queue_Behind_the_Frontier.pdf       # Companion module: Longevity-biotechnology access (7 pages)
├── biotech_module_sourced_facts.xlsx   # Verified empirical citations & parameters for companion module (Excel)
├── biotech_module_sourced_facts.csv    # Verified empirical citations & parameters for companion module (CSV)
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
│   └── processed/                      # Analysis-ready datasets (e.g. ai_clean_runs.csv, all_tables.xlsx)
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
│   ├── The_Floor_That_Does_Not_Rise_FINAL.pdf # Master formal manuscript
│   ├── Queue_Behind_the_Frontier.pdf   # Companion quantitative module
│   ├── biotech_module_sourced_facts.xlsx # Sourced facts workbook (Excel)
│   ├── biotech_module_sourced_facts.csv  # Sourced facts dataset (CSV)
│   ├── all_tables.xlsx                 # Complete 13-sheet publication workbook
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

## 🧠 Corpus-Wide Knowledge Graphs & Dialectic Citation Networks

This branch (`corpus-knowledge-graphs`) incorporates the complete set-theoretic and dialectic citation networks for the author's broader research universe:

1. **[The Floor That Does Not Rise (`knowledge_graph/`)](knowledge_graph/00_Master_Mindmap_and_Cite_Network.md)**:
   - 23 nodes covering queueing theorists (Kleinrock, Kingman, Little, Pollaczek-Khinchine), economists (Baumol, Arrow, Solow), and philosophers (Popper, Lakatos, Polanyi).
2. **[Institutional Endurance Series / ERI (`knowledge_graph_eri/`)](knowledge_graph_eri/00_Master_Mindmap_and_Cite_Network_ERI.md)**:
   - Locked $N=6$ fsQCA baseline table ($\text{Collapse} = (O \cdot M) + (M \cdot \sim B)$) across Tang, Morocco, Nigeria, Tunisia, Japan, and Comparative Anchor.
   - 10 Thinker cards (Dardess 1973, Dower 1999, Perkins 2004, Lugard 1922, Burke 1976, Ragin 2000, North 1990, Skocpol 1979; Acemoglu & Robinson and Lipset countered).
3. **[Longevity Asymmetry Corpus / LAC (`knowledge_graph_lac/`)](knowledge_graph_lac/00_Master_Mindmap_and_Cite_Network_LAC.md)**:
   - 5 Foundational Monographs (*Till Death Tear Us Apart*, *The Unfalsifiable Critic*, *The Biological Zero-Day Mechanism*, *The Closing Window*, *The Two Biases That Blind Governance*).
   - 6 Doctrines (*The Calibration Trap*, *The Separation That Doesn't Register*, *The Third Leg That Never Existed*, *The Unprotected Floor*, *The Best Case Already Failed*, *When Death Becomes Poverty*).
   - Thinker dialectic (Mannheim, Kuhn & Planck, Piketty, Sen, Rawls; De Grey, Fukuyama, Modigliani countered).
4. **[War Correspondent Philosophy (`knowledge_graph_war_correspondent/`)](knowledge_graph_war_correspondent/00_Master_Mindmap_and_Cite_Network_WCP.md)**:
   - Complete 6-Volume Edition ([Zenodo DOI: 10.5281/zenodo.22822036](https://doi.org/10.5281/zenodo.22822036)).
   - Thinker dialectic (Popper, Gadamer, Ricoeur, Benjamin, Polanyi; Carnap and Baudrillard countered).
5. **[The Fact Before the Vote & In the Name of Merit (`knowledge_graph_fact_and_merit/`)](knowledge_graph_fact_and_merit/00_Master_Mindmap_and_Cite_Network_Fact_and_Merit.md)**:
   - Legal personhood at the species boundary (4 volumes) and academic gatekeeping mechanisms (6 volumes).

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
