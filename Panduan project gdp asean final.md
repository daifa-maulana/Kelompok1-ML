# Panduan Project — GDP Growth Asia Tenggara (Versi Final)

Dokumen ini **beda dari `Panduan_Revisi_GDP_ASEAN.pdf` yang lama** — kalau dokumen lama itu isinya rencana/tugas yang *harus* dikerjakan, dokumen ini isinya dokumentasi apa yang **benar-benar ada** di project final kalian sekarang (hasil sinkron dengan `gdp-prediction-asean-main`), lengkap dengan nama fungsi, kolom, dan struktur yang sebenarnya. Tujuannya biar kalian (dan siapa pun yang lanjutin/presentasi project ini) nggak salah acuan lagi.

> ⚠️ Catatan: dokumentasi bawaan repo ini sendiri (`docs/data_dictionary.md`, `docs/design_guide.md`) **belum diupdate** dan masih menjelaskan versi lama (Indonesia 1 negara, tema light). Jangan jadikan acuan — pakai dokumen ini saja.

---

## 1. Ringkasan Project

| | |
|---|---|
| **Nama** | Prediksi & Analisis GDP Growth Asia Tenggara |
| **Sumber data** | World Bank |
| **Cakupan negara** | 9 negara (lihat daftar di bawah) |
| **Rentang tahun** | 1961–2024 |
| **Total observasi (data siap pakai)** | 576 baris |
| **Model terbaik** | Random Forest |

**Daftar 9 negara** (perhatikan penulisannya — pakai nama resmi World Bank, bukan nama umum):

`Brunei Darussalam`, `Cambodia`, `Indonesia`, `Lao PDR`, `Malaysia`, `Philippines`, `Singapore`, `Thailand`, `Viet Nam`

> Catatan: Myanmar tidak masuk karena datanya sendiri (`Exports_pct`/`Imports_pct`) kosong 100% di sumber World Bank yang dipakai — sudah pernah dibahas sebelumnya.

---

## 2. Struktur Folder (yang benar-benar dipakai aplikasi)

```
├── app.py                      → Halaman utama (KPI ringkasan)
├── requirements.txt            → Daftar dependency
├── runtime.txt                 → Versi Python
├── assets/style.css            → Dark theme
├── data/
│   ├── raw/dataset_asean.csv         → Data mentah 10 negara
│   └── processed/dataset_asean.csv   → Data siap pakai, 9 negara, 17 kolom
├── models/
│   ├── best_model.pkl, linear_regression.pkl, ridge_regression.pkl,
│   │   decision_tree.pkl, random_forest.pkl   → 4 model + best model
│   ├── scaler.pkl               → StandardScaler
│   ├── features.json            → {"features": [...8 fitur...]}
│   ├── model_report.json        → Metrik evaluasi semua model
│   └── forecast_report.json     → Hasil forecasting tersimpan
├── pages/
│   ├── 02_EDA.py
│   ├── 03_Prediksi.py
│   ├── 04_Analisis_Global.py
│   └── 05_Kesimpulan.py
├── scripts/
│   ├── train_models.py          → Training 4 model (dipakai)
│   ├── visualization.py         → Fungsi chart Plotly (dipakai)
│   └── preprocessing.py         → ⚠️ LEGACY, lihat catatan di §4
└── utils/
    ├── navigation.py            → Navbar 4 link
    ├── predictor.py             → Load model & prediksi
    └── world_data.py            → Loader data untuk peta & timeseries
```

`pages/01_Home.py` **tidak ada** — konten beranda memang sudah dipindah ke `app.py` langsung (sesuai revisi).

---

## 3. Dataset — `data/processed/dataset_asean.csv`

Ini kolom yang **benar-benar ada** di file processed final (17 kolom, bukan 11 seperti versi awal kalian):

