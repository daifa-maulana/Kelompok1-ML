# Panduan Upload File Per Anggota

Dokumen ini menjelaskan file yang harus di-upload oleh setiap anggota, nama branch yang harus dipakai, dan langkah lengkap dari clone sampai membuat PR. Gunakan format commit `gitmoji` untuk konsistensi.

---

## Aturan Umum

- Jangan push langsung ke `main`.
- Setiap anggota bekerja di branch miliknya: `feature/<nama>-<task>` atau sesuai tabel di bawah.
- Commit harus menggunakan gitmoji (contoh: `✨ feat: ...`, `📝 docs: ...`).
- Setelah push, buat Pull Request ke `main` dan minta minimal 1 review.

---

## Langkah Umum (copyable)

```bash
git clone https://github.com/daifa-maulana/Kelompok1-ML.git
cd Kelompok1-ML
git checkout -b feature/<nama>-<task>
# tambahkan file/ubah sesuai jobdes
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

## Tugas dan Nama Branch Per Anggota

1. Mochamad Firmansyah — (Data Analyst & ML)
- Branch: `feature/mochamad-data`
- Upload/kerjakan:
  - `notebooks/03_preprocessing.ipynb` (hasil preprocessing)
  - `scripts/preprocessing.py` (fungsi preprocessing jika ada perubahan)
  - `data/processed/<nama_file>.csv` (hasil yang dibersihkan)
  - `models/<model_name>.pkl` (opsional, hasil training)

2. Fauzi Rizky Maulana — (Data Analyst & ML)
- Branch: `feature/fauzi-eda`
- Upload/kerjakan:
  - `notebooks/02_eda.ipynb` (analisis EDA)
  - `data/eda_outputs/<fig>.png` (grafik hasil EDA)
  - `scripts/visualization.py` (jika membuat fungsi visualisasi)

3. Dini Sriastuti — (Data Analyst & ML)
- Branch: `feature/dini-modeling`
- Upload/kerjakan:
  - `notebooks/04_modeling.ipynb` (experimen model)
  - `models/<model_name>.pkl` (model final)
  - `models/model_report.json` (report hasil evaluasi)

4. Nazwa Nur Hapidah — (UI/UX Designer)
- Branch: `feature/nazwa-design`
- Upload/kerjakan:
  - `assets/style.css` (style baru)
  - `docs/wireframe/<nama_file>.png` atau `.svg`
  - update `docs/design_guide.md` (opsional)

5. Muhammad Raufan Umarulloh — (Frontend Developer)
- Branch: `feature/raufan-frontend`
- Upload/kerjakan:
  - `pages/<page>.py` (perbaikan atau halaman baru di Streamlit)
  - `utils/navigation.py` (penyesuaian navigasi jika perlu)

6. Fajar Muhammad Ramdhani — (Backend & Deployment)
- Branch: `feature/fajar-deploy`
- Upload/kerjakan:
  - `scripts/train_models.py` (script training/CI hooks)
  - `utils/predictor.py` (API / inference helper)
  - `docs/DEPLOY_GUIDE.md` (update langkah deploy / Docker)

---

## Contoh Pesan Commit (gitmoji)

- `✨ feat: add preprocessing notebook`
- `📝 docs: update deploy guide`
- `🐛 fix: correct prediction bug`
- `🎨 style: update CSS layout`

---

## Review & Merge

- Buat PR ke `main` dengan deskripsi lengkap (apa yang diubah, file utama, langkah reproducible).
- Minta reviewer: paling tidak 1 approval dari tim.
- Pastikan CI (jika ada) lulus sebelum merge.

---

Jika mau, saya bisa generate pesan PR template singkat untuk tiap tugas atau menambahkan checklist ke `PULL_REQUEST_TEMPLATE.md`.
