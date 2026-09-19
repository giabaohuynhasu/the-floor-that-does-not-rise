import os
import sys
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def read_text_safe(path, max_chars=3000):
    p = Path(path)
    if not p.exists():
        return f"[NOT FOUND: {path}]"
    try:
        content = p.read_text(encoding="utf-8", errors="ignore")
        return content[:max_chars]
    except Exception as e:
        return f"[ERROR READING: {e}]"

def summarize_eri():
    print("=================== ERI (INSTITUTIONAL ENDURANCE) ===================")
    eri_dir = Path(r"C:\Users\nswcl\OneDrive\Documents\Obsidian Vault\01_AI_Copilot_Hub\00_LAR_OS\ERI")
    for f in eri_dir.glob("*.md"):
        print(f"\n--- {f.name} ---")
        print(read_text_safe(f, 1500))

def summarize_war_correspondent():
    print("\n=================== WAR CORRESPONDENT PHILOSOPHY ===================")
    wc_dir = Path(r"C:\Users\nswcl\OneDrive\Documents\Obsidian Vault\01_AI_Copilot_Hub\War_Correspondent_Philosophy")
    for f in wc_dir.glob("*.md"):
        print(f"\n--- {f.name} ---")
        print(read_text_safe(f, 1200))

def summarize_fact_before_vote():
    print("\n=================== THE FACT BEFORE THE VOTE ===================")
    fbv_dir = Path(r"G:\Drive của tôi\02_The_Fact_Before_the_Vote\AI_PERSONHOOD_Archive")
    for f in fbv_dir.glob("*.md"):
        print(f"\n--- {f.name} ---")
        print(read_text_safe(f, 1200))

def summarize_merit_gatekeeping():
    print("\n=================== IN THE NAME OF MERIT ===================")
    merit_dir = Path(r"G:\Drive của tôi\05_In_the_Name_of_Merit_and_Gatekeeping\Manuscripts_and_Notes")
    for f in merit_dir.glob("*.docx"):
        print(f"[DOCX] {f.name} ({f.stat().st_size} bytes)")
    for f in merit_dir.glob("*.pdf"):
        print(f"[PDF]  {f.name} ({f.stat().st_size} bytes)")

if __name__ == "__main__":
    summarize_eri()
    summarize_war_correspondent()
    summarize_fact_before_vote()
    summarize_merit_gatekeeping()
