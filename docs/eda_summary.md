# Ringkasan Analisis Hubungan Fitur Makroekonomi ASEAN terhadap GDP Growth

Berdasarkan hasil Exploratory Data Analysis (EDA) terhadap 10 negara ASEAN dari tahun 2015 hingga 2024, berikut adalah poin penting yang ditemukan:

## 1. Tren Pertumbuhan GDP (GDP Growth)
* Negara berkembang di ASEAN (seperti Kamboja, Laos, Myanmar, dan Vietnam) menunjukkan rata-rata persentase pertumbuhan tahunan yang cenderung lebih tinggi dan agresif (berada di kisaran 5% - 7.5%).
* Negara dengan ekonomi yang sudah sangat matang/maju seperti Singapura dan Brunei memiliki tren persentase pertumbuhan GDP yang lebih rendah namun cenderung stabil (berada di kisaran 1% - 3.5%).

## 2. Karakteristik Unik & Outlier (Hasil Boxplot)
* Melalui analisis sebaran data, ditemukan variasi kontras pada fitur `GDP_Per_Capita` dan `Life_Expectancy`. 
* Singapura dan Brunei bertindak sebagai pencilan (*outlier*) positif yang sangat masif dalam hal GDP per kapita (mencapai angka $35,000 - $65,000) serta memiliki angka harapan hidup (*Life Expectancy*) tertinggi, memisahkan diri secara signifikan dari klaster 8 negara ASEAN lainnya.

## 3. Hubungan Antar Fitur (Hasil Scatter & Heatmap)
* Aktivitas perdagangan internasional (`Exports_pct` dan `Imports_pct`) menunjukkan pola korelasi yang searah di sebagian besar wilayah regional ASEAN.
* Nilai `GDP_Per_Capita` yang tinggi tidak selalu berkorelasi lurus dengan lonjakan persentase `GDP_Growth` tahunan, mengingat kapasitas ekspansi ekonomi negara berkembang jauh lebih fluktuatif dibanding negara maju.