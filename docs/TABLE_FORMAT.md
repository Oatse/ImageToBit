# Format Tabel RGB Matrix - Update

## Format Baru Table

Tabel sekarang menggunakan format **matrix** dimana:
- **Kolom pertama (X/Y)**: Label untuk baris (koordinat Y)
- **Kolom 2 dst**: Koordinat X (0, 1, 2, 3, ...)
- **Isi cell**: Nilai RGB dalam format (R,G,B)

### Contoh Tampilan:

```
X/Y | 0             | 1             | 2             | 3             | ...
----+---------------+---------------+---------------+---------------+-----
0   | (255,128,64)  | (128,255,32)  | (64,128,255)  | (200,100,50)  | ...
1   | (200,100,50)  | (100,200,25)  | (50,100,200)  | (150,75,40)   | ...
2   | (150,75,40)   | (75,150,20)   | (40,75,150)   | (100,50,25)   | ...
3   | (100,50,25)   | (50,100,12)   | (25,50,100)   | (75,40,20)    | ...
... | ...           | ...           | ...           | ...           | ...
```

## Cara Membaca Tabel

### Contoh: Mencari RGB di koordinat (2, 1)
- **X = 2** (kolom ke-3, karena dimulai dari 0)
- **Y = 1** (baris ke-2, karena dimulai dari 0)
- Lihat perpotongan kolom "2" dan baris "1"
- Hasil: **(50,100,200)** → R=50, G=100, B=200

### Format Koordinat
```
        X (Kolom) →
Y   +---+---+---+---+
(B) | 0 | 1 | 2 | 3 |
a   +---+---+---+---+
r 0 |   |   |   |   |
i   +---+---+---+---+
s 1 |   | X |   |   |  ← Koordinat (1,1)
)   +---+---+---+---+
↓ 2 |   |   |   |   |
    +---+---+---+---+
```

## Perubahan dari Format Lama

### Format Lama (List):
```
X  | Y  | R   | G   | B   | RGB Hex
---+----+-----+-----+-----+---------
0  | 0  | 255 | 128 | 64  | #FF8040
1  | 0  | 128 | 255 | 32  | #80FF20
2  | 0  | 64  | 128 | 255 | #4080FF
...
```

### Format Baru (Matrix):
```
X/Y | 0             | 1             | 2             | ...
----+---------------+---------------+---------------+-----
0   | (255,128,64)  | (128,255,32)  | (64,128,255)  | ...
1   | (200,100,50)  | (100,200,25)  | (50,100,200)  | ...
...
```

## Keuntungan Format Baru

✅ **Lebih Intuitif**: Seperti melihat matrix asli gambar
✅ **Mudah Dibaca**: Langsung lihat posisi X,Y
✅ **Compact**: Lebih banyak data dalam satu view
✅ **Visual**: Lebih mudah melihat pola warna
❌ **RGB Hex dihilangkan**: Fokus pada nilai RGB tuple

## Limitasi Display

Untuk performa optimal:
- **Maksimal 20 kolom** (X: 0-19)
- **Maksimal 50 baris** (Y: 0-49)
- Jika gambar lebih besar, akan ada indikator "..."
- **Gunakan fitur Search** untuk koordinat di luar range display

## Fitur Search Tetap Berfungsi

Meskipun tabel dibatasi, fitur search tetap bisa mencari **semua koordinat** dalam gambar:

1. Masukkan X dan Y
2. Klik Search
3. Hasil akan ditampilkan di panel search
4. Jika koordinat ada di tabel, akan di-highlight

## Export Data

Format export **TETAP LENGKAP**:
- CSV/Excel berisi **SEMUA pixel** (tidak dibatasi 20x50)
- Format: X, Y, R, G, B, RGB_Hex
- Cocok untuk analisis data lengkap

### Contoh Export CSV:
```csv
X,Y,R,G,B,RGB_Hex
0,0,255,128,64,#FF8040
1,0,128,255,32,#80FF20
2,0,64,128,255,#4080FF
...
```

## Tips Penggunaan

### Untuk Gambar Kecil (< 20x50)
- Semua pixel akan terlihat di tabel
- Matrix lengkap ditampilkan
- Tidak ada "..." indicator

### Untuk Gambar Besar (> 20x50)
- Tabel menampilkan 20x50 pixel pertama
- Gunakan **Search** untuk koordinat spesifik
- **Export** untuk data lengkap
- Hover tetap berfungsi untuk semua pixel

### Melihat Area Tertentu
1. Hover di gambar untuk lihat koordinat
2. Jika koordinat < 20 (X) dan < 50 (Y), lihat di tabel
3. Jika koordinat > range, gunakan Search
4. Untuk analisis lengkap, gunakan Export

---

**Update**: Format tabel baru lebih intuitif dan sesuai dengan representasi matrix gambar! 🎨
