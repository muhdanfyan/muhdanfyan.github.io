#!/bin/bash
echo "🚀 Memulai proses publikasi otomatis..."

# 1. Build Proyek
npm run build

if [ $? -eq 0 ]; then
    echo "✅ Build berhasil. Memulai sinkronisasi..."
    
    # 2. Bersihkan aset lama di root agar tidak terjadi penumpukan/konflik
    rm -rf _astro
    
    # 3. Sinkronisasi dari folder dist ke root
    cp -r dist/_astro .
    cp dist/index.html .
    cp dist/404.html .
    
    # Sinkronisasi folder portofolio, tulisan, dan gambar
    cp -r dist/portofolio/* portofolio/ 2>/dev/null || :
    cp -r dist/tulisan/* tulisan/ 2>/dev/null || :
    cp -r dist/img/* img/ 2>/dev/null || :
    
    echo "📂 Sinkronisasi selesai."
    
    # 4. Git Automations
    git add .
    git add -f dist/
    git commit -m "site: automated production build and asset sync"
    git push origin main
    
    echo "🎉 Website berhasil diperbarui dan dipublish!"
else
    echo "❌ Build gagal. Silakan cek error di atas."
    exit 1
fi
