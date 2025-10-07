# 🚀 QUICK START - Image to Color Bit Converter

## Cara Termudah untuk Memulai

### Windows - PowerShell (RECOMMENDED)
```powershell
.\run.ps1
```

### Windows - Command Prompt
```cmd
run.bat
```

Itu saja! Script akan otomatis:
1. ✅ Membuat virtual environment (jika belum ada)
2. ✅ Mengaktifkan virtual environment
3. ✅ Install semua dependencies
4. ✅ Menjalankan aplikasi

---

## 🎯 Cara Menggunakan Aplikasi

### Step 1: Upload Image
```
Click [📁 Upload Image] → Pilih gambar
```

### Step 2: Lihat Warna
```
Hover mouse di atas gambar
→ Lihat info RGB, Binary, Hex
```

### Step 3: Simpan Warna
```
Click pada pixel yang ingin disimpan
→ Data masuk ke tabel
```

### Step 4: Export CSV
```
Click [💾 Export to CSV] → Pilih lokasi → Done!
```

---

## 📊 Data yang Dihasilkan

Tabel dengan 10 kolom:
1. **No** - Nomor urut
2. **X** - Koordinat X
3. **Y** - Koordinat Y
4. **Red (Dec)** - Merah (0-255)
5. **Green (Dec)** - Hijau (0-255)
6. **Blue (Dec)** - Biru (0-255)
7. **Red (Bin)** - Merah (binary 8-bit)
8. **Green (Bin)** - Hijau (binary 8-bit)
9. **Blue (Bin)** - Biru (binary 8-bit)
10. **Hex Color** - Kode hex (#RRGGBB)

---

## 📁 File yang Penting

- **`run.ps1`** atau **`run.bat`** → Jalankan aplikasi
- **`main.py`** → Aplikasi utama
- **`USER_GUIDE.md`** → Panduan lengkap
- **`README.md`** → Info project

---

## ❓ Troubleshooting

### Masalah: "python not found"
**Solusi**: Install Python 3.8+ dari python.org

### Masalah: "pip not found"
**Solusi**: 
```powershell
python -m ensurepip --upgrade
```

### Masalah: Script tidak bisa dijalankan di PowerShell
**Solusi**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 💡 Tips

- Gunakan `test_image.png` untuk testing
- Hover untuk lihat, Click untuk simpan
- Export CSV bisa dibuka di Excel
- Read `USER_GUIDE.md` untuk detail lengkap

---

## 🆘 Butuh Bantuan?

1. Baca **USER_GUIDE.md** untuk panduan detail
2. Baca **TECHNICAL_DOC.md** untuk info teknis
3. Check **COMPLETION_REPORT.md** untuk overview

---

**Ready to start?** 🎨

```powershell
.\run.ps1
```

**Happy color hunting!** ✨
