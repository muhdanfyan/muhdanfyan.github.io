#!/bin/bash
# Deploy digital garden ke branch gh-pages
# Pakai file dari dist/ (hasil build garden + Astro)

set -e

echo "=== BUILD GARDEN ==="
python3 scripts/build_garden.py

echo ""
echo "=== PUSH KE gh-pages ==="
cd "$(dirname "$0")/.."

# Simpan index utama buat landing page
# Semua file di dist/ — Astro build + garden build — langsung deploy ke gh-pages
cd dist

# Init git di folder dist
git init
git remote add origin https://github.com/muhdanfyan/muhdanfyan.github.io.git
git checkout -b gh-pages

# Tambah semua file
git add -A
git commit -m "deploy garden: $(date '+%Y-%m-%d %H:%M WITA')"

# Push force — gh-pages cuma buat deployment
git push origin gh-pages --force

cd ..
rm -rf dist/.git

echo ""
echo "=== DONE ==="
echo "URL: https://muhdanfyan.github.io/catatan/"
