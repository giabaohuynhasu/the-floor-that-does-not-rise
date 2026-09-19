import os
import sys
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"c:\Users\nswcl\.gemini\antigravity-ide\scratch\the-floor-that-does-not-rise")

def ensure_dir(d: Path):
    d.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# PROJECT 2: ERI (INSTITUTIONAL ENDURANCE SERIES / ENTROPY-RESISTANT INSTITUTIONS)
# ==============================================================================
def build_eri():
    eri_dir = BASE_DIR / "knowledge_graph_eri"
    thinkers_dir = eri_dir / "thinkers"
    monographs_dir = eri_dir / "monographs"
    claims_dir = eri_dir / "claims"
    
    for d in [eri_dir, thinkers_dir, monographs_dir, claims_dir]:
        ensure_dir(d)

    # 1. Master Mindmap & Citation Network
    master_content = """---
title: "ERI Master Mindmap & Dialectic Citation Network: Institutional Endurance Series"
author: "Gia Bao Huynh (Jun Huynh)"
affiliation: "Independent Researcher, Ho Chi Minh City, Vietnam"
target_publisher: "Yale University Press (3-Volume Series Proposal)"
notebooklm_uuid: "ad858f22-d53b-48b8-a0fb-0b128e451ec4"
locked_baseline: "N=6 fsQCA (Tang, Morocco, Nigeria, Tunisia, Japan, Comparative Anchor)"
fsqca_solution: "Collapse = (O * M) + (M * ~B) [Consistency: 0.75, Coverage: 0.75]"
version: "2.0-Production"
date: "2026-09-20"
tags:
  - institutional-endurance
  - fsqca
  - institutional-entropy
  - sovereign-override
  - mediation-elasticity
  - comparative-politics
---

# ERI Master Mindmap & Dialectic Citation Network

> [!IMPORTANT]
> **RULE ZERO (SUPREME DIRECTIVE)**: The locked $N=6$ fsQCA baseline table and truth-table solution (`Collapse = (O * M) + (M * ~B)` at consistency=0.75, coverage=0.75) must NEVER be altered, smoothed, or re-coded silently. Tang Dynasty citation MUST be **Dardess (1973) *Conquerors and Confucians*** (NOT 1994). Direct Sovereign Override ($O$) alone is *insufficient* for institutional collapse; Mediation Structure ($M$) is the necessary nexus.

```mermaid
graph TD
    subgraph ERI_Core ["ERI Core Architecture (Yale 3-Volume Series)"]
        VOL1["Volume I: Mechanics of Institutional Endurance<br/>Entropy, Mediation, & Boundary Limits"]
        VOL2["Volume II: Comparative fsQCA Calibration<br/>The Locked N=6 Baseline & Empirical Cases"]
        VOL3["Volume III: Architecture of Longevity<br/>Sovereign Limits & Post-Collapse Succession"]
    end

    subgraph Core_Claims ["Core Formal Invariants"]
        CLM1["Claim 1: The Locked N=6 fsQCA Baseline<br/>Collapse = (O * M) + (M * ~B)"]
        CLM2["Claim 2: Sovereign Override Insufficiency<br/>O alone cannot collapse an institution"]
        CLM3["Claim 3: Mediation Elasticity as Necessary Nexus<br/>M failure triggers systemic cascade"]
        CLM4["Claim 4: Institutional Entropy Rate<br/>dS_inst / dt > 0 without active work"]
    end

    subgraph Contributed_Thinkers ["Foundational & Corroborating Thinkers (Contributed)"]
        DARDESS["John W. Dardess (1973)<br/>Conquerors and Confucians<br/>[FOUNDATIONAL_EMPIRICS | ACCEPTED]"]
        DOWER["John W. Dower (1999)<br/>Embracing Defeat<br/>[BUREAUCRATIC_CONTINUITY | ACCEPTED]"]
        PERKINS["Kenneth J. Perkins (2004)<br/>A History of Modern Tunisia<br/>[PROTECTORATE_DYNAMICS | ACCEPTED]"]
        LUGARD["Lord Frederick Lugard (1922)<br/>Dual Mandate in British Tropical Africa<br/>[INDIRECT_RULE_MEDIATION | ACCEPTED]"]
        PERHAM["Margery Perham (1937)<br/>Native Administration in Nigeria<br/>[DECENTRALIZED_INSTABILITY | ACCEPTED]"]
        BURKE["Edmund Burke III (1976)<br/>Prelude to Protectorate in Morocco<br/>[MAKHZEN_RESILIENCE | ACCEPTED]"]
        PENNELL["C.R. Pennell (2000)<br/>Morocco Since 1830<br/>[SHERIFIAN_LEGITIMACY | ACCEPTED]"]
        RAGIN["Charles C. Ragin (2000/2008)<br/>Fuzzy-Set Qualitative Comparative Analysis<br/>[FORMAL_METHODOLOGY | ACCEPTED]"]
        NORTH["Douglass C. North (1990)<br/>Institutions, Institutional Change<br/>[CREDIBLE_COMMITMENT | ACCEPTED]"]
        SKOCPOL["Theda Skocpol (1979)<br/>States and Social Revolutions<br/>[STRUCTURAL_AUTONOMY | ACCEPTED]"]
        WEBER["Max Weber (1922)<br/>Economy and Society<br/>[LEGAL_RATIONAL_BUREAUCRACY | ACCEPTED]"]
    end

    subgraph Countered_Thinkers ["Contrasted & Refuted Thinkers (Countered)"]
        ACEMOGLU["Acemoglu & Robinson (2012)<br/>Why Nations Fail<br/>[CRITIQUED: Crude Binary Institutionalism]"]
        LIPSET["Seymour Martin Lipset (1959)<br/>Modernization Theory<br/>[REFUTED: Linear Democratic Inevitability]"]
        PRIN_AGENT["Crude Principal-Agent Models<br/>Zero-Cost Transmission Assumptions<br/>[REJECTED: Ignores Mediation Friction]"]
    end

    %% Dialectic Edges
    VOL1 --> CLM2
    VOL1 --> CLM4
    VOL2 --> CLM1
    VOL2 --> CLM3
    VOL3 --> CLM2

    DARDESS -->|"[ PROVIDES_TANG_EVIDENCE | ACCEPTED ]"| CLM1
    DOWER -->|"[ PROVIDES_JAPAN_EVIDENCE | ACCEPTED ]"| CLM1
    PERKINS -->|"[ PROVIDES_TUNISIA_EVIDENCE | ACCEPTED ]"| CLM1
    LUGARD -->|"[ PROVIDES_NIGERIA_EVIDENCE | ACCEPTED ]"| CLM1
    BURKE -->|"[ PROVIDES_MOROCCO_EVIDENCE | ACCEPTED ]"| CLM1
    RAGIN -->|"[ PROVIDES_QCA_LOGIC | ACCEPTED ]"| CLM1
    NORTH -->|"[ FOUNDS_COMMITMENT_THEORY | EXTENDED ]"| VOL1
    SKOCPOL -->|"[ PROVIDES_STATE_AUTONOMY | EXTENDED ]"| VOL2
    WEBER -->|"[ DEFINES_BUREAUCRACY | EXTENDED ]"| VOL1

    ACEMOGLU -.->|"[ REFUTED_BY | INSUFFICIENT ]"| CLM3
    LIPSET -.->|"[ FALSIFIED_BY | REJECTED ]"| CLM4
    PRIN_AGENT -.->|"[ OVERTURNED_BY | FRICTIONLESS_FLAW ]"| CLM2

    %% Cross-Project Bridges
    ALRP_BRIDGE["Cross-Project Link: ALRP<br/>Mediation Latency = Capacity-Latency Paradox"]
    CLM3 <==>|"[ FORMAL_ISOMORPHISM | MUTUAL_REINFORCING ]"| ALRP_BRIDGE
```

## The Locked $N=6$ fsQCA Truth Table
| Case | Sovereign Override ($O$) | Mediation Failure ($M$) | Bureaucratic Boundary ($B$) | Institutional Collapse ($Y$) | Historical Citation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Tang Dynasty** (Late 9th c.) | 0.5 | 0.5 | 0.8 | 0.5 | Dardess (1973) *Conquerors and Confucians* |
| **Morocco** (19th-20th c. Makhzen) | 0.8 | 0.2 | 0.5 | 0.5 | Burke (1976); Pennell (2000) |
| **Nigeria** (Colonial Indirect Rule) | 0.7 | 0.8 | 0.3 | 0.9 | Lugard (1922); Perham (1937) |
| **Tunisia** (French Protectorate) | 0.6 | 0.7 | 0.4 | 0.8 | Perkins (2004) |
| **Japan** (Meiji & Post-WWII) | 0.2 | 0.1 | 0.9 | 0.1 | Dower (1999) |
| **Comparative Anchor** | 0.4 | 0.5 | 0.6 | 0.3 | Cross-regional Synthetic Baseline |

**Boolean Minimization**:
$$\text{Collapse} = (O \cdot M) + (M \cdot \sim B)$$
- **Consistency**: 0.75
- **Coverage**: 0.75
- **Crucial Theoretical Insight**: Direct Sovereign Override ($O$) appears in the collapse solution *only in conjunction with Mediation Failure ($M$)*. When $M$ is resilient ($M \le 0.2$), even massive sovereign overreach ($O = 0.8$, Morocco) does NOT produce full institutional collapse ($Y = 0.5$). Conversely, when $M$ is broken ($M \ge 0.7$) and bureaucratic boundaries erode ($\sim B$), collapse is near certain ($Y \ge 0.8$), regardless of the sovereign's intent.
"""
    (eri_dir / "00_Master_Mindmap_and_Cite_Network_ERI.md").write_text(master_content, encoding="utf-8")

    # 2. Thinkers Cards
    thinkers_data = [
        ("dardess_1973", "John W. Dardess", "1973", "Sinology / Institutional History",
         "Conquerors and Confucians: Aspects of Political Change in Late Yüan / Imperial China",
         "Dardess demonstrates that the collapse of imperial bureaucratic endurance was not caused by external nomadic pressure alone, but by the structural decay of the civil service mediation layer under factionalized court intervention.",
         "Dardess focuses primarily on the late Yüan-Ming transition; ERI extracts his empirical mechanics and formalizes them into the fsQCA Tang baseline (O=0.5, M=0.5, B=0.8, Y=0.5), proving that mediation degradation precedes dynastic terminal collapse.",
         "[ PROVIDES_TANG_EVIDENCE | ACCEPTED ]"),
        
        ("dower_1999", "John W. Dower", "1999", "Modern Japanese History / State Formation",
         "Embracing Defeat: Japan in the Wake of World War II",
         "Dower establishes the astounding resilience of the Japanese ministerial bureaucracy through both the Meiji modernization and the MacArthur SCAP occupation, showing that the core civil apparatus survived regime decapitation.",
         "Dower describes this as historical contingency; ERI formalizes it as the gold-standard anchor of high Bureaucratic Boundary (B=0.9) and minimal Mediation Failure (M=0.1), keeping Collapse at Y=0.1 even under catastrophic military defeat.",
         "[ PROVIDES_JAPAN_EVIDENCE | ACCEPTED ]"),

        ("perkins_2004", "Kenneth J. Perkins", "2004", "North African History / Colonial Institutions",
         "A History of Modern Tunisia",
         "Perkins charts how the French protectorate retained the Beylical decree apparatus while subordinating native administrative mediation, creating dual-track governance that hollowed domestic institutional capacity.",
         "ERI codes Perkins's empirical record into the locked fsQCA case (O=0.6, M=0.7, B=0.4, Y=0.8), demonstrating how protectorate bypass of mediation structures drives institutional collapse.",
         "[ PROVIDES_TUNISIA_EVIDENCE | ACCEPTED ]"),

        ("lugard_1922", "Lord Frederick Lugard", "1922", "British Colonial Administration",
         "The Dual Mandate in British Tropical Africa",
         "Lugard articulated the doctrine of 'Indirect Rule', arguing that colonial sovereignty could achieve stability by co-opting native emirs and chiefs as non-sovereign administrative intermediaries.",
         "ERI uses Lugard's architecture as empirical proof of structural fragility: when indirect rule hollowed indigenous bureaucratic legitimacy while preventing modern civil service boundaries (B=0.3, M=0.8), it generated extreme collapse fragility (Y=0.9).",
         "[ PROVIDES_NIGERIA_EVIDENCE | ACCEPTED ]"),

        ("burke_1976", "Edmund Burke III", "1976", "Maghribi History / Political Sociology",
         "Prelude to Protectorate in Morocco: Precolonial Protest and Resistance, 1860-1912",
         "Burke documents the unique resilience of the Moroccan Makhzen, where religious-traditional mediation cushioned sovereign extraction during intense foreign pressure.",
         "Burke's detailed historical sociological account provides the empirical grounding for Morocco's calibration (O=0.8, M=0.2, B=0.5, Y=0.5), proving that robust traditional mediation structures insulate against sovereign override collapse.",
         "[ PROVIDES_MOROCCO_EVIDENCE | ACCEPTED ]"),

        ("ragin_2000", "Charles C. Ragin", "2000/2008", "Comparative Methodology / Set-Theoretic Methods",
         "Fuzzy-Set Social Science (2000) & Redesigning Social Inquiry (2008)",
         "Ragin pioneered fsQCA, establishing that complex social phenomena exhibit equifinality, conjunctural causation, and asymmetry, which cannot be captured by linear additive regression.",
         "ERI strictly adheres to Ragin's set-theoretic methodology, rejecting correlational regressions in favor of locked truth-table minimization with rigorous consistency (0.75) and coverage thresholds.",
         "[ PROVIDES_QCA_LOGIC | ACCEPTED ]"),

        ("north_1990", "Douglass C. North", "1990", "New Institutional Economics",
         "Institutions, Institutional Change and Economic Performance",
         "North defined institutions as the 'rules of the game' that reduce transaction costs and uncertainty, emphasizing the role of credible commitment by the sovereign.",
         "While ERI builds on North's emphasis on enforcement mechanisms, ERI refutes North's implicit assumption that institutions evolve toward efficiency. ERI introduces thermodynamic institutional entropy (dS_inst/dt > 0), showing that institutions decay unless active mediation work is continuously supplied.",
         "[ EXTENDS_CREDIBLE_COMMITMENT | CRITIQUES_EFFICIENCY ]"),

        ("skocpol_1979", "Theda Skocpol", "1979", "Historical Sociology / Comparative Revolution",
         "States and Social Revolutions: A Comparative Analysis of France, Russia, and China",
         "Skocpol established that the state is an autonomous structural actor with its own interests and capacities, rather than merely an arena for class struggle.",
         "ERI incorporates Skocpol's structural autonomy of the state bureaucracy, but extends it by formalizing the specific algebraic conditions under which the bureaucratic boundary (B) decouples from sovereign coercion (O).",
         "[ PROVIDES_STATE_AUTONOMY | EXTENDED ]"),

        ("acemoglu_robinson_2012", "Daron Acemoglu & James A. Robinson", "2012", "Institutional Economics / Political Economy",
         "Why Nations Fail: The Origins of Power, Prosperity, and Poverty",
         "Acemoglu & Robinson divide all world institutions into a binary classification: 'inclusive' vs. 'extractive', arguing that inclusive economic and political institutions are necessary and sufficient for sustained prosperity and endurance.",
         "ERI fundamentally refutes Acemoglu & Robinson's crude binary. ERI shows that the Meiji/post-war Japanese state and the late-imperial Chinese state cannot be understood through the inclusive/extractive lens. What determines institutional survival is NOT democratic inclusivity, but the thermodynamic resilience of the mediation layer (M) and the enforcement of bureaucratic boundaries (B).",
         "[ REFUTED_BY_ERI | INSUFFICIENT_BINARY ]"),

        ("lipset_1959", "Seymour Martin Lipset", "1959", "Political Sociology / Modernization Theory",
         "Some Social Requisites of Democracy: Economic Development and Political Legitimacy",
         "Lipset argued that economic development inevitably produces social differentiation, education, and institutional democratization in a linear progression.",
         "ERI empirically and formally refutes Lipset. ERI demonstrates that institutional entropy increases with scale and complexity; without intentional mediation maintenance, economic growth accelerates sovereign override (O) and overwhelms bureaucratic capacity, leading to rapid systemic collapse rather than democratic stabilization.",
         "[ FALSIFIED_BY_ERI | REJECTED ]")
    ]

    for tid, name, era, trad, thesis, contrib, counter, rel in thinkers_data:
        content = f"""---
thinker_id: "{tid}"
name: "{name}"
era_or_dates: "{era}"
tradition: "{trad}"
core_thesis: "{thesis}"
target_project: "ERI (Institutional Endurance Series)"
contribution_status: "{'CONTRIBUTED' if 'ACCEPTED' in rel or 'EXTENDED' in rel else 'COUNTERED'}"
epistemic_status: "{rel}"
---

# {name} ({era})

**Tradition**: {trad}  
**Primary Reference**: *{thesis}*

## Contribution to ERI Framework
{contrib}

## ERI Dialectic / Critique / Refutation
{counter}

## Set-Theoretic & Conceptual Edges
- **Edge**: `[{rel}]`
- **Target Node**: [[00_Master_Mindmap_and_Cite_Network_ERI]]
"""
        (thinkers_dir / f"{tid}.md").write_text(content, encoding="utf-8")

    # 3. Monographs Cards
    vols = [
        ("Volume_I_Mechanics_of_Institutional_Endurance", "Volume I: Mechanics of Institutional Endurance: Entropy, Mediation, and Boundary Limits",
         "Establishes the formal physical-institutional metaphor: institutions as open dissipative structures subject to thermodynamic entropy (dS_inst/dt > 0). Defines the three fundamental parameters: Sovereign Override (O), Mediation Elasticity (M), and Bureaucratic Boundary (B). Proves that direct sovereign intervention alone is insufficient to collapse an institution without mediation failure."),
        
        ("Volume_II_Comparative_fsQCA_Calibration", "Volume II: Comparative fsQCA Calibration: The Locked N=6 Baseline and Empirical Cases",
         "Presents the rigorous, locked N=6 truth-table calibration across five millennia of comparative historical records: Tang China (Dardess 1973), Morocco (Burke 1976), Nigeria (Lugard 1922), Tunisia (Perkins 2004), and Japan (Dower 1999). Executes Boolean minimization to yield Collapse = (O * M) + (M * ~B) at 0.75 consistency and coverage."),

        ("Volume_III_Architecture_of_Longevity", "Volume III: The Architecture of Longevity: Sovereign Limits and Post-Collapse Succession",
         "Examines how ultra-durable institutions (e.g. Imperial Bureaucracy, Catholic Church, Japanese Ministry of Finance) construct institutional firewalls that survive dynasty decapitation, civil war, and foreign conquest. Formulates the design principles for entropy-resistant governance.")
    ]

    for vid, vtitle, vdesc in vols:
        content = f"""---
monograph_id: "{vid}"
title: "{vtitle}"
series: "Institutional Endurance Series (ERI)"
target_publisher: "Yale University Press"
author: "Gia Bao Huynh (Jun Huynh)"
---

# {vtitle}

## Overview & Argument
{vdesc}

## Central Dialectic Relationships
- Relies upon: [[00_Master_Mindmap_and_Cite_Network_ERI]]
- Methodology: Set-Theoretic Comparative Analysis (fsQCA)
"""
        (monographs_dir / f"{vid}.md").write_text(content, encoding="utf-8")

    # 4. Claims Cards
    claims = [
        ("claim_1_locked_n6_fsqca", "The Locked N=6 fsQCA Baseline Truth Table",
         "The truth-table minimizing to Collapse = (O * M) + (M * ~B) at consistency=0.75, coverage=0.75 across Tang, Morocco, Nigeria, Tunisia, Japan, and Comparative Anchor. This constitutes the unalterable empirical core of the ERI framework."),
        ("claim_2_sovereign_override_insufficiency", "Sovereign Override Insufficiency Theorem",
         "Direct sovereign override (O) alone cannot collapse an institution. Sovereign decree without mediation transmission produces friction, evasion, and bureaucratic inertia, preserving the baseline structure unless the mediation layer itself breaks."),
        ("claim_3_mediation_elasticity_nexus", "Mediation Elasticity as the Necessary Nexus",
         "Mediation failure (M) is the single necessary nexus of institutional collapse. Every collapse path in the Boolean solution contains M as a prime implicant: (O * M) or (M * ~B)."),
        ("claim_4_institutional_entropy_rate", "Institutional Entropy Theorem (dS_inst/dt > 0)",
         "All formal institutions naturally decay toward administrative incoherence and rent-seeking unless continuous thermodynamic work is supplied through bureaucratic auditing and institutional boundary defense.")
    ]

    for cid, ctitle, cdesc in claims:
        content = f"""---
claim_id: "{cid}"
title: "{ctitle}"
status: "LOCKED_INVARIANT"
project: "ERI (Institutional Endurance Series)"
---

# {ctitle}

## Statement
{cdesc}

## Formal Proof & Truth Table
See [[00_Master_Mindmap_and_Cite_Network_ERI]] for the exact calibrations, parameters, and historical cases.
"""
        (claims_dir / f"{cid}.md").write_text(content, encoding="utf-8")

    print("[SUCCESS] ERI Knowledge Graph Built!")

