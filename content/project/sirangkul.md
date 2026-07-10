---
title: "SiRangkul — Sistem Rencana Anggaran Kelola Usulan"
date: 2026-07-10
tags: [sirangkul, dokumentasi, man2-makassar]
status: published
---

# SiRangkul

**SiRangkul** (Sistem Rencana Anggaran Kelola Usulan) adalah aplikasi manajemen pengajuan anggaran berbasis web untuk MAN 2 Kota Makassar.

## Stack Teknis

- **Backend**: Laravel 11 (PHP 8.3)
- **Frontend**: React + Vite (SPA)
- **Database**: MySQL 8
- **Server**: Nginx, VPS 89.233.105.92
- **Domain**: sirangkul.man2kotamakassar.sch.id

## Alur Persetujuan

1. **Pengusul** → Membuat & mengajukan proposal (status: `draft` → `submitted`)
2. **Verifikator** → Memeriksa kelengkapan (status: `submitted` → `verified`)
3. **Komite Madrasah** → Menyetujui secara komite (status: `verified` → `approved`)
4. **Kepala Madrasah** → Persetujuan akhir (status: `approved` → `final_approved`)
5. **Bendahara** → Pemrosesan pembayaran (status: `final_approved` → `payment_processing` → `completed`)

## Struktur Database

Tabel utama:
- `users` — User dengan role UUID
- `proposals` — Data pengajuan dengan status workflow
- `rkam` — Rencana Kegiatan dan Anggaran Madrasah
- `audit_logs` — Catatan semua aktivitas
- `payments` — Data pembayaran

## Catatan Penting

- Ada issue bypass approval: proposal langsung `draft → final_approved` tanpa mengisi kolom `approved_by` dan `final_approved_by`
- Role `administrator` ada 3 user — perlu dibersihkan agar hanya 1
