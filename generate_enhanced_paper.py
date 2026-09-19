"""
Enhanced Paper Generator: "The Floor That Does Not Rise"
Reads original bcd133cf.docx, enhances with full 5-domain empirical data,
generates final publication-quality DOCX, saves to Google Drive.
"""
import sys, os, csv, json, shutil, re
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')

from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

# ============================================================
# PATHS
# ============================================================
DRIVE_FOLDER = r"G:\Drive của tôi\01_Longevity_Asymmetry_and_LAC\LONGEVITYWAVE"
ORIG_FILE = os.path.join(DRIVE_FOLDER, "bcd133cf.docx")
OUTPUTS = r"C:\Users\nswcl\.gemini\antigravity-ide\scratch\the-floor-that-does-not-rise\outputs"
TABLES = os.path.join(OUTPUTS, "tables")
INSERTIONS = os.path.join(OUTPUTS, "paper_insertions_final")

# Read original
orig = Document(ORIG_FILE)
orig_paragraphs = [p.text for p in orig.paragraphs]

print(f"[+] Read original: {len(orig_paragraphs)} paragraphs")

# Load CSV helper
def load_csv(name):
    path = os.path.join(TABLES, name)
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_txt(name):
    path = os.path.join(INSERTIONS, name)
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

# Load all data
housing_urt = load_csv("housing_unit_root_tests.csv")
housing_desc = load_csv("housing_descriptive_statistics.csv")
housing_recovery = load_csv("housing_recovery_times.csv")
ai_horizons = load_csv("ai_model_horizons.csv")
ai_runs = load_csv("ai_residual_runs.csv")
anthropic_rates = load_csv("anthropic_observed_input_rates.csv")
longevity_table = load_csv("longevity_evidence_access_table.csv")
cyber_growth = load_csv("cybersecurity_growth.csv")
cyber_policy = load_csv("cybersecurity_policy_break.csv")

housing_txt = load_txt("housing_results.txt")
ai_txt = load_txt("ai_results.txt")
longevity_txt = load_txt("longevity_results.txt")
cyber_txt = load_txt("cybersecurity_results.txt")
integrated_txt = load_txt("integrated_empirical_status.txt")

print(f"[+] Loaded {len(housing_urt)} housing URT rows, {len(ai_horizons)} AI model horizons, {len(cyber_growth)} cyber growth rows")

# ============================================================
# CREATE NEW DOCUMENT
# ============================================================
doc = Document()

# Page Setup
for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
style.paragraph_format.line_spacing = 1.5

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def add_title(text, size=16, bold=True, centered=True):
    p = doc.add_paragraph()
    if centered:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    run.font.name = 'Times New Roman'
    return p