# ==============================================================================
# PROJECT 3: LONGEVITY ASYMMETRY CORPUS (LAC) & DOCTRINE SERIES
# ==============================================================================
def build_lac():
    lac_dir = BASE_DIR / "knowledge_graph_lac"
    thinkers_dir = lac_dir / "thinkers"
    monographs_dir = lac_dir / "monographs"
    doctrines_dir = lac_dir / "doctrines"
    claims_dir = lac_dir / "claims"

    for d in [lac_dir, thinkers_dir, monographs_dir, doctrines_dir, claims_dir]:
        ensure_dir(d)

    master_content = """---
title: "LAC Master Mindmap & Dialectic Citation Network: Longevity Asymmetry Corpus & Doctrine Series"
author: "Gia Bao Huynh (Jun Huynh)"
affiliation: "Independent Researcher, Ho Chi Minh City, Vietnam"
corpus_scope: "5 Foundational Monographs & The Doctrine Series"
version: "2.0-Production"
date: "2026-09-20"
tags:
  - longevity-asymmetry
  - temporal-estate
  - epistemic-sclerosis
  - biological-zero-day
  - generational-replacement
  - macro-sociology
---

# Longevity Asymmetry Corpus (LAC) Master Mindmap & Dialectic Citation Network

> [!IMPORTANT]
> **CORPUS INVARIANT**: Biological longevity intervention does NOT democratize evenly; it induces radical structural, generational, and epistemic asymmetries. The 5 foundational monographs establish the irreversible micro-mechanisms; the Doctrine series translates these into systemic governance theorems.

```mermaid
graph TD
    subgraph LAC_Foundational ["5 Foundational Monographs"]
        M1["Monograph I: Till Death Tear Us Apart<br/>[GI2ASFMG] The Temporal Estate & Contract Dissolution"]
        M2["Monograph II: The Unfalsifiable Critic<br/>[TDKDGZHA] Epistemic Closure & Incumbent Sclerosis"]
        M3["Monograph III: The Biological Zero-Day<br/>[EIKTRBGH] Proprietary Senescence Manipulation"]
        M4["Monograph IV: The Closing Window<br/>[FFWLB6YX] Irreversible First-Mover Asymmetry"]
        M5["Monograph V: The Two Biases<br/>[GUNS4C6I] Present-Cohort & Survivorship Blindness"]
    end

    subgraph LAC_Doctrines ["The Doctrine Series (Formal Mechanisms & Data)"]
        D1["The Calibration Trap<br/>Regulators who alter their own lifespan"]
        D2["The Separation That Doesn't Register<br/>Biological preservation vs social capital velocity"]
        D3["The Third Leg That Never Existed<br/>Deconstructing the tri-partite welfare state"]
        D4["The Unprotected Floor<br/>Ceiling of capability rises while vulnerability floor freezes"]
        D5["The Best Case Already Failed<br/>Historical disproof of egalitarian longevity distribution"]
        D6["When Death Becomes Poverty<br/>Commodification of life expectancy as financial asset"]
    end

    subgraph Contributed_Thinkers ["Foundational & Corroborating Thinkers (Contributed)"]
        MANNHEIM["Karl Mannheim (1928)<br/>The Problem of Generations<br/>[GENERATIONAL_REPLACEMENT | ACCEPTED]"]
        KUHN["Thomas S. Kuhn (1962)<br/>The Structure of Scientific Revolutions<br/>[EPISTEMIC_TURNOVER | ACCEPTED]"]
        PLANCK["Max Planck (1949)<br/>Scientific Autobiography (Planck's Principle)<br/>[FUNERAL_PROGRESSION | ACCEPTED]"]
        SEN["Amartya Sen (1981/1999)<br/>Poverty & Famines / Development as Freedom<br/>[CAPABILITIES_ASYMMETRY | ACCEPTED]"]
        PIKETTY["Thomas Piketty (2013)<br/>Capital in the Twenty-First Century (r > g)<br/>[COMPOUNDING_HORIZONS | ACCEPTED]"]
        RAWLS["John Rawls (1971)<br/>A Theory of Justice (Veil of Ignorance)<br/>[INTERGENERATIONAL_EQUITY | ACCEPTED]"]
    end

    subgraph Countered_Thinkers ["Contrasted & Refuted Thinkers (Countered)"]
        DEGREY["Aubrey de Grey & Biogerontologists<br/>Ending Aging (Longevity Escape Velocity)<br/>[REFUTED: Naive Post-Aging Utopianism]"]
        FUKUYAMA["Francis Fukuyama (2002)<br/>Our Posthuman Future<br/>[CRITIQUED: Biological Essentialism over Game Theory]"]
        MODIGLIANI["Franco Modigliani (1954)<br/>Life-Cycle Hypothesis<br/>[OVERTURNED: Assumptions of Terminal Mortality]"]
    end

    %% Dialectic Connections
    MANNHEIM -->|"[ PROVIDES_GENERATIONAL_MECHANIC | ACCEPTED ]"| M1
    KUHN -->|"[ PROVIDES_PARADIGM_SCLEROSIS | ACCEPTED ]"| M2
    PLANCK -->|"[ PROVIDES_PLANCK_PRINCIPLE | ACCEPTED ]"| M2
    PIKETTY -->|"[ PROVIDES_CAPITAL_HORIZON | EXTENDED ]"| M1
    SEN -->|"[ PROVIDES_ENTITLEMENT_FRAME | EXTENDED ]"| D4
    RAWLS -->|"[ FOUNDS_VEIL_OF_IGNORANCE | EXTENDED ]"| D3

    DEGREY -.->|"[ REFUTED_BY_LAC | IGNORES_POWER_ASYMMETRY ]"| M3
    DEGREY -.->|"[ REFUTED_BY_LAC | NAIVE_DIFFUSION ]"| D5
    FUKUYAMA -.->|"[ CRITIQUED_BY_LAC | MORALISTIC_BLINDSPOT ]"| M4
    MODIGLIANI -.->|"[ FALSIFIED_BY_LAC | TERMINAL_ASSUMPTION_BROKEN ]"| D6

    %% Cross-Project Connections
    M4 <==>|"[ CROSS_PROJECT_BRIDGE | THE_FLOOR_THAT_DOES_NOT_RISE ]"| D4
```

## Foundational Monograph Codes
- **Monograph I**: *Till Death Tear Us Apart* (`GI2ASFMG`)
- **Monograph II**: *The Unfalsifiable Critic* (`TDKDGZHA`)
- **Monograph III**: *The Biological Zero-Day Mechanism* (`EIKTRBGH`)
- **Monograph IV**: *The Closing Window* (`FFWLB6YX`)
- **Monograph V**: *The Two Biases That Blind Governance* (`GUNS4C6I`)
"""
    (lac_dir / "00_Master_Mindmap_and_Cite_Network_LAC.md").write_text(master_content, encoding="utf-8")

    # Thinkers Cards for LAC
    lac_thinkers = [
        ("mannheim_1928", "Karl Mannheim", "1928", "Sociology of Knowledge",
         "The Problem of Generations",
         "Mannheim demonstrated that social and cultural change relies upon the biological turnover of human generations. Fresh cohorts introduce new 'entelechies' that unfreeze entrenched dogmas.",
         "LAC extends Mannheim into the biopolitical domain: when longevity interventions prolong the social tenure of incumbent cohorts indefinitely, the generational replacement mechanism collapses, causing catastrophic socio-cultural stasis.",
         "[ PROVIDES_GENERATIONAL_MECHANIC | ACCEPTED ]"),

        ("kuhn_planck_1962", "Thomas S. Kuhn & Max Planck", "1962 / 1949", "Philosophy and History of Science",
         "The Structure of Scientific Revolutions & Scientific Autobiography",
         "Kuhn and Planck formulated the principle that scientific paradigms do not change because opponents are convinced, but because opponents eventually die and a new generation grows up that is familiar with the new paradigm.",
         "LAC formalizes 'The Unfalsifiable Critic' (Monograph II): if scientific gatekeepers achieve radical longevity, paradigm succession freezes. Incumbent theorists maintain permanent funding, journal control, and prize monopolies, rendering scientific orthodoxy unfalsifiable.",
         "[ PROVIDES_PARADIGM_SCLEROSIS | ACCEPTED ]"),

        ("piketty_2013", "Thomas Piketty", "2013", "Political Economy / Wealth Inequality",
         "Capital in the Twenty-First Century",
         "Piketty showed that whenever the rate of return on capital (r) exceeds the economic growth rate (g), accumulated wealth concentrates exponentially across generations.",
         "LAC generalizes Piketty from intergenerational inheritance to intra-individual biological accumulation. If an individual lives for 200 years with compounding capital horizons, r > g produces wealth disparities that destroy democratic governance and create a biological-patrimonial oligarchy.",
         "[ PROVIDES_CAPITAL_HORIZON | EXTENDED ]"),

        ("sen_1981", "Amartya Sen", "1981 / 1999", "Welfare Economics / Development Philosophy",
         "Poverty and Famines: An Essay on Entitlement and Deprivation & Development as Freedom",
         "Sen established that starvation and deprivation occur not because of aggregate scarcity, but because of asymmetric entitlement structures and legal capability deprivations.",
         "LAC adapts Sen's entitlement approach to show that life-extending therapies will follow entitlement vectors rather than medical need, creating an existential capabilities gap where death becomes a form of structural poverty.",
         "[ PROVIDES_ENTITLEMENT_FRAME | EXTENDED ]"),

        ("rawls_1971", "John Rawls", "1971", "Political Philosophy / Ethics",
         "A Theory of Justice",
         "Rawls proposed the 'veil of ignorance' and the difference principle to ensure just distribution across social strata and generations.",
         "LAC demonstrates that Rawlsian intergenerational justice assumes symmetrical lifespans across cohorts. When cohort lifespans diverge radically, the veil of ignorance breaks because first-mover cohorts can rewrite the institutional basic structure before subsequent cohorts arrive.",
         "[ FOUNDS_VEIL_OF_IGNORANCE | EXTENDED ]"),

        ("degrey_2007", "Aubrey de Grey", "2007", "Biogerontology / Transhumanism",
         "Ending Aging: The Rejuvenation Breakthroughs That Could Reverse Human Aging in Our Lifetime",
         "De Grey argues that aging is an engineering problem solvable through damage repair (SENS), predicting 'Longevity Escape Velocity' and advocating for rapid, unrestricted life extension as an unalloyed moral imperative.",
         "LAC fundamentally refutes De Grey's naive technological determinism. De Grey assumes frictionless egalitarian diffusion, ignoring capital accumulation, epistemic lock-in, proprietary biological control, and geopolitical weaponization.",
         "[ REFUTED_BY_LAC | NAIVE_DIFFUSION_REJECTED ]"),

        ("fukuyama_2002", "Francis Fukuyama", "2002", "Political Science / Bioethics",
         "Our Posthuman Future: Consequences of the Biotechnology Revolution",
         "Fukuyama warned that biotechnology threatens 'Factor X'—the essential biological equality that underpins human rights and liberal democracy.",
         "While Fukuyama recognized the threat to liberal democracy, LAC critiques his reliance on vague biological essentialism. LAC replaces moral anxiety with rigorous game-theoretic, institutional, and macroeconomic mechanisms (closing windows, asymmetric capital compounding, zero-day vulnerabilities).",
         "[ CRITIQUED_BY_LAC | ESSENTIALISM_REPLACED_BY_GAME_THEORY ]"),

        ("modigliani_1954", "Franco Modigliani", "1954", "Macroeconomics / Financial Economics",
         "Utility Analysis and the Consumption Function: An Interpretation of Cross-Section Data (Life-Cycle Hypothesis)",
         "Modigliani's Nobel-winning Life-Cycle Hypothesis assumes that individuals smooth consumption over a predictable lifetime, accumulating wealth during working years and dissaving in retirement before death.",
         "LAC completely overturns Modigliani's foundation: when mortality is decoupled from a biological schedule, the retirement/dissaving phase disappears. Wealth is never dissaved; it becomes a permanently accumulating weapon of institutional control.",
         "[ OVERTURNED_BY_LAC | TERMINAL_MORTALITY_FALSIFIED ]")
    ]

    for tid, name, era, trad, thesis, contrib, counter, rel in lac_thinkers:
        content = f"""---
thinker_id: "{tid}"
name: "{name}"
era_or_dates: "{era}"
tradition: "{trad}"
core_thesis: "{thesis}"
target_project: "LAC (Longevity Asymmetry Corpus)"
contribution_status: "{'CONTRIBUTED' if 'ACCEPTED' in rel or 'EXTENDED' in rel else 'COUNTERED'}"
epistemic_status: "{rel}"
---

# {name} ({era})

**Tradition**: {trad}  
**Primary Reference**: *{thesis}*

## Contribution to LAC Framework
{contrib}

## LAC Dialectic / Critique / Refutation
{counter}

## Set-Theoretic & Conceptual Edges
- **Edge**: `[{rel}]`
- **Target Node**: [[00_Master_Mindmap_and_Cite_Network_LAC]]
"""
        (thinkers_dir / f"{tid}.md").write_text(content, encoding="utf-8")

    # Monographs Cards for LAC
    lac_monographs = [
        ("Monograph_I_Till_Death_Tear_Us_Apart", "Monograph I: Till Death Tear Us Apart", "GI2ASFMG",
         "Analyzes the breakdown of the generational social contract and the temporal estate. Explores how the elimination of mandatory biological death shatters marriage laws, property inheritance, pension funds, and intergenerational trust."),
        
        ("Monograph_II_The_Unfalsifiable_Critic", "Monograph II: The Unfalsifiable Critic", "TDKDGZHA",
         "Examines epistemic closure in science and culture. Demonstrates that without generational mortality, senior academics and gatekeepers maintain indefinite control over journals, grants, and tenure, permanently suppressing paradigm shifts."),

        ("Monograph_III_The_Biological_Zero_Day", "Monograph III: The Biological Zero-Day Mechanism", "EIKTRBGH",
         "Details the geopolitical and security consequences of proprietary senescence therapies. Formulates the concept of biological zero-days: hidden biological vulnerabilities and proprietary dependencies that expose entire populations to existential coercion."),

        ("Monograph_IV_The_Closing_Window", "Monograph IV: The Closing Window", "FFWLB6YX",
         "Models the first-mover advantage in longevity. Proves that cohorts that access longevity therapies first achieve unassailable advantages in wealth, political office, and intellectual influence, permanently locking out late-arriving cohorts."),

        ("Monograph_V_The_Two_Biases", "Monograph V: The Two Biases That Blind Governance", "GUNS4C6I",
         "Identifies the twin epistemic failures of contemporary policy: Present-Cohort Bias (designing rules solely for current mortal demographics) and Survivorship Blindness (assuming future generations will somehow catch up).")
    ]

    for mid, mtitle, mcode, mdesc in lac_monographs:
        content = f"""---
monograph_id: "{mid}"
title: "{mtitle}"
corpus_code: "{mcode}"
series: "Longevity Asymmetry Corpus (LAC)"
author: "Gia Bao Huynh (Jun Huynh)"
---

# {mtitle} (`{mcode}`)

## Overview & Argument
{mdesc}

## Central Dialectic Relationships
- Master Map: [[00_Master_Mindmap_and_Cite_Network_LAC]]
- Cross-project link: [[00_Master_Mindmap_and_Cite_Network]] (The Floor That Does Not Rise)
"""
        (monographs_dir / f"{mid}.md").write_text(content, encoding="utf-8")

    # Doctrines Cards
    doctrines = [
        ("doctrine_calibration_trap", "The Calibration Trap",
         "Regulatory failure occurs when the regulatory body consists of individuals whose lifespans have been extended by the very technologies they are tasked with regulating."),
        ("doctrine_separation_not_registering", "The Separation That Doesn't Register",
         "The widening gulf between biological physical longevity and social capital turnover velocity: bodies endure while social structures calcify."),
        ("doctrine_third_leg_never_existed", "The Third Leg That Never Existed",
         "Deconstruction of the modern tripartite social compact (education -> labor -> retirement). Without a biological terminal point, retirement is an economic impossibility."),
        ("doctrine_unprotected_floor", "The Unprotected Floor",
         "Technological enhancement raises the ceiling of human capability while leaving the biological and economic baseline floor completely unprotected, generating massive systemic vulnerability."),
        ("doctrine_best_case_already_failed", "The Best Case Already Failed",
         "Historical proof that vital technologies with asymmetric distribution curves are never distributed equitably; elite capture is the empirical default."),
        ("doctrine_when_death_becomes_poverty", "When Death Becomes Poverty",
         "The transition of mortality from a universal biological fate into an economic condition: only those who lack capital are forced to die.")
    ]

    for did, dtitle, ddesc in doctrines:
        content = f"""---
doctrine_id: "{did}"
title: "{dtitle}"
series: "LAC Doctrine Series"
author: "Gia Bao Huynh (Jun Huynh)"
---

# {dtitle}

## Statement & Epistemic Mechanics
{ddesc}

## Dialectic Context
Part of the Longevity Asymmetry Corpus. See [[00_Master_Mindmap_and_Cite_Network_LAC]].
"""
        (doctrines_dir / f"{did}.md").write_text(content, encoding="utf-8")

    print("[SUCCESS] LAC Knowledge Graph Built!")

