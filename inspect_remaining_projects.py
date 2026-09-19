import os
import glob
from pathlib import Path

def scan_dir(title, path, depth=2):
    print(f"\n=================== {title} ===================")
    p = Path(path)
    if not p.exists():
        print(f"Path does not exist: {path}")
        return
    for item in p.glob("*"):
        if item.is_dir():
            print(f"[DIR]  {item.name}")
            if depth > 1:
                for sub in item.glob("*"):
                    print(f"       -> {sub.name}")
        else:
            print(f"[FILE] {item.name} ({item.stat().st_size} bytes)")

def inspect_obsidian():
    obs_path = Path(r"C:\Users\nswcl\OneDrive\Documents\Obsidian Vault")
    print("\n=================== OBSIDIAN ERI ===================")
    eri_path = obs_path / "01_AI_Copilot_Hub" / "00_LAR_OS" / "ERI"
    if eri_path.exists():
        for f in eri_path.glob("*.md"):
            print(f"--- {f.name} ---")
            content = f.read_text(encoding="utf-8", errors="ignore")
            print(content[:500] + ("..." if len(content) > 500 else ""))

    print("\n=================== OBSIDIAN WAR CORRESPONDENT ===================")
    wc_path = obs_path / "01_AI_Copilot_Hub" / "War_Correspondent_Philosophy"
    if wc_path.exists():
        for f in wc_path.glob("*.md"):
            print(f"--- {f.name} ---")
            content = f.read_text(encoding="utf-8", errors="ignore")
            print(content[:400] + ("..." if len(content) > 400 else ""))

def inspect_drive_projects():
    base = Path(r"G:\Drive của tôi")
    projects = [
        ("04_Institutional_Endurance_and_History", base / "04_Institutional_Endurance_and_History"),
        ("01_Longevity_Asymmetry_and_LAC", base / "01_Longevity_Asymmetry_and_LAC"),
        ("02_The_Fact_Before_the_Vote", base / "02_The_Fact_Before_the_Vote"),
        ("03_War_Correspondent_Philosophy", base / "03_War_Correspondent_Philosophy"),
        ("05_In_the_Name_of_Merit_and_Gatekeeping", base / "05_In_the_Name_of_Merit_and_Gatekeeping"),
    ]
    for name, p in projects:
        scan_dir(name, p, depth=2)

if __name__ == "__main__":
    inspect_obsidian()
    inspect_drive_projects()
