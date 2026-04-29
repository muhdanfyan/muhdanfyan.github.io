---
name: muhdanfyan-standard
description: Standarisasi Alur Kerja Agen AI untuk Workspace Muhdan Fyan. Mengatur publikasi konten premium, rekayasa konteks, dan sinkronisasi infrastruktur.
---

# 🤖 Muhdan Fyan Agentic Mandates

Instruksi ini bersifat FOUNDATIONAL. Setiap agen Gemini CLI yang bekerja di workspace ini WAJIB mematuhi standar ini tanpa kompromi.

## ✍️ Content & Publication Standards (Premium UX)

### 1. Manual Publication Procedure (Critical)
Setiap publikasi tulisan baru di `muhdanfyan.github.io` wajib mengikuti langkah pasca-build:
- **Aset Sync:** Salin gambar dari `public/img/screenshots/` ke root `/img/screenshots/` dan `/dist/img/screenshots/`.
- **Sorting Logic:** Pastikan data tulisan diurutkan berdasarkan tanggal terbaru (`descending`) agar tulisan baru otomatis muncul di 4 slot utama halaman depan.
- **HTML Static Generation:** Setiap artikel wajib memiliki `index.html` manual di foldernya. Gunakan struktur "Premium Layout" (Support ID/EN, OG Tags, High-end CSS).
- **Homepage Sync:** Setelah build, wajib menyalin `dist/index.html` ke root `/index.html` dan `dist/tulisan/index.html` ke `/tulisan/index.html` untuk memperbarui daftar tulisan terbaru di halaman utama.
- **Force Sync:** Gunakan `git add -f` untuk folder `dist/` guna memastikan file statis terunggah meskipun di-ignore oleh git standar.

### 2. Article Formatting & Typography
- **Drop Cap:** Paragraf pertama artikel WAJIB menggunakan class `.dropcap` (Huruf pertama besar & artistik).
- **Proportional Sub-heads:** Elemen `h2` menggunakan font-size `1.5rem`, tebal (bold), dan memiliki batang aksen vertikal Indigo di sampingnya.
- **Foreign Terms:** Semua istilah asing (Inggris/teknis) WAJIB ditulis *miring (italic)*.
- **Deep Linking:** Setiap istilah teknis penting WAJIB memiliki tautan (hyperlink) ke dokumentasi resmi atau referensi otoritatif.
- **Technical Highlights:** Gunakan tag `<span class="highlight">` dengan font *JetBrains Mono* untuk istilah alat atau teknologi.
- **Footer Wajib:** Di akhir setiap artikel, sertakan: **Sumber:** [Link] | **Pengkaji:** Muhdan Fyan Syah Sofian.

### 3. SEO & Rich Preview (Rich Media)
- **Absolute URLs for Meta Tags:** Tag `og:image` dan `twitter:image` WAJIB menggunakan URL absolut lengkap (misal: `https://muhdanfyan.github.io/img/...`).
- **Relative Paths for Content:** Tag `<img>` di dalam konten artikel menggunakan path relatif (`/img/...`) untuk portabilitas.
- **Image Optimization:** Dimensi ideal 1200x630px. Pastikan ekstensi file (JPG/PNG) sinkron dengan kode (case-sensitive).

## 🧩 AI-Native Engineering Workflow

### 1. Context Engineering
- **Modular Skills:** Jangan membuat satu file instruksi raksasa. Pecah menjadi skill kecil.
- **Progressive Disclosure:** Muat detail instruksi hanya saat agen memutuskan membutuhkannya untuk menghemat token.
- **Recursive Skill Building:** Kodifikasi alur kerja sukses menjadi file `.md` baru di folder `.gemini/skills/`.

### 2. Quality Gatekeeping
- **Unit Test-First:** Agen wajib menulis tes sebelum menulis fitur utama.
- **Architecture Review:** Manusia (Muhdan Fyan) bertindak sebagai orkestrator yang meninjau 30% keputusan kritis, sementara agen mengeksekusi 70% beban teknis.

---
*Standard established April 2026. This is the single source of truth for all AI-Native activities in this workspace.*
