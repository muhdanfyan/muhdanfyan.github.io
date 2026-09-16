#!/usr/bin/env bash
# sync_dist_assets.sh — Sinkronkan aset yang di-track git ke dist/ setelah build.
#
# Kenapa perlu: dist/ ada di .gitignore, jadi di CI `astro build` membuat dist/
# dari nol. Tapi banyak aset situs (index.html, img/, portofolio/, tulisan/,
# mengajar/) di-track di root repo — bukan hasil Astro. Script ini menyalinnya
# balik ke dist/ supaya deploy lengkap.
#
# Prinsip: file di ROOT repo = sumber kebenaran untuk halaman statis.
#          Jangan biarkan `astro build` menimpa index.html root yang lebih baru.

set -euo pipefail

cd "$(dirname "$0")/.."
BASE="$(pwd)"

echo "=== Sync aset statis ke dist/ ==="

# 1. index.html root SELALU menang (punya card teaching terbaru).
#    Astro build menghasilkan index minimal tanpa konten teaching.
if [ -f index.html ]; then
  cp index.html dist/index.html
  echo "  ✓ index.html (dari root, $(stat -c%s index.html) bytes)"
fi

# 2. Folder & file statis yang di-track git → salin ke dist/
#    PENTING: `mengajar` TIDAK termasuk di sini — folder itu di-generate
#    oleh build_teaching.py. Kalau ikut disalin, versi lama dari git akan
#    MENIMPA halaman baru hasil generator (bug: halaman baru 404).
for item in img catatan portofolio project tulisan writing laporan \
            manifest.json robots.txt sw.js favicon.svg silent.mp3 \
            sitemap-index.xml garden-sitemap.xml; do
  if [ -e "$item" ]; then
    if [ -d "$item" ]; then
      mkdir -p "dist/$item"
      cp -r "$item"/. "dist/$item"/ 2>/dev/null || true
    else
      cp "$item" "dist/$item" 2>/dev/null || true
    fi
    echo "  ✓ $item"
  fi
done

# 3. public/ → dist/ (aset Astro standar), tanpa menimpa yang sudah ada
if [ -d public ]; then
  cp -rn public/. dist/ 2>/dev/null || true
  echo "  ✓ public/ → dist/"
fi

# 4. Sitemap gabungan: pastikan URL mengajar & writing terdaftar
if [ -f dist/sitemap-0.xml ]; then
  echo "  ✓ sitemap-0.xml ($(grep -c '<loc>' dist/sitemap-0.xml) URL)"
fi

touch dist/.nojekyll

echo ""
echo "=== Isi dist/ ==="
ls dist/ | head -30
echo ""
echo "=== Halaman mengajar ==="
ls dist/mengajar/ 2>/dev/null | head -20 || echo "  (kosong)"
