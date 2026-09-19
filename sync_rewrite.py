import sys
import os
import subprocess
import ctypes
from ctypes import wintypes
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parent

# Read credentials from Windows Credential Manager
CRED_TYPE_GENERIC = 1

class CREDENTIAL(ctypes.Structure):
    _fields_ = [
        ('Flags', wintypes.DWORD),
        ('Type', wintypes.DWORD),
        ('TargetName', wintypes.LPWSTR),
        ('Comment', wintypes.LPWSTR),
        ('LastWritten', wintypes.FILETIME),
        ('CredentialBlobSize', wintypes.DWORD),
        ('CredentialBlob', ctypes.POINTER(ctypes.c_byte)),
        ('Persist', wintypes.DWORD),
        ('AttributeCount', wintypes.DWORD),
        ('Attributes', ctypes.c_void_p),
        ('TargetAlias', wintypes.LPWSTR),
        ('UserName', wintypes.LPWSTR),
    ]

PCREDENTIAL = ctypes.POINTER(CREDENTIAL)
CredRead = ctypes.windll.advapi32.CredReadW
CredRead.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.POINTER(PCREDENTIAL)]
CredRead.restype = wintypes.BOOL
CredFree = ctypes.windll.advapi32.CredFree
CredFree.argtypes = [ctypes.c_void_p]

def get_credential(target):
    pcred = PCREDENTIAL()
    res = CredRead(target, CRED_TYPE_GENERIC, 0, ctypes.byref(pcred))
    if not res:
        return None, None
    cred = pcred.contents
    username = cred.UserName
    blob_size = cred.CredentialBlobSize
    blob = ctypes.string_at(cred.CredentialBlob, blob_size)
    CredFree(pcred)
    try:
        secret = blob.decode('utf-16-le')
    except Exception:
        try:
            secret = blob.decode('utf-8')
        except Exception:
            secret = str(blob)
    return username, secret

_, gh_token = get_credential("git:https://github.com")
_, hf_token = get_credential("git:https://huggingface.co")

# 1. Push to GitHub
print("\n[+] Syncing with GitHub...")
try:
    subprocess.run(["git", "add", "."], cwd=PROJECT_ROOT, check=True)
    status_output = subprocess.run(["git", "status", "--porcelain"], cwd=PROJECT_ROOT, capture_output=True, text=True).stdout
    if status_output.strip():
        commit_msg = "feat: Complete rewrite of The Floor That Does Not Rise grounded in ALRP canon (13 queueing models, 4 bottleneck floors, Rule Zero)"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=PROJECT_ROOT, check=True)
        print("[+] Created commit for rewrite.")
    else:
        print("[i] Nothing new to commit.")

    gh_username = "giabaohuynhasu"
    gh_repo_name = "the-floor-that-does-not-rise"
    remote_url = f"https://{gh_username}:{gh_token}@github.com/{gh_username}/{gh_repo_name}.git" if gh_token else f"https://github.com/{gh_username}/{gh_repo_name}.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], cwd=PROJECT_ROOT, check=True)

    push_res = subprocess.run(["git", "push", "origin", "main"], cwd=PROJECT_ROOT, capture_output=True, text=True)
    if push_res.returncode == 0:
        print(f"[✓] Successfully pushed rewrite to GitHub: https://github.com/{gh_username}/{gh_repo_name}")
    else:
        print(f"[-] Git push error: {push_res.stderr or push_res.stdout}")

    # Reset remote URL for security
    subprocess.run(["git", "remote", "set-url", "origin", f"https://github.com/{gh_username}/{gh_repo_name}.git"], cwd=PROJECT_ROOT)

except Exception as e:
    print(f"[-] GitHub sync error: {e}")

# 2. Upload to Hugging Face
print("\n[+] Syncing with Hugging Face Hub...")
if hf_token:
    try:
        from huggingface_hub import HfApi
        api = HfApi(token=hf_token)
        hf_repo_id = "Jun33550336/the-floor-that-does-not-rise"
        api.upload_folder(
            folder_path=str(PROJECT_ROOT),
            repo_id=hf_repo_id,
            repo_type="dataset",
            ignore_patterns=[
                ".venv/**",
                "**/__pycache__/**",
                ".pytest_cache/**",
                ".git/**",
                "data/raw/ai_metr/eval-analysis-public/**",
                "test_*.py",
                "read_*.py",
                "send_*.py",
                "sync_*.py",
                "alrp_context_dump.txt"
            ],
            commit_message="feat: Complete rewrite of The Floor That Does Not Rise grounded in ALRP canon (13 queueing models, 4 bottleneck floors, Rule Zero)"
        )
        print(f"[✓] Successfully synced to Hugging Face Dataset: https://huggingface.co/datasets/{hf_repo_id}")
    except Exception as e:
        print(f"[-] Hugging Face sync error: {e}")
else:
    print("[-] Hugging Face token not found.")
