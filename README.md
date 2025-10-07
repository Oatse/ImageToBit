# 🎨 Image to Color Bit Converter

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

Aplikasi desktop untuk mengkonversi gambar ke color bit dengan fitur hover detection dan export CSV. Ideal untuk pembelajaran image processing, analisis warna, dan ekstraksi color palette.

![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)

## ✨ Fitur Utama

- � **AUTO-READ ALL PIXELS** - Upload image langsung baca semua color bit! (NEW!)
- �🖼️ **Upload Image** - Support PNG, JPG, BMP, GIF, TIFF
- 🎯 **Hover Detection** - Real-time color detection saat hover
- 💾 **Click to Save** - Click pixel untuk menyimpan warna
- 📊 **Data Table** - Tabel interaktif dengan 10 kolom
- 📤 **Export CSV** - Export data ke CSV format
- 🎨 **Color Preview** - Visual preview warna real-time
- 🗑️ **Clear Table** - Hapus semua data dengan satu click
- 📍 **Visual Markers** - Marker pada pixel yang disimpan
- 📏 **Status Bar** - Info real-time tentang operasi
- ⚡ **Progress Indicator** - Monitor proses pembacaan pixel

## 🖼️ Screenshot

```
+--------------------------------------------------------+
| [Upload] [Export CSV] [Clear]  | Color Info | [Preview]|
+--------------------------------------------------------+
|                        |                                |
|    Image Canvas        |        Data Table             |
|    (with markers)      |    (X, Y, RGB, Binary, Hex)   |
|                        |                                |
+--------------------------------------------------------+
| Status: Ready                                          |
+--------------------------------------------------------+
```

## 🚀 Quick Start

### Cara Termudah (Windows)

#### PowerShell:
```powershell
.\run.ps1
```

#### Command Prompt:
```cmd
run.bat
```

### Manual Installation

1. **Clone atau Download Project**
   ```bash
   cd ImageToBit
   ```

2. **Buat Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Aktivasi Virtual Environment**
   
   Windows PowerShell:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   Windows CMD:
   ```cmd
   venv\Scripts\activate.bat
   ```
   
   Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Application**
   ```bash
   python main.py
   ```

## 📖 Cara Menggunakan

### 1. Upload Gambar (AUTO-READ!)
- Click tombol **"📁 Upload Image"**
- Pilih file gambar (PNG, JPG, BMP, dll)
- Gambar akan ditampilkan di canvas kiri
- **SEMUA PIXEL OTOMATIS TERBACA!** 🚀
- Progress bar menunjukkan proses pembacaan
- Konfirmasi untuk gambar besar (>1 juta pixel)

### 2. Explore Warna (Optional)
- **Hover** mouse di atas gambar
- Lihat info warna di label atas
- Color preview menampilkan warna secara visual

### 3. Simpan Warna Tambahan (Optional)
- **Click** pada pixel yang ingin disimpan
- Data tersimpan ke tabel kanan
- Marker muncul di posisi click

### 4. Export Data
- Click tombol **"💾 Export to CSV"**
- Pilih lokasi save
- File CSV berhasil dibuat dengan SEMUA pixel!

### 5. Clear Data
- Click tombol **"🗑️ Clear Table"**
- Konfirmasi untuk hapus semua data

## 📊 Format Data

### Kolom Tabel (10 Kolom)
| Column | Description | Example |
|--------|-------------|---------|
| No | Nomor urut | 1 |
| X | Koordinat X | 50 |
| Y | Koordinat Y | 100 |
| Red (Dec) | Nilai merah (0-255) | 255 |
| Green (Dec) | Nilai hijau (0-255) | 128 |
| Blue (Dec) | Nilai biru (0-255) | 64 |
| Red (Bin) | Binary 8-bit merah | 11111111 |
| Green (Bin) | Binary 8-bit hijau | 10000000 |
| Blue (Bin) | Binary 8-bit biru | 01000000 |
| Hex Color | Kode hex | #FF8040 |

### CSV Output Example
```csv
X,Y,Red_Dec,Green_Dec,Blue_Dec,Red_Bin,Green_Bin,Blue_Bin,Hex_Color
50,100,255,128,64,11111111,10000000,01000000,#FF8040
120,200,0,255,0,00000000,11111111,00000000,#00FF00
```

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Core language |
| tkinter | Built-in | GUI Framework |
| Pillow | 11.3.0 | Image processing |
| pandas | 2.3.3 | Data management |
| numpy | 2.3.3 | Array operations |

## 📦 Dependencies

```txt
Pillow>=10.0.0
pandas>=2.0.0
numpy>=1.24.0
```

## 🎓 Use Cases

### 1. Education
- Belajar representasi warna digital (RGB, Binary, Hex)
- Memahami konversi decimal ke binary
- Praktik image processing dasar

### 2. Design
- Extract color palette dari design
- Dokumentasi brand colors
- Analisis color scheme

### 3. Development
- Testing color values
- Debugging image processing
- Color consistency check

### 4. Research
- Color analysis
- Image quality assessment
- Data collection

## 📚 Documentation

- 📄 **[USER_GUIDE.md](USER_GUIDE.md)** - Detailed user guide
- 📄 **[TECHNICAL_DOC.md](TECHNICAL_DOC.md)** - Technical documentation
- 📄 **[CHANGELOG.md](CHANGELOG.md)** - Version history
- 📄 **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project overview

## 🧪 Testing

### Generate Test Image
```bash
python create_test_image.py
```

Akan membuat `test_image.png` dengan berbagai warna untuk testing.

## 🎯 Features in Detail

### Real-time Color Detection
- Deteksi warna saat mouse hover
- No lag, instant response
- Support semua image mode (RGB, RGBA, Grayscale)

### Data Management
- Efficient storage dengan pandas DataFrame
- Easy export ke CSV
- Support hundreds of saved colors

### User Interface
- Clean and intuitive
- Responsive layout
- Visual feedback untuk semua action
- Error handling dengan user-friendly messages

## 🔒 Security & Privacy

- ✅ 100% Local processing
- ✅ No internet required
- ✅ No data collection
- ✅ Your images stay private

## 💡 Tips & Tricks

1. **Large Images**: Gunakan scrollbar untuk navigate
2. **Multiple Colors**: Click beberapa pixel untuk compare
3. **Binary Analysis**: Gunakan kolom binary untuk bit-level analysis
4. **CSV Analysis**: Export untuk analisis di Excel atau Python

## ⚠️ System Requirements

- **OS**: Windows 10+, macOS 10.14+, Linux
- **Python**: 3.8 or higher
- **RAM**: 2 GB minimum (4 GB recommended)
- **Display**: 1280x720 minimum

## 🐛 Troubleshooting

### Common Issues

**Q: ModuleNotFoundError**  
A: Install dependencies: `pip install -r requirements.txt`

**Q: Image not loading**  
A: Check if file format is supported (PNG, JPG, BMP, GIF, TIFF)

**Q: CSV export failed**  
A: Check write permissions in target folder

**Q: Hover not working**  
A: Ensure mouse is over the image area

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created with ❤️ for Image Processing Education

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

## 📧 Contact

For questions or support, please open an issue in the repository.

---

**Happy Color Hunting!** 🎨✨
