# 🇮🇩 GDP Prediction Indonesia — Machine Learning

Prediksi laju pertumbuhan ekonomi (GDP Growth) Indonesia menggunakan indikator ekonomi makro dari World Bank Open Data.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![GitHub](https://img.shields.io/badge/GitHub-Collaboration-black)

---

## 👥 Tim Kelompok 1

| No | Nama                      | Peran              | Branch                  |
| -- | ------------------------- | ------------------ | ----------------------- |
| 1  | Daifa Maulana             | Project Manager    | `main` / `develop`      |
| 2  | Mochamad Firmansyah       | Data Analyst       | `feature/data-analysis` |
| 3  | Fauzi Rizky Maulana       | Data Analyst       | `feature/data-analysis` |
| 4  | Nazwa Nur Hapidah         | UI/UX Designer     | `feature/ui-ux`         |
| 5  | Dini Sriastuti            | Frontend Developer | `feature/frontend`      |
| 6  | Muhammad Raufan Umarulloh | Frontend Developer | `feature/frontend`      |
| 7  | Fajar Muhammad Ramdhani   | Backend Developer  | `feature/backend`       |


---

## 🎯 Tujuan Proyek

- Memprediksi GDP Growth Indonesia menggunakan teknik Machine Learning yang sesuai untuk dataset kecil
- Mengidentifikasi indikator ekonomi yang paling berpengaruh terhadap pertumbuhan ekonomi
- Membangun website interaktif berbasis Streamlit sebagai antarmuka pengguna
- Menerapkan kolaborasi tim menggunakan GitHub dengan alur kerja yang terstruktur

---

## 📊 Dataset

- **Sumber:** [World Bank Open Data](https://data.worldbank.org)
- **Rentang Tahun:** 1991–2024 (~34 baris data tahunan)
- **Target (Y):** GDP Growth Indonesia (% per tahun)

### Variabel yang Digunakan

| Variabel              | Deskripsi                                            | Sumber Data                                                                                                                  |
| --------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **GDP Growth**        | Target — Pertumbuhan ekonomi Indonesia (% per tahun) | [NY.GDP.MKTP.KD.ZG (GDP Growth)](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=ID&utm_source=chatgpt.com) |
| **Inflation**         | Tingkat inflasi tahunan (%)                          | [FP.CPI.TOTL.ZG (Inflation CPI)](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=ID&utm_source=chatgpt.com)    |
| **Unemployment**      | Tingkat pengangguran (% dari angkatan kerja)         | [SL.UEM.TOTL.ZS (Unemployment)](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?locations=ID&utm_source=chatgpt.com)     |
| **Population Growth** | Pertumbuhan populasi tahunan (%)                     | [SP.POP.GROW (Population Growth)](https://data.worldbank.org/indicator/SP.POP.GROW?locations=ID&utm_source=chatgpt.com)      |
| **Exports**           | Nilai ekspor barang dan jasa (% dari GDP)            | [NE.EXP.GNFS.ZS (Exports)](https://data.worldbank.org/indicator/NE.EXP.GNFS.ZS?locations=ID&utm_source=chatgpt.com)          |
| **Imports**           | Nilai impor barang dan jasa (% dari GDP)             | [NE.IMP.GNFS.ZS (Imports)](https://data.worldbank.org/indicator/NE.IMP.GNFS.ZS?locations=ID&utm_source=chatgpt.com)          |
| **FDI**               | Foreign Direct Investment (% dari GDP)               | [BX.KLT.DINV.WD.GD.ZS (FDI)](https://data.worldbank.org/indicator/BX.KLT.DINV.WD.GD.ZS?locations=ID&utm_source=chatgpt.com)  |
| **Exchange Rate**     | Nilai tukar Rupiah terhadap USD                      | [PA.NUS.FCRF (Exchange Rate)](https://data.worldbank.org/indicator/PA.NUS.FCRF?locations=ID&utm_source=chatgpt.com)          |


---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|-----------|----------|
| Python 3.10 | Bahasa pemrograman utama |
| Pandas & NumPy | Manipulasi dan analisis data |
| Scikit-learn | Pemodelan Machine Learning |
| Matplotlib & Seaborn | Visualisasi statis |
| Plotly | Visualisasi interaktif |
| Streamlit | Framework website interaktif |
| Joblib | Menyimpan dan memuat model |
| GitHub | Version control & kolaborasi |

---

## 🌐 Website Streamlit

Website interaktif terdiri dari 5 halaman:

| Halaman | Deskripsi |
|---------|-----------|
| 🏠 Home | Penjelasan proyek, tujuan, panduan penggunaan |
| 📂 Dataset | Tabel data, statistik deskriptif, kamus data |
| 📈 Visualisasi | Grafik interaktif: tren GDP, korelasi, distribusi |
| 🔮 Prediksi GDP | Form input indikator, output prediksi + visualisasi |
| 📝 Kesimpulan | Rangkuman temuan, evaluasi model, rekomendasi |

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python 3.10 atau lebih baru
- Git

### 1. Clone repo
```bash
git clone [https://github.com/daifa-maulana/Kelompok1-ML.git](https://github.com/daifa-maulana/Kelompok1-ML.git)
cd Kelompok1-ML

```

### 2. Install dependencies

```bash
pip install -r requirements.txt

```

### 3. Jalankan Streamlit

```bash
streamlit run app.py

```

### 4. Buka di browser

```
http://localhost:8501

```

---

## 📁 Struktur Folder

```text
Kelompok1-ML/
├── data/
│   ├── raw/                    ← Data mentah CSV dari World Bank
│   └── processed/              ← Dataset final siap pakai
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing.ipynb
│   └── 04_modeling.ipynb
├── models/
│   ├── best_model.pkl          ← Model terbaik
│   ├── scaler.pkl              ← Objek scaler
│   └── model_report.json       ← Laporan performa model
├── gdp_prediction_indonesia/   ← Module utama Python
│   ├── config.py
│   ├── dataset.py
│   ├── features.py
│   ├── plots.py
│   └── modeling/
│       ├── train.py
│       └── predict.py
├── pages/                      ← Halaman Streamlit
│   ├── 01_Home.py
│   ├── 02_Dataset.py
│   ├── 03_Visualisasi.py
│   ├── 04_Prediksi.py
│   └── 05_Kesimpulan.py
├── reports/                    ← Laporan dan visualisasi
├── references/                 ← Referensi dan jurnal
├── docs/
│   ├── data_dictionary.md
│   ├── data_quality_report.md
│   ├── laporan_akhir.md
│   └── meeting_notes/          ← Notulen rapat mingguan
├── presentation/
│   └── slide_presentasi.pptx
├── app.py                      ← Entry point Streamlit
├── requirements.txt
├── README.md
└── CONTRIBUTING.md

```

---

## 🌿 Struktur Branch

| Branch                  | Fungsi                                                          |
| ----------------------- | --------------------------------------------------------------- |
| `main`                  | Branch utama (rilis final)                                      |
| `develop`               | Branch integrasi seluruh fitur                                  |
| `feature/data-analysis` | Pengumpulan data, EDA, preprocessing, dan analisis data         |
| `feature/ui-ux`         | Wireframe, desain UI, dan prototipe Streamlit                   |
| `feature/frontend`      | Implementasi tampilan Streamlit berdasarkan desain UI/UX        |
| `feature/backend`       | Integrasi model Machine Learning, prediksi, dan pengolahan data |


---

## 📜 Mata Kuliah

Machine Learning — 2025/2026

```

```
