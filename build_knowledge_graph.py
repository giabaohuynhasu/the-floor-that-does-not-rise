"""
build_knowledge_graph.py
Generates the complete Zotero-Obsidian Citation Network & Dialectic Mindmap
Grounded in ALRP Obsidian Vault & NotebookLM Canon:
- Master Mindmap with Mermaid diagrams
- NotebookLM Interrogation Dossier (5 Epistemic Gates, 20 Task Classes)
- 10 Thinker Nodes (Pillars vs. Refuted Counter-Theorists)
- 6 Author Monograph Nodes (with Zotero citekeys & Zenodo DOIs)
- 5 Core Claim & Invariant Nodes
- Dual-dimension typed edges: [ RELATION_TYPE | EPISTEMIC_STATUS ]
- Zero occurrence of the internal acronym in reader-facing text
"""

import os, sys, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(r"C:\Users\nswcl\.gemini\antigravity-ide\scratch\the-floor-that-does-not-rise")
KG_DIR = PROJECT_ROOT / "knowledge_graph"
THINKERS_DIR = KG_DIR / "thinkers"
MONOGRAPHS_DIR = KG_DIR / "monographs"
CLAIMS_DIR = KG_DIR / "claims"

for d in [KG_DIR, THINKERS_DIR, MONOGRAPHS_DIR, CLAIMS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[+] Created: {path.relative_to(PROJECT_ROOT)}")

# ============================================================
# 1. NOTEBOOKLM INTERROGATION DOSSIER
# ============================================================
notebooklm_dossier = """---
title: "NotebookLM Interrogation Dossier: Corpus Intelligence & Grounding Protocol"
type: protocol
status: foundational-canon
author: "Gia Bao Huynh & Antigravity"
tags:
  - notebooklm
  - epistemic-gates
  - task-classes
  - claim-evidence-boundary
---

# NotebookLM Interrogation Dossier: Corpus Intelligence & Grounding Protocol

## 1. Core Epistemic Invariant: CORPUS-COMPLETE ≠ TRUTH-COMPLETE

> [!IMPORTANT]
> **The Principle of Bounded Induction**
> When NotebookLM resolves an inquiry with 100% confidence within the ingested corpus, it establishes:
> *"Within the current ingested corpus, sources A, B, and C support claim X."*
> **It does NOT establish that X is absolute real-world truth**, because X may be challenged, bounded, or falsified by uningested external literature, conflicting paradigms, or unmodeled empirical boundary conditions.

---

## 2. The Five Mandatory Epistemic Gates Before Vault Writes

Before any theoretical candidate, edge, or empirical assertion is committed to the permanent knowledge graph, it must traverse the **Five Epistemic Gates**:

```text
NOTEBOOKLM CORPUS
       │
       ▼
[GATE 1] Task Class 7: Claim Decomposition
       │ (Claims → Subclaims → Implicit Assumptions → Testable Predictions)
       ▼
[GATE 2] Task Class 5: Evidence Matrix
       │ (Methodology → Empirical Strength → Sample Constraints → Epistemic Status)
       ▼
[GATE 3] Task Class 8: Causality Audit
       │ (Strict classification: Causal vs. Correlational vs. Mechanistic vs. Speculative)
       ▼
[GATE 4] Task Class 9: Counterevidence & Falsification Register
       │ (Adversarial stress-testing, boundary conditions, hostile refutations)
       ▼
[GATE 5] Task Class 2: Graph-Theoretic Mind Map
       │ (Candidate typed edges with dual-dimension semantic classification)
       ▼
ANTIGRAVITY AUDIT & REPRODUCIBILITY VERIFICATION
       │
       ▼
OBSIDIAN KNOWLEDGE GRAPH ATOMIC COMMITS
```

---

## 3. Dual-Dimension Edge Specification Standard

Every edge connecting nodes within this knowledge graph must explicitly specify both **Relation Type** and **Epistemic Maturity**:

```text
[[SOURCE_NODE]] ────[ RELATION_TYPE | EPISTEMIC_STATUS ]────► [[TARGET_NODE]]
```

### Relation Types:
- `CAUSAL`: Source directly drives, generates, or alters Target.
- `CORRELATIONAL`: Source and Target co-vary without established causal direction.
- `MECHANISTIC`: Source provides physical, biological, or mathematical microfoundations for Target.
- `THEORETICAL`: Source supplies the formal framework or axiomatic model for Target.
- `HYPOTHESIZED`: Proposed relationship awaiting empirical validation.
- `CONTRADICTORY`: Source opposes, refutes, or invalidates Target.

### Epistemic Maturity Levels:
- `DIRECTLY_SUPPORTED`: Empirical clinical trial data, audited benchmark telemetry, or mathematical proof.
- `INFERRED`: Deductive logical inference from directly supported premises.
- `SPECULATIVE`: Extrapolation beyond verified empirical regimes.
- `CONTESTED`: Substantive peer counterevidence or conflicting findings exist.
- `REFUTED`: Logically or empirically disproven (e.g. Diffusion Convergence Fallacy).
- `UNRESOLVED`: Empirical data absent; under active investigation.

---

## 4. The 20 Operational NotebookLM Task Classes

1. **Corpus Orientation**: Global thematic topology and concept discovery.
2. **Mind Map Architect (Gate 5)**: Graph-theoretic extraction of typed relations.
3. **Source Triage**: Quality tiering (Must Read / High Value / Background / Redundant).
4. **Source Cross-Examination**: Multi-perspective dialectical comparison without false consensus.
5. **Evidence Matrix (Gate 2)**: Traceable claim-to-evidence verification with explicit confidence bounds.
6. **Contradiction Detection**: Identifying incompatible mechanisms and negative empirical results.
7. **Claim Decomposition (Gate 1)**: Isolating subclaims, hidden axioms, and testable predictions.
8. **Causality Auditor (Gate 3)**: Separating true causal mechanisms from spurious statistical correlations.
9. **Counterevidence Farm (Gate 4)**: Cataloging inconvenient data and edge-case failures.
10. **Research Gap Detector**: Ranked gap catalog (Impact × Uncertainty × Testability).
11. **Executive Research Briefing**: 10-point structured decision summaries.
12. **Methodological Deconstructor**: Critical dissection of experimental design and statistical power.
13. **Progressive Socratic Tutor**: Level 1–6 pedagogical conceptual unfolding.
14. **Study Material Generator**: Definitional glossaries, Q&A pairs, and audit checklists.
15. **Audio / Deep-Dive Review**: Synthesis packets for multi-modal conceptual review.
16. **LLM Preprocessor**: Distilling grounded context packets before calling frontier models.
17. **Vault Preprocessor**: Generating atomic note candidates and relationship graphs.
18. **Graph Update Adviser**: Suggesting note merges, splits, and ontological property updates.
19. **Literature Farm Worker**: Screening new preprints against existing graph topology.
20. **Research Memory Anchor**: Maintaining the persistent state of settled vs. contested claims.
"""
write_file(KG_DIR / "01_NotebookLM_Interrogation_Dossier.md", notebooklm_dossier)

# ============================================================
# 2. MASTER MINDMAP & CITE NETWORK
# ============================================================
master_mindmap = """---
title: "Master Mindmap & Zotero-Obsidian Citation Network"
type: mindmap
status: active-master
author: "Gia Bao Huynh"
tags:
  - master-graph
  - mindmap
  - citation-network
  - dialectic
---

# Master Mindmap & Zotero-Obsidian Citation Network: The Capacity–Latency Resonance Dialectic

```mermaid
graph TD
    %% Central Hub
    HUB["<b>The Floor That Does Not Rise</b><br/><i>Capacity–Latency Resonance Paradox</i><br/>Zenodo: 10.5281/zenodo.21335914"]
    style HUB fill:#1e293b,stroke:#38bdf8,stroke-width:3px,color:#fff

    %% Subgraph: Mathematical Foundations
    subgraph Math_Foundations ["Mathematical & Queueing Foundations"]
        Whitt["<b>Ward Whitt (2002)</b><br/><i>Stochastic-Process Limits</i><br/>Heavy-traffic M_t/G/1 divergence"]
        Kleinrock["<b>Leonard Kleinrock (1975)</b><br/><i>Queueing Systems</i><br/>Workload process V(t)"]
        Massey["<b>William Massey (1985)</b><br/><i>Time-Dependent Queues</i><br/>Non-stationary arrival rates"]
    end
    style Math_Foundations fill:#0f172a,stroke:#3b82f6,stroke-dasharray: 5 5

    %% Subgraph: Economic & Evolutionary Pillars
    subgraph Socio_Econ ["Socio-Economic & Evolutionary Mechanics"]
        Aghion["<b>Aghion & Howitt (1992)</b><br/><i>Creative Destruction</i><br/>Non-equilibrium growth"]
        Hirsch["<b>Fred Hirsch (1977)</b><br/><i>Social Limits to Growth</i><br/>Positional goods & biological privilege"]
        Bostrom["<b>Nick Bostrom (2002)</b><br/><i>Differential Technological Dev.</i><br/>Unilateral acceleration dilemma"]
        VanValen["<b>Leigh Van Valen (1973)</b><br/><i>Red Queen Hypothesis</i><br/>Asymmetric adaptation pressure"]
        Chetty["<b>Chetty et al. (2016) / Cutler (2006)</b><br/><i>Mortality Stratification</i><br/>Income-life expectancy divergence"]
    end
    style Socio_Econ fill:#0f172a,stroke:#10b981,stroke-dasharray: 5 5

    %% Subgraph: Refuted Paradigms (Counter-Theories)
    subgraph Counter_Theories ["Refuted Counter-Paradigms & Fallacies"]
        Rogers["<b>Rogers (2003) & Berwick (2003)</b><br/><i>Diffusion Convergence Fallacy</i><br/>Universal S-curve democratization"]
        Kurzweil["<b>Kurzweil / Diamandis</b><br/><i>The Smartphone Fallacy</i><br/>Moore's Law applied to biology"]
        InSilico["<b>In Silico Trial Techno-Optimists</b><br/><i>Digital Twin Hubris</i><br/>Neural simulation replacing Phase III"]
        Generics["<b>Patent Cliff Theorists</b><br/><i>Generic Commoditization</i><br/>Biosimilars closing the gap"]
    end
    style Counter_Theories fill:#450a0a,stroke:#ef4444,stroke-width:2px

    %% Subgraph: Author's Monograph Series
    subgraph Author_Corpus ["Author's Foundational Research Series (Huynh 2026)"]
        M1["<b>Till Death Tear Us Apart</b><br/><i>Closing Window Framework</i><br/>DOI: 10.5281/zenodo.20777406"]
        M2["<b>The Unfalsifiable Critic</b><br/><i>Epistemic Asymmetry</i><br/>DOI: 10.5281/zenodo.20776160"]
        M3["<b>Biological Zero-Day</b><br/><i>Dynamic Expansion of Death</i><br/>DOI: 10.5281/zenodo.20780733"]
        M4["<b>The Closing Window</b><br/><i>Political Escalation</i><br/>DOI: 10.5281/zenodo.20785465"]
        M5["<b>The Two Biases</b><br/><i>Consumer-Tech Optimism</i><br/>DOI: 10.5281/zenodo.20792546"]
    end
    style Author_Corpus fill:#1e1b4b,stroke:#8b5cf6,stroke-width:2px

    %% Subgraph: Core Claims & Invariants
    subgraph Core_Claims ["Core Theorems & Invariants"]
        T1["<b>CLAIM-T1: Resonance Lock</b><br/>t* = (1/r_A) ln(μ_clin / λ₀) = 7.33 yrs"]
        T2["<b>CLAIM-T2: Workload Divergence</b><br/>W(30) = 594.8 years"]
        T3["<b>CLAIM-T3: Biological Stratification</b><br/>Mortality as an economic variable"]
        T4["<b>CLAIM-T4: Bottleneck Hierarchy</b><br/>μ_eff = min(μ_i) = 1.25/yr"]
        R0["<b>INVARIANT: Rule Zero</b><br/>Raw residual sequence: + + - - - - - - + - + + - + - - + + - +"]
    end
    style Core_Claims fill:#172554,stroke:#06b6d4,stroke-width:2px

    %% Edges: Mathematical Foundations -> HUB
    Whitt -->|"[THEORETICAL | DIRECTLY_SUPPORTED]"| HUB
    Kleinrock -->|"[THEORETICAL | DIRECTLY_SUPPORTED]"| HUB
    Massey -->|"[THEORETICAL | DIRECTLY_SUPPORTED]"| HUB

    %% Edges: Socio-Economic -> HUB
    Aghion -->|"[MECHANISTIC | INFERRED]"| HUB
    Hirsch -->|"[CAUSAL | DIRECTLY_SUPPORTED]"| HUB
    Bostrom -->|"[THEORETICAL | INFERRED]"| HUB
    VanValen -->|"[MECHANISTIC | INFERRED]"| HUB
    Chetty -->|"[CAUSAL | DIRECTLY_SUPPORTED]"| HUB

    %% Edges: Refuted Paradigms -> HUB (Contradictory / Refuted)
    Rogers -.->|"[CONTRADICTORY | REFUTED]"| HUB
    Kurzweil -.->|"[CONTRADICTORY | REFUTED]"| HUB
    InSilico -.->|"[CONTRADICTORY | REFUTED]"| HUB
    Generics -.->|"[CONTRADICTORY | REFUTED]"| HUB

    %% Edges: Author's Monograph Series -> HUB
    M1 ==>|"[FOUNDATIONAL_PILLAR | DIRECTLY_SUPPORTED]"| HUB
    M2 ==>|"[EPISTEMIC_IMMUNIZATION | DIRECTLY_SUPPORTED]"| HUB
    M3 ==>|"[MECHANISTIC_EXTENSION | DIRECTLY_SUPPORTED]"| HUB
    M4 ==>|"[POLITICAL_ECONOMY | DIRECTLY_SUPPORTED]"| HUB
    M5 ==>|"[COGNITIVE_BIAS_AUDIT | DIRECTLY_SUPPORTED]"| HUB

    %% Edges: HUB -> Core Claims
    HUB -->|"[PROVES | DIRECTLY_SUPPORTED]"| T1
    HUB -->|"[PROVES | DIRECTLY_SUPPORTED]"| T2
    HUB -->|"[PROVES | DIRECTLY_SUPPORTED]"| T3
    HUB -->|"[PROVES | DIRECTLY_SUPPORTED]"| T4
    HUB -->|"[ENFORCES | DIRECTLY_SUPPORTED]"| R0
```

---

## 🧭 Topological Knowledge Graph Index

### 1. Thinkers & Theoretical Paradigms
- [[Whitt_Ward_Queueing_Limits|Ward Whitt (2002)]] — Heavy-traffic limits, non-stationary queue lengths, and backlog divergence.
- [[Kleinrock_Massey_Time_Dependent|Leonard Kleinrock (1975) & William Massey (1985)]] — The workload process $V(t)$ and time-dependent Poisson arrivals.
- [[Rogers_Berwick_Diffusion_Fallacy|Everett Rogers (2003) & Donald Berwick (2003)]] — **[REFUTED]** The Neoclassical Diffusion Convergence Fallacy.
- [[Kurzweil_Smartphone_Fallacy|Ray Kurzweil & Peter Diamandis]] — **[REFUTED]** The Smartphone Fallacy (confusing silicon scaling with biological observation).
- [[Aghion_Howitt_Creative_Destruction|Philippe Aghion & Peter Howitt (1992)]] — Creative destruction and non-equilibrium growth.
- [[Hirsch_Fred_Positional_Limits|Fred Hirsch (1977)]] — Social limits to growth, positional goods, and biological privilege.
- [[Bostrom_Nick_Differential_Tech|Nick Bostrom (2002)]] — Differential technological development and the unilateral acceleration dilemma.
- [[Van_Valen_Red_Queen|Leigh Van Valen (1973)]] — The Red Queen hypothesis adapted to asymmetric technological competition.
- [[Chetty_Cutler_Mortality_Inequality|Raj Chetty (2016) & David Cutler (2006)]] — Empirical documentation of income-stratified mortality divergence.
- [[InSilico_Trialists_Epistemic_Hubris|In Silico Trialists & Digital Twin Proponents]] — **[REFUTED]** The fallacy that neural simulation replaces physical human longitudinal trials.

### 2. Author's Foundational Monograph Series (Gia Bao Huynh 2026)
- [[Huynh_2026_Till_Death_Tear_Us_Apart|Till Death Tear Us Apart: A Structural Analysis of the Longevity Asymmetry]] — Zotero: `GI2ASFMG` · DOI: `10.5281/zenodo.20777406`
- [[Huynh_2026_Unfalsifiable_Critic|The Unfalsifiable Critic: Prospective Immunization and Epistemic Asymmetry]] — Zotero: `TDKDGZHA` · DOI: `10.5281/zenodo.20776160`
- [[Huynh_2026_Biological_Zero_Day|The Biological Zero-Day Mechanism: Reclassification & Preventable Death]] — Zotero: `EIKTRBGH` · DOI: `10.5281/zenodo.20780733`
- [[Huynh_2026_Closing_Window|The Closing Window: Structural Conditions for Political Escalation]] — Zotero: `FFWLB6YX` · DOI: `10.5281/zenodo.20785465`
- [[Huynh_2026_Two_Biases|The Two Biases That Blind Governance: Consumer Optimism & Therapeutic Reasoning]] — Zotero: `GUNS4C6I` · DOI: `10.5281/zenodo.20792546`
- [[Huynh_2026_Floor_That_Does_Not_Rise|The Floor That Does Not Rise: Mathematical Proof & Five-Domain Audit]] — Zenodo DOI: `10.5281/zenodo.21335914`

### 3. Core Theorems, Claims & Invariants
- [[CLAIM_T1_Resonance_Lock_Threshold|CLAIM-T1]]: Critical transition threshold $t^* = 7.33\text{ years}$ where $\rho(t) \ge 1.0$.
- [[CLAIM_T2_Workload_Divergence|CLAIM-T2]]: Workload divergence $W(30) = 594.8\text{ years}$ under heavy-traffic queueing.
- [[CLAIM_T3_Biological_Stratification|CLAIM-T3]]: Mortality transitions from a biological invariant to an economic variable.
- [[CLAIM_T4_Bottleneck_Hierarchy|CLAIM-T4]]: Serial bottleneck theorem $\mu_{\\text{eff}} = \\min(\\mu_i) = 1.25/\\text{year}$.
- [[INVARIANT_Rule_Zero_Raw_Residuals|INVARIANT-R0]]: Rule Zero enforcement of the exact raw residual sign sequence `+ + - - - - - - + - + + - + - - + + - +`.
"""
write_file(KG_DIR / "00_Master_Mindmap_and_Cite_Network.md", master_mindmap)

# ============================================================
# 3. THINKER NODES (CONTRIBUTORS & REFUTED ADVERSARIES)
# ============================================================

# 3.1 Ward Whitt
whitt_node = """---
title: "Thinker: Ward Whitt (2002) — Heavy-Traffic Queueing Limits"
type: thinker
role: mathematical-foundation
citekey: "@Whitt2002"
tags:
  - queueing-theory
  - heavy-traffic
  - non-stationary
  - backlog-divergence
---

# Ward Whitt: Heavy-Traffic Limits & Stochastic Workload Divergence

## 1. Intellectual Profile
- **Scholar**: Ward Whitt (Columbia University)
- **Foundational Work**: *Stochastic-Process Limits: An Introduction to Stochastic-Process Limits for Heavy-Traffic Limits of Queues* (Springer, 2002).
- **Zotero Citekey**: `[[@Whitt2002]]`
- **Core Contribution**: Formalized the asymptotic behavior of queueing systems as the traffic intensity $\\rho(t) \\to 1$ and beyond, proving that queues under non-stationary heavy traffic do not experience simple linear backlog growth, but undergo diffusion-process phase transitions where waiting times diverge asymptotically.

## 2. Dialectical Role in Our Framework: FOUNDATIONAL PILLAR
Our model directly implements Whitt's heavy-traffic approximation to formalize the **Capacity–Latency Resonance Paradox**:
$$L_q(t) \\approx \\frac{\\rho(t)^2 (c_a^2 + c_s^2)}{2(1 - \\rho(t))} + \\int_0^t [\\lambda(s) - c\\mu(s)]^+ ds$$
When discovery arrivals compound exponentially ($\\lambda(t) = \\lambda_0 e^{r_A t}$), Whitt's formulation proves that the system crosses the stability threshold in finite time $t^* = \\frac{1}{r_A} \\ln\\left(\\frac{c\\mu}{\\lambda_0}\\right)$. For all $t > t^*$, the unfinished workload $W(t)$ explodes as $O(e^{r_A t})$, providing the mathematical microfoundation for the refutation of S-curve convergence.

## 3. Typed Graph Edges
- `[[Whitt_Ward_Queueing_Limits]] ────[ THEORETICAL | DIRECTLY_SUPPORTED ]────► [[CLAIM_T1_Resonance_Lock_Threshold]]`
- `[[Whitt_Ward_Queueing_Limits]] ────[ THEORETICAL | DIRECTLY_SUPPORTED ]────► [[CLAIM_T2_Workload_Divergence]]`
- `[[Whitt_Ward_Queueing_Limits]] ────[ CONTRADICTORY | DIRECTLY_SUPPORTED ]────► [[Rogers_Berwick_Diffusion_Fallacy]]`
"""
write_file(THINKERS_DIR / "Whitt_Ward_Queueing_Limits.md", whitt_node)

# 3.2 Kleinrock & Massey
kleinrock_massey_node = """---
title: "Thinker: Leonard Kleinrock (1975) & William Massey (1985) — Workload Processes"
type: thinker
role: mathematical-foundation
citekey: "@Kleinrock1975, @Massey1985"
tags:
  - queueing-systems
  - workload-process
  - time-dependent
---

# Leonard Kleinrock & William Massey: The Workload Process V(t)

## 1. Intellectual Profile
- **Scholars**: Leonard Kleinrock (UCLA, father of packet switching) & William A. Massey (Princeton University).
- **Key Works**:
  - Kleinrock, L. (1975). *Queueing Systems, Volume 1: Theory*. Wiley-Interscience.
  - Massey, W. A. (1985). "Asymptotic analysis of the time dependent M/M/1 queue." *Mathematics of Operations Research*, 10(2), 305–327.
- **Core Contribution**: Defined the virtual waiting time / workload process $V(t)$, representing the total unfinished work in a queueing system at time $t$, and formulated the asymptotic expansion of queues driven by non-stationary arrival rates.

## 2. Dialectical Role in Our Framework: FOUNDATIONAL PILLAR
Kleinrock's $V(t)$ is the central mathematical object of our paper:
$$V(t) = F(t) - D(t)$$
Each technological reset event adds a jump requirement $\\delta_k$, raising $F(t)$ and restarting the diffusion clock. Massey's time-dependent queueing analysis allows us to model time-varying arrival rates $\\lambda(t)$ without assuming steady-state stationarity, proving that transient stability cannot be maintained when arrival growth rates outpace service scaling.

## 3. Typed Graph Edges
- `[[Kleinrock_Massey_Time_Dependent]] ────[ THEORETICAL | DIRECTLY_SUPPORTED ]────► [[CLAIM_T2_Workload_Divergence]]`
- `[[Kleinrock_Massey_Time_Dependent]] ────[ MECHANISTIC | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Floor_That_Does_Not_Rise]]`
"""
write_file(THINKERS_DIR / "Kleinrock_Massey_Time_Dependent.md", kleinrock_massey_node)

# 3.3 Rogers & Berwick (REFUTED)
rogers_berwick_node = """---
title: "Thinker: Everett Rogers (2003) & Donald Berwick (2003) — The Diffusion Convergence Fallacy"
type: thinker
role: counter-theorist-refuted
citekey: "@Rogers2003, @Berwick2003"
tags:
  - diffusion-of-innovations
  - neoclassical-fallacy
  - s-curve-dogma
  - refuted
---

# Everett Rogers & Donald Berwick: The Neoclassical Diffusion Convergence Fallacy [REFUTED]

## 1. Intellectual Profile
- **Scholars**: Everett M. Rogers (Diffusion of Innovations pioneer) & Donald M. Berwick (Harvard Medical School, former CMS Administrator).
- **Key Works**:
  - Rogers, E. M. (2003). *Diffusion of Innovations* (5th ed.). Free Press.
  - Berwick, D. M. (2003). "Disseminating Innovations in Health Care." *JAMA*, 289(15), 1969–1975.
- **Their Thesis**: Technological and medical innovations inevitably follow a logistic S-curve of adoption (innovators → early adopters → early majority → late majority → laggards). They argue that initial distributional inequalities are temporary, naturally resolving through economies of scale, peer education, institutional learning, and commoditization.

## 2. Dialectical Role in Our Framework: COUNTER-PARADIGM REFUTED
Our paper formally refutes Rogers and Berwick by exposing the **Diffusion Convergence Fallacy**:
1. **The Static Horizon Error**: Rogers assumes the innovation is a *fixed, stationary target* (e.g. hybrid seed corn or boiling water). When the target compounds under recursive self-improvement ($\lambda(t) = \lambda_0 e^{r_A t}$), the frontier moves before the majority reaches the previous floor.
2. **The Incompressible Floor Error**: Berwick assumes clinical dissemination delays are purely cultural, administrative, or educational frictions that can be accelerated through institutional leadership. He ignores the **Clinical Hard Floor** ($\mu_{\\text{clin}} = 1.25/\\text{year}$): longitudinal safety endpoints in human bodies cannot be accelerated by administrative willpower without destroying statistical validity.
3. **The Result**: Instead of S-curve convergence, the system undergoes exponential queueing divergence ($W(30) = 594.8\\text{ years}$).

## 3. Typed Graph Edges
- `[[Rogers_Berwick_Diffusion_Fallacy]] ────[ CONTRADICTORY | REFUTED ]────► [[CLAIM_T1_Resonance_Lock_Threshold]]`
- `[[Rogers_Berwick_Diffusion_Fallacy]] ────[ CONTRADICTORY | REFUTED ]────► [[CLAIM_T4_Bottleneck_Hierarchy]]`
- `[[Huynh_2026_Floor_That_Does_Not_Rise]] ────[ REFUTES | DIRECTLY_SUPPORTED ]────► [[Rogers_Berwick_Diffusion_Fallacy]]`
"""
write_file(THINKERS_DIR / "Rogers_Berwick_Diffusion_Fallacy.md", rogers_berwick_node)

# 3.4 Kurzweil & Diamandis (REFUTED)
kurzweil_node = """---
title: "Thinker: Ray Kurzweil & Peter Diamandis — The Smartphone Fallacy"
type: thinker
role: counter-theorist-refuted
citekey: "@Kurzweil2005, @Diamandis2012"
tags:
  - techno-optimism
  - moores-law-conflation
  - smartphone-fallacy
  - refuted
---

# Ray Kurzweil & Peter Diamandis: The Smartphone Fallacy [REFUTED]

## 1. Intellectual Profile
- **Thinkers**: Ray Kurzweil (Author of *The Singularity Is Near*) & Peter Diamandis (Author of *Abundance*).
- **Their Thesis**: The "Law of Accelerating Returns" guarantees that every technology (including health, energy, and biotech) undergoes exponential cost reduction and universal democratization, just as supercomputers became $50 smartphones accessible to billions in the Global South.

## 2. Dialectical Role in Our Framework: COUNTER-PARADIGM REFUTED
Our paper dismantles this worldview as **The Smartphone Fallacy**:
1. **Substrate Incompatibility**: Silicon photolithography obeys geometric scaling (shrinking transistors on a 2D wafer). Human biological cells do not. A cell's transcriptional, metabolic, and apoptotic pathways operate on fixed thermodynamic and biological timescales.
2. **Symmetric vs. Asymmetric Clocks**: Smartphones diffuse rapidly because manufacturing draws on the exact same computational efficiency it creates. In longevity, synthetic discovery is digital, but safety verification is biological. The clocks are fundamentally decoupled.
3. **The Biopolitical Consequence**: Treating longevity therapeutics like smartphones blinds policymakers to the emergence of permanent biological stratification.

## 3. Typed Graph Edges
- `[[Kurzweil_Smartphone_Fallacy]] ────[ CONTRADICTORY | REFUTED ]────► [[CLAIM_T3_Biological_Stratification]]`
- `[[Huynh_2026_Two_Biases]] ────[ REFUTES | DIRECTLY_SUPPORTED ]────► [[Kurzweil_Smartphone_Fallacy]]`
"""
write_file(THINKERS_DIR / "Kurzweil_Smartphone_Fallacy.md", kurzweil_node)

# 3.5 Philippe Aghion & Peter Howitt
aghion_howitt_node = """---
title: "Thinker: Philippe Aghion & Peter Howitt (1992) — Creative Destruction Microfoundations"
type: thinker
role: economic-pillar
citekey: "@AghionHowitt1992"
tags:
  - creative-destruction
  - endogenous-growth
  - non-equilibrium
---

# Philippe Aghion & Peter Howitt: Creative Destruction & Non-Equilibrium Growth

## 1. Intellectual Profile
- **Scholars**: Philippe Aghion (Collège de France) & Peter Howitt (Brown University).
- **Foundational Work**: "A Model of Growth Through Creative Destruction." *Econometrica*, 60(2), 323–351 (1992).
- **Core Contribution**: Developed the formal microeconomic model of Schumpeterian growth, demonstrating that innovation does not lead to distributional equilibrium; each successive innovation renders existing capital and skills obsolete, creating transient monopoly rents that are displaced by subsequent innovations.

## 2. Dialectical Role in Our Framework: ECONOMIC PILLAR
Aghion & Howitt provide the microeconomic foundation for why the floor can never catch the ceiling under compounding reset events:
1. **Perpetual Displacement**: Even if older therapies experience patent cliffs and become cheap generic commodities, the economic and biological advantage resides exclusively at the frontier.
2. **Non-Equilibrium Dynamics**: The arrival of each reset event destroys the positional value of the previous floor, ensuring that absolute improvements at the bottom fail to close relative inequality gaps.

## 3. Typed Graph Edges
- `[[Aghion_Howitt_Creative_Destruction]] ────[ MECHANISTIC | INFERRED ]────► [[CLAIM_T2_Workload_Divergence]]`
- `[[Aghion_Howitt_Creative_Destruction]] ────[ THEORETICAL | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Floor_That_Does_Not_Rise]]`
"""
write_file(THINKERS_DIR / "Aghion_Howitt_Creative_Destruction.md", aghion_howitt_node)

# 3.6 Fred Hirsch
hirsch_node = """---
title: "Thinker: Fred Hirsch (1977) — Positional Goods & Social Limits to Growth"
type: thinker
role: sociological-pillar
citekey: "@Hirsch1977"
tags:
  - positional-goods
  - social-limits
  - relative-inequality
---

# Fred Hirsch: Positional Goods & The Asymmetry of Relative Advantage

## 1. Intellectual Profile
- **Scholar**: Fred Hirsch (Warwick University, former IMF Senior Advisor).
- **Foundational Work**: *Social Limits to Growth* (Harvard University Press, 1977).
- **Core Contribution**: Formulated the theory of **positional goods** — goods whose value derives strictly from their exclusivity and relative rank compared to what others possess. Proved that economic growth cannot democratize positional goods because increasing aggregate wealth simply inflates their access threshold.

## 2. Dialectical Role in Our Framework: SOCIOLOGICAL PILLAR
Hirsch explains why biological longevity and frontier AI capabilities remain acutely politically volatile even as absolute living standards rise:
1. **Health as a Positional Good**: When elite cohorts purchase access to biological age deceleration, cognitive longevity, and multi-decade disease immunity, longevity ceases to be a pure consumption good and becomes the ultimate positional asset, guaranteeing dynastic wealth preservation and intergenerational cognitive compounding.
2. **The Illusion of Democratic Lift**: Even if the median floor lives to 85 via generic metformin, if the elite frontier reaches a functional lifespan of 130, political and economic power becomes structurally asymmetric.

## 3. Typed Graph Edges
- `[[Hirsch_Fred_Positional_Limits]] ────[ CAUSAL | DIRECTLY_SUPPORTED ]────► [[CLAIM_T3_Biological_Stratification]]`
- `[[Hirsch_Fred_Positional_Limits]] ────[ MECHANISTIC | INFERRED ]────► [[Huynh_2026_Closing_Window]]`
"""
write_file(THINKERS_DIR / "Hirsch_Fred_Positional_Limits.md", hirsch_node)

# 3.7 Nick Bostrom
bostrom_node = """---
title: "Thinker: Nick Bostrom (2002) — Differential Technological Development"
type: thinker
role: governance-pillar
citekey: "@Bostrom2002"
tags:
  - differential-development
  - technological-risk
  - unilateral-acceleration
---

# Nick Bostrom: Differential Technological Development & The Acceleration Dilemma

## 1. Intellectual Profile
- **Scholar**: Nick Bostrom (Oxford University, Future of Humanity Institute).
- **Foundational Work**: "Existential Risks: Analyzing Human Extinction Scenarios and Related Hazards." *Journal of Evolution and Technology*, 9(1), 2002.
- **Core Contribution**: Formulated the principle of **Differential Technological Development**: policy should seek to accelerate risk-reducing, defensive, and restorative technologies while actively decelerating risk-generating, offensive, and disruptive technologies.

## 2. Dialectical Role in Our Framework: GOVERNANCE PILLAR
Bostrom's principle directly motivates our inquiry into whether technological deceleration is achievable:
1. **The Unilateral Deceleration Failure**: In a multipolar competitive arena, no individual actor can unilaterally decelerate the discovery frontier $\\lambda(t)$ without conceding absolute geopolitical and commercial supremacy to rival actors.
2. **The Inevitability of Resonance Lock**: Because deceleration of $\\lambda(t)$ is politically unviable, and acceleration of $\\mu_{\\text{clin}}$ is biologically impossible, the system is mathematically locked into $\\rho(t) > 1.0$ until structural translation governance is redesigned from first principles.

## 3. Typed Graph Edges
- `[[Bostrom_Nick_Differential_Tech]] ────[ THEORETICAL | INFERRED ]────► [[CLAIM_T1_Resonance_Lock_Threshold]]`
- `[[Bostrom_Nick_Differential_Tech]] ────[ MECHANISTIC | INFERRED ]────► [[Huynh_2026_Two_Biases]]`
"""
write_file(THINKERS_DIR / "Bostrom_Nick_Differential_Tech.md", bostrom_node)

# 3.8 Leigh Van Valen
van_valen_node = """---
title: "Thinker: Leigh Van Valen (1973) — The Red Queen Hypothesis"
type: thinker
role: evolutionary-pillar
citekey: "@VanValen1973"
tags:
  - red-queen
  - evolutionary-dynamics
  - asymmetric-arms-race
---

# Leigh Van Valen: The Red Queen Hypothesis in Asymmetric Technological Systems

## 1. Intellectual Profile
- **Scholar**: Leigh Van Valen (University of Chicago).
- **Foundational Work**: "A New Evolutionary Law." *Evolutionary Theory*, 1, 1–30 (1973).
- **Core Contribution**: Proposed that in co-evolving biological systems, an organism must constantly adapt, evolve, and proliferate simply to maintain its relative fitness against competing, co-evolving species ("It takes all the running you can do, to keep in the same place").

## 2. Dialectical Role in Our Framework: EVOLUTIONARY PILLAR
Our framework adapts the Red Queen dynamic to asymmetric technological diffusion:
1. **Asymmetric Red Queen**: Unlike Van Valen's symmetric co-evolution, technological discovery ($\lambda(t)$) runs on a compounding digital clock while human verification ($\mu$) is rate-limited by biological incompressibility.
2. **The Running Laggard**: The human institutional floor must accelerate its processing merely to prevent the backlog from diverging to infinity. Once $\rho(t) > 1.0$, even "running as fast as possible" results in falling exponentially behind.

## 3. Typed Graph Edges
- `[[Van_Valen_Red_Queen]] ────[ MECHANISTIC | INFERRED ]────► [[CLAIM_T2_Workload_Divergence]]`
- `[[Van_Valen_Red_Queen]] ────[ THEORETICAL | INFERRED ]────► [[Huynh_2026_Biological_Zero_Day]]`
"""
write_file(THINKERS_DIR / "Van_Valen_Red_Queen.md", van_valen_node)

# 3.9 Chetty & Cutler
chetty_cutler_node = """---
title: "Thinker: Raj Chetty (2016) & David Cutler (2006) — Mortality Stratification"
type: thinker
role: empirical-pillar
citekey: "@Chetty2016, @Cutler2006"
tags:
  - mortality-inequality
  - health-economics
  - empirical-divergence
---

# Raj Chetty & David Cutler: Empirical Documentation of Mortality Stratification

## 1. Intellectual Profile
- **Scholars**: Raj Chetty (Harvard / Opportunity Insights) & David M. Cutler (Harvard Economics).
- **Key Works**:
  - Chetty, R. et al. (2016). "The Association Between Income and Life Expectancy in the United States, 2001–2014." *JAMA*, 315(16), 1750–1766.
  - Cutler, D., Deaton, A., & Lleras-Muney, A. (2006). "The Determinants of Mortality." *Journal of Economic Perspectives*, 20(3), 97–120.
- **Core Contribution**: Proved that the gap in life expectancy between the top 1% and bottom 1% of income earners in the United States exceeds 14.6 years for men and 10.1 years for women, and that this gap has widened monotonically across the 21st century despite aggregate advances in medical science.

## 2. Dialectical Role in Our Framework: EMPIRICAL PILLAR
Chetty and Cutler provide the historical empirical baseline proving that medical advance does *not* automatically compress health inequality:
1. **Empirical Grounding**: Even before radical AI-driven longevity interventions, existing healthcare translation already exhibited divergence rather than convergence.
2. **Resonance Amplification**: When exponential ARSI longevity therapies enter this pre-existing stratified landscape, the gap transitions from a 15-year divergence into a multi-decade biological chasm.

## 3. Typed Graph Edges
- `[[Chetty_Cutler_Mortality_Inequality]] ────[ CAUSAL | DIRECTLY_SUPPORTED ]────► [[CLAIM_T3_Biological_Stratification]]`
- `[[Chetty_Cutler_Mortality_Inequality]] ────[ EMPIRICAL_CORROBORATION | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Till_Death_Tear_Us_Apart]]`
"""
write_file(THINKERS_DIR / "Chetty_Cutler_Mortality_Inequality.md", chetty_cutler_node)

# 3.10 In Silico Trialists (REFUTED)
insilico_node = """---
title: "Thinker: In Silico Trialists & Digital Twin Proponents — The Simulation Hubris"
type: thinker
role: counter-theorist-refuted
citekey: "@InSilico2024"
tags:
  - in-silico-trials
  - digital-twins
  - regulatory-hubris
  - refuted
---

# In Silico Clinical Trialists: The Digital Twin Hubris [REFUTED]

## 1. Intellectual Profile
- **Proponents**: Computational biology techno-optimists and commercial in silico simulation vendors.
- **Their Thesis**: Advancements in AI foundation models, multi-scale biological simulations, and synthetic patient digital twins will render physical human Phase I–III clinical trials obsolete, allowing drugs to be validated computationally in minutes rather than decades.

## 2. Dialectical Role in Our Framework: COUNTER-PARADIGM REFUTED
Our paper exposes the fatal epistemological flaw of in silico validation:
1. **Simulation ≠ Proof**: A neural network simulation is an inductive extrapolation based on prior training data. It cannot predict novel, emergent off-target toxicities, delayed epigenetic drift, or multi-decade autoimmune cross-reactivities in a live human organism.
2. **The Regulatory Impossibility**: No regulatory agency (FDA, EMA) can legally or ethically grant marketing authorization for irreversible human genome modification or lifespan interventions without live human survival data.
3. **The Hard Floor Persists**: In silico tools dramatically accelerate upstream discovery ($\lambda(t)$), but downstream safety verification remains stubbornly locked to the **Clinical Hard Floor** ($\mu_{\\text{clin}} = 1.25/\\text{year}$), exacerbating rather than curing queueing collapse.

## 3. Typed Graph Edges
- `[[InSilico_Trialists_Epistemic_Hubris]] ────[ CONTRADICTORY | REFUTED ]────► [[CLAIM_T4_Bottleneck_Hierarchy]]`
- `[[Huynh_2026_Floor_That_Does_Not_Rise]] ────[ REFUTES | DIRECTLY_SUPPORTED ]────► [[InSilico_Trialists_Epistemic_Hubris]]`
"""
write_file(THINKERS_DIR / "InSilico_Trialists_Epistemic_Hubris.md", insilico_node)

# ============================================================
# 4. AUTHOR MONOGRAPH NODES (GIA BAO HUYNH 2026)
# ============================================================

# M1: Till Death Tear Us Apart
m1_node = """---
title: "Monograph: Till Death Tear Us Apart — The Longevity Asymmetry"
type: author-monograph
author: "Gia Bao Huynh"
year: 2026
zotero_key: "GI2ASFMG"
doi: "10.5281/zenodo.20777406"
tags:
  - foundational-monograph
  - closing-window
  - biological-stratification
---

# Till Death Tear Us Apart: A Structural Analysis of the Longevity Asymmetry and the Closing Window

- **Author**: Gia Bao Huynh
- **Zotero Key**: `GI2ASFMG`
- **Permanent DOI**: [10.5281/zenodo.20777406](https://doi.org/10.5281/zenodo.20777406)
- **Role in Research Series**: Foundational biopolitical treatise establishing the structural reality of the longevity asymmetry.

## 1. Abstract & Core Thesis
Examines the emergence of biological life extension as an unprecendented driver of structural inequality. Argues that unlike prior technological divisions, biological inequality is irreversible once established: cohorts that receive early biological age deceleration compound their biological and cognitive advantage over calendar time, permanently severing the shared demographic foundation of democratic institutions.

## 2. Dialectical Connection to "The Floor That Does Not Rise"
*Till Death Tear Us Apart* established the biopolitical stakes; *The Floor That Does Not Rise* supplies the mathematical queueing proof, demonstrating that the divergence is not a transient policy failure but the inevitable outcome of non-stationary queueing collapse ($\rho(t) > 1.0$).

## 3. Typed Graph Edges
- `[[Huynh_2026_Till_Death_Tear_Us_Apart]] ────[ FOUNDATIONAL_PILLAR | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Floor_That_Does_Not_Rise]]`
- `[[Huynh_2026_Till_Death_Tear_Us_Apart]] ────[ CAUSAL | DIRECTLY_SUPPORTED ]────► [[CLAIM_T3_Biological_Stratification]]`
"""
write_file(MONOGRAPHS_DIR / "Huynh_2026_Till_Death_Tear_Us_Apart.md", m1_node)

# M2: The Unfalsifiable Critic
m2_node = """---
title: "Monograph: The Unfalsifiable Critic — Epistemic Asymmetry"
type: author-monograph
author: "Gia Bao Huynh"
year: 2026
zotero_key: "TDKDGZHA"
doi: "10.5281/zenodo.20776160"
tags:
  - epistemic-asymmetry
  - prospective-immunization
  - falsifiability
---

# The Unfalsifiable Critic: Prospective Immunization, Epistemic Asymmetry, and the Capacity–Latency Resonance Impossibility

- **Author**: Gia Bao Huynh
- **Zotero Key**: `TDKDGZHA`
- **Permanent DOI**: [10.5281/zenodo.20776160](https://doi.org/10.5281/zenodo.20776160)
- **Role in Research Series**: Epistemological defense establishing the falsifiability criteria of the research program.

## 1. Abstract & Core Thesis
Analyzes the rhetorical strategies used by critics to immunize neoclassical diffusion theories against empirical counterevidence. Proves that dismissing biological divergence as "merely a temporary delay before the inevitable S-curve" is an unfalsifiable prospective defense. Establishes the five exact empirical falsification conditions required for rigorous scientific debate.

## 2. Dialectical Connection to "The Floor That Does Not Rise"
Supplies the epistemological framework for Section XI (Falsification Conditions) and establishes **Rule Zero** (The Raw Residual Invariant).

## 3. Typed Graph Edges
- `[[Huynh_2026_Unfalsifiable_Critic]] ────[ EPISTEMIC_IMMUNIZATION | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Floor_That_Does_Not_Rise]]`
- `[[Huynh_2026_Unfalsifiable_Critic]] ────[ ENFORCES | DIRECTLY_SUPPORTED ]────► [[INVARIANT_Rule_Zero_Raw_Residuals]]`
"""
write_file(MONOGRAPHS_DIR / "Huynh_2026_Unfalsifiable_Critic.md", m2_node)

# M3: The Biological Zero-Day
m3_node = """---
title: "Monograph: The Biological Zero-Day Mechanism"
type: author-monograph
author: "Gia Bao Huynh"
year: 2026
zotero_key: "EIKTRBGH"
doi: "10.5281/zenodo.20780733"
tags:
  - biological-zero-day
  - discovery-acceleration
  - preventable-death
---

# The Biological Zero-Day Mechanism: Reclassification, Discovery Acceleration, and the Dynamic Expansion of Preventable Death

- **Author**: Gia Bao Huynh
- **Zotero Key**: `EIKTRBGH`
- **Permanent DOI**: [10.5281/zenodo.20780733](https://doi.org/10.5281/zenodo.20780733)
- **Role in Research Series**: Formulates the concept of biological vulnerability windows analogous to software zero-days.

## 1. Abstract & Core Thesis
Demonstrates that accelerating scientific discovery dynamically reclassifies natural deaths into preventable deaths faster than institutional medicine can deploy remedies. Introduces the concept of the "Biological Zero-Day" — the interval between the discovery of an actionable life-extension target and its verified clinical delivery.

## 2. Dialectical Connection to "The Floor That Does Not Rise"
Directly links the empirical cybersecurity analysis (CVE weaponization windows) to the longevity clinical trial bottleneck.

## 3. Typed Graph Edges
- `[[Huynh_2026_Biological_Zero_Day]] ────[ MECHANISTIC_EXTENSION | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Floor_That_Does_Not_Rise]]`
- `[[Huynh_2026_Biological_Zero_Day]] ────[ THEORETICAL | DIRECTLY_SUPPORTED ]────► [[CLAIM_T4_Bottleneck_Hierarchy]]`
"""
write_file(MONOGRAPHS_DIR / "Huynh_2026_Biological_Zero_Day.md", m3_node)

# M4: The Closing Window
m4_node = """---
title: "Monograph: The Closing Window — Structural Conditions for Political Escalation"
type: author-monograph
author: "Gia Bao Huynh"
year: 2026
zotero_key: "FFWLB6YX"
doi: "10.5281/zenodo.20785465"
tags:
  - political-economy
  - institutional-crisis
  - escalation
---

# The Closing Window: Structural Conditions for Political Escalation Under Biological Stratification

- **Author**: Gia Bao Huynh
- **Zotero Key**: `FFWLB6YX`
- **Permanent DOI**: [10.5281/zenodo.20785465](https://doi.org/10.5281/zenodo.20785465)
- **Role in Research Series**: Political economy and game-theoretic analysis of institutional stability.

## 1. Abstract & Core Thesis
Models the geopolitical and civil conflict risks that emerge when mortality becomes recognized as an economic variable. Proves that there exists a finite temporal window during which democratic consensus can regulate biological translation before elite longevity entrenchment closes the window permanently.

## 2. Dialectical Connection to "The Floor That Does Not Rise"
Traces the downstream political and institutional consequences of the queueing divergence proved in *The Floor That Does Not Rise*.

## 3. Typed Graph Edges
- `[[Huynh_2026_Closing_Window]] ────[ POLITICAL_ECONOMY | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Floor_That_Does_Not_Rise]]`
- `[[Huynh_2026_Closing_Window]] ────[ CAUSAL | INFERRED ]────► [[CLAIM_T3_Biological_Stratification]]`
"""
write_file(MONOGRAPHS_DIR / "Huynh_2026_Closing_Window.md", m4_node)

# M5: The Two Biases
m5_node = """---
title: "Monograph: The Two Biases That Blind Governance"
type: author-monograph
author: "Gia Bao Huynh"
year: 2026
zotero_key: "GUNS4C6I"
doi: "10.5281/zenodo.20792546"
tags:
  - cognitive-biases
  - consumer-optimism
  - therapeutic-reasoning
---

# The Two Biases That Blind Governance: How Consumer-Technology Optimism and Therapeutic Reasoning Mistake an Unbounded Process for a Bounded Disease

- **Author**: Gia Bao Huynh
- **Zotero Key**: `GUNS4C6I`
- **Permanent DOI**: [10.5281/zenodo.20792546](https://doi.org/10.5281/zenodo.20792546)
- **Role in Research Series**: Deconstruction of governance and regulatory cognitive traps.

## 1. Abstract & Core Thesis
Identifies two systemic intellectual traps paralyzing health policy:
1. **Consumer-Technology Optimism**: Blindly assuming health technologies follow smartphone cost-reduction trajectories.
2. **Therapeutic Reasoning**: Mistaking aging for a discrete, treatable disease rather than an unbounded non-stationary queueing process.

## 2. Dialectical Connection to "The Floor That Does Not Rise"
Supplies the critique of the *Smartphone Fallacy* and explains why institutional policymakers consistently misinterpret empirical healthcare data.

## 3. Typed Graph Edges
- `[[Huynh_2026_Two_Biases]] ────[ COGNITIVE_BIAS_AUDIT | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Floor_That_Does_Not_Rise]]`
- `[[Huynh_2026_Two_Biases]] ────[ REFUTES | DIRECTLY_SUPPORTED ]────► [[Kurzweil_Smartphone_Fallacy]]`
"""
write_file(MONOGRAPHS_DIR / "Huynh_2026_Two_Biases.md", m5_node)

# M6: The Floor That Does Not Rise (Central Manuscript)
m6_node = """---
title: "Monograph: The Floor That Does Not Rise (Central Theorem)"
type: author-monograph
author: "Gia Bao Huynh"
year: 2026
doi: "10.5281/zenodo.21335914"
tags:
  - central-manuscript
  - queueing-proof
  - empirical-audit
---

# The Floor That Does Not Rise: Reset Events, Non-Stationary Queueing Collapse, and the Hard–Soft Floor Distinction

- **Author**: Gia Bao Huynh
- **Permanent DOI**: [10.5281/zenodo.21335914](https://doi.org/10.5281/zenodo.21335914)
- **Role in Research Series**: The central mathematical, queueing-theoretic, and empirical proof paper of the Longevity Asymmetry program.

## 1. Abstract & Master Claims
Formulates the Capacity–Latency Resonance Paradox within a 13-model non-stationary $M_t/G/1$ queueing framework. Demonstrates that under exponential discovery compounding ($\lambda(t) = \lambda_0 e^{r_A t}$), system utilization crosses $\rho(t) > 1.0$ at $t^* = 7.33\text{ years}$, causing backlog workload $W(t)$ to explode to $594.8\text{ years}$ at $t=30$. Empirically validated across 5 independent domains (Housing null case, METR AI capability, Anthropic distillation, CALERIE longevity biotech, and CISA cybersecurity).

## 2. Connected Nodes
- Proves: `[[CLAIM_T1_Resonance_Lock_Threshold]]`
- Proves: `[[CLAIM_T2_Workload_Divergence]]`
- Proves: `[[CLAIM_T3_Biological_Stratification]]`
- Proves: `[[CLAIM_T4_Bottleneck_Hierarchy]]`
- Enforces: `[[INVARIANT_Rule_Zero_Raw_Residuals]]`
"""
write_file(MONOGRAPHS_DIR / "Huynh_2026_Floor_That_Does_Not_Rise.md", m6_node)

# ============================================================
# 5. CORE CLAIM & INVARIANT NODES
# ============================================================

# Claim T1
t1_node = """---
title: "Claim: CLAIM-T1 — Resonance Lock Transition Threshold"
type: claim
status: DIRECTLY_SUPPORTED
tags:
  - theorem
  - resonance-lock
  - queueing-threshold
---

# CLAIM-T1: Finite-Time Transition to Resonance Lock

## 1. Proposition Statement
Under exponential discovery compounding $\\lambda(t) = \\lambda_0 e^{r_A t}$ and bounded service capacity $\\mu_{\\text{clin}}$, system utilization $\\rho(t) = \\frac{\\lambda(t)}{c \\mu_{\\text{clin}}}$ crosses unity in finite time:
$$t^* = \\frac{1}{r_A} \\ln\\left(\\frac{c \\mu_{\\text{clin}}}{\\lambda_0}\\right)$$

## 2. Empirical Calibration & Proof
- Baseline parameters: $\\lambda_0 = 0.20/\\text{year}$, $r_A = 0.25/\\text{year}$, $\\mu_{\\text{clin}} = 1.25/\\text{year}$, $c = 1$.
- Transition threshold calculation:
  $$t^* = \\frac{1}{0.25} \\ln\\left(\\frac{1.25}{0.20}\\right) = 4 \\cdot \\ln(6.25) \\approx 4 \\cdot 1.8326 = 7.33\\text{ years}$$
- Epistemic Status: **DIRECTLY_SUPPORTED** (Analytical deduction in $M_t/G/1$ queueing framework).

## 3. Connected Nodes
- Supported by: `[[Whitt_Ward_Queueing_Limits]]`
- Formulated in: `[[Huynh_2026_Floor_That_Does_Not_Rise]]`
- Refutes: `[[Rogers_Berwick_Diffusion_Fallacy]]`
"""
write_file(CLAIMS_DIR / "CLAIM_T1_Resonance_Lock_Threshold.md", t1_node)

# Claim T2
t2_node = """---
title: "Claim: CLAIM-T2 — Exponential Workload Divergence"
type: claim
status: DIRECTLY_SUPPORTED
tags:
  - theorem
  - workload-divergence
  - heavy-traffic
---

# CLAIM-T2: Exponential Workload Divergence for All t > t*

## 1. Proposition Statement
For all $t > t^*$, the expected unfinished workload process $W(t) = F(t) - D(t)$ diverges exponentially as $O(e^{r_A t})$, violating S-curve diffusion convergence.

## 2. Empirical Numerical Trajectory
Under numerical integration of the non-homogeneous workload differential equation:
- $t = 0$: $W(0) = 0.00\\text{ years}$ (Equilibrium)
- $t = 10$: $W(10) = 3.84\\text{ years}$ (Nascent Backlog)
- $t = 20$: $W(20) = 48.91\\text{ years}$ (Structural Decoupling)
- $t = 30$: $W(30) = 594.80\\text{ years}$ (Complete Catastrophic Divergence)
- Epistemic Status: **DIRECTLY_SUPPORTED** (Numerical integration & heavy-traffic limit theorems).

## 3. Connected Nodes
- Supported by: `[[Whitt_Ward_Queueing_Limits]]`, `[[Kleinrock_Massey_Time_Dependent]]`
- Refutes: `[[Rogers_Berwick_Diffusion_Fallacy]]`, `[[Kurzweil_Smartphone_Fallacy]]`
"""
write_file(CLAIMS_DIR / "CLAIM_T2_Workload_Divergence.md", t2_node)

# Claim T3
t3_node = """---
title: "Claim: CLAIM-T3 — Biological Stratification of Mortality"
type: claim
status: DIRECTLY_SUPPORTED
tags:
  - biopolitics
  - mortality-stratification
  - economic-variable
---

# CLAIM-T3: Transition of Mortality from a Biological Invariant into an Economic Variable

## 1. Proposition Statement
Under prolonged Resonance Lock ($t \\gg t^*$), human mortality ceases to be a universal biological invariant shared equally across the species; it transitions into a class-stratified economic variable.

## 2. Empirical Corroboration
- Supported by Chetty et al. (2016) documenting a pre-existing 14.6-year life expectancy gap between top and bottom 1% income tiers.
- Corroborated by our empirical price/access stratification table:
  - Generic Metformin: $4/mo (Affordability index 0.98, unvalidated for longevity).
  - Off-label Rapamycin: $65/mo (Affordability index 0.675, off-label risk).
  - Concierge Longevity Clinics: $1,250–$10,000/mo (Affordability index 0.00, elite cash-pay isolation).
- Epistemic Status: **DIRECTLY_SUPPORTED**.

## 3. Connected Nodes
- Corroborated by: `[[Chetty_Cutler_Mortality_Inequality]]`, `[[Hirsch_Fred_Positional_Limits]]`
- Formulated in: `[[Huynh_2026_Till_Death_Tear_Us_Apart]]`
"""
write_file(CLAIMS_DIR / "CLAIM_T3_Biological_Stratification.md", t3_node)

# Claim T4
t4_node = """---
title: "Claim: CLAIM-T4 — The Four Bottleneck Hierarchy & Serial Bottleneck Theorem"
type: claim
status: DIRECTLY_SUPPORTED
tags:
  - bottleneck-hierarchy
  - serial-bottleneck
  - hard-floor
---

# CLAIM-T4: The Four Bottleneck Hierarchy & Serial Bottleneck Incompressibility

## 1. Proposition Statement
The diffusion floor is structured as a serial four-stage pipeline:
1. **Clinical Hard Floor (Incompressible)**: $\\mu_{\\text{clin}} = 1.25/\\text{year}$
2. **Manufacturing Semi-Soft Floor**: $\\mu_{\\text{mfg}} = 2.50/\\text{year}$
3. **Regulatory Soft Floor**: $\\mu_{\\text{reg}} = 3.00/\\text{year}$
4. **Distribution Soft Floor**: $\\mu_{\\text{dist}} = 4.00/\\text{year}$

By the Serial Bottleneck Theorem, effective throughput is governed strictly by the infimum:
$$\\mu_{\\text{eff}} = \\min(\\mu_i) = \\mu_{\\text{clin}} = 1.25/\\text{year}$$

## 2. Policy Corollary
Capital subsidies to soft floors (e.g. accelerating FDA paperwork or subsidizing generic manufacturing) produce zero increase in effective throughput $\\mu_{\\text{eff}}$ as long as the Clinical Hard Floor binds. Interventions accumulate in front of the clinical trial barrier.

## 3. Connected Nodes
- Refutes: `[[InSilico_Trialists_Epistemic_Hubris]]`, `[[Rogers_Berwick_Diffusion_Fallacy]]`
- Formulated in: `[[Huynh_2026_Floor_That_Does_Not_Rise]]`
"""
write_file(CLAIMS_DIR / "CLAIM_T4_Bottleneck_Hierarchy.md", t4_node)

# Invariant Rule Zero
r0_node = """---
title: "Invariant: Rule Zero — The Raw Residual Invariant"
type: invariant
status: ENFORCED
tags:
  - rule-zero
  - raw-residuals
  - empirical-rigor
  - lull-detection
---

# INVARIANT-R0: The Raw Residual Invariant (Rule Zero)

## 1. Operational Mandate
> **RULE ZERO**: No model, regression script, or theoretical visualization may present smoothed, monotonic, or idealized curves of capability expansion without providing the point-by-point raw residuals alongside the empirical observations.

## 2. The March–October 2024 Lull Signature
Every capability claim must explicitly confront the March–October 2024 empirical lull.
The exact empirical residual sign sequence across the evaluated frontier models:
$$\\mathbf{+ \\quad + \\quad - \\quad - \\quad - \\quad - \\quad - \\quad - \\quad + \\quad - \\quad + \\quad + \\quad - \\quad + \\quad - \\quad - \\quad + \\quad + \\quad - \\quad +}$$
must be preserved without post-hoc smoothing, moving-average erasure, or outlier filtering.

## 3. Significance
This sequence contains an unbroken run of six consecutive models below trend (Claude 3 Haiku, Gemini 1.5 Pro, Llama 3 70B, GPT-4o, Claude 3.5 Sonnet, Llama 3 405B), disproving naive monotonic acceleration narratives.

## 4. Connected Nodes
- Enforced by: `[[Huynh_2026_Unfalsifiable_Critic]]`
- Validated in: `[[Huynh_2026_Floor_That_Does_Not_Rise]]`
"""
write_file(CLAIMS_DIR / "INVARIANT_Rule_Zero_Raw_Residuals.md", r0_node)

print("\n" + "="*60)
print("COMPLETED KNOWLEDGE GRAPH GENERATION")
print("="*60)
"""
"""
