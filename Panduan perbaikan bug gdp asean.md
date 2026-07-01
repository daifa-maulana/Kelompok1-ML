# Panduan UAS Praktikum Orange Data Mining
## Klasifikasi: Deteksi HOAX vs FAKTA (Naive Bayes) — Studi Kasus Berita Corona

---

## 1. Ringkasan Dataset

| File | Baris | Kolom | Keterangan |
|---|---|---|---|
| `training_klasifikasi_nb.xlsx` | 134 | id, claim, label | Data latih. Label: FAKTA (124) / HOAX (10) |
| `testing_klasifikasi_nb.xls` | 351 | id, claim | Data uji, **belum ada label** — ini yang akan diprediksi modelnya |

**Kolom penting:**
- `claim` → teks judul berita (dipakai sebagai fitur/text)
- `label` → kelas target (FAKTA / HOAX), hanya ada di data training

---

## 2. Langkah-Langkah di Orange Data Mining

### A. Persiapan Add-on
1. Buka Orange Data Mining → buat **New file/Workflow**.
2. Klik **Options → Add-ons**.
3. Centang **Text** (dan **Text Mining**/Textable jika muncul terpisah).
4. Klik **OK**, biarkan Orange restart. Setelah restart akan muncul kategori widget **Text Mining** di sidebar kiri.

### B. Load Data (Corpus)
5. Tambahkan 2 widget **Corpus** dari kategori Text Mining.
   - Rename widget pertama jadi **training_corpus**
   - Rename widget kedua jadi **testing_corpus**
6. Double click **training_corpus** → Load file → pilih `training_klasifikasi_nb.xlsx`.
   - Pastikan kolom **claim** diset sebagai **Text feature**.
   - Pastikan kolom **label** diset sebagai **Target/Class variable** (biasanya lewat opsi "used as class").
7. Double click **testing_corpus** → Load file → pilih `testing_klasifikasi_nb.xls`.
   - Set kolom **claim** sebagai Text feature (tidak ada label, jadi biarkan tanpa class).

### C. Corpus Viewer (opsional tapi disarankan sesuai modul)
8. Tambahkan 2 widget **Corpus Viewer**, rename jadi **cviewer_training** dan **cviewer_testing**.
9. Hubungkan `training_corpus → cviewer_training` dan `testing_corpus → cviewer_testing`.
10. Buka masing-masing viewer, tekan **Ctrl+A** untuk select all data (menandakan semua data dipakai).

### D. Preprocessing
11. Tambahkan 2 widget **Preprocess Text**, rename jadi **preprocess_training** dan **preprocess_testing**.
12. Hubungkan `cviewer_training → preprocess_training` dan `cviewer_testing → preprocess_testing`.
13. Di kedua widget, set **Stopwords** ke **Indonesian** (karena teks berbahasa Indonesia).
14. Aktifkan langkah standar lain jika tersedia: lowercase, tokenization (default biasanya sudah cukup).

### E. Representasi Fitur (Bag of Words)
15. Tambahkan widget **Bag of Words**.
16. Hubungkan `preprocess_training → Bag of Words`.
17. Tambahkan widget **Select Columns**, hubungkan `Bag of Words → Select Columns`.
    - Widget ini untuk memastikan atribut fitur teks dan target `label` terpasang benar di domain data training.

### F. Modeling
18. Tambahkan widget **Naive Bayes** (kategori Model).
19. Hubungkan `Select Columns → Naive Bayes`.

### G. Prediksi & Evaluasi
20. Tambahkan widget **Predictions**.
    - Hubungkan `Naive Bayes → Predictions` dan `preprocess_testing → Predictions`.
    - Double click **Predictions** untuk melihat hasil prediksi tiap judul berita di data testing (FAKTA/HOAX).
21. Tambahkan widget **Test and Score**.
    - Hubungkan `Naive Bayes → Test and Score` dan `Select Columns → Test and Score`.
    - Double click untuk melihat metrik akurasi, precision, recall, F1 model pada data training (cross-validation).

> Catatan: Karena data testing tidak berlabel, **Test and Score** (yang butuh label ground-truth) dijalankan di atas data training (cross-validation), sedangkan **Predictions** dipakai untuk melihat hasil prediksi label di data testing yang belum diketahui jawabannya.

---

## 3. Interpretasi Hasil (isi setelah kamu jalankan)

Saat rekam video, jelaskan:
- Berapa **akurasi** model dari Test and Score (misal: "akurasi model 92%")
- Contoh 2-3 prediksi dari widget Predictions (judul berita apa diprediksi HOAX/FAKTA)
- Catatan: dataset training timpang (124 FAKTA vs 10 HOAX) — sebutkan ini sebagai potensi bias model condong memprediksi FAKTA.

---

## 4. Naskah Video (5–15 menit)

**[00:00–00:45] Pembukaan (wajah harus tampil di kamera)**
> "Assalamualaikum/Halo, perkenalkan saya [Nama], NIM [NIM], dari kelas [Kelas]. Video ini adalah tugas UAS Praktikum mata kuliah Data Mining dengan dosen pengampu Ibu Tarsinah Sumarni, S.Kom., M.Kom. Pada video ini saya akan mendemonstrasikan proses klasifikasi menggunakan algoritma Naive Bayes di Orange Data Mining, dengan studi kasus deteksi berita HOAX vs FAKTA seputar virus corona."

**[00:45–01:30] Penjelasan Dataset**
> "Dataset yang saya gunakan terdiri dari dua bagian: data training berisi 134 judul berita yang sudah diberi label FAKTA atau HOAX, dan data testing berisi 351 judul berita yang belum diberi label, yang nantinya akan diprediksi oleh model."

**[01:30–08:00] Demo Langkah di Orange (ikuti urutan Bagian 2 di atas)**
> Jelaskan tiap widget sambil menunjukkan layar: install add-on Text → load Corpus → Corpus Viewer → Preprocess Text (stopword Indonesia) → Bag of Words → Select Columns → Naive Bayes → Predictions → Test and Score.
> Untuk tiap widget, sebutkan singkat fungsinya sebelum klik (contoh: "Widget Preprocess Text ini saya gunakan untuk membersihkan teks dari stopword bahasa Indonesia, supaya kata-kata umum tidak mengganggu proses klasifikasi").

**[08:00–09:30] Hasil dan Evaluasi**
> "Berdasarkan Test and Score, model Naive Bayes ini memiliki akurasi sebesar [isi angka]%. Kita bisa melihat juga contoh hasil prediksi pada data testing, misalnya judul berita '[contoh judul]' diprediksi sebagai [FAKTA/HOAX]."

**[09:30–10:00] Penutup**
> "Demikian demonstrasi klasifikasi Naive Bayes menggunakan Orange Data Mining yang saya lakukan. Terima kasih telah menyaksikan, mohon maaf jika ada kekurangan. Wassalamualaikum warahmatullahi wabarakatuh."

---

## 5. Checklist Sebelum Submit

- [ ] Wajah tampil selama video (bukan hanya suara)
- [ ] Durasi 5–15 menit
- [ ] Upload ke YouTube/Google Drive, akses "dapat dilihat" (bukan private)
- [ ] Buat file PDF berisi link video, submit ke E-Learning sesuai jadwal UAS
