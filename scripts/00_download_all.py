"""
00_download_all.py - Complete Automated Retrieval Pipeline

Downloads raw empirical data across Housing, AI (METR), Anthropic Distillation,
Longevity Biotechnology, and Cybersecurity.
Logs full metadata, HTTP headers, SHA-256 checksums, and source classifications.
"""

import os
import sys
import json
import hashlib
import datetime
import urllib.request
import urllib.error
import subprocess
import csv
from pathlib import Path

# Base paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
METADATA_DIR = PROJECT_ROOT / "metadata"

RETRIEVAL_LOG = METADATA_DIR / "retrieval_log.csv"
SOURCE_LEDGER = METADATA_DIR / "source_ledger.csv"
CHECKSUM_MANIFEST = METADATA_DIR / "checksum_manifest.csv"

def compute_sha256(filepath):
    """Computes SHA-256 checksum of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def append_csv(filepath, row_dict, fieldnames):
    """Appends a dictionary row to a CSV file."""
    file_exists = os.path.exists(filepath) and os.path.getsize(filepath) > 0
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row_dict)

def log_retrieval(url, source_title, publisher, pub_date, status, ctype, size, sha, tier, local_path, notes):
    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    fields = [
        "url", "source_title", "publisher_institution", "publication_date",
        "retrieval_timestamp_utc", "http_status", "content_type",
        "file_size_bytes", "sha256", "source_tier", "local_path", "notes"
    ]
    row = {
        "url": url,
        "source_title": source_title,
        "publisher_institution": publisher,
        "publication_date": pub_date,
        "retrieval_timestamp_utc": now_utc,
        "http_status": status,
        "content_type": ctype,
        "file_size_bytes": size,
        "sha256": sha,
        "source_tier": tier,
        "local_path": str(local_path),
        "notes": notes
    }
    append_csv(RETRIEVAL_LOG, row, fields)

def log_source(source_id, domain, title, publisher, stype, tier, url_or_repo, local_path, sha, version, status):
    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    fields = [
        "source_id", "domain", "source_title", "publisher_institution",
        "source_type", "source_tier", "url_or_repo", "local_path",
        "sha256", "retrieval_date_utc", "version_or_commit", "evidentiary_status"
    ]
    row = {
        "source_id": source_id,
        "domain": domain,
        "source_title": title,
        "publisher_institution": publisher,
        "source_type": stype,
        "source_tier": tier,
        "url_or_repo": url_or_repo,
        "local_path": str(local_path),
        "sha256": sha,
        "retrieval_date_utc": now_utc,
        "version_or_commit": version,
        "evidentiary_status": status
    }
    append_csv(SOURCE_LEDGER, row, fields)

def log_checksum(local_path, domain, status):
    p = Path(local_path)
    if not p.exists():
        return
    size = p.stat().st_size
    sha = compute_sha256(p)
    mtime = datetime.datetime.fromtimestamp(p.stat().st_mtime, datetime.timezone.utc).isoformat()
    fields = ["file_path", "file_size_bytes", "sha256", "last_modified_utc", "domain", "evidentiary_status"]
    row = {
        "file_path": str(p.relative_to(PROJECT_ROOT)),
        "file_size_bytes": size,
        "sha256": sha,
        "last_modified_utc": mtime,
        "domain": domain,
        "evidentiary_status": status
    }
    append_csv(CHECKSUM_MANIFEST, row, fields)

def download_file(url, target_path, source_title, publisher, tier, domain, pub_date="", headers=None):
    """Downloads a file with HTTP headers, logs provenance and checksum."""
    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    req_headers = {"User-Agent": "AntigravityResearchEngine/1.0 (reproducible-research-agent)"}
    if headers:
        req_headers.update(headers)
        
    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
            status = resp.status
            ctype = resp.headers.get("Content-Type", "")
            with open(target_path, "wb") as f:
                f.write(content)
            size = len(content)
            sha = compute_sha256(target_path)
            
            print(f"[SUCCESS] Downloaded: {url} -> {target_path} ({size} bytes, SHA: {sha[:8]}...)")
            log_retrieval(url, source_title, publisher, pub_date, status, ctype, size, sha, tier, target_path, "Success")
            log_checksum(target_path, domain, "observed")
            return target_path, sha
    except urllib.error.HTTPError as e:
        print(f"[HTTP ERROR] {url}: {e.code} {e.reason}")
        log_retrieval(url, source_title, publisher, pub_date, e.code, "", 0, "", tier, target_path, f"HTTPError: {e.reason}")
        return None, None
    except Exception as e:
        print(f"[ERROR] {url}: {str(e)}")
        log_retrieval(url, source_title, publisher, pub_date, 0, "", 0, "", tier, target_path, f"Error: {str(e)}")
        return None, None

def download_housing():
    print("\n=== 1. Downloading Housing Series ===")
    housing_dir = DATA_RAW / "housing"
    census_dir = housing_dir / "census"
    housing_dir.mkdir(parents=True, exist_ok=True)
    census_dir.mkdir(parents=True, exist_ok=True)
    
    fred_series = [
        ("PERMIT", "fred_PERMIT.csv", "New Privately-Owned Housing Units Authorized in Permit-Issuing Places"),
        ("HOUST", "fred_HOUST.csv", "New Privately-Owned Housing Units Started"),
        ("COMPUTSA", "fred_COMPUTSA.csv", "New Privately-Owned Housing Units Completed")
    ]
    
    for sid, fname, title in fred_series:
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"
        target = housing_dir / fname
        path, sha = download_file(url, target, title, "Federal Reserve Bank of St. Louis (FRED)", "primary official data", "housing")
        if path:
            log_source(f"FRED_{sid}", "housing", title, "Federal Reserve Bank of St. Louis", "CSV Time Series", "primary official data", url, path, sha, "latest", "observed")

    # Census historical tables
    census_tables = [
        ("https://www.census.gov/construction/nrc/xls/starts_cust.xlsx", census_dir / "starts_cust.xlsx", "Census NRC Historical Starts", "primary official data"),
        ("https://www.census.gov/construction/nrc/xls/co_cust.xlsx", census_dir / "co_cust.xlsx", "Census NRC Historical Completions", "primary official data"),
        ("https://www.census.gov/construction/nrc/xls/authnotstart_cust.xlsx", census_dir / "authnotstart_cust.xlsx", "Census NRC Authorized Not Started", "primary official data")
    ]
    for url, target, title, tier in census_tables:
        path, sha = download_file(url, target, title, "U.S. Census Bureau", tier, "housing")
        if path:
            log_source(f"CENSUS_{target.stem}", "housing", title, "U.S. Census Bureau", "Excel Historical Table", tier, url, path, sha, "historical", "observed")

def download_ai_metr():
    print("\n=== 2. Downloading METR AI Capability Data ===")
    ai_dir = DATA_RAW / "ai_metr"
    ai_dir.mkdir(parents=True, exist_ok=True)
    repo_dir = ai_dir / "eval-analysis-public"
    
    commit_hash = "unknown"
    branch = "main"
    
    # Try git clone first
    if not repo_dir.exists():
        print(f"[GIT] Cloning https://github.com/METR/eval-analysis-public.git into {repo_dir}...")
        try:
            res = subprocess.run(
                ["git", "clone", "--depth", "1", "https://github.com/METR/eval-analysis-public.git", str(repo_dir)],
                capture_output=True, text=True, timeout=120
            )
            if res.returncode == 0:
                print("[GIT] Clone successful.")
            else:
                print(f"[GIT ERROR] {res.stderr}")
        except Exception as e:
            print(f"[GIT EXCEPTION] {e}")
            
    # If clone succeeded, extract git info
    if repo_dir.exists() and (repo_dir / ".git").exists():
        try:
            c = subprocess.run(["git", "-C", str(repo_dir), "rev-parse", "HEAD"], capture_output=True, text=True)
            commit_hash = c.stdout.strip()
            b = subprocess.run(["git", "-C", str(repo_dir), "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True)
            branch = b.stdout.strip()
        except Exception:
            pass
            
    # Search for runs.jsonl or runs.csv in cloned repo
    raw_runs = []
    if repo_dir.exists():
        for root, _, files in os.walk(repo_dir):
            for f in files:
                if f in ["runs.jsonl", "runs.csv"]:
                    raw_runs.append(Path(root) / f)
                    
    print(f"[METR] Found {len(raw_runs)} candidate raw run files in repository.")
    for r in raw_runs:
        rel = r.relative_to(repo_dir)
        dest = ai_dir / f"{r.parent.name}_{r.name}"
        # Copy raw file unchanged
        with open(r, "rb") as sf, open(dest, "wb") as df:
            df.write(sf.read())
        sha = compute_sha256(dest)
        print(f"[METR RAW] Copied {rel} -> {dest} (SHA: {sha[:8]}...)")
        log_source(f"METR_{dest.stem}", "ai_metr", f"METR Evaluation Runs ({rel})", "METR", "Repository Raw JSONL/CSV", "repository data", "https://github.com/METR/eval-analysis-public", dest, sha, commit_hash, "observed")
        log_checksum(dest, "ai_metr", "observed")

    # Direct fallback if git clone was empty or failed
    if not raw_runs:
        print("[METR FALLBACK] Fetching raw runs.jsonl directly from GitHub raw content...")
        endpoints = [
            ("https://raw.githubusercontent.com/METR/eval-analysis-public/main/reports/time-horizon-1-1/data/raw/runs.jsonl", ai_dir / "time-horizon-1-1_runs.jsonl"),
            ("https://raw.githubusercontent.com/METR/eval-analysis-public/main/reports/time-horizon-1-0/data/raw/runs.jsonl", ai_dir / "time-horizon-1-0_runs.jsonl")
        ]
        for url, dest in endpoints:
            path, sha = download_file(url, dest, "METR Raw Task Evaluation Runs", "METR", "repository data", "ai_metr")
            if path:
                log_source(f"METR_{dest.stem}", "ai_metr", f"METR Evaluation Runs ({dest.name})", "METR", "Repository Raw JSONL", "repository data", url, path, sha, "main", "observed")

def download_anthropic():
    print("\n=== 3. Downloading Anthropic Distillation Data ===")
    ant_dir = DATA_RAW / "anthropic"
    ant_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. February 23, 2026 primary disclosure
    feb_url = "https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks"
    feb_target = ant_dir / "2026-02-23_primary_disclosure.html"
    path, sha = download_file(feb_url, feb_target, "Detecting and Preventing Distillation Attacks", "Anthropic", "primary organizational report", "anthropic", pub_date="2026-02-23")
    if path:
        log_source("ANTHROPIC_FEB2026_PRIMARY", "anthropic", "Detecting and Preventing Distillation Attacks", "Anthropic", "Web Disclosure", "primary organizational report", feb_url, path, sha, "2026-02-23", "reported_attribution")

    # 2. September 2026 Threat Intelligence Report
    sep_url = "https://www.anthropic.com/threat-intelligence-report-september-2026"
    sep_target = ant_dir / "threat_intelligence_report_september_2026.html"
    path, sha = download_file(sep_url, sep_target, "Anthropic Threat Intelligence Report September 2026", "Anthropic", "primary organizational report", "anthropic", pub_date="2026-09")
    if path:
        log_source("ANTHROPIC_SEP2026_REPORT", "anthropic", "Threat Intelligence Report September 2026", "Anthropic", "Web Landing / Report", "primary organizational report", sep_url, path, sha, "2026-09", "reported_attribution")

def download_longevity():
    print("\n=== 4. Downloading Longevity Biotechnology Data ===")
    lon_dir = DATA_RAW / "longevity"
    lon_dir.mkdir(parents=True, exist_ok=True)
    
    # CALERIE publications
    calerie_urls = [
        ("https://pubmed.ncbi.nlm.nih.gov/39418098/", lon_dir / "pubmed_39418098.html", "CALERIE Trial Primary Report (PMID: 39418098)", "peer-reviewed research"),
        ("https://pmc.ncbi.nlm.nih.gov/articles/PMC11552646/", lon_dir / "pmc_11552646.html", "CALERIE Trial Epigenetic and Biological Aging (PMC11552646)", "peer-reviewed research"),
        ("https://pmc.ncbi.nlm.nih.gov/articles/PMC11956694/", lon_dir / "pmc_11956694.html", "CALERIE Trial Long-term Outcomes (PMC11956694)", "peer-reviewed research")
    ]
    for url, target, title, tier in calerie_urls:
        path, sha = download_file(url, target, title, "National Center for Biotechnology Information (NCBI)", tier, "longevity")
        if path:
            log_source(f"NCBI_{target.stem}", "longevity", title, "NCBI / PMC", "Peer-Reviewed Article HTML", tier, url, path, sha, "published", "observed")

def download_cybersecurity():
    print("\n=== 5. Ingesting Cybersecurity Vulnerability & Policy Data ===")
    sec_dir = DATA_RAW / "cybersecurity"
    sec_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. CISA KEV JSON
    kev_url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    kev_target = sec_dir / "known_exploited_vulnerabilities.json"
    path, sha = download_file(kev_url, kev_target, "CISA Known Exploited Vulnerabilities Catalog", "Cybersecurity and Infrastructure Security Agency (CISA)", "primary official data", "cybersecurity")
    if path:
        log_source("CISA_KEV_CATALOG", "cybersecurity", "CISA Known Exploited Vulnerabilities Catalog", "CISA", "JSON Catalog", "primary official data", kev_url, path, sha, "live", "observed")

    # 2. Link or ingest existing comprehensive CNA 28-year Census data
    census_source = Path(r"C:\Users\nswcl\.gemini\antigravity-ide\scratch\cna-vulnerability-census-replication\data\processed")
    if census_source.exists():
        for f in census_source.glob("*.csv"):
            dest = sec_dir / f.name
            with open(f, "rb") as s, open(dest, "wb") as d:
                d.write(s.read())
            sha = compute_sha256(dest)
            print(f"[CYBER CENSUS] Linked {f.name} -> {dest} (SHA: {sha[:8]}...)")
            log_source(f"CNA_CENSUS_{f.stem}", "cybersecurity", f"Audited CNA Vulnerability Census ({f.name})", "CNA Census Project", "Audited Census CSV", "repository data", str(f), dest, sha, "28-year-census", "observed")
            log_checksum(dest, "cybersecurity", "observed")

def main():
    print("=" * 60)
    print("Starting Automated Download Pipeline (00_download_all.py)")
    print(f"Project Root: {PROJECT_ROOT}")
    print("=" * 60)
    
    download_housing()
    download_ai_metr()
    download_anthropic()
    download_longevity()
    download_cybersecurity()
    
    print("\n[COMPLETE] All download tasks finished.")

if __name__ == "__main__":
    main()
