"""
08_make_tables.py - Table Consolidation & Master Excel Workbook Generation

Reads all individual tables from outputs/tables/ and compiles them into
a unified, publication-ready Excel workbook: outputs/all_tables.xlsx.
"""

import os
import sys
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_TABLES = PROJECT_ROOT / "outputs" / "tables"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

def main():
    print("=" * 60)
    print("Consolidating Tables into Master Workbook (08_make_tables.py)")
    print("=" * 60)
    
    excel_path = OUTPUTS_DIR / "all_tables.xlsx"
    csv_files = sorted(list(OUTPUTS_TABLES.glob("*.csv")))
    
    if not csv_files:
        print("[WARNING] No CSV tables found in outputs/tables/.")
        return
        
    print(f"Found {len(csv_files)} tables to compile into {excel_path.name}:")
    
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for f in csv_files:
            sheet_name = f.stem[:31] # Excel 31-char limit
            df = pd.read_csv(f)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"  + Sheet '{sheet_name}': {len(df)} rows, {len(df.columns)} columns")
            
    print(f"\n[COMPLETE] Successfully generated master workbook: {excel_path} ({excel_path.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()
