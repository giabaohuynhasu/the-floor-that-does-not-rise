import os
import shutil
import sys
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE = Path(r"c:\Users\nswcl\.gemini\antigravity-ide\scratch\the-floor-that-does-not-rise")
OBSIDIAN_HUB = Path(r"C:\Users\nswcl\OneDrive\Documents\Obsidian Vault\01_AI_Copilot_Hub")
DRIVE_ROOT = Path(r"G:\Drive của tôi")

def copy_tree_safe(src: Path, dst: Path):
    if not src.exists():
        print(f"[SKIP] Source does not exist: {src}")
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            shutil.copy2(item, target)
    print(f"[COPIED] {src.name} -> {dst}")

def sync_all():
    print("=== SYNCING KNOWLEDGE GRAPHS TO OBSIDIAN VAULT ===")
    copy_tree_safe(BASE / "knowledge_graph", OBSIDIAN_HUB / "knowledge_graph_alrp")
    copy_tree_safe(BASE / "knowledge_graph_eri", OBSIDIAN_HUB / "knowledge_graph_eri")
    copy_tree_safe(BASE / "knowledge_graph_lac", OBSIDIAN_HUB / "knowledge_graph_lac")
    copy_tree_safe(BASE / "knowledge_graph_war_correspondent", OBSIDIAN_HUB / "knowledge_graph_war_correspondent")
    copy_tree_safe(BASE / "knowledge_graph_fact_and_merit", OBSIDIAN_HUB / "knowledge_graph_fact_and_merit")

    print("\n=== SYNCING KNOWLEDGE GRAPHS TO GOOGLE DRIVE ===")
    copy_tree_safe(BASE / "knowledge_graph", DRIVE_ROOT / "01_Longevity_Asymmetry_and_LAC" / "LONGEVITYWAVE" / "knowledge_graph_alrp")
    copy_tree_safe(BASE / "knowledge_graph_eri", DRIVE_ROOT / "04_Institutional_Endurance_and_History" / "knowledge_graph_eri")
    copy_tree_safe(BASE / "knowledge_graph_lac", DRIVE_ROOT / "01_Longevity_Asymmetry_and_LAC" / "knowledge_graph_lac")
    copy_tree_safe(BASE / "knowledge_graph_war_correspondent", DRIVE_ROOT / "03_War_Correspondent_Philosophy" / "knowledge_graph_war_correspondent")
    copy_tree_safe(BASE / "knowledge_graph_fact_and_merit", DRIVE_ROOT / "02_The_Fact_Before_the_Vote" / "knowledge_graph_fact_and_merit")
    copy_tree_safe(BASE / "knowledge_graph_fact_and_merit", DRIVE_ROOT / "05_In_the_Name_of_Merit_and_Gatekeeping" / "knowledge_graph_fact_and_merit")

    print("\n[ALL KNOWLEDGE GRAPHS SUCCESSFULLY SYNCED TO OBSIDIAN & DRIVE!]")

if __name__ == "__main__":
    sync_all()