| Kolom | Keterangan |
|---|---|
| `Country` | Nama negara |
| `Year` | Tahun (1961–2024) |
| `Exports`, `Imports` | Nilai ekspor/impor mentah |
| `GDP` | GDP total |
| `GDP_Per_Capita` | GDP per kapita (fitur model) |
| `GNI` | Gross National Income |
| `Life_Expectancy` | Angka harapan hidup (fitur model) |
| `Population` | Jumlah populasi |
| `prev_gdp` | GDP tahun sebelumnya (dipakai hitung growth) |
| `GDP_Growth` | **Target model** — pertumbuhan GDP (%) |
| `GDP_B` | GDP dalam satuan miliar (dipakai untuk peta) |
| `Exports_pct`, `Imports_pct` | Ekspor/impor sebagai % GDP (fitur model) |
| `Population_Growth` | Pertumbuhan populasi (fitur model) |
| `GDP_Growth_lag1`, `GDP_Growth_lag2` | Lag GDP Growth 1 & 2 tahun (fitur model) |
| `GDP_lag1` | Lag GDP Per Kapita 1 tahun (fitur model) |

**8 fitur yang dipakai model** (persis sama dengan isi `models/features.json`):
```
GDP_Per_Capita, Population_Growth, Exports_pct, Imports_pct,
Life_Expectancy, GDP_Growth_lag1, GDP_Growth_lag2, GDP_lag1
```

---

## 4. Preprocessing

⚠️ **Penting:** `scripts/preprocessing.py` di project final ini **tidak dipakai lagi** oleh pipeline yang jalan sekarang — isinya masih fungsi lama (FEATURES = `Inflation, Unemployment, FDI, Exchange_Rate`, default path `dataset_world.csv`). Ini file sisa dari versi Indonesia yang belum dibersihkan, bukan bug baru yang perlu diperbaiki untuk aplikasi jalan, tapi **jangan jadikan referensi** kalau ditanya dosen "preprocessing-nya gimana" — jelaskan alur yang sebenarnya, yaitu langsung dari `data/processed/dataset_asean.csv` yang sudah jadi.

Kalau mau rapi & jujur ke penilai, sebaiknya salah satu dari kalian (idealnya yang pegang bagian data) **hapus atau update file ini** supaya tidak membingungkan saat dicek.

---

## 5. Modeling — `scripts/train_models.py`

- Baca data dari `data/processed/dataset_asean.csv`
- Fitur: 8 fitur ASEAN di atas, Target: `GDP_Growth`
- Split & scaling disimpan ke `models/data_split.pkl`, `models/scaler.pkl`
- 4 model dilatih & disimpan: `linear_regression.pkl`, `ridge_regression.pkl`, `decision_tree.pkl`, `random_forest.pkl`, plus `best_model.pkl` (salinan model terbaik)

**Hasil evaluasi final** (dari `models/model_report.json`):

| Model | CV R² | CV MAE | CV RMSE | Test R² | Test MAE |
|---|---|---|---|---|---|
| Linear Regression | 0.032 | 3.62 | 5.44 | −0.248 | 3.20 |
| Ridge Regression | 0.048 | 3.60 | 5.41 | −0.217 | 3.14 |
| Decision Tree | −0.071 | 3.86 | 5.56 | −0.370 | 3.47 |
| **Random Forest (terbaik)** | **0.233** | **3.28** | **4.74** | −0.071 | 2.77 |

> Catatan jujur: Test R² semua model masih negatif, artinya di data test model belum lebih baik dari sekadar menebak rata-rata. Ini wajar untuk data macroeconomic yang noisy dan observasi terbatas (576 baris untuk 9 negara) — kalau ditanya dosen, ini poin diskusi yang valid untuk bagian "keterbatasan model" di laporan/`05_Kesimpulan.py`.

---

## 6. Visualisasi — `scripts/visualization.py`

Semua fungsi pakai **Plotly** (bukan matplotlib/seaborn seperti versi draft kalian), dan semua sudah dites jalan:

