# Panduan Penggunaan Image to RGB Matrix Converter

## Cara Menjalankan Program

1. **Buka Terminal/Command Prompt**
2. **Navigasi ke folder project**:
   ```bash
   cd "D:\Tugas\Pengolahan Citra\ImageToBit"
   ```

3. **Jalankan program**:
   ```bash
   python main.py
   ```
   atau jika menggunakan virtual environment:
   ```bash
   venv\Scripts\python.exe main.py
   ```

## Fitur-Fitur Program

### 1. 📁 Upload Image
**Cara Menggunakan:**
- Klik tombol "📁 Upload Image" di bagian atas panel kiri
- Pilih file gambar (support: PNG, JPG, JPEG, BMP, GIF, TIFF)
- Gambar akan langsung ditampilkan dan dianalisis

**Informasi yang Ditampilkan:**
- Ukuran gambar (width x height pixels)
- Preview gambar dengan scrollbar

### 2. 🖱️ Hover untuk Melihat RGB
**Cara Menggunakan:**
- Setelah upload gambar, gerakkan mouse di atas gambar
- Informasi akan muncul secara real-time di bawah gambar

**Informasi yang Ditampilkan:**
```
Position: (x, y) | RGB: (r, g, b) | Hex: #RRGGBB
```
- **Position**: Koordinat pixel (x horizontal, y vertikal)
- **RGB**: Nilai merah, hijau, biru (0-255)
- **Hex**: Format warna hexadecimal

### 3. 🔍 Search Coordinate
**Cara Menggunakan:**
1. Masukkan nilai **X** (koordinat horizontal)
2. Masukkan nilai **Y** (koordinat vertikal)
3. Klik tombol "🔍 Search"

**Hasil:**
- Nilai RGB untuk koordinat tersebut
- Koordinat akan di-highlight kuning di tabel (jika ada)
- Tabel akan scroll otomatis ke koordinat tersebut

**Contoh:**
- X: 100
- Y: 50
- Hasil: RGB(255, 128, 64) | Hex: #FF8040

### 4. 📊 RGB Matrix Table
**Kolom-kolom:**
- **X**: Koordinat horizontal (0 hingga width-1)
- **Y**: Koordinat vertikal (0 hingga height-1)
- **R**: Red value (0-255)
- **G**: Green value (0-255)
- **B**: Blue value (0-255)
- **RGB Hex**: Format hexadecimal (#RRGGBB)

**Catatan:**
- Untuk gambar besar, tabel menampilkan sample data untuk performa optimal
- Gunakan fitur search untuk mencari koordinat spesifik
- Scroll vertikal dan horizontal tersedia

### 5. 💾 Export Data

#### Export to CSV
**Cara Menggunakan:**
1. Klik tombol "💾 Export to CSV"
2. Pilih lokasi penyimpanan
3. Beri nama file (otomatis .csv)
4. Klik Save

**Format File CSV:**
```csv
X,Y,R,G,B,RGB_Hex
0,0,255,128,64,#FF8040
1,0,200,100,50,#C86432
...
```

#### Export to Excel
**Cara Menggunakan:**
1. Klik tombol "📊 Export to Excel"
2. Pilih lokasi penyimpanan
3. Beri nama file (otomatis .xlsx)
4. Klik Save

**Format File Excel:**
- Sheet dengan kolom: X, Y, R, G, B, RGB_Hex
- Data terformat rapi dalam cells
- Mudah untuk analisis lebih lanjut

## Tips & Trik

### 1. Mencari Warna Spesifik
- Upload gambar
- Hover di area yang ingin dicek warnanya
- Catat koordinat (x, y) yang ditampilkan
- Gunakan search untuk konfirmasi

### 2. Analisis Gambar Besar
- Gunakan search untuk koordinat spesifik
- Export ke Excel untuk analisis lengkap
- Gunakan filter di Excel untuk menemukan nilai RGB tertentu

### 3. Membandingkan Warna
- Search beberapa koordinat berbeda
- Bandingkan nilai RGB-nya
- Export data untuk visualisasi di tools lain

### 4. Koordinat Image
```
(0,0)────────────────────► X
  │
  │        Gambar
  │
  │
  ▼
  Y
```
- X: kiri ke kanan (horizontal)
- Y: atas ke bawah (vertikal)
- Origin (0,0) ada di kiri atas

## Contoh Penggunaan

### Contoh 1: Menganalisis Logo
1. Upload logo perusahaan
2. Hover di bagian logo untuk cek warna brand
3. Catat nilai RGB atau Hex
4. Gunakan untuk konsistensi brand di desain lain

### Contoh 2: Ekstrak Palet Warna
1. Upload gambar yang menarik
2. Search berbagai koordinat untuk sample warna
3. Kumpulkan nilai Hex dari warna-warna menarik
4. Gunakan untuk inspirasi desain

### Contoh 3: Verifikasi Gradient
1. Upload gambar dengan gradient
2. Search koordinat di berbagai titik gradient
3. Verifikasi transisi warna smooth atau tidak
4. Export data untuk analisis matematis

## Troubleshooting

### Gambar Tidak Muncul
- Pastikan format file didukung
- Coba convert gambar ke PNG atau JPG dulu
- Check ukuran file tidak terlalu besar

### Hover Tidak Responsif
- Pastikan mouse berada di area gambar
- Untuk gambar besar, mungkin ada sedikit delay
- Refresh dengan upload ulang jika perlu

### Search Tidak Menemukan
- Pastikan koordinat dalam range gambar
- X harus: 0 sampai (width - 1)
- Y harus: 0 sampai (height - 1)
- Check apakah sudah upload gambar

### Export Gagal
- Pastikan punya permission write di folder tujuan
- Pastikan nama file valid
- Close file Excel jika sudah terbuka
- Check disk space cukup

## Keyboard Shortcuts

- **Tab**: Pindah antara input X dan Y
- **Enter**: (di search box) Execute search
- **Scroll Wheel**: Scroll canvas/table

## Batasan Program

- **Ukuran Gambar**: Semua ukuran didukung, tapi gambar besar akan di-sample di tabel
- **Format**: RGB images (otomatis convert dari format lain)
- **Memory**: Tergantung RAM, gambar sangat besar mungkin lambat

## Support

Untuk pertanyaan atau bug report:
- Check README.md untuk info teknis
- Lihat kode di main.py untuk detail implementasi

---
**Selamat menggunakan Image to RGB Matrix Converter!** 🎨
