# 📋 Panduan Kontribusi — Kelompok 1 ML

Dokumen ini berisi panduan lengkap untuk berkontribusi pada repositori ini. Baca seluruh panduan sebelum mulai bekerja!

---

## 🚀 Setup Awal (Lakukan Sekali)

### 1. Clone repositori
```bash
git clone [https://github.com/daifa-maulana/Kelompok1-ML.git](https://github.com/daifa-maulana/Kelompok1-ML.git)
cd Kelompok1-ML

```

### 2. Install semua dependencies

```bash
pip install -r requirements.txt

```

### 3. Pindah ke branch milikmu

```bash
# Lihat semua branch yang tersedia
git branch -a

# Pindah ke branch milikmu
git checkout feature/nama-branchmu

```

### 4. Verifikasi kamu sudah di branch yang benar

```bash
git branch
# Tanda * menunjukkan branch aktif saat ini

```

---

## 🌿 Branch Masing-Masing Anggota

| Nama | Branch | Tugas |
| --- | --- | --- |
| Mochamad Firmansyah | `feature/data-collection` | Kumpulkan & validasi data World Bank |
| Fajar Muhammad Ramdhani | `feature/eda-visualization` | EDA & fungsi visualisasi |
| Fauzi Rizky Maulana | `feature/preprocessing` | Preprocessing & normalisasi data |
| Muhammad Raufan Umarulloh | `feature/modeling` | Training & evaluasi model ML |
| Nazwa Nur Hapidah | `feature/streamlit-ui` | Desain halaman Streamlit |
| Dini Sriastuti | `feature/streamlit-backend` | Integrasi model & deployment |

> ⚠️ **PENTING:** Jangan pernah push langsung ke `main` atau `develop`!

---

## 🔄 Alur Kerja Harian

### Sebelum mulai kerja — selalu pull dulu!

```bash
git checkout feature/nama-branchmu
git pull origin feature/nama-branchmu

```

### Setelah selesai mengerjakan sesuatu — commit!

```bash
# Lihat file apa saja yang berubah
git status

# Tambahkan file yang mau di-commit
git add nama-file.py
# atau tambahkan semua sekaligus
git add .

# Commit dengan pesan yang deskriptif
git commit -m "✨ feat: tambah fungsi visualisasi heatmap korelasi"

# Push ke branch kamu
git push origin feature/nama-branchmu

```

### Setelah selesai satu tugas besar — buat Pull Request!

1. Buka GitHub → repositori ini
2. Klik **"Compare & pull request"** atau **"New pull request"**
3. Set target branch: `base: develop` ← `compare: feature/nama-branchmu`
4. Isi judul dan deskripsi PR (lihat contoh di bawah)
5. Assign reviewer ke **Daifa Maulana (PM)**
6. Klik **"Create pull request"**
7. Tunggu review dan approval sebelum merge

---

## 💬 Format Commit (Wajib Pakai Gitmoji)

Format penulisan pesan commit:

```text
<emoji> <type>: <deskripsi singkat dalam bahasa Indonesia>

```

### Daftar Emoji & Type

| Emoji | Type | Kapan Dipakai | Contoh |
| --- | --- | --- | --- |
| 🎉 | `feat` | Initial commit pertama | `🎉 feat: initial project structure` |
| ✨ | `feat` | Fitur baru | `✨ feat: tambah fungsi heatmap korelasi` |
| 🐛 | `fix` | Perbaikan bug | `🐛 fix: perbaikan error scaling data` |
| 📝 | `docs` | Update dokumentasi | `📝 docs: update README dengan info tim` |
| 📊 | `data` | Tambah/update dataset | `📊 data: tambah dataset GDP mentah` |
| ♻️ | `refactor` | Restructuring kode | `♻️ refactor: rapikan fungsi preprocessing` |
| 💄 | `style` | Update tampilan UI | `💄 style: update warna tema Streamlit` |
| 🔧 | `chore` | Update konfigurasi | `🔧 chore: update requirements.txt` |
| 🚀 | `deploy` | Deploy aplikasi | `🚀 deploy: upload ke Streamlit Cloud` |

### Contoh commit yang BENAR ✅

```bash
git commit -m "✨ feat: tambah notebook EDA dengan statistik deskriptif"
git commit -m "📊 data: tambah 8 file CSV mentah dari World Bank"
git commit -m "🐛 fix: perbaikan missing values di kolom FDI"
git commit -m "📝 docs: tambah data_dictionary.md"

```

### Contoh commit yang SALAH ❌

```bash
git commit -m "update"
git commit -m "fix"
git commit -m "done"
git commit -m "asjkdhaksjdh"

```

---

## 📬 Format Pull Request

### Judul PR:

```text
✨ feat: [nama fitur] — [nama kamu]

```

*Contoh:* `✨ feat: EDA lengkap dengan 5 visualisasi — Fajar`

### Deskripsi PR (isi di kolom description):

```markdown
## 📋 Apa yang dikerjakan?
- Tambah notebook 02_eda.ipynb
- Buat heatmap korelasi antar variabel
- Buat line chart tren GDP 1991-2024
- Buat scatter plot 7 variabel vs GDP Growth

## ✅ Checklist
- [ ] Kode sudah ditest dan berjalan tanpa error
- [ ] Tidak ada file yang tidak perlu (misal .ipynb_checkpoints)
- [ ] Sudah sesuai dengan tugas yang ditetapkan

## 📎 Catatan untuk Reviewer
Tolong cek apakah visualisasi sudah tampil dengan benar.

```

---

## ⚠️ Aturan Penting

| Aturan | Penjelasan |
| --- | --- |
| ✅ Commit pakai akun GitHub pribadi | Kontribusi harus terlacak per orang |
| ✅ Pull dulu sebelum mulai kerja | Hindari konflik dengan kode terbaru |
| ✅ Commit rutin setiap sub-tugas selesai | Jangan tunggu semua selesai baru commit |
| ❌ Jangan push ke main langsung | Harus melalui Pull Request |
| ❌ Jangan commit file > 50MB | GitHub tidak mendukung file besar |
| ❌ Jangan commit file `.env` | Berisi informasi sensitif |
| ❌ Jangan commit folder `__pycache__` | Sudah di-handle oleh `.gitignore` |

---

## ❓ Kalau Ada Masalah

* **Merge conflict?** → Hubungi Daifa (PM) segera
* **Error saat install?** → Cek versi Python sudah 3.10+
* **Tidak bisa push?** → Pastikan sudah di branch yang benar, bukan main
* **Pertanyaan lain?** → Tanya di grup WhatsApp/Discord tim

