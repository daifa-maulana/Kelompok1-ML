import pandas as pd
import numpy as np
import os

# =====================================================================
# KONSTANTA: 8 Fitur ASEAN + Target
# =====================================================================
FEATURES = [
    'GDP_Per_Capita',
    'Population_Growth',
    'Exports_pct',
    'Imports_pct',
    'Life_Expectancy',
    'GDP_Growth_lag1',
    'GDP_Growth_lag2',
    'GDP_lag1'
]
TARGET = 'GDP_Growth'


# =====================================================================
# FUNGSI 1: handle_missing — Interpolasi per Negara
# =====================================================================
def handle_missing(df):
    """
    Mengisi nilai yang hilang (missing values) menggunakan interpolasi linear,
    dilakukan per kelompok negara agar tidak bocor lintas negara.
    """
    df_clean = df.copy()

    # 1. Urutkan berdasarkan negara dan tahun
    df_clean = df_clean.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    # 2. Kolom numerik yang perlu diinterpolasi
    numeric_cols = [
        'GDP_Growth',
        'GDP_Per_Capita',
        'Population_Growth',
        'Exports_pct',
        'Imports_pct',
        'Life_Expectancy'
    ]

    # 3. Paksa tipe data jadi numerik (teks '..' atau kosong → NaN)
    for col in numeric_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

    # 4. Interpolasi per negara — tanpa groupby agar Country tidak hilang
    #    Loop per negara lebih aman dari pada groupby().apply() yang bisa drop kolom
    results = []
    for country, group in df_clean.groupby('Country', sort=False):
        cols_in_group = [c for c in numeric_cols if c in group.columns]
        group = group.copy()
        group[cols_in_group] = group[cols_in_group].interpolate(
            method='linear', limit_direction='both'
        )
        results.append(group)

    df_clean = pd.concat(results).reset_index(drop=True)

    return df_clean


# =====================================================================
# FUNGSI 2: add_lag_features — Fitur Lag per Negara
# =====================================================================
def add_lag_features(df):
    """
    Membuat fitur pergeseran waktu (lag) per negara menggunakan groupby + shift.
    - GDP_Growth_lag1 : GDP_Growth tahun sebelumnya (t-1)
    - GDP_Growth_lag2 : GDP_Growth dua tahun sebelumnya (t-2)
    - GDP_lag1        : GDP_Per_Capita tahun sebelumnya (t-1)
    """
    df_lag = df.copy()

    # Urutkan agar shift bekerja benar per negara
    df_lag = df_lag.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_lag['GDP_Growth_lag1'] = df_lag.groupby('Country')['GDP_Growth'].shift(1)
    df_lag['GDP_Growth_lag2'] = df_lag.groupby('Country')['GDP_Growth'].shift(2)
    df_lag['GDP_lag1']        = df_lag.groupby('Country')['GDP_Per_Capita'].shift(1)

    return df_lag


# =====================================================================
# FUNGSI 3: preprocess_data — Pipeline Utama
# =====================================================================
def preprocess_data(input_path, output_path):
    """
    Pipeline utama preprocessing data ASEAN.
    Langkah: baca → tangani missing → tambah lag → drop NaN → simpan → return df
    """

    # --- LANGKAH 1: Baca data mentah ---
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File input tidak ditemukan: {input_path}")

    print(f"Membaca data mentah dari: {input_path}")
    df = pd.read_csv(input_path)
    print(f"  Shape awal          : {df.shape[0]} baris x {df.shape[1]} kolom")

    # --- LANGKAH 2: Tangani missing values per negara ---
    print("  Menangani missing values (interpolasi per negara)...")
    df = handle_missing(df)
    print(f"  Kolom setelah handle_missing: {df.columns.tolist()}")  # debug

    # --- LANGKAH 3: Tambahkan fitur lag ---
    print("  Membuat fitur lag (lag1, lag2)...")
    df = add_lag_features(df)

    # --- LANGKAH 4: Hapus baris NaN sisa lag di awal tiap negara ---
    rows_before = len(df)
    df = df.dropna(subset=FEATURES + [TARGET])
    rows_dropped = rows_before - len(df)
    print(f"  Baris dihapus (NaN lag awal): {rows_dropped}")
    print(f"  Shape akhir         : {df.shape[0]} baris x {df.shape[1]} kolom")

    # --- LANGKAH 5: Simpan hasil ke folder processed ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"  Data berhasil disimpan ke: {output_path}")

    return df