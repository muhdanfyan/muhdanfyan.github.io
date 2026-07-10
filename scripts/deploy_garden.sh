#!/usr/bin/env bash
# deploy_garden.sh — Pull, build, dan deploy Digital Garden
set -e

REPO_DIR="/home/pondokinformatika/muhdanfyan.github.io"
LOG_FILE="/home/pondokinformatika/muhdanfyan.github.io/garden-deploy.log"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 🌱 Memulai deploy Digital Garden..." >> "$LOG_FILE"

cd "$REPO_DIR"

# Pull perubahan terbaru dari GitHub
git pull origin main 2>&1 >> "$LOG_FILE"
echo "  ✅ Pull selesai" >> "$LOG_FILE"

# Build garden (convert .md → .html)
python3 scripts/build_garden.py 2>&1 >> "$LOG_FILE"
echo "  ✅ Build selesai" >> "$LOG_FILE"

# Commit & push hasil build ke GitHub Pages
git add -A 2>&1 >> "$LOG_FILE"
git commit -m "gardener: auto-build $(date '+%Y-%m-%d %H:%M')" 2>&1 >> "$LOG_FILE" || echo "  ℹ️  Tidak ada perubahan" >> "$LOG_FILE"
git push origin main 2>&1 >> "$LOG_FILE"
echo "  ✅ Push ke GitHub Pages selesai" >> "$LOG_FILE"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ Selesai!" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