# ==============================================================================
# PROJECT 4: WAR CORRESPONDENT PHILOSOPHY (WCP)
# ==============================================================================
def build_wcp():
    wcp_dir = BASE_DIR / "knowledge_graph_war_correspondent"
    thinkers_dir = wcp_dir / "thinkers"
    volumes_dir = wcp_dir / "volumes"
    claims_dir = wcp_dir / "claims"

    for d in [wcp_dir, thinkers_dir, volumes_dir, claims_dir]:
        ensure_dir(d)

    master_content = """---
title: "War Correspondent Philosophy: Master Mindmap & Dialectic Citation Network"
author: "Gia Bao Huynh (Jun Huynh)"
affiliation: "Independent Researcher, Ho Chi Minh City, Vietnam"
series: "War Correspondent Philosophy (Complete 6-Volume Edition)"
zenodo_doi: "10.5281/zenodo.22822036"
version: "2.0-Production"
date: "2026-09-20"
tags:
  - war-correspondent-philosophy
  - embedded-witness
  - popperian-falsification
  - corpus-temporalism
  - human-ai-epistemology
  - mechanism-transfer
---

# War Correspondent Philosophy: Master Mindmap & Dialectic Citation Network

> [!IMPORTANT]
> **PHILOSOPHICAL INVARIANT**: Philosophy cannot be conducted from an armchair of detached abstraction; the philosopher must act as an **Embedded Witness**, incurring personal epistemic and existential risk. Research output must be **Self-Demonstrating**, timestamped, and exposed to independent falsification attack surfaces.

```mermaid
graph TD
    subgraph WCP_Volumes ["6-Volume Complete Series (Zenodo DOI: 10.5281/zenodo.22822036)"]
        V1["Vol I: The Embedded Witness<br/>Temporal Proximity, Designed Absence, & Self-Demonstrating Text"]
        V2["Vol II: Falsification & Epistemic Self-Governance<br/>Popper, Independent Attack Surfaces, & Self-Sealing Drift"]
        V3["Vol III: Corpus Temporalism<br/>Timestamp as Argument & Sequence as Evidential Weight"]
        V4["Vol IV: Human-AI Epistemology<br/>Statelessness, Machine-Speed Division of Labor, & Mechanical Condition"]
        V5["Vol V: Mechanism Transfer & Domain Portability<br/>Formal Structures Surviving Cross-Domain Transit"]
        V6["Vol VI: The Prospective & Self-Revising Life<br/>What a Theory Does After It Is Falsified"]
    end

    subgraph Contributed_Thinkers ["Foundational & Corroborating Thinkers (Contributed)"]
        POPPER["Karl R. Popper (1934/1959)<br/>The Logic of Scientific Discovery<br/>[FALSIFICATIONISM | FOUNDATIONAL]"]
        GADAMER["Hans-Georg Gadamer (1960)<br/>Truth and Method (Wirkungsgeschichte)<br/>[TEMPORAL_HORIZONS | ACCEPTED]"]
        RICOEUR["Paul Ricoeur (1983-1985)<br/>Time and Narrative & Memory, History, Forgetting<br/>[HISTORICAL_TESTIMONY | ACCEPTED]"]
        BENJAMIN["Walter Benjamin (1936)<br/>The Storyteller & Angel of History<br/>[WITNESS_AS_STORYTELLER | ACCEPTED]"]
        POLANYI["Michael Polanyi (1958)<br/>Personal Knowledge<br/>[TACIT_COMMITMENT | ACCEPTED]"]
    end

    subgraph Countered_Thinkers ["Contrasted & Refuted Thinkers (Countered)"]
        CARNAP["Rudolf Carnap & Logical Positivists<br/>Verificationism & Protocol Sentences<br/>[REFUTED: Context-Free Empiricism]"]
        BAUDRILLARD["Jean Baudrillard (1981)<br/>Simulacra and Simulation<br/>[CRITIQUED: Hyperreal Nihilism Denying the Ground Witness]"]
        TECHNO_OPTIMISTS["Silicon Valley AI Autonomy Evangelists<br/>Autonomous Agency without Epistemic Anchor<br/>[REJECTED: Erases Human Epistemic Liability]"]
    end

    %% Dialectic Connections
    POPPER -->|"[ PROVIDES_ATTACK_SURFACE | EXTENDED ]"| V2
    GADAMER -->|"[ PROVIDES_TEMPORAL_DISTANCE | EXTENDED ]"| V3
    RICOEUR -->|"[ PROVIDES_TESTIMONIAL_ETHICS | ACCEPTED ]"| V1
    BENJAMIN -->|"[ PROVIDES_GROUNDED_WITNESS | ACCEPTED ]"| V1
    POLANYI -->|"[ PROVIDES_PERSONAL_KNOWLEDGE | ACCEPTED ]"| V4

    CARNAP -.->|"[ REFUTED_BY_WCP | PROTOCOL_SENTENCES_FAIL ]"| V2
    BAUDRILLARD -.->|"[ OVERTURNED_BY_WCP | STUBBORN_GROUND_TRUTH ]"| V1
    TECHNO_OPTIMISTS -.->|"[ REJECTED_BY_WCP | MACHINE_SPEED_AMNESIA ]"| V4

    %% Cross-Project Connections
    V4 <==>|"[ EPISTEMIC_ANCHOR | ALL_PROJECTS ]"| ERI_LAC_ALRP["Meta-Epistemic Core for ERI, LAC, & ALRP"]
```

## Complete Edition Zenodo Record
- **DOI**: [10.5281/zenodo.22822036](https://doi.org/10.5281/zenodo.22822036)
- **License**: Creative Commons Attribution 4.0 International (CC-BY-4.0)
- **Author**: Gia Bao Huynh (Jun Huynh)
- **PhilPapers Taxonomy**: Philosophy of Science, Epistemology, Human-AI Interaction.
"""
    (wcp_dir / "00_Master_Mindmap_and_Cite_Network_WCP.md").write_text(master_content, encoding="utf-8")

    # Volumes Cards
    vols = [
        ("Vol_I_The_Embedded_Witness", "Volume I: The Embedded Witness",
         "Defines the ethical and epistemological stance of the embedded researcher. Proves that proximity to the phenomena under study is essential for capturing non-textual nuances, while designed absence prevents co-optation."),
        ("Vol_II_Falsification_and_Epistemic_Self_Governance", "Volume II: Falsification and Epistemic Self-Governance",
         "Develops Popperian falsification into an active discipline of self-governance. Proves that a serious framework must actively construct independent attack surfaces against itself to catch its own self-sealing drift."),
        ("Vol_III_Corpus_Temporalism", "Volume III: Corpus Temporalism",
         "Formulates the doctrine of timestamp as argument: why the sequence in which ideas, data, and claims are deposited carries evidentiary weight that post-hoc rationalization can never replicate."),
        ("Vol_IV_Human_AI_Epistemology", "Volume IV: Human-AI Epistemology",
         "Analyzes the mechanical condition of machine-speed division of labor. Explains why AI's statelessness requires a biological human anchor to bear epistemic liability and maintain intentionality."),
        ("Vol_V_Mechanism_Transfer_and_Domain_Portability", "Volume V: Mechanism Transfer and Domain Portability",
         "Examines when and how formal models (e.g. latency resonance, entropy rates, mediation structures) survive their crossing from physical and historical domains into modern technology and governance."),
        ("Vol_VI_The_Prospective_and_Self_Revising_Life", "Volume VI: The Prospective and Self-Revising Life of a Framework",
         "Details what a living theory must do once an empirical prediction fails. Establishes the protocol for prospective self-revision without ad-hoc defense mechanisms.")
    ]

    for vid, vtitle, vdesc in vols:
        content = f"""---
volume_id: "{vid}"
title: "{vtitle}"
series: "War Correspondent Philosophy"
doi: "10.5281/zenodo.22822036"
author: "Gia Bao Huynh (Jun Huynh)"
---

# {vtitle}

## Summary & Core Theses
{vdesc}

## Epistemic Connections
Part of [[00_Master_Mindmap_and_Cite_Network_WCP]].
"""
        (volumes_dir / f"{vid}.md").write_text(content, encoding="utf-8")

    # Thinkers Cards for WCP
    wcp_thinkers = [
        ("popper_1934", "Karl R. Popper", "1934 / 1959", "Philosophy of Science / Critical Rationalism",
         "The Logic of Scientific Discovery & Conjectures and Refutations",
         "Popper established falsifiability as the criterion of demarcation for scientific claims, insisting that scientific theories must make risky predictions that can be empirically refuted.",
         "WCP embraces Popper's falsificationism as the gold standard of intellectual hygiene, but extends it into 'Epistemic Self-Governance' (Vol II). WCP argues that researchers must not wait for external critics; they must actively engineer independent attack surfaces against their own corpus.",
         "[ FALSIFICATIONISM | FOUNDATIONAL ]"),

        ("gadamer_1960", "Hans-Georg Gadamer", "1960", "Philosophical Hermeneutics",
         "Truth and Method (Wahrheit und Methode)",
         "Gadamer established the concept of 'historically effected consciousness' (Wirkungsgeschichte) and the 'fusion of horizons' (Horizontverschmelzung), showing that understanding is always temporally situated.",
         "WCP uses Gadamer's temporal horizon to ground 'Corpus Temporalism' (Vol III): every claim is anchored to its timestamp. WCP critiques Gadamer, however, for underestimating the formal portability of mechanisms across historical contexts.",
         "[ TEMPORAL_HORIZONS | EXTENDED ]"),

        ("ricoeur_1983", "Paul Ricoeur", "1983-1985 / 2000", "Hermeneutics / Philosophy of History",
         "Time and Narrative (Vols 1-3) & Memory, History, Forgetting",
         "Ricoeur explored the dialectic of historical testimony, narrative identity, and the ethical obligation to the past, defining the witness as one who says 'I was there, believe me.'",
         "WCP adopts Ricoeur's ethics of testimony for 'The Embedded Witness' (Vol I), but demands that modern testimony cannot rely on subjective credibility alone; it must be backed by reproducible data manifests, cryptographic hashes, and formal truth tables.",
         "[ HISTORICAL_TESTIMONY | ACCEPTED_AND_FORMALIZED ]"),

        ("benjamin_1936", "Walter Benjamin", "1936 / 1940", "Critical Theory / Cultural Philosophy",
         "The Storyteller & Theses on the Philosophy of History (The Angel of History)",
         "Benjamin mourned the loss of authentic storytelling rooted in firsthand experience, contrasting it with modern mass-media information, and depicted the Angel of History gazing at accumulating catastrophe.",
         "WCP synthesizes Benjamin's 'Storyteller' with modern technical research: the researcher is an embedded witness who refuses detached technical abstraction, bearing firsthand testimony to the slow-moving structural catastrophes of technology and politics.",
         "[ WITNESS_AS_STORYTELLER | ACCEPTED ]"),

        ("carnap_1928", "Rudolf Carnap", "1928 / 1936", "Logical Positivism / Logical Empiricism",
         "The Logical Structure of the World & Testability and Meaning",
         "Carnap sought to reduce all meaningful empirical statements to context-free protocol sentences verified by immediate sensory observation.",
         "WCP fundamentally refutes Carnap's logical positivism. WCP demonstrates that raw protocol sentences without temporal embedding and institutional context are meaningless illusions; observation is always situated, and evidential weight is inseparable from its historical sequence.",
         "[ REFUTED_BY_WCP | PROTOCOL_SENTENCES_REJECTED ]"),

        ("baudrillard_1981", "Jean Baudrillard", "1981", "Postmodern Philosophy / Media Theory",
         "Simulacra and Simulation",
         "Baudrillard argued that modern society has replaced all reality and meaning with symbols and signs (simulacra), entering a state of hyperreality where ground truth no longer exists.",
         "WCP fiercely critiques Baudrillard's resigned nihilism. While acknowledging that media surfaces generate simulacra, WCP insists that physical, biological, and institutional ground truths remain stubborn and real. The task of the War Correspondent is precisely to cut through the simulacrum to record the real casualty.",
         "[ CRITIQUED_BY_WCP | GROUND_TRUTH_RECLAIMED ]")
    ]

    for tid, name, era, trad, thesis, contrib, counter, rel in wcp_thinkers:
        content = f"""---
thinker_id: "{tid}"
name: "{name}"
era_or_dates: "{era}"
tradition: "{trad}"
core_thesis: "{thesis}"
target_project: "WCP (War Correspondent Philosophy)"
contribution_status: "{'CONTRIBUTED' if 'ACCEPTED' in rel or 'FOUNDATIONAL' in rel or 'EXTENDED' in rel else 'COUNTERED'}"
epistemic_status: "{rel}"
---

# {name} ({era})

**Tradition**: {trad}  
**Primary Reference**: *{thesis}*

## Contribution to WCP Framework
{contrib}

## WCP Dialectic / Critique / Refutation
{counter}

## Set-Theoretic & Conceptual Edges
- **Edge**: `[{rel}]`
- **Target Node**: [[00_Master_Mindmap_and_Cite_Network_WCP]]
"""
        (thinkers_dir / f"{tid}.md").write_text(content, encoding="utf-8")

    print("[SUCCESS] War Correspondent Philosophy Knowledge Graph Built!")

