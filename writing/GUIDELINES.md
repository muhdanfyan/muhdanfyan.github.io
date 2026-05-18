# 📘 Panduan Standar Penulisan Artikel (Standard Operating Procedure)

Dokumen ini adalah acuan resmi untuk setiap artikel yang dipublikasikan di `muhdanfyan.github.io`.

## 1. Persiapan File
Setiap artikel baru harus memiliki struktur:
- `tulisan/[slug]/tulisan.md` (Konten utama untuk sistem SPA)
- `tulisan/[slug]/index.html` (File statis khusus untuk SEO & Link Preview)

## 2. Aturan Bahasa & Formatting
- **Italicize Foreign Terms:** Semua kata bahasa asing (Inggris/Arab/dll) wajib *miring*. Contoh: *Agent*, *terminal*, *database*.
- **Bold Important Points:** Gunakan **tebal** untuk penekanan argumen atau poin utama.
- **Visuals:** Gunakan gambar berkualitas tinggi dari sumber valid (Unsplash/Official Docs). Gambar pertama harus mewakili isi konten (Hero Image).

## 3. SEO Checklist
- Update `manifest.json` di folder `data/` agar tulisan muncul di beranda.
- Pastikan Meta Tag `og:image` di `index.html` merujuk pada gambar pertama artikel.
- Gunakan deskripsi meta antara 120-160 karakter.

## 4. Struktur Template Markdown
```markdown
# [Judul yang Menarik] 🚀

![Hero Image Description](URL_Gambar_Utama)

[Paragraf pembuka yang menghubungkan pembaca dengan masalah]

---

### [Sub Judul 1 - Fokus ke Indonesia/Pengalaman Pribadi]
[Isi pembahasan...]

### [Sub Judul 2 - Tips Teknis/Pro]
> [Gunakan blockquote untuk kutipan atau filosofi penting]

![Additional Visual](URL_Gambar_Pendukung)

[Isi pembahasan...]

---

### 🛠️ Referensi / Link GitHub
[Berikan box atau link yang jelas ke project terkait]

---
*Ditulis menggunakan Gemini CLI - [Bulan] [Tahun]*
```
