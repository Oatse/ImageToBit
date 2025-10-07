# Image to Color Bit Converter - User Guide

## 📋 Deskripsi Aplikasi
Aplikasi desktop untuk mengkonversi gambar ke color bit dengan fitur hover detection dan export CSV.

## ✨ Fitur Utama

### 1. Upload Image (AUTO-READ ALL PIXELS!) 🚀 NEW!
- Support multiple format: PNG, JPG, JPEG, BMP, GIF, TIFF
- Auto display di canvas
- **OTOMATIS MEMBACA SEMUA PIXEL!**
- Progress indicator menampilkan kemajuan
- Warning untuk gambar besar (>1 juta pixel)
- Success notification setelah selesai
- Maintain aspect ratio

### 2. Hover Detection (Real-time)
- Hover mouse di atas gambar untuk melihat informasi warna
- Menampilkan:
  - Koordinat pixel (X, Y)
  - Nilai RGB (decimal)
  - Nilai Binary (8-bit per channel R, G, B)
  - Hex color code
- Color preview box menampilkan warna secara visual

### 3. Click to Save (Optional)
- Click pada pixel untuk menyimpan warna ke tabel
- Visual marker (lingkaran) muncul pada posisi yang di-click
- Marker menggunakan warna asli pixel
- Auto numbering di tabel
- **Note**: Fitur ini optional karena semua pixel sudah terbaca otomatis

### 4. Tabel Data
Kolom-kolom tabel:
- **No**: Nomor urut
- **X**: Koordinat X pixel
- **Y**: Koordinat Y pixel
- **Red (Dec)**: Nilai merah (0-255)
- **Green (Dec)**: Nilai hijau (0-255)
- **Blue (Dec)**: Nilai biru (0-255)
- **Red (Bin)**: Nilai merah dalam binary (8-bit)
- **Green (Bin)**: Nilai hijau dalam binary (8-bit)
- **Blue (Bin)**: Nilai biru dalam binary (8-bit)
- **Hex Color**: Kode warna hexadecimal

### 5. Export to CSV
- Export semua data tabel ke file CSV
- Format CSV dengan header yang jelas
- File dialog untuk pilih lokasi save
- Success notification setelah export

### 6. Clear Table
- Hapus semua data dari tabel
- Hapus semua marker dari gambar
- Konfirmasi dialog untuk mencegah kesalahan

### 7. Status Bar
- Menampilkan nama file dan ukuran gambar
- Update status operasi (save, export, clear)
- Menampilkan jumlah data yang tersimpan

## 🚀 Cara Menggunakan

### Langkah 1: Jalankan Aplikasi
```bash
# Aktivasi virtual environment
venv\Scripts\activate

# Jalankan aplikasi
python main.py
```

### Langkah 2: Upload Gambar
1. Click tombol "📁 Upload Image"
2. Pilih gambar dari file dialog
3. Gambar akan ditampilkan di canvas sebelah kiri

### Langkah 3: Explore Warna
1. **Hover** mouse di atas gambar
2. Lihat informasi warna real-time di label atas
3. Color preview box menampilkan warna secara visual

### Langkah 4: Save Warna
1. **Click** pada pixel yang ingin disimpan
2. Marker muncul di posisi click
3. Data otomatis tersimpan di tabel sebelah kanan

### Langkah 5: Export Data
1. Click tombol "💾 Export to CSV"
2. Pilih lokasi save file
3. File CSV berhasil disimpan

### Langkah 6: Clear Data (Optional)
1. Click tombol "🗑️ Clear Table"
2. Konfirmasi di dialog
3. Semua data dan marker terhapus

## 📊 Format CSV Output

File CSV yang dihasilkan memiliki format:
```csv
X,Y,Red_Dec,Green_Dec,Blue_Dec,Red_Bin,Green_Bin,Blue_Bin,Hex_Color
50,100,255,128,64,11111111,10000000,01000000,#FF8040
120,200,0,255,0,00000000,11111111,00000000,#00FF00
```

## 🎨 UI Layout

```
+--------------------------------------------------------+
| [Upload] [Export CSV] [Clear]  | Color Info | [Preview]|
+--------------------------------------------------------+
|                        |                                |
|    Image Canvas        |        Data Table             |
|    (with markers)      |    (scrollable)               |
|                        |                                |
+--------------------------------------------------------+
| Status Bar                                             |
+--------------------------------------------------------+
```

## 🔧 Fitur Teknis

### Image Processing
- Menggunakan **Pillow (PIL)** untuk image processing
- Support RGB, RGBA, dan Grayscale mode
- Efficient pixel access dengan `getpixel()`

### Data Management
- Menggunakan **pandas DataFrame** untuk data storage
- Easy export dengan `to_csv()`
- Efficient data manipulation

### GUI
- Menggunakan **tkinter** (built-in Python)
- ttk.Treeview untuk tabel yang powerful
- Canvas untuk image display dengan scrollbar
- Responsive layout dengan grid system

## 💡 Tips Penggunaan

1. **Zoom dengan Scrollbar**: Gunakan scrollbar untuk navigate gambar besar
2. **Multiple Click**: Click beberapa pixel untuk compare warna
3. **Binary Analysis**: Gunakan kolom binary untuk analisis bit-level
4. **CSV untuk Analysis**: Export CSV untuk analisis lebih lanjut di Excel/Python

## 🐛 Troubleshooting

### Gambar tidak muncul
- Pastikan format gambar supported (PNG, JPG, BMP, dll)
- Check ukuran file tidak terlalu besar

### Hover tidak respon
- Pastikan mouse berada di dalam area gambar
- Check gambar sudah ter-load dengan baik

### Export CSV gagal
- Pastikan ada data di tabel
- Check permission write di folder tujuan

## 📝 Contoh Use Case

### 1. Analisis Warna Desain
- Upload desain grafis
- Click pada area warna penting
- Export untuk dokumentasi color palette

### 2. Image Processing Analysis
- Upload hasil processing
- Compare nilai RGB sebelum/sesudah
- Analisis bit-level changes

### 3. Color Palette Extraction
- Upload foto/gambar
- Click pada warna-warna menarik
- Export sebagai color reference

### 4. Educational Purpose
- Belajar representasi warna digital
- Understand RGB to Binary conversion
- Hands-on dengan pixel manipulation

## 🔐 Security & Privacy
- Semua processing dilakukan local
- Tidak ada upload ke server
- Data hanya tersimpan di komputer Anda

## 📦 Dependencies
- Python 3.8+
- tkinter (built-in)
- Pillow >= 10.0.0
- pandas >= 2.0.0
- numpy >= 1.24.0

## 🎓 Educational Value
Aplikasi ini berguna untuk:
- Memahami representasi warna digital (RGB)
- Belajar konversi decimal ke binary
- Memahami hexadecimal color code
- Praktik image processing dasar
- Data export dan analysis

## 📞 Support
Jika ada pertanyaan atau bug, silakan contact developer atau buat issue di repository.

---
**Created with ❤️ for Image Processing Education**
