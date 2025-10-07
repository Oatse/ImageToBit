# Panduan Fitur Klik RGB Matrix

## 🆕 Fitur Baru: Klik untuk Melihat RGB Matrix

Fitur ini memungkinkan Anda untuk mengklik posisi mana pun pada gambar dan langsung melihat matrix RGB 7x7 pixel di sekitar posisi tersebut dalam popup window terpisah.

## Cara Menggunakan

### 1. Upload Gambar
Pertama, upload gambar seperti biasa menggunakan tombol "📁 Upload Image".

### 2. Klik pada Gambar
- Klik pada posisi mana pun di gambar yang ditampilkan
- Popup window akan langsung muncul

### 3. Lihat RGB Matrix Table
Popup window akan menampilkan:
- **Informasi Posisi**: Koordinat yang diklik (x, y)
- **RGB Value**: Nilai RGB dan Hex dari pixel yang diklik
- **Matrix 7x7**: Tabel matrix 7x7 pixel di sekitar posisi klik
- **Highlight**: Pixel yang diklik ditandai dengan ★ dan background kuning

### 4. Export Matrix (Opsional)
- Klik tombol "💾 Export This Matrix to CSV"
- Pilih lokasi dan nama file
- Matrix tersebut akan diekspor ke CSV

## Detail Fitur

### Matrix Size
- **Default**: 7x7 pixel (3 pixel di setiap sisi dari posisi klik)
- **Dynamic**: Menyesuaikan jika klik di tepi gambar
  - Contoh: Klik di pojok kiri atas hanya menampilkan pixel yang tersedia

### Format Table

#### Header
```
X/Y | 45 | 46 | 47 | 48 | 49 | 50 | 51
```

#### Data Rows
```
45  | (255,128,64) | (128,255,32) | ... 
46  | (200,100,50) | ★ (100,200,25) ★ | ...  <- Posisi klik
47  | (150,75,40)  | (75,150,30)  | ...
```

### Visual Indicators

#### Pixel yang Diklik
- **Text**: Ditandai dengan bintang `★ (R,G,B) ★`
- **Background**: Baris dengan background kuning
- **Position Info**: Ditampilkan di header popup

#### Coordinate System
- **X**: Kolom (horizontal) - dari kiri ke kanan
- **Y**: Baris (vertical) - dari atas ke bawah
- **Origin (0,0)**: Pojok kiri atas gambar

## Contoh Penggunaan

### Skenario 1: Analisis Warna Lokal
**Use Case**: Ingin melihat transisi warna di area tertentu

**Steps**:
1. Klik pada area yang menarik
2. Lihat matrix 7x7 untuk melihat pola warna sekitar
3. Export matrix untuk analisis lebih lanjut

### Skenario 2: Debugging Pixel Tertentu
**Use Case**: Ada pixel yang terlihat aneh, ingin melihat sekitarnya

**Steps**:
1. Klik pada pixel tersebut
2. Bandingkan nilai RGB dengan pixel sekitarnya
3. Identifikasi apakah pixel tersebut outlier

### Skenario 3: Ekstraksi Region of Interest
**Use Case**: Ingin mengambil sample kecil dari gambar

**Steps**:
1. Klik pada center dari region yang diinginkan
2. Export matrix 7x7 ke CSV
3. Gunakan data tersebut untuk analisis terpisah

## Format Export

### CSV Format untuk Click Matrix

File CSV akan berformat matrix dengan struktur:

```csv
X/Y,45,46,47,48,49,50,51
45,"(255,128,64)","(128,255,32)","(64,128,255)","(200,100,50)","(150,75,40)","(100,50,25)","(80,40,20)"
46,"(200,100,50)","[CLICKED] (100,200,25)","(50,100,200)","(150,75,40)","(100,50,25)","(80,40,20)","(60,30,15)"
47,"(150,75,40)","(75,150,30)","(40,75,150)","(120,60,30)","(80,40,20)","(60,30,15)","(50,25,12)"
```

**Note**: Pixel yang diklik ditandai dengan prefix `[CLICKED]`

## Tips dan Trik

### 💡 Tip 1: Quick Sampling
- Klik berbagai posisi untuk quick sampling
- Tidak perlu menutup popup untuk klik lagi
- Bisa buka multiple popup sekaligus

### 💡 Tip 2: Edge Cases
- Klik di tepi atau pojok gambar akan menampilkan matrix yang available
- Matrix akan otomatis menyesuaikan size (bisa <7x7)

### 💡 Tip 3: Kombinasi dengan Hover
- Gunakan hover untuk explorasi cepat
- Gunakan klik untuk analisis detail
- Gunakan search untuk koordinat spesifik

### 💡 Tip 4: Workflow Efisien
1. **Hover** - Cari area menarik
2. **Click** - Analisis detail matrix
3. **Export** - Simpan data untuk dokumentasi
4. **Search** - Verifikasi koordinat exact

## Keyboard Shortcuts

Saat popup terbuka:
- **Escape** atau **Close button**: Tutup popup
- **Klik di gambar lagi**: Buka popup baru untuk posisi lain

## Technical Details

### Matrix Calculation
```python
# Center pixel: (center_x, center_y)
# Matrix size: 7x7
# Half size: 3

start_x = max(0, center_x - 3)
end_x = min(width, center_x + 3 + 1)
start_y = max(0, center_y - 3)
end_y = min(height, center_y + 3 + 1)
```

### Boundary Handling
- Automatic clipping jika dekat edge
- No error untuk click di edge/corner
- Matrix size adapts (3x3 sampai 7x7)

## FAQ

**Q: Bisa ubah matrix size dari 7x7?**
A: Saat ini fixed di 7x7, tapi bisa dimodifikasi di source code pada variable `matrix_size = 7`

**Q: Bisa export semua click dalam satu file?**
A: Saat ini setiap click diekspor terpisah. Bisa gunakan main table export untuk full data.

**Q: Popup tidak muncul?**
A: Pastikan sudah upload gambar terlebih dahulu dan klik di dalam area gambar.

**Q: Bisa klik multiple times?**
A: Ya! Setiap klik akan membuka popup baru. Bisa buka multiple popup sekaligus.

**Q: Matrix overlap dengan main table?**
A: Matrix dari click adalah subset dari main table. Main table tetap menampilkan semua koordinat.

## Lihat Juga

- [USAGE_GUIDE.md](USAGE_GUIDE.md) - Panduan lengkap aplikasi
- [EXPORT_GUIDE.md](EXPORT_GUIDE.md) - Detail format export
- [TABLE_FORMAT.md](TABLE_FORMAT.md) - Format tabel RGB matrix
- [README.md](../README.md) - Overview aplikasi
