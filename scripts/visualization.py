import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_gdp_trend(df, country=None):
    """
    Menampilkan tren GDP Growth untuk negara spesifik atau rata-rata ASEAN.
    """
    plt.figure(figsize=(12, 6))
    if country:
        df_filtered = df[df['country'].str.lower() == country.lower()]
        if df_filtered.empty:
            print(f"[⚠️ WARNING] Negara '{country}' tidak ditemukan.")
            return
        sns.lineplot(data=df_filtered, x='Year', y='GDP_Growth', marker='o', linewidth=2.5, color='dodgerblue')
        plt.title(f'Tren Perkembangan GDP Growth - {country.title()}', fontsize=14, fontweight='bold')
    else:
        df_avg = df.groupby('Year')['GDP_Growth'].mean().reset_index()
        sns.lineplot(data=df_avg, x='Year', y='GDP_Growth', marker='s', linewidth=2.5, color='crimson')
        plt.title('Tren Rata-Rata GDP Growth Keseluruhan Negara ASEAN', fontsize=14, fontweight='bold')

    plt.xlabel('Tahun')
    plt.ylabel('GDP Growth (%)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    return plt.gcf()

def plot_country_comparison(df, country_list, metric='GDP_Growth'):
    """
    Fungsi perbandingan antar negara berdasarkan metrik pilihan terbaru.
    """
    df_filtered = df[df['country'].isin(country_list)]
    if df_filtered.empty:
        print("[⚠️ WARNING] Tidak ada negara dari list yang cocok.")
        return

    plt.figure(figsize=(14, 7))
    sns.lineplot(
        data=df_filtered, 
        x='Year', 
        y=metric, 
        hue='country', 
        marker='o', 
        linewidth=2.5,
        palette='tab10'
    )

    plt.title(f'Analisis Perbandingan {metric} Antar Negara ASEAN', fontsize=14, fontweight='bold')
    plt.xlabel('Tahun')
    plt.ylabel(metric)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(title='Negara', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    return plt.gcf()

def plot_correlation_heatmap(df):
    """
    Heatmap Korelasi menggunakan daftar fitur makroekonomi terbaru.
    """
    fitur_makro_baru = ['GDP_Growth', 'Inflation', 'Unemployment', 'Population_Growth', 'Exports', 'Imports', 'FDI', 'Exchange_Rate']
    fitur_tersedia = [col for col in fitur_makro_baru if col in df.columns]

    if len(fitur_tersedia) < 2:
        print("[⚠️ INFO] Fitur tidak mencukupi untuk menghitung korelasi.")
        return

    corr = df[fitur_tersedia].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(11, 9))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r', center=0, square=True, linewidths=0.5, ax=ax)
    ax.set_title('Heatmap Korelasi Antar Variabel Makroekonomi ASEAN (Revisi)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig
