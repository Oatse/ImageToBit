# Image to RGB Matrix Converter

Program untuk mengkonversi gambar menjadi tabel koordinat matriks RGB dengan fitur interaktif.

## Fitur

✅ **Upload Image** - Upload gambar dengan berbagai format (PNG, JPG, BMP, GIF, TIFF)

✅ **Hover RGB Display** - Hover mouse di atas gambar untuk melihat nilai RGB pada koordinat tersebut

✅ **Click RGB Matrix** - 🆕 Klik pada gambar untuk melihat matrix RGB 7x7 di sekitar posisi klik dengan popup window

✅ **Search Coordinate** - Cari koordinat spesifik (x, y) untuk melihat nilai RGB-nya

✅ **RGB Matrix Table** - Tampilan tabel lengkap dengan koordinat x/y dan nilai RGB

✅ **Export Data** - Export data ke CSV (2 format) atau Excel

## Instalasi

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Cara Menggunakan

1. Jalankan program:
```bash
python main.py
```

2. **Upload Image**:
   - Klik tombol "📁 Upload Image"
   - Pilih file gambar yang ingin dikonversi
   - Gambar akan ditampilkan di panel kiri

3. **Hover untuk Melihat RGB**:
   - Gerakkan mouse di atas gambar
   - Nilai RGB pada posisi cursor akan ditampilkan di bawah gambar
   - Format: Position: (x, y) | RGB: (r, g, b) | Hex: #RRGGBB

4. **Klik untuk Melihat RGB Matrix**:
   - **FITUR BARU!** Klik pada gambar untuk melihat matrix RGB di sekitar posisi yang diklik
   - Window popup akan muncul menampilkan tabel 7x7 pixel di sekitar posisi klik
   - Pixel yang diklik akan ditandai dengan bintang (★) dan highlight kuning
   - Tabel menampilkan koordinat dan nilai RGB untuk setiap pixel
   - Bisa export matrix tersebut ke CSV secara terpisah

5. **Search Koordinat**:
   - Masukkan nilai X dan Y di panel kanan
   - Klik tombol "🔍 Search"
   - Nilai RGB untuk koordinat tersebut akan ditampilkan
   - Koordinat akan di-highlight di tabel (jika ada)

6. **Lihat Tabel RGB Matrix**:
   - Tabel di panel kanan menampilkan **SEMUA koordinat** sesuai ukuran gambar
   - Format matrix: X/Y grid dengan RGB tuples
   - **No limit** - gambar 500x300 = tabel 500 kolom x 300 baris
   - Scroll horizontal dan vertikal untuk navigasi
   - Search auto-scroll ke koordinat yang dicari

7. **Export Data**:
   - Klik "💾 CSV (List)" untuk export format list dengan kolom X, Y, R, G, B, RGB_Hex
   - Klik "📋 CSV (Matrix)" untuk export format matrix seperti tampilan tabel
   - Klik "📊 Excel" untuk export ke Excel format
   - Pilih lokasi dan nama file

## Screenshot Fitur

### Panel Kiri - Image Display
- Display gambar dengan scrollbar
- Hover information real-time
- Info ukuran gambar

### Panel Kanan - RGB Matrix Data
- Search coordinate box
- RGB Matrix table dengan semua pixel
- Export buttons

## Format Output

### CSV List Format:
Kolom: X, Y, R, G, B, RGB_Hex
- **X**: Koordinat horizontal (0 sampai width-1)
- **Y**: Koordinat vertikal (0 sampai height-1)
- **R**: Red value (0-255)
- **G**: Green value (0-255)
- **B**: Blue value (0-255)
- **RGB_Hex**: Nilai RGB dalam format hexadecimal (#RRGGBB)

### CSV Matrix Format:
Format grid X/Y dengan RGB tuple:
```
X/Y,0,1,2,3
0,"(255,128,64)","(128,255,32)","(64,128,255)","(200,100,50)"
1,"(200,100,50)","(100,200,25)","(50,100,200)","(150,75,40)"
```

### Excel Format:
Same as CSV List format in Excel worksheet

📖 **Detail lengkap**: Lihat `docs/EXPORT_GUIDE.md`

## Teknologi

- **Python 3.x**
- **Tkinter** - GUI framework
- **Pillow (PIL)** - Image processing
- **Pandas** - Data manipulation
- **NumPy** - Array operations
- **OpenPyXL** - Excel export

## Catatan

- ✅ **Tabel menampilkan SEMUA koordinat** tanpa batasan
- Untuk gambar besar (>10,000 pixels), ada loading message
- Loading time proporsional dengan ukuran gambar
- Gunakan Search untuk navigasi cepat ke koordinat tertentu
- Search akan auto-scroll tabel ke posisi yang dicari
- Export menyimpan semua pixel data dalam format pilihan

## License

MIT License
