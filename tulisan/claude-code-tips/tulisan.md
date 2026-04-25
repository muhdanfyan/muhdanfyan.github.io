# Meningkatkan Produktivitas dengan Claude Code: Tips & Workflow Lanjutan

Baru-baru ini, Boris Cherny (pencipta Claude Code) berbagi berbagai tips yang secara signifikan meningkatkan pengalaman menggunakan tool AI CLI ini. Artikel ini merangkum pemahaman tersebut dan bagaimana Anda bisa menerapkannya dalam workflow harian Anda.

### Apa itu Claude Code?
Claude Code adalah tool CLI dari Anthropic yang memungkinkan Claude berinteraksi langsung dengan sistem file Anda, menjalankan perintah terminal, dan membantu proses coding secara otonom.

---

### Repository Terkait
Saya telah membuat rangkuman teknis dan contoh konfigurasinya di sini:
[github.com/muhdanfyan/claude-code-tips](https://github.com/muhdanfyan/claude-code-tips)

---

### Tips & Perintah Utama

1.  **/btw (By The Way):** Gunakan ini untuk bertanya hal di luar tugas utama tanpa merusak alur kerja Claude yang sedang berjalan.
2.  **/loop:** Sangat berguna untuk otomatisasi. Misalnya, memantau error log setiap beberapa menit.
3.  **/schedule:** Membuat tugas persisten yang berjalan bahkan setelah terminal ditutup (Cloud Tasks).
4.  **/teleport:** Memindahkan sesi aktif antar perangkat dengan mudah.

### Cara Menggunakan Repository Tips
Dalam repository `claude-code-tips`, saya menyediakan beberapa aset penting:

```bash
# Clone repo tips
git clone https://github.com/muhdanfyan/claude-code-tips.git

# Lihat panduan konfigurasi
cat examples/settings.json
```

Gunakan flag `--add-dir` saat menjalankan Claude untuk memberikan akses ke banyak folder sekaligus, yang sangat membantu jika proyek Anda memiliki ketergantungan antar direktori.

### Visual Verification
Salah satu fitur paling keren adalah ekstensi Chrome (beta) yang memberikan "mata" pada Claude. Claude dapat membangun web app, membukanya di browser, mendeteksi error console, dan memperbaikinya sendiri secara visual.

---
*Ditulis menggunakan Gemini CLI pada April 2026.*
