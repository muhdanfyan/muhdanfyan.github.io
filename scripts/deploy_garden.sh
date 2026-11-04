#!/usr/bin/env bash
# deploy_garden.sh — Pull, build, dan deploy Digital Garden
set -e

REPO_DIR="/home/pondokinformatika/muhdanfyan.github.io"
LOG_FILE="$REPO_DIR/.git/garden-deploy.log"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 🌱 Memulai deploy Digital Garden..." >> "$LOG_FILE"

cd "$REPO_DIR"

# Pull perubahan terbaru dari GitHub tanpa membuat merge commit otomatis
git pull --ff-only origin main 2>&1 >> "$LOG_FILE"
echo "  ✅ Pull selesai" >> "$LOG_FILE"

# Build garden (convert .md → .html)
python3 scripts/build_garden.py 2>&1 >> "$LOG_FILE"
echo "  ✅ Build selesai" >> "$LOG_FILE"

# Hasil build berada di dist/ dan memang tidak dilacak Git.
# Deployment produksi dijalankan GitHub Actions setiap kali source di-push.
# Jangan commit log atau hasil runtime dari cron ke branch main.
echo "  ✅ Build lokal selesai; tidak ada commit runtime ke main" >> "$LOG_FILE"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ Selesai!" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
