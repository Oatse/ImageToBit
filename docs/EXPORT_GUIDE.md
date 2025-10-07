# Dokumentasi Fitur Export CSV

Program sekarang memiliki **3 opsi export** yang berbeda untuk kebutuhan yang berbeda.

## 📊 Pilihan Export

### 1. 💾 CSV (List Format)
Export data dalam format **list/tabel** dengan semua detail per pixel.

#### Format File:
```csv
X,Y,R,G,B,RGB_Hex
0,0,255,128,64,#FF8040
1,0,128,255,32,#80FF20
2,0,64,128,255,#4080FF
0,1,200,100,50,#C86432
1,1,100,200,25,#64C819
2,1,50,100,200,#3264C8
...
```

#### Kegunaan:
✅ Analisis data dengan tools statistik
✅ Filter berdasarkan nilai RGB tertentu
✅ Sorting berdasarkan koordinat atau warna
✅ Import ke database
✅ Analisis pixel-by-pixel detail

#### Kolom:
- **X**: Koordinat horizontal (0 sampai width-1)
- **Y**: Koordinat vertikal (0 sampai height-1)
- **R**: Red value (0-255)
- **G**: Green value (0-255)
- **B**: Blue value (0-255)
- **RGB_Hex**: Warna dalam format hexadecimal

---

### 2. 📋 CSV (Matrix Format)
Export data dalam format **matrix/grid** seperti tampilan tabel di program.

#### Format File:
```csv
X/Y,0,1,2,3,4
0,"(255,128,64)","(128,255,32)","(64,128,255)","(200,100,50)","(150,75,40)"
1,"(200,100,50)","(100,200,25)","(50,100,200)","(150,75,40)","(100,50,25)"
2,"(150,75,40)","(75,150,20)","(40,75,150)","(100,50,25)","(75,40,20)"
3,"(100,50,25)","(50,100,12)","(25,50,100)","(75,40,20)","(50,25,12)"
```

#### Kegunaan:
✅ Visual representation yang mudah dibaca
✅ Langsung lihat pola warna dalam grid
✅ Import ke spreadsheet untuk visualisasi
✅ Compare warna antar koordinat dengan mudah
✅ Format yang mirip dengan matrix asli image

#### Struktur:
- **Kolom pertama**: Y coordinates (0, 1, 2, ...)
- **Kolom lainnya**: X coordinates (0, 1, 2, ...)
- **Cell**: RGB tuple dalam format (R,G,B)

---

### 3. 📊 Excel Format
Export ke Excel dengan format list (seperti CSV List).

#### Format File:
Excel worksheet dengan kolom:
```
| X | Y | R   | G   | B   | RGB_Hex |
|---|---|-----|-----|-----|---------|
| 0 | 0 | 255 | 128 | 64  | #FF8040 |
| 1 | 0 | 128 | 255 | 32  | #80FF20 |
| 2 | 0 | 64  | 128 | 255 | #4080FF |
```

#### Kegunaan:
✅ Formatting dan styling di Excel
✅ Pivot tables untuk analisis
✅ Charts dan graphs
✅ Formula dan calculations
✅ Professional reports

---

## 🎯 Kapan Menggunakan Format Apa?

### CSV List Format 💾
**Gunakan untuk:**
- Data analysis dengan Python/R
- Database import
- Filtering dan sorting kompleks
- Machine learning datasets
- Mencari pixel dengan RGB tertentu

**Contoh Use Case:**
```python
import pandas as pd
df = pd.read_csv('image_data.csv')

# Cari semua pixel merah
red_pixels = df[df['R'] > 200]

# Rata-rata RGB per koordinat Y
avg_by_y = df.groupby('Y')[['R', 'G', 'B']].mean()
```

### CSV Matrix Format 📋
**Gunakan untuk:**
- Quick visual inspection
- Membandingkan warna bersebelahan
- Dokumentasi visual
- Presentasi yang mudah dibaca
- Pattern recognition manual

