# 📖 Standar Penulisan & Media (Pedoman Agen AI)

Dokumen ini adalah acuan resmi untuk setiap penulisan artikel dan pengelolaan media di website `muhdanfyan.github.io`. Setiap agen AI yang bekerja di repositori ini **WAJIB** mengikuti standar ini.

---

## 1. Standar Konten (Editorial)
*   **Tone & Gaya Bahasa**: Menggunakan bahasa Indonesia yang tajam, kritis, namun tetap elegan (Premium). Hindari tone yang terlalu suram; gunakan pendekatan solutif dan optimis.
*   **Riset Berbasis Data**: Setiap artikel isu sosial/teknis (seperti Engineering Risk) wajib merujuk pada sumber video YouTube yang relevan (misal: Ferry Irwandi, Eko Kurniawan Khannedy, dsb) untuk mendapatkan data primer dan kutipan langsung.
*   **Struktur Artikel**:
    1.  **Hero Image**: Gambar pembuka yang cerah dan positif.
    2.  **Hook**: Kalimat pembuka yang menggugah eksistensi pembaca.
    3.  **Insight**: Analisis mendalam berbasis poin-poin.
    4.  **Referensi**: Daftar link YouTube/sumber asli di bagian akhir.

---

## 2. Standar Teknis SEO & Social Media
*   **Image Link Preview (OG Image)**: 
    *   Sistem Astro sudah dikonfigurasi untuk mengambil gambar pertama di Markdown sebagai pratinjau secara otomatis.
    *   **PENTING**: Pastikan URL gambar di metadata menggunakan link absolut (dimulai dengan `https://muhdanfyan.github.io/`).
    *   Jangan lupa tanda `/` setelah domain.
*   **Canonical Tags**: Setiap halaman wajib memiliki tag canonical yang mengarah ke URL aslinya di GitHub Pages untuk menghindari duplikasi konten di mata Google.
*   **Sitemap**: Jalankan `npm run build` setiap kali ada tulisan baru untuk memperbarui `sitemap-index.xml`.

---

## 3. Alur Kerja Deployment (Penting!)
Untuk menghindari masalah "konten kembali ke versi lama" (Reversion Bug):
1.  **Hapus File Penghalang**: Selalu jalankan `find tulisan -name "index.html" -delete` sebelum membangun ulang.
2.  **Surgical Copy**: Jangan gunakan `cp -r dist/tulisan .` secara sembarangan karena dapat menimpa file sumber `.md`.
3.  **Commit Manual**: Selalu commit file `.md` sumber **sebelum** melakukan proses build hasil produksi.

---

## 4. Estetika Visual
*   Gunakan ilustrasi yang dihasilkan AI dengan tone cerah, wajah tersenyum, dan atmosfer yang profesional namun ramah.
*   Resolusi standar untuk Link Preview adalah **1200x630 piksel**.

---
*Ditetapkan pada: April 2026*  
*Oleh: Muhdan Fyan & Antigravity (AI Assistant)*
