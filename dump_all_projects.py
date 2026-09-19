import os, sys

sys.stdout.reconfigure(encoding='utf-8')

out_path = r"C:\Users\nswcl\.gemini\antigravity-ide\scratch\the-floor-that-does-not-rise\all_projects_context_dump.txt"

files_to_read = [
    r"G:\Drive của tôi\Obsidian_Vault\01_AI_Copilot_Hub\NOTEBOOKLM_ERI_FULL_CONTEXT_AND_AGENT_MEMORY.md",
    r"G:\Drive của tôi\Obsidian_Vault\01_AI_Copilot_Hub\ERI_RESEARCH_AGENT.md",
    r"G:\Drive của tôi\Obsidian_Vault\01_AI_Copilot_Hub\THU_TUONG_CHATGPT_ALRP_ERI_SAC_LENH.md",
    r"G:\Drive của tôi\Obsidian_Vault\01_AI_Copilot_Hub\operaneon_notebooklm_bridge.js",
    r"G:\Drive của tôi\Obsidian_Vault\01_AI_Copilot_Hub\ALRP_Queueing_Theory_Formal_Report_for_Claude.md"
]

with open(out_path, 'w', encoding='utf-8', errors='ignore') as out:
    for f in files_to_read:
        out.write(f"\n{'='*70}\nFILE: {f}\n{'='*70}\n")
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8', errors='ignore') as src:
                content = src.read()
                out.write(content + "\n")
                print(f"[+] Read {f}: {len(content)} characters")
        else:
            out.write("[-] Not found\n")
            print(f"[-] Not found: {f}")

print(f"\n[+] Dumped to {out_path} ({os.path.getsize(out_path)} bytes)")
