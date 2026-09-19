import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

out_path = r"C:\Users\nswcl\.gemini\antigravity-ide\scratch\the-floor-that-does-not-rise\alrp_context_dump.txt"

with open(out_path, 'w', encoding='utf-8', errors='ignore') as out:
    def log(text):
        out.write(text + "\n")

    def read_file_safe(path):
        log(f"\n{'='*70}\nFILE: {path}\n{'='*70}")
        if not os.path.exists(path):
            log(f"[-] Not found: {path}")
            return
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            log(content)
            print(f"[+] Read {path}: {len(content)} characters")

    # 1. Read NOTEBOOKLM_ALRP_FULL_CONTEXT_AND_AGENT_MEMORY.md
    nb_path = r"G:\Drive của tôi\Obsidian_Vault\01_AI_Copilot_Hub\NOTEBOOKLM_ALRP_FULL_CONTEXT_AND_AGENT_MEMORY.md"
    read_file_safe(nb_path)

    # 2. Read ALRP files from Claude directory
    alrp_dir = r"C:\Users\nswcl\Claude\00_LAR_OS\ALRP"
    for f in sorted(glob.glob(os.path.join(alrp_dir, "*.md"))):
        read_file_safe(f)

    # 3. Read Protocol_NotebookLM_Task_Expansion.md if exists
    proto_path = r"G:\Drive của tôi\Obsidian_Vault\Protocol_NotebookLM_Task_Expansion.md"
    read_file_safe(proto_path)

print(f"\n[+] Full ALRP context dumped to {out_path} ({os.path.getsize(out_path)} bytes)")

