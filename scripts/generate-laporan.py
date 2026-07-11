#!/usr/bin/env python3
"""
generate-laporan.py — Generate laporan harian dari cron output untuk Digital Garden.
Baca output cron terbaru, simpan markdown ke content/laporan/, lalu deploy.

Usage: python3 scripts/generate-laporan.py
"""
import os
import re
import glob
from datetime import datetime, date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
CRON_OUTPUT_DIR = Path(os.path.expanduser("~/.hermes/cron/output"))

JOBS = {
    "d6f447d622d6": "Daily Standup — ringkas",
    "b1692c3fb86f": "Ekosistem SKOM — Laporan Harian",
    # Tambah job lain nanti
}

def get_latest_cron(job_id):
    """Get latest cron output file for a job."""
    job_dir = CRON_OUTPUT_DIR / job_id
    if not job_dir.exists():
        return None
    files = sorted(job_dir.glob("*.md"), reverse=True)
    return files[0] if files else None

def extract_response_section(content):
    """Extract the response section from cron markdown output."""
    # Cari ## Response atau setelah prompt
    parts = content.split("## Response", 1)
    if len(parts) > 1:
        return parts[1].strip()
    # Fallback: after --- separator
    parts = content.split("\n---\n", 2)
    if len(parts) > 2:
        return parts[2].strip()
    return content

def generate_laporan():
    """Generate today's laporan from cron outputs."""
    today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    output_path = CONTENT_DIR / "laporan" / f"{today_str}.md"
    
    if output_path.exists():
        print(f"  ℹ️  Laporan {today_str} sudah ada, skip.")
        return False
    
    sections = []
    
    for job_id, job_name in JOBS.items():
        f = get_latest_cron(job_id)
        if not f:
            continue
        
        content = f.read_text(encoding="utf-8")
        response = extract_response_section(content)
        
        # Ambil baris meaningful (bukan prompt/skill/caveman)
        lines = []
        in_response = False
        for line in response.split("\n"):
            if line.startswith("## LAPORAN") or line.startswith("LAPORAN"):
                in_response = True
            if in_response:
                lines.append(line)
        
        if lines:
            sections.append(f"\n## Dari: {job_name}\n\n" + "\n".join(lines[:50]))
    
    if not sections:
        print("  ℹ️  Tidak ada cron output untuk dibuat laporan.")
        return False
    
    # Build frontmatter + konten
    month_names = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
    month_name = month_names[today.month - 1]
    date_formatted = f"{today.day} {month_name} {today.year}"
    
    content = f"""---
title: "Laporan Harian — {today_str}"
date: {today_str}
tags: [laporan, harian, otomatis]
status: published
---

# Laporan Harian: {date_formatted}

Laporan otomatis dari cron job Aiman.

{''.join(sections)}

---

_Laporan digenerate otomatis oleh Aiman pada {datetime.now().strftime('%H:%M WITA')}._
"""
    
    output_path.write_text(content, encoding="utf-8")
    print(f"  ✅ Laporan {today_str} dibuat: {output_path}")
    return True

if __name__ == "__main__":
    generate_laporan()
