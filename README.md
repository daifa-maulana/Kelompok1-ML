# 🇮🇩 GDP Prediction Indonesia — Machine Learning

Prediksi laju pertumbuhan ekonomi (GDP Growth) Indonesia menggunakan indikator ekonomi makro dari World Bank Open Data.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![GitHub](https://img.shields.io/badge/GitHub-Collaboration-black)

---

## 👥 Tim Kelompok 1

| No | Nama | Peran | Branch |
|----|------|-------|--------|
| 1  | Daifa Maulana | Project Manager & GitHub Manager | `main` / `develop` |
| 2  | Mochamad Firmansyah | Data Collection & Dataset Management | `feature/data-collection` |
| 3  | Fajar Muhammad Ramdhani | EDA & Visualisasi | `feature/eda-visualization` |
| 4  | Fauzi Rizky Maulana | Data Preparation & Preprocessing | `feature/preprocessing` |
| 5  | Muhammad Raufan Umarulloh | Machine Learning Engineer | `feature/modeling` |
| 6  | Nazwa Nur Hapidah | UI/UX & Streamlit Frontend | `feature/streamlit-ui` |
| 7  | Dini Sriastuti | Backend Streamlit & Deployment | `feature/streamlit-backend` |

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

| Variabel | Keterangan | Satuan |
|----------|------------|--------|
| GDP Growth | Pertumbuhan ekonomi Indonesia | % per tahun |
| Inflation | Tingkat inflasi tahunan | % |
| Unemployment | Tingkat pengangguran | % dari angkatan kerja |
| Population Growth | Pertumbuhan populasi tahunan | % |
| Exports | Nilai ekspor barang dan jasa | % dari GDP |
| Imports | Nilai impor barang dan jasa | % dari GDP |
| FDI | Foreign Direct Investment | % dari GDP |
| Exchange Rate | Nilai tukar Rupiah terhadap USD | IDR/USD |

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

| Branch | Fungsi |
| --- | --- |
| `main` | Branch utama — hanya kode final via Pull Request |
| `develop` | Branch integrasi semua fitur |
| `feature/data-collection` | Pengumpulan dan validasi data |
| `feature/eda-visualization` | EDA dan visualisasi |
| `feature/preprocessing` | Preprocessing dan normalisasi |
| `feature/modeling` | Training dan evaluasi model ML |
| `feature/streamlit-ui` | Desain dan layout halaman Streamlit |
| `feature/streamlit-backend` | Integrasi model dan deployment |

---

## 📜 Mata Kuliah

Machine Learning — 2025/2026

```

```
