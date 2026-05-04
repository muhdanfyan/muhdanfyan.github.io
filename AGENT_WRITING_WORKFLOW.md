# 🚀 End-to-End Writing Workflow for AI Agents

Dokumen ini adalah instruksi operasional untuk Agen AI agar dapat mengeksekusi publikasi tulisan dari nol hingga terbit secara otonom.

## 📋 Tahapan Eksekusi

### 1. Perencanaan & Riset (Phase: Content Generation)
- **Topik**: Terima topik dari user atau tentukan berdasarkan tren.
- **Riset**: Lakukan pencarian mendalam mengenai topik tersebut.
- **Drafting (ID)**: Tulis dalam Bahasa Indonesia. 
  - Wajib menggunakan `<p class="dropcap">` di paragraf pertama.
  - Gunakan `<i>` untuk istilah asing/teknis.
  - Gunakan `<span class="highlight">` untuk nama alat/teknologi.
- **Translation (EN)**: Terjemahkan ke Bahasa Inggris dengan gaya bahasa yang profesional namun mengalir.

### 2. Produksi Aset Visual (Phase: Visual Assets)
- **Prompting**: Buat prompt gambar yang merepresentasikan isi tulisan (gaya: premium, clean, professional).
- **Generation**: Gunakan tool `generate_image`.
- **Saving**: Simpan ke `public/img/tulisan/<slug>-cover.png`.

### 3. Implementasi File (Phase: File System)
- **Slug**: Buat slug URL yang SEO-friendly (semua huruf kecil, pisahkan dengan tanda hubung).
- **Directory**: Buat folder di `tulisan/<slug>/`.
- **Metadata (Frontmatter)**:
  ```yaml
  slug: "sesuai-nama-folder"
  title_id: "Judul Indonesia"
  title_en: "English Title"
  date: "YYYY-MM-DD" (Hari ini)
  category: "Pilih dari kategori yang ada di keystatic.config.ts"
  description_id: "Ringkasan pendek ID"
  description_en: "Short summary EN"
  image: "<slug>-cover.png"
  ```
- **Files**: Buat `index.mdoc` (versi ID) dan `index.en.mdoc` (versi EN).

### 4. Validasi & Perbaikan Logika (Phase: Technical Check)
- **Language Detection**: Pastikan `available_langs` di halaman daftar tulisan mengenali kedua file tersebut.
- **Sorting Check**: Pastikan tanggal diatur agar tulisan muncul paling atas.
- **Test**: Jalankan `npm test -- --run` untuk memastikan tidak ada logika yang rusak.

### 5. Publikasi (Phase: Deployment)
- **Publish Script**: Jalankan `npm run publish`.
- **Commit Message**: Gunakan format `feat: add article about <topic> with automated workflow`.

## 🛠️ Perintah Utama untuk User
Cukup katakan:
> "Tolong buatkan tulisan tentang [Topik] dengan alur kerja otomatis (AGENT_WRITING_WORKFLOW.md)"

---
*Last updated: May 2026*
