# 🗺️ Skema Implementasi CMS & Alur Kerja AI Terpadu

Rencana ini bertujuan untuk memusatkan seluruh konten dinamis website ke dalam sistem berbasis Markdown yang dikelola oleh Keystatic CMS, sehingga agen AI dapat melakukan pembaruan secara otonom.

## 🏗️ Fase 1: Migrasi Arsitektur Konten (Unifikasi Markdown)

Saat ini, data website tersebar di beberapa format. Kita akan menyatukannya ke dalam folder `content/`.

| Bagian | Status Saat Ini | Target Implementasi |
| :--- | :--- | :--- |
| **Tulisan (Blog)** | Markdown (`tulisan/`) | Tetap (Sudah optimal) |
| **Portofolio** | JSON (`manifest.json`) | Koleksi Markdown (`content/portfolio/*.mdoc`) |
| **Pekerjaan** | Hardcoded (`index.astro`) | Koleksi Markdown (`content/experience/*.mdoc`) |
| **Pendidikan** | Hardcoded (`index.astro`) | Koleksi Markdown (`content/education/*.mdoc`) |
| **Pengalaman Mengajar** | Belum Ada | Koleksi Markdown (`content/teaching/*.mdoc`) |

### Langkah Teknis:
1. **Pembaruan `keystatic.config.ts`**: Menambahkan koleksi untuk `experience`, `education`, `teaching`, dan `portfolio`.
2. **Refactoring `index.astro`**: Mengganti teks hardcoded dengan fungsi `fs.readdirSync` yang membaca folder `content/` (serupa dengan logika pada bagian tulisan).

## 🤖 Fase 2: Peningkatan Agen Writing Workflow (One-Command Publish)

Kita akan menyempurnakan `AGENT_WRITING_WORKFLOW.md` agar lebih otonom. Agen AI tidak perlu menunggu konfirmasi di setiap tahap.

### Skematik Alur Kerja Baru:
1. **Research & Drafting**: Agen melakukan riset, menulis draft ID (dengan Dropcap & Highlights) dan menerjemahkan ke EN.
2. **Visual Asset Generation**: Agen membuat gambar sampul premium (1200x630px) dan menyimpannya ke `public/img/tulisan/`.
3. **File Creation**: Agen membuat folder slug dan file `.mdoc` (ID/EN) dengan metadata lengkap.
4. **Validation**: Agen mengecek validitas YAML, link, dan konsistensi styling.
5. **Sanity Build**: Agen menjalankan `npm run build` lokal untuk memastikan tidak ada error.
6. **Auto-Publish**: Agen menjalankan `npm run publish` untuk sinkronisasi ke root dan push ke GitHub.

## 🚀 Fase 3: Deployment & Sinkronisasi Global

Memastikan sistem CI/CD (`publish.sh`) menangani semua jenis konten baru.

1. **Automation Script**: Memperbarui `publish.sh` agar secara otomatis melakukan sinkronisasi untuk folder `content/` yang baru.
2. **Safety Gate**: Menambahkan tahap `npm test` dalam alur kerja agen sebelum melakukan `git push` untuk mencegah error produksi.

---
*Plan created May 2026 for Muhdan Fyan Portfolio.*