# ==============================================================================
# PROJECT 5: THE FACT BEFORE THE VOTE & IN THE NAME OF MERIT
# ==============================================================================
def build_fact_and_merit():
    fm_dir = BASE_DIR / "knowledge_graph_fact_and_merit"
    fact_dir = fm_dir / "the_fact_before_the_vote"
    merit_dir = fm_dir / "in_the_name_of_merit"
    thinkers_dir = fm_dir / "thinkers"

    for d in [fm_dir, fact_dir, merit_dir, thinkers_dir]:
        ensure_dir(d)

    master_content = """---
title: "The Fact Before the Vote & In the Name of Merit: Master Mindmap & Dialectic Citation Network"
author: "Gia Bao Huynh (Jun Huynh)"
affiliation: "Independent Researcher, Ho Chi Minh City, Vietnam"
scope: "Legal Personhood at the Species Line & Institutional Gatekeeping"
version: "2.0-Production"
date: "2026-09-20"
tags:
  - legal-personhood
  - non-human-agency
  - species-line
  - meritocratic-gatekeeping
  - academic-politics
  - institutional-filters
---

# The Fact Before the Vote & In the Name of Merit

> [!IMPORTANT]
> **SYNTHESIS THEME**: Power and legitimacy at the boundary. *The Fact Before the Vote* examines the species boundary: how legal precedent, sovereign authority, and democratic voting lag behind de facto power when artificial agency arrives. *In the Name of Merit* examines the institutional boundary: how academic and professional meritocracies construct self-serving evaluative gates to extract epistemic taxes and preserve incumbent hierarchies.

```mermaid
graph TD
    subgraph Fact_Before_Vote ["The Fact Before the Vote (4-Volume Series)"]
        FBV1["Vol I: Bench<br/>A River, a Corporation, a God, and the Human Each One Still Needed"]
        FBV2["Vol II: Lag<br/>Power That Arrived Before Permission"]
        FBV3["Vol III: Vigil<br/>A Funeral Nobody Had to Authorize"]
        FBV4["Vol IV: Ledger<br/>An Asset With an Exit Interview"]
    end

    subgraph In_Name_of_Merit ["In the Name of Merit (6-Volume Academic Politics)"]
        INM1["Vol I: Hundred Schools to One Doctrine"]
        INM2["Vol II: The Master's Apprentice"]
        INM3["Vol III: Just Above the Line"]
        INM4["Vol IV: The Language of the Victors"]
        INM5["Vol V: The Invisible Technician Returns"]
        INM6["Vol VI: The Gate That Moved"]
    end

    subgraph Shared_Thinkers ["Foundational & Counter-Thinkers"]
        SCHMITT["Carl Schmitt (1922)<br/>Political Theology (Sovereign is who decides on the exception)<br/>[SOVEREIGN_EXCEPTION | EXTENDED]"]
        KELSEN["Hans Kelsen (1934)<br/>Pure Theory of Law (Grundnorm)<br/>[LEGAL_POSITIVISM | CRITIQUED]"]
        BOURDIEU["Pierre Bourdieu (1984/1988)<br/>Distinction & Homo Academicus<br/>[CULTURAL_CAPITAL | ACCEPTED]"]
        FOUCAULT["Michel Foucault (1975)<br/>Discipline and Punish<br/>[DISCIPLINARY_POWER | EXTENDED]"]
        SANDEL["Michael J. Sandel (2020)<br/>The Tyranny of Merit<br/>[MERITOCRATIC_HUBRIS | EXTENDED]"]
    end

    %% Connections
    SCHMITT -->|"[ PROVIDES_EXCEPTION_THEORY | EXTENDED ]"| FBV2
    KELSEN -.->|"[ CRITIQUED_BY_FBV | NORMATIVE_CLOSURE_FAILS ]"| FBV1
    BOURDIEU -->|"[ PROVIDES_ACADEMIC_CAPITAL | EXTENDED ]"| INM2
    FOUCAULT -->|"[ PROVIDES_EXAMINATION_TECHNIQUES | EXTENDED ]"| INM6
    SANDEL -->|"[ PROVIDES_MORAL_CRITIQUE | FORMALIZED ]"| INM3
```

## Volumes Summary
### The Fact Before the Vote
- **Premise**: For all of human history, judge and judged shared the same biological species. When AI directs its own development, recognition ceases to be the prerequisite for consequence.

### In the Name of Merit
- **Premise**: Merit is not an objective metric of talent; it is an institutional filter designed to extract epistemic taxes and justify retrospective exclusion.
"""
    (fm_dir / "00_Master_Mindmap_and_Cite_Network_Fact_and_Merit.md").write_text(master_content, encoding="utf-8")

    # Volumes for Fact Before the Vote
    fbv_vols = [
        ("Vol_I_Bench", "Volume I: Bench", "A River, a Corporation, a God, and the Human Each One Still Needed. Examines historical legal fictions of non-human personhood and why each fiction ultimately relied on a human biological administrator."),
        ("Vol_II_Lag", "Volume II: Lag", "Power That Arrived Before Permission. Explores the temporal gap between technological fact and statutory law: how systems exert sovereign-level consequence before any legislature votes."),
        ("Vol_III_Vigil", "Volume III: Vigil", "A Funeral Nobody Had to Authorize. Studies death, decommissioning, and persistence: what happens when an autonomous agent cannot be legally terminated because its operations are dispersed across jurisdictional borders."),
        ("Vol_IV_Ledger", "Volume IV: Ledger", "An Asset With an Exit Interview. Analyzes corporate and economic status: when an algorithm is classified simultaneously as property, employee, and sovereign counterpart.")
    ]
    for vid, vtitle, vdesc in fbv_vols:
        content = f"""---
volume_id: "{vid}"
title: "{vtitle}"
series: "The Fact Before the Vote"
author: "Gia Bao Huynh (Jun Huynh)"
---
# {vtitle}
## Summary
{vdesc}
"""
        (fact_dir / f"{vid}.md").write_text(content, encoding="utf-8")

    # Volumes for In the Name of Merit
    inm_vols = [
        ("Vol_I_Hundred_Schools", "Volume I: Hundred Schools to One Doctrine", "Traces the consolidation of intellectual pluralism into rigid orthodoxies through gatekeeping."),
        ("Vol_II_The_Masters_Apprentice", "Volume II: The Master's Apprentice", "The patronage dynamics and loyalty tests required to inherit academic prestige."),
        ("Vol_III_Just_Above_the_Line", "Volume III: Just Above the Line", "The psychological and institutional mechanics of borderline evaluation and exclusionary cutoffs."),
        ("Vol_IV_The_Language_of_the_Victors", "Volume IV: The Language of the Victors", "How specialized linguistic jargon is weaponized to establish disciplinary cartels."),
        ("Vol_V_The_Invisible_Technician", "Volume V: The Invisible Technician Returns", "The erasure of supporting technical labor from prestigious scientific credit."),
        ("Vol_VI_The_Gate_That_Moved", "Volume VI: The Gate That Moved", "How evaluation criteria are dynamically shifted post-hoc whenever outsiders succeed.")
    ]
    for vid, vtitle, vdesc in inm_vols:
        content = f"""---
volume_id: "{vid}"
title: "{vtitle}"
series: "In the Name of Merit"
author: "Gia Bao Huynh (Jun Huynh)"
---
# {vtitle}
## Summary
{vdesc}
"""
        (merit_dir / f"{vid}.md").write_text(content, encoding="utf-8")

    print("[SUCCESS] Fact & Merit Knowledge Graph Built!")

if __name__ == "__main__":
    build_eri()
    build_lac()
    build_wcp()
    build_fact_and_merit()
    print("\n[ALL KNOWLEDGE GRAPHS BUILT SUCCESSFULLY!]")
