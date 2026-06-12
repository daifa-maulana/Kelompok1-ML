# Panduan Upload File Per Anggota

Dokumen ini berisi daftar tugas upload file project per anggota dan langkah lengkap untuk mengerjakan.

Perhatian singkat: kamu (owner) tetap pegang `README.md`, `CONTRIBUTING.md`, `LICENSE`, dan konfigurasi `.github/*`. Semua anggota upload hanya file yang tercantum di bawah ke folder yang sudah ada.

---

## Instruksi Umum

```bash
git clone https://github.com/daifa-maulana/Kelompok1-ML.git
cd KElompok1-ML
git checkout -b feature/<nama>-<task>
# salin/letakkan file yang jadi tanggung jawabmu ke folder yang sesuai
git add <paths>
git commit -m "✨ feat: add <deskripsi singkat>"
git push origin feature/<nama>-<task>
# buat PR ke main, minta 1 reviewer (Daifa)
```

---

## Tugas Per Anggota

### 1. Mochamad Firmansyah — Data Analyst & ML
Branch: `feature/mochamad-data`

Upload/kerjakan:
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
Branch: `feature/fauzi-eda`

Upload/kerjakan:
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

### 3. Dini Sriastuti — Modeling
Branch: `feature/dini-modeling`

Upload/kerjakan:
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
Branch: `feature/nazwa-design`

Upload/kerjakan:
- `assets/style.css` (update atau full file)
- `docs/design_guide.md`
- `docs/wireframe/<nama_file>.png` atau `docs/wireframe/<nama_file>.svg`
- Tambah file baru di `docs/wireframe/` bila perlu

### 5. Muhammad Raufan Umarulloh — Frontend Developer
Branch: `feature/raufan-frontend`

Upload/kerjakan:
- `pages/01_Home.py`
- `pages/02_Dataset.py`
- `pages/03_Visualisasi.py`
- `pages/04_Prediksi.py`
- `pages/05_Kesimpulan.py`
- `pages/06_Forecasting.py`
- `utils/navigation.py` (jika perlu perubahan)

### 6. Fajar Muhammad Ramdhani — Backend & Deployment
Branch: `feature/fajar-deploy`

Upload/kerjakan:
- `scripts/train_models.py`
- `utils/predictor.py`
- `docs/DEPLOY_GUIDE.md`
- `requirements.txt` dan `runtime.txt` (jika perlu update)
- Deployment artifacts bila ada (Dockerfile, CI scripts) di root atau `docs/`

---

## Commit & PR Conventions

- Gunakan gitmoji di pesan commit:
  - `✨ feat: add preprocessing notebook`
  - `📝 docs: add wireframe`
  - `🐛 fix: correct predictor logic`
  - `🎨 style: update CSS layout`
- Judul PR: `<nama> — <feature> — short summary`
- Deskripsi PR: list changed files, purpose, how to test, reviewer requested
- Jangan merge sampai CI pass dan minimal 1 approval

---

## Jika File Sudah Ada di GitHub

- Overwrite file lokal, commit di branchmu, push, lalu buka PR.
- Merge PR akan meng-update `main`.

---

## Jika Perlu Copy Dari Project Asli

Jika anggota butuh file lengkap untuk copy dari project asli:

```bash
git fetch origin
git checkout -b temp-copy origin/backup/full-content
# copy required files dari branch ini ke folder lokalmu
git checkout main
# buat branch feature baru lalu tambahkan file yang sesuai
git checkout -b feature/<nama>-<task>
```

---

Silakan edit teks ini sendiri bila perlu sebelum dibagikan ke tim.