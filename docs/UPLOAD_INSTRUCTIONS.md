# Panduan Upload File Per Anggota

Dokumen ini menjelaskan file yang harus di-upload oleh setiap anggota, nama branch yang harus dipakai, dan langkah lengkap dari clone sampai membuat PR. Gunakan format commit `gitmoji` untuk konsistensi.

---

## Aturan Umum

- Jangan push langsung ke `main`.
- Semua anggota harus membuat branch feature: `feature/<nama>-<task>`.
- Commit harus menggunakan gitmoji (contoh: `✨ feat: ...`, `📝 docs: ...`).
- Setelah push, buat Pull Request ke `main` dan minta minimal 1 review.
- `README.md`, `CONTRIBUTING.md`, `LICENSE`, dan konfigurasi repo adalah tugas owner.

---

## Langkah Umum (copyable)

```bash
git clone https://github.com/daifa-maulana/Kelompok1-ML.git
cd KElompok1-ML
git checkout -b feature/<nama>-<task>
# salin/unggah file sesuai jobdes
# contoh: cp /path/ke/file notebooks/03_preprocessing.ipynb
# lalu tambahkan file ke git
git add .
git commit -m "✨ feat: add <deskripsi singkat>"
git push origin feature/<nama>-<task>
# buat PR di GitHub -> base: main, compare: feature/<nama>-<task>
```

Gunakan `gitmoji-cli` jika ingin interaktif:

```bash
npm install -g gitmoji-cli
gitmoji -c
```

---

## Tugas Per Anggota: Semua File Project

### 1. Mochamad Firmansyah — Data Analyst & ML
- Branch: `feature/mochamad-data`
- File yang harus di-upload:
  - `notebooks/01_data_collection.ipynb`
  - `notebooks/03_preprocessing.ipynb`
  - `scripts/preprocessing.py`
  - `data/raw/Exchange_Rate.csv`
  - `data/raw/Exports.csv`
  - `data/raw/FDI.csv`
  - `data/raw/GDP_Growth.csv`
  - `data/raw/Imports.csv`
  - `data/raw/Inflation.csv`
  - `data/raw/Population_Growth.csv`
  - `data/raw/Unemployment.csv`
  - `data/processed/dataset_clean.csv`
  - `data/processed/dataset_indonesia.csv`

### 2. Fauzi Rizky Maulana — Data Analyst & ML
- Branch: `feature/fauzi-eda`
- File yang harus di-upload:
  - `notebooks/02_eda.ipynb`
  - `data/eda_outputs/descriptive_stats.csv`
  - `data/eda_outputs/correlation_heatmap.png`
  - `data/eda_outputs/distributions.png`
  - `data/eda_outputs/scatter_plots.png`
  - `data/eda_outputs/feature_importance.png`
  - `data/eda_outputs/gdp_trend.png`
  - `data/eda_outputs/gdp_forecast.png`
  - `data/eda_outputs/actual_vs_predicted.png`
  - `scripts/visualization.py`

### 3. Dini Sriastuti — Data Analyst & ML
- Branch: `feature/dini-modeling`
- File yang harus di-upload:
  - `notebooks/04_modeling.ipynb`
  - `notebooks/05_forecasting.ipynb`
  - `models/linear_regression.pkl`
  - `models/ridge_regression.pkl`
  - `models/random_forest.pkl`
  - `models/decision_tree.pkl`
  - `models/best_model.pkl`
  - `models/scaler.pkl`
  - `models/data_split.pkl`
  - `models/model_report.json`
  - `models/forecast_report.json`

### 4. Nazwa Nur Hapidah — UI/UX Designer
- Branch: `feature/nazwa-design`
- File yang harus di-upload:
  - `assets/style.css`
  - `docs/design_guide.md`
  - `docs/wireframe/<nama_file>.png` atau `docs/wireframe/<nama_file>.svg`
  - jika perlu, tambahkan file `/docs/wireframe/` baru

### 5. Muhammad Raufan Umarulloh — Frontend Developer
- Branch: `feature/raufan-frontend`
- File yang harus di-upload:
  - `pages/01_Home.py`
  - `pages/02_Dataset.py`
  - `pages/03_Visualisasi.py`
  - `pages/04_Prediksi.py`
  - `pages/05_Kesimpulan.py`
  - `pages/06_Forecasting.py`
  - `utils/navigation.py`

### 6. Fajar Muhammad Ramdhani — Backend & Deployment
- Branch: `feature/fajar-deploy`
- File yang harus di-upload:
  - `scripts/train_models.py`
  - `utils/predictor.py`
  - `docs/DEPLOY_GUIDE.md`
  - `requirements.txt` (jika ada pembaruan dependensi)
  - `runtime.txt` (jika perlu update runtime)

---

## Tugas Owner / Kamu
- `README.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `.gitignore`
- `.github/CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/ci.yml`
- `.streamlit/config.toml`
- `app.py`
- `fix_encoding.py`

Jika kamu mau, kamu bisa upload sendiri `README.md` dan `LICENSE` dulu di branch khusus:

```bash
git checkout -b docs/update-readme
git add README.md LICENSE
git commit -m "📝 docs: update README and LICENSE"
git push origin docs/update-readme
```

---

## Contoh Pesan Commit (gitmoji)

- `✨ feat: add preprocessing notebook`
- `📝 docs: update deploy guide`
- `🐛 fix: correct prediction bug`
- `🎨 style: update CSS layout`

---

## Review & Merge

- Buat PR ke `main` dengan deskripsi lengkap (apa yang diubah, file utama, langkah uji).
- Minta reviewer: paling tidak 1 approval dari tim.
- Pastikan CI (jika ada) lulus sebelum merge.

---

Jika mau, saya bisa tambah checklist `docs/UPLOAD_CHECKLIST.md` agar setiap anggota bisa cek file mana yang sudah mereka upload.