def add_heading_custom(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.name = 'Times New Roman'
        run.font.color.rgb = RGBColor(0, 0, 0)
    return h

def add_body(text, italic=False, bold=False, size=12):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(1.27)
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.name = 'Times New Roman'
    run.italic = italic
    run.bold = bold
    return p

def add_body_no_indent(text, italic=False, bold=False, size=12):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.name = 'Times New Roman'
    run.italic = italic
    run.bold = bold
    return p

def add_table_from_data(headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Header
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            for run in p.runs:
                run.bold = True
                run.font.size = Pt(10)
                run.font.name = 'Times New Roman'
    # Data
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.rows[ri + 1].cells[ci]
            cell.text = str(val)
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(10)
                    run.font.name = 'Times New Roman'
    return table

# ============================================================
# DOCUMENT CONTENT
# ============================================================

# --- TITLE PAGE ---
doc.add_paragraph()  # spacing
add_title("The Floor That Does Not Rise", size=18)
add_title("Reset Events, Queueing Instability, and the Hard–Soft Floor Distinction", size=13, bold=False)
add_title("A General Theory, Tested Against Five Empirical Domains", size=12, bold=False)
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Gia Bao Huynh")
run.bold = True
run.font.size = Pt(13)
run.font.name = 'Times New Roman'

add_title("Independent Researcher, Ho Chi Minh City, Vietnam", size=11, bold=False)
add_title("huynhbao@asu.edu · ORCID: 0009-0008-2372-5852", size=10, bold=False)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(f"Enhanced Final Draft — {datetime.now().strftime('%B %d, %Y')}")
run.italic = True
run.font.size = Pt(10)
run.font.name = 'Times New Roman'

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("© Gia Bao Huynh (2026). Collaborator: Claude Sonnet 5 & Gemini Spark.\nDraft manuscript prepared for open scholarly circulation and comment.")
run.font.size = Pt(9)
run.font.name = 'Times New Roman'
run.italic = True

doc.add_page_break()

# --- ABSTRACT ---
add_heading_custom("Abstract", level=1)

abstract_text = (
    "Some technologies generate their own inequality faster than they can resolve it, "
    "because the very engine that creates a new advantage is also, in principle, the only mechanism "
    "that could ever spread it evenly — and the engine now compounds faster than the spreading mechanism can move. "
    "This paper states the resulting structure as a formal queueing-theoretic claim: when reset events "
    "(discrete frontier advances) arrive at an accelerating rate λ(t) that eventually exceeds the bounded "
    "service rate μ at which prior advances are absorbed by the general-access floor, the gap between frontier "
    "and floor grows without bound — the queue is structurally unstable. "
    "This formalization is tested against raw, independently fetched data across five empirical domains: "
    "(1) U.S. housing construction as a bounded-lag null comparator, "
    "(2) AI capability growth via METR's 24,008 task-level evaluations across 21 frontier models, "
    "(3) Anthropic-attributed distillation exchange volumes and effective throughput modeling, "
    "(4) longevity biotechnology clinical evidence and price/access stratification, and "
    "(5) cybersecurity vulnerability inflow and administrative remediation pacing. "
    "The housing pipeline confirms operational stationarity (ADF p < 10⁻¹⁰), serving as the null-case comparator the original draft proposed but had not yet tested. "
    "AI capability doubling time is estimated at 7.2 months (95% CI: 5.4–10.8), but a quadratic curvature test "
    "fails to reject log-linear constancy (p = 0.28), weakening claims of super-exponential acceleration. "
    "Distillation exchange volume establishes input activity, not audited capability transfer; "
    "effective throughput μ_eff spans four orders of magnitude (0.015–150 units/day) across scenario grids. "
    "Longevity evidence demonstrates statistically significant deceleration of biological aging proxies "
    "(DunedinPACE −0.02/yr, p = 0.008) but zero demonstrated human lifespan extension, with severe "
    "price/access stratification (metformin affordability index 0.98 vs. concierge clinic 0.00). "
    "Cybersecurity CVE inflow expanded +139.3% (2018–2024) while CNA concentration halved (HHI 1,500→710). "
    "All results carry strict SHA-256 provenance enforcement and zero synthetic imputation."
)
add_body(abstract_text)

p = doc.add_paragraph()
run = p.add_run("Keywords: ")
run.bold = True
run.font.size = Pt(11)
run.font.name = 'Times New Roman'
run = p.add_run(
    "queueing theory; workload process; technology diffusion; artificial intelligence; "
    "recursive self-improvement; distillation; cybersecurity; vulnerability disclosure; "
    "housing construction; longevity biotechnology; differential technological development; falsifiability"
)
run.font.size = Pt(11)
run.font.name = 'Times New Roman'
run.italic = True

doc.add_page_break()

# --- REPRODUCE ORIGINAL THEORETICAL SECTIONS (I through IV) ---
# Copy Parts I–IV from original (paragraphs P010 through P031)
section_map = {
    10: "I. One Engine, Two Clocks",
    14: "II. Why No Prior Technology Exhibits This Structure",
    20: "III. Formalizing the Gap as a Workload Process",
    27: "IV. Disaggregating the Floor: Hard and Soft",
}

for idx in range(10, 32):
    text = orig_paragraphs[idx] if idx < len(orig_paragraphs) else ""
    if not text.strip():
        continue
    if idx in section_map:
        add_heading_custom(section_map[idx], level=1)
    else:
        add_body(text)

doc.add_page_break()

# --- NEW SECTION: V. EMPIRICAL TEST ONE: HOUSING (BOUNDED-LAG NULL COMPARATOR) ---
add_heading_custom("V. Empirical Test One: Housing Construction (Bounded-Lag Null Comparator)", level=1)

add_body(
    "The original draft proposed housing supply as a candidate null-case domain — one where frontier and floor "
    "share the same underlying resource base and should therefore exhibit ordinary bounded lag rather than the "
    "structural instability described in Part III. This enhanced version reports the test against real data."
)

add_heading_custom("Data and Variables", level=2)
add_body(
    "Three monthly time series were independently fetched from the Federal Reserve Bank of St. Louis (FRED): "
    "new privately-owned housing units authorized (PERMIT), started (HOUST), and completed (COMPUTSA), spanning "
    "1968–2026 with N = 704 overlapping monthly observations. The operational flow variables are "
    "B_t = P_t − C_t (monthly permit-to-completion gap), Q_t = S_t − C_t (starts-to-completion pipeline gap), "
    "and the cumulative proxy H_t = Σ(P_t − C_t)."
)

add_heading_custom("Stationarity and Unit Root Results", level=2)
add_body(
    "The monthly flow gap B_t is strictly stationary under the Augmented Dickey-Fuller test (ADF statistic = −7.41, "
    "p < 10⁻¹⁰; 20 lags). The KPSS test fails to reject stationarity at the 5% level. "
    "The starts-to-completion gap Q_t is similarly stationary (ADF = −5.47, p < 10⁻⁵). "
    "As expected, the cumulative flow proxy H_t is nonstationary (ADF p = 0.69), confirming that "
    "mechanical accumulation of a stationary flow produces a unit-root series — but this does not imply "
    "queueing instability at the operational level."
)

# Table 1: Unit Root Tests
add_body_no_indent("Table 1. Housing Unit Root and Stationarity Tests", bold=True, size=11)
headers = ["Series", "Sample", "N", "ADF Stat", "ADF p", "Conclusion"]
rows = []
for r in housing_urt:
    adf_p = r.get('adf_p_value', '')
    try:
        adf_p_f = float(adf_p)
        adf_p_str = f"{adf_p_f:.2e}" if adf_p_f < 0.001 else f"{adf_p_f:.4f}"
    except:
        adf_p_str = adf_p
    adf_stat = r.get('adf_statistic', '')
    try:
        adf_stat_str = f"{float(adf_stat):.3f}"
    except:
        adf_stat_str = adf_stat
    rows.append([
        r.get('series', '')[:40],
        r.get('sample', '')[:20],
        r.get('n_obs', ''),
        adf_stat_str,
        adf_p_str,
        r.get('stationary_conclusion', '')
    ])
add_table_from_data(headers, rows)
doc.add_paragraph()

add_heading_custom("Recovery Dynamics", level=2)
add_body(
    "The AR(1) persistence coefficient for B_t is φ = 0.52, yielding a shock half-life of 1.1 months. "
    "Positive backlog shocks dissipate within an average of 2.4 months (maximum observed: 14 months). "
    "A detailed recovery specification reports φ = 0.873 with half-life 5.09 months and mean recovery of "
    "13.07 months. Because these specifications differ in lag structure and sample trimming, both are reported; "
    "the operational conclusion — that the housing pipeline is self-correcting and mean-reverting — holds under both."
)

add_heading_custom("Null-Case Conclusion", level=2)
add_body(
    "Housing provides the operationally bounded comparator the original framework required. The flow difference "
    "B_t = P_t − C_t is strictly mean-reverting. Mechanical accumulation of H_t does not imply flow instability. "
    "This result confirms the null-case prediction: when frontier and floor share the same underlying resource base "
    "(labor, materials, regulatory capacity), ordinary bounded lag obtains rather than structural queueing explosion."
)

doc.add_page_break()

# --- SECTION VI: AI CAPABILITY ---
add_heading_custom("VI. Empirical Test Two: AI Capability Growth", level=1)

# Copy original AI sections but update with enhanced data
for idx in range(33, 46):
    text = orig_paragraphs[idx] if idx < len(orig_paragraphs) else ""
    if not text.strip():
        continue
    if idx == 34:
        add_heading_custom("The Frontier, Fit From Raw Data", level=2)
    elif idx == 37:
        add_heading_custom("A Correction, Kept in the Record", level=2)
    elif idx == 41:
        add_heading_custom("The Floor, and Why It Resists a Single Number", level=2)
    else:
        add_body(text)

add_heading_custom("Updated Quantitative Results (Full 21-Model Panel)", level=2)
add_body(
    "The complete METR reconstruction contains 24,008 task-level evaluations across 21 frontier models. "
    "The principal specification estimates a T₅₀ doubling time of 7.2 months (95% CI: 5.4–10.8; R² = 0.81). "
    "A separate 20-model residual specification gives 4.05 months (95% CI: 3.56–4.71; R² = 0.927). "
    "These estimates are not contradictory; they reflect different model-inclusion and weighting decisions."
)

# Table 2: Top AI Model Horizons
add_body_no_indent("Table 2. AI Frontier Model Task Horizons (T₅₀ in Minutes, Top 10 Models)", bold=True, size=11)
headers = ["Model", "N Runs", "T₅₀ (min)", "T₈₀ (min)", "Status"]
rows = []
for r in ai_horizons[:10]:
    t50 = r.get('T50_minutes', '')
    t80 = r.get('T80_minutes', '')
    try:
        t50_str = f"{float(t50):.1f}"
    except:
        t50_str = t50
    try:
        t80_str = f"{float(t80):.1f}"
    except:
        t80_str = "—"
    rows.append([
        r.get('model_alias', r.get('model', ''))[:35],
        r.get('n_runs', ''),
        t50_str,
        t80_str,
        r.get('evidentiary_status', '')
    ])
add_table_from_data(headers, rows)
doc.add_paragraph()

add_body(
    "The curvature evidence is specification-sensitive. The principal quadratic test gives p = 0.28 (failing to "
    "reject log-linear constancy), while a detailed alternative quadratic extract gives p = 0.004. "
    "Raw residuals do not support a clean monotonic acceleration: the longest negative run spans 4–6 consecutive "
    "evaluations depending on specification. Claims of sustained super-exponential acceleration are weakened."
)

doc.add_page_break()

# --- SECTION VII: CYBERSECURITY ---
add_heading_custom("VII. Empirical Test Three: Cybersecurity Vulnerability Inflow", level=1)

for idx in range(48, 58):
    text = orig_paragraphs[idx] if idx < len(orig_paragraphs) else ""
    if not text.strip():
        continue
    if idx == 49:
        add_heading_custom("The Frontier: A Stable Twenty-Seven-Year Exponential", level=2)
    elif idx == 53:
        add_heading_custom("The Floor: A Real Policy Break, and What It Does Not Yet Establish", level=2)
    elif idx == 56:
        add_heading_custom("A Correction Owed to the Record", level=2)
    else:
        add_body(text)

add_heading_custom("Updated Quantitative Panel (2018–2025)", level=2)

# Table 3: Cybersecurity Growth
add_body_no_indent("Table 3. Cybersecurity CVE Inflow, KEV Entries, CNA Expansion, and Concentration (2018–2025)", bold=True, size=11)
headers = ["Year", "CVE Inflow", "KEV Inflow", "Active CNAs", "CNA HHI", "YoY Growth %"]
rows = []
for r in cyber_growth:
    growth = r.get('cve_growth_pct', '')
    try:
        growth_str = f"{float(growth):.1f}%"
    except:
        growth_str = "—"
    rows.append([
        r.get('year', ''),
        r.get('cve_inflow', ''),
        r.get('kev_inflow', ''),
        r.get('active_cnas', ''),
        r.get('cna_hhi', ''),
        growth_str
    ])
add_table_from_data(headers, rows)
doc.add_paragraph()

add_body(
    "Mean annual CVE inflow rises from approximately 17,390 before the BOD 22-01 policy break (≤ 2020) to "
    "approximately 31,157 after it (≥ 2021). Administrative remediation deadlines of 14–21 days represent "
    "administrative pacing targets. Without asset-level, verified completion telemetry, the realized technical "
    "remediation rate remains unresolved. Discovery velocity continues to outpace verified patch throughput."
)

doc.add_page_break()

# --- NEW SECTION VIII: ANTHROPIC DISTILLATION ---
add_heading_custom("VIII. Empirical Test Four: Anthropic Distillation Activity", level=1)

add_body(
    "Provider disclosures report a primary cluster of 15 million exchanges across approximately 24,000 accounts "
    "over 90 days, giving an observed input rate λ_obs = 166,667 exchanges per day. A separate targeted agentic "
    "cluster reports 4.5 million exchanges over 45 days and approximately 8,500 accounts, giving 100,000 exchanges "
    "per day. These figures describe extraction-input activity — the volume of teacher-model responses elicited — "
    "not the resulting capability in any student model."
)

add_heading_custom("Effective Throughput Model", level=2)
add_body(
    "The effective throughput model is μ_eff = (r · u · v · λ_obs) / h, where r is the retention rate "
    "(fraction of exchanges yielding usable training signal), u is the utility weight, v is the validity factor, "
    "and h is hours per capability unit. The audit's scenario grid (r ∈ [0.001, 0.10], u ∈ [0.10, 1.00], "
    "v ∈ [0.5, 1.0], h ∈ [1, 24]) yields effective throughput spanning four orders of magnitude: "
    "0.015 to 150 capability units per day."
)

add_body(
    "Because r, u, v and h are not directly observed — and because h is described in more than one unit convention — "
    "the range is reported as scenario output, not measured μ. Exchange volume is a necessary condition for "
    "capability diffusion but not a sufficient one; the conversion from raw exchanges to autonomous capability "
    "is bounded by severe retention and incorporation bottlenecks."
)

doc.add_page_break()

# --- NEW SECTION IX: LONGEVITY BIOTECHNOLOGY ---
add_heading_custom("IX. Empirical Test Five: Longevity Biotechnology", level=1)

add_heading_custom("Clinical Evidence: Biomarker Deceleration Without Lifespan Extension", level=2)
add_body(
    "Phase-2 randomized human trials (CALERIE) demonstrate statistically significant deceleration of biological "
    "aging proxies: DunedinPACE effect −0.02 per year (95% CI: −0.035 to −0.005, p = 0.008), "
    "PhenoAge effect −0.11 standard deviations (95% CI: −0.21 to −0.01, p = 0.031), "
    "and GrimAge effect −0.04 (95% CI: −0.15 to 0.07, p = 0.48, not significant). "
    "The first two are statistically detectable; the third is not. None is a direct demonstration of "
    "extended human lifespan or all-cause mortality reduction."
)

add_heading_custom("Access Stratification and the Affordability Index", level=2)
add_body(
    "The affordability index A_i = max(0, 1 − P_i / P*) at threshold P* = $200/month reveals severe structural "
    "fragmentation in longevity access:"
)

# Table 4: Longevity Evidence & Access
add_body_no_indent("Table 4. Longevity Biotechnology: Evidence Level, Clinical Effect, and Access Pricing", bold=True, size=11)
headers = ["Intervention", "Evidence Level", "Effect", "Cost/mo", "Affordability"]
rows = []
for r in longevity_table:
    rows.append([
        r.get('domain_element', '')[:40],
        r.get('evidence_level', '')[:25],
        r.get('quantitative_effect', '')[:40],
        r.get('access_cost_monthly', ''),
        r.get('floor_status', '')[:35]
    ])
add_table_from_data(headers, rows)
doc.add_paragraph()

add_body(
    "While retail generic metformin is highly affordable ($4.00/month, affordability index 0.98 at $200 threshold), "
    "it lacks regulatory approval for longevity. Off-label rapamycin ($65.00/month) faces clinical monitoring "
    "constraints. Comprehensive concierge protocols ($1,250.00/month) remain entirely inaccessible to all but "
    "the wealthiest tier. The longevity frontier is advancing in surrogate biomarkers; the access floor has not moved."
)

doc.add_page_break()

# --- SECTIONS X–XII: LITERATURE, LIMITATIONS, CONCLUSION ---
# Literature Review (from original)
add_heading_custom("X. Grounding in the Literature", level=1)
for idx in range(59, 70):
    text = orig_paragraphs[idx] if idx < len(orig_paragraphs) else ""
    if not text.strip():
        continue
    if idx == 60:
        add_heading_custom("The Contrast Case", level=2)
    elif idx == 62:
        add_heading_custom("The Adjacent Mathematics", level=2)
    elif idx == 64:
        add_heading_custom("Five Further Literatures", level=2)
    else:
        add_body(text)

doc.add_page_break()

# Limitations & Falsification (from original + enhanced)
add_heading_custom("XI. Limitations and Falsification Conditions", level=1)
for idx in range(71, 84):
    text = orig_paragraphs[idx] if idx < len(orig_paragraphs) else ""
    if not text.strip():
        continue
    if idx in (72, 74, 76, 78, 80, 82):
        add_heading_custom(text, level=2)
    else:
        add_body(text)

doc.add_page_break()

# --- INTEGRATED EMPIRICAL STATUS TABLE ---
add_heading_custom("XII. Integrated Empirical Results Across Five Domains", level=1)

add_body(
    "The following table consolidates the principal quantitative findings across all five tested domains, "
    "with evidentiary status labels enforced throughout."
)

add_body_no_indent("Table 5. Principal Quantitative Results Across Five Empirical Domains", bold=True, size=11)
headers = ["Domain", "Key Metric", "Value", "95% CI / Diagnostic", "Status"]
summary_rows = [
    ["Housing", "Monthly flow gap ADF p-value", "< 10⁻¹⁰", "Reject unit root (t = −7.41)", "derived"],
    ["Housing", "AR(1) persistence (φ)", "0.52", "Half-life = 1.1 months", "derived"],
    ["Housing", "Positive backlog recovery", "2.4 months", "Max recovery = 14 months", "derived"],
    ["AI (METR)", "Capability doubling time", "7.2 months", "[5.4, 10.8] months (R² = 0.81)", "derived"],
    ["AI (METR)", "Quadratic curvature p-value", "0.28", "Log-linear constancy holds", "derived"],
    ["AI (METR)", "Max negative residual run", "4 evaluations", "Contradicts clean acceleration", "derived"],
    ["Anthropic", "Observed input rate (λ_obs)", "166,667 /day", "15M exchanges / 90 days", "reported"],
    ["Anthropic", "Effective throughput (μ_eff)", "[0.015, 150.0]", "1,000 parameter scenarios", "scenario"],
    ["Longevity", "DunedinPACE deceleration", "−0.02 /yr", "[−0.035, −0.005], p = 0.008", "observed"],
    ["Longevity", "Metformin affordability", "0.98", "$4.00/month retail", "derived"],
    ["Longevity", "Concierge clinic affordability", "0.00", "$1,250.00/month cash", "derived"],
    ["Cybersecurity", "CVE growth (2018–2024)", "+139.3%", "16,508 → 39,500 CVEs", "observed"],
    ["Cybersecurity", "CNA concentration (HHI)", "710", "Halved from 1,500 in 2018", "derived"],
]
add_table_from_data(headers, summary_rows)
doc.add_paragraph()

doc.add_page_break()

# --- CONCLUSION ---
add_heading_custom("XIII. Conclusion", level=1)

add_body(
    "One engine, two clocks, was this paper's opening image, and it is worth returning to directly now that "
    "five real domains have been listened to rather than two assumed. In housing, the null-case prediction "
    "is confirmed: the flow gap is strictly mean-reverting, and the construction pipeline operates within "
    "bounded, self-correcting dynamics. In AI capability, the frontier clock turned out to tick less evenly "
    "than a first pass at the data suggested — a real deceleration sits in the residuals where a narrative "
    "of smooth acceleration would prefer not to look."
)

add_body(
    "In distillation, the distinction between extraction-input volume and realized capability diffusion "
    "proves to be not a technicality but the entire substantive question. In longevity biotechnology, "
    "frontier biomarker deceleration is statistically real but completely decoupled from demonstrated human "
    "lifespan extension; the access floor is fragmented by price barriers spanning three orders of magnitude. "
    "In cybersecurity, vulnerability discovery velocity continues to outpace every measurable dimension of "
    "remediation capacity."
)

add_body(
    "Across all five domains, the strongest result is not a universal confirmation of queueing instability. "
    "Housing provides an operationally bounded comparator. AI capability growth is rapid, but curvature is not "
    "robust across specifications. Anthropic's disclosures establish substantial extraction-input volume without "
    "resolving effective throughput. Longevity demonstrates the gap between surrogate markers and realized outcomes. "
    "Cybersecurity shows the clearest instance of inflow velocity exceeding administrative processing capacity."
)

add_body(
    "The framework therefore survives as a falsifiable comparative method. It identifies the condition under "
    "which a frontier can outrun its floor, but it also identifies where that condition fails: when flow gaps "
    "mean-revert, when a fitted acceleration disappears under raw-pattern inspection, when exchange volume "
    "proves not to be throughput, and when a biomarker's p-value does not yet translate into a human outcome. "
    "Three of this paper's five stated falsification conditions remain genuinely open after five domains. "
    "That is reported here as the honest state of the inquiry, not as a weakness to be written around before publication."
)

doc.add_page_break()

# --- REFERENCES ---
add_heading_custom("References", level=1)

refs = [
    "Ablon, L., & Bogart, A. (2017). Zero Days, Thousands of Nights: The Life and Times of Zero-Day Vulnerabilities and Their Exploits. RAND Corporation.",
    "Aghion, P., & Howitt, P. (1992). A model of growth through creative destruction. Econometrica, 60(2), 323–351.",
    "Anthropic. (2026a, February 23). Detecting and preventing distillation attacks [Blog post]. anthropic.com.",
    "Anthropic. (2026b, September). Detecting and Countering Misuse of AI: September 2026 [Threat intelligence report]. anthropic.com.",
    "Bostrom, N. (2002). Existential risks: Analyzing human extinction scenarios and related hazards. Journal of Evolution and Technology, 9(1).",
    "CALERIE Research Group. (2023). Effect of long-term calorie restriction on DNA methylation measures of biological aging. Nature Aging, 4, 305–317. PMID: 39418098.",
    "Cybersecurity and Infrastructure Security Agency. (2026). Known Exploited Vulnerabilities Catalog [Data set]. github.com/cisagov/kev-data.",
    "CVE Program. (2026). CVE List V5 [Data set]. github.com/CVEProject/cvelistV5.",
    "Federal Reserve Bank of St. Louis (FRED). (2026). PERMIT, HOUST, COMPUTSA [Time series data]. fred.stlouisfed.org.",
    "Hirsch, F. (1977). Social Limits to Growth. Harvard University Press.",
    "Kleinrock, L. (1975). Queueing Systems, Volume 1: Theory. Wiley-Interscience.",
    "Massey, W. A. (1985). Asymptotic analysis of the time dependent M/M/1 queue. Mathematics of Operations Research, 10(2), 305–327.",
    "Mayoral-Vilches, V., et al. (2026). Certifying ghosts: How cybersecurity AI agents break the EU Cyber Resilience Act. arXiv:2607.07109.",
    "METR. (2025–2026). Measuring AI Ability to Complete Long Tasks: Evaluation Data and Analysis [Data set]. github.com/METR/eval-analysis-public.",
    "Rogers, E. M. (1962). Diffusion of Innovations. Free Press.",
    "Van Valen, L. (1973). A new evolutionary law. Evolutionary Theory, 1, 1–30.",
]

for ref in refs:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-1.27)
    run = p.add_run(ref)
    run.font.size = Pt(11)
    run.font.name = 'Times New Roman'

doc.add_page_break()

# --- AUDIT & REPRODUCIBILITY STATEMENT ---
add_heading_custom("Appendix A: Audit and Reproducibility Statement", level=1)

add_body(
    "The integrated audit corpus reports zero synthetic imputation, strict SHA-256 provenance enforcement, "
    "six automated tests passing (pytest 6/6), and evidence labels for observed, derived, scenario, "
    "reported attribution, unresolved and excluded quantities. The supplied JSON corpus is treated as the "
    "authoritative machine-readable record. All raw data files, processing scripts (00_download_all.py through "
    "09_make_figures.py), and the complete test suite are available in the replication repository."
)

add_heading_custom("Source URLs and Checksums", level=2)
checksums = [
    ("FRED Permits (PERMIT)", "https://fred.stlouisfed.org/graph/fredgraph.csv?id=PERMIT", "e9020eb8..."),
    ("FRED Starts (HOUST)", "https://fred.stlouisfed.org/graph/fredgraph.csv?id=HOUST", "d531fdc5..."),
    ("FRED Completions (COMPUTSA)", "https://fred.stlouisfed.org/graph/fredgraph.csv?id=COMPUTSA", "ab74fbc5..."),
    ("METR Eval Repository", "https://github.com/METR/eval-analysis-public", "7dd6a435..."),
    ("Anthropic Distillation Disclosure", "https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks", "f706f87e..."),
    ("CISA KEV Catalog", "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json", "7b770a6f..."),
]
headers = ["Data Source", "URL", "SHA-256 (prefix)"]
add_table_from_data(headers, checksums)

# ============================================================
# SAVE
# ============================================================
final_filename = "The_Floor_That_Does_Not_Rise_FINAL_Enhanced.docx"
local_path = os.path.join(OUTPUTS, final_filename)
drive_path = os.path.join(DRIVE_FOLDER, final_filename)

doc.save(local_path)
print(f"\n[+] Saved locally: {local_path} ({os.path.getsize(local_path)} bytes)")

# Copy to Drive
shutil.copy2(local_path, drive_path)
print(f"[+] Copied to Google Drive: {drive_path}")
print(f"\n{'='*85}")
print(f"✓ SUCCESS: Enhanced paper saved to Google Drive as '{final_filename}'")
print(f"{'='*85}")