**Contoh Use Case:**
- Print dan analisis manual
- Compare gambar A vs B secara visual
- Check gradient transitions
- Verify color consistency

### Excel Format 📊
**Gunakan untuk:**
- Business reports
- Color analysis dengan charts
- Conditional formatting untuk visualisasi
- Sharing dengan non-technical users
- Professional documentation

**Contoh Use Case:**
- Laporan analisis warna produk
- Visualisasi distribusi warna
- Documentation dengan screenshots
- Client presentations

---

## 📝 Cara Menggunakan Export

### Langkah-langkah:

1. **Upload Image** terlebih dahulu
2. Pilih tombol export sesuai kebutuhan:
   - **💾 CSV (List)** - untuk analisis detail
   - **📋 CSV (Matrix)** - untuk visual matrix
   - **📊 Excel** - untuk laporan professional
3. Pilih lokasi penyimpanan
4. Beri nama file
5. Klik **Save**
6. Tunggu konfirmasi sukses

### Tips:
- Untuk gambar besar, export mungkin memakan waktu beberapa detik
- Pastikan ada cukup disk space
- Close file Excel jika ingin overwrite
- Gunakan nama file yang deskriptif (contoh: `logo_rgb_matrix.csv`)

---

## 📐 Contoh Output Real

### Gambar 5x3 pixels

#### CSV List Output:
```csv
X,Y,R,G,B,RGB_Hex
0,0,255,0,0,#FF0000
1,0,255,0,0,#FF0000
2,0,0,255,0,#00FF00
3,0,0,255,0,#00FF00
4,0,0,0,255,#0000FF
0,1,255,0,0,#FF0000
1,1,255,0,0,#FF0000
2,1,0,255,0,#00FF00
3,1,0,255,0,#00FF00
4,1,0,0,255,#0000FF
0,2,255,0,0,#FF0000
1,2,255,0,0,#FF0000
2,2,0,255,0,#00FF00
3,2,0,255,0,#00FF00
4,2,0,0,255,#0000FF
```
**Total: 16 rows (termasuk header)**

#### CSV Matrix Output:
```csv
X/Y,0,1,2,3,4
0,"(255,0,0)","(255,0,0)","(0,255,0)","(0,255,0)","(0,0,255)"
1,"(255,0,0)","(255,0,0)","(0,255,0)","(0,255,0)","(0,0,255)"
2,"(255,0,0)","(255,0,0)","(0,255,0)","(0,255,0)","(0,0,255)"
```
**Total: 4 rows (termasuk header)**

Terlihat matrix format **lebih compact** dan **lebih mudah dibaca** untuk melihat pola!

---

## 🔍 Membaca CSV di Program Lain

### Python (Pandas):
```python
import pandas as pd

# List format
df_list = pd.read_csv('image_list.csv')
print(df_list.head())

# Matrix format
df_matrix = pd.read_csv('image_matrix.csv', index_col=0)
print(df_matrix)
```

### Excel:
1. Open Excel
2. File → Open → pilih CSV file
3. Data akan ter-format otomatis
4. Gunakan filters dan sorting

### Google Sheets:
1. File → Import
2. Upload CSV file
3. Choose "Replace current sheet"
4. Data ready to use

---

## 💡 Tips Advanced

### Combining Formats:
1. Export **Matrix** untuk visual quick check
2. Export **List** untuk detailed analysis
3. Export **Excel** untuk final report

### Large Images:
- Export time tergantung ukuran image
- 100x100 pixels ≈ 10,000 rows (List format)
- Consider sampling untuk gambar sangat besar

### Automation:
Bisa diintegrasikan dengan script Python untuk batch processing:
```python
# Pseudo-code
for image in image_folder:
    load_image(image)
    export_to_csv_matrix(f"{image}_matrix.csv")
```

---

**Fitur export CSV sudah lengkap dan siap digunakan!** 🎉