| Fungsi | Kegunaan |
|---|---|
| `plot_gdp_trend(df, country=None)` | Tren GDP Growth — 1 negara atau rata-rata semua |
| `plot_correlation_heatmap(df)` | Heatmap korelasi antar fitur |
| `plot_scatter(df, feature)` | Scatter 1 fitur vs GDP Growth |
| `plot_all_scatter(df)` | Scatter semua fitur sekaligus |
| `plot_distribution(df, column)` | Distribusi 1 kolom |
| `plot_actual_vs_predicted(y_test, y_pred)` | Perbandingan aktual vs prediksi |
| `plot_model_comparison(results)` | Bar chart perbandingan metrik antar model |
| `plot_all_models_vs_actual(results, y_test)` | Semua model vs aktual dalam 1 chart |
| `plot_feature_importance(fi, model_name)` | Feature importance |
| `plot_prediction_comparison(predictions)` | Perbandingan hasil prediksi antar model |

---

## 7. Prediksi — `utils/predictor.py`

Dua fungsi utama yang dipakai halaman `03_Prediksi.py` dan `04_Analisis_Global.py`:

```python
predict_all_models(input_dict: dict) -> dict
# input_dict = {"GDP_Per_Capita": ..., "Population_Growth": ..., ... 8 fitur}
# return: {"predictions": {nama_model: nilai, ...}, "best_model": ..., "best_metrics": {...}}

predict_future(input_dict: dict, n_years: int, start_year: int = 2025) -> dict
# return: {"years": [...], "predictions": {nama_model: [nilai per tahun]}, "metrics": {...}, "best_model": ...}
```

Model dan scaler di-load dari `models/best_model.pkl`, `models/scaler.pkl`, dan semua model individual via `models/model_report.json`.

---

## 8. Data Peta & Analisis Global — `utils/world_data.py`

```python
load_world_gdp() -> DataFrame           # load dataset_asean.csv lengkap
get_available_years(df) -> list         # daftar tahun yang ada
get_map_data(df, year, metric="GDP_B")  # data siap pakai untuk peta ECharts
get_country_timeseries(df, country)     # data historis 1 negara
get_top_countries(df, year, metric="GDP_B")  # ranking negara
```

Dipakai di `pages/04_Analisis_Global.py` untuk peta interaktif + tabel ranking + forecasting.

---

## 9. Halaman & Navigasi

`utils/navigation.py` → `show_navbar()` menampilkan 4 link: EDA, Prediksi, Analisis ASEAN, Kesimpulan — dipanggil di awal tiap halaman di `pages/`.

| Halaman | Isi |
|---|---|
| `app.py` | Beranda + KPI ringkasan |
| `pages/02_EDA.py` | Eksplorasi data, filter negara |
| `pages/03_Prediksi.py` | Input 8 fitur → prediksi 4 model |
| `pages/04_Analisis_Global.py` | Peta ASEAN + forecasting |
| `pages/05_Kesimpulan.py` | Perbandingan model & insight |

---

## 10. Dependency (`requirements.txt`)

```
streamlit>=1.35.0
streamlit-echarts>=0.4.0
pandas, numpy, scikit-learn
matplotlib, seaborn, plotly
joblib, requests, wbgapi
openpyxl, xgboost, prophet, statsmodels, scipy
```

Install dengan `pip install -r requirements.txt`, lalu jalankan `streamlit run app.py`.

---

## 11. Rangkuman untuk Presentasi

Kalau kalian butuh menjelaskan alur project ke dosen/penguji, urutan yang **benar** (sesuai kode yang jalan) adalah:

1. Data mentah dari World Bank → `data/raw/dataset_asean.csv` (10 negara)
2. Data diproses (interpolasi, lag features) → `data/processed/dataset_asean.csv` (9 negara, Myanmar dikecualikan karena data ekspor-impor kosong)
3. Training 4 model via `scripts/train_models.py` → tersimpan di `models/`
4. Streamlit app (`app.py` + `pages/`) baca model & data untuk EDA, prediksi, dan analisis peta
5. Model terbaik: **Random Forest** (CV R² 0.233)
