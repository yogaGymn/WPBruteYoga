
## 🔐 WordPress Brute Force & Auth Bypass Tool

> WPBruteYoga adalah tools berbasis CLI untuk melakukan brute force login WordPress secara otomatis, dilengkapi dengan deteksi akses dashboard, user-agent acak, dan retry koneksi.

---

### 🎯 Fitur
- Brute force form login WordPress (`wp-login.php`)
- Deteksi login berhasil berdasarkan redirect dan konten dashboard
- Retry otomatis jika koneksi gagal
- Random `User-Agent` untuk mimikri
- Dukungan URL login & dashboard kustom


---

### 🚀 Cara Penggunaan

```bash
python BruteForce.py -u https://targetdomain.com/wp-login.php

### Opsi tambahan (jika dashboard URL berbeda)
python BruteForce.py -u https://targetdomain.com/wp-login.php -d https://targetdomain.com/wp-admin/

###
Tools ini dibuat oleh Prayoga Gymnastiar (@YogaGymn) dari Cilacap hanya untuk tujuan edukasi dan pentesting legal.
Penggunaan terhadap sistem tanpa izin adalah pelanggaran hukum. Developer tidak bertanggung jawab atas penyalahgunaan.
