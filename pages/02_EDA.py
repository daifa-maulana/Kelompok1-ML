import streamlit as st
import pandas as pd
from utils.navigation import show_navbar
from scripts.visualization import (
    plot_gdp_trend,
    plot_country_comparison,
    plot_correlation_heatmap
)

st.set_page_config(
    page_title="EDA — GDP ASEAN",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_navbar()

# with open("assets/style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# CSS sementara - tunggu Nazwa push style.css kalo udah hapus try ini sampe pass yang diatas hapus pagar nya
try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

st.title("📊 Exploratory Data Analysis")
st.markdown("Eksplorasi data GDP Growth negara-negara ASEAN dari tahun 1990–2024.")
st.markdown("---")

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/dataset_asean.csv")

df = load_data()

st.subheader("📋 Overview Dataset")
col1, col2, col3 = st.columns(3)
col1.metric("Total Baris", f"{len(df):,}")
col2.metric("Jumlah Negara", df["Country"].nunique())
col3.metric("Rentang Tahun", f"{int(df['Year'].min())}–{int(df['Year'].max())}")

st.markdown("---")
st.subheader("🔍 Filter Data")

negara_list      = sorted(df["Country"].unique().tolist())
selected_country = st.selectbox(
    "Pilih Negara ASEAN:",
    options=["Semua Negara"] + negara_list
)

df_filtered = (
    df[df["Country"] == selected_country].copy()
    if selected_country != "Semua Negara"
    else df.copy()
)

st.markdown("---")
st.subheader("📄 Tabel Data")

with st.expander("Lihat Tabel Data", expanded=False):
    st.dataframe(df_filtered, use_container_width=True)
    st.caption(f"Menampilkan {len(df_filtered):,} baris")

st.markdown("---")
st.subheader("📈 Statistik Deskriptif")

tab1, tab2 = st.tabs(["Overall", "Per Negara"])

with tab1:
    st.dataframe(df_filtered.describe().round(3), use_container_width=True)

with tab2:
    fitur_cols = ["GDP_Growth", "GDP_Per_Capita", "Population_Growth",
                  "Exports_pct", "Imports_pct", "Life_Expectancy"]
    available  = [c for c in fitur_cols if c in df.columns]
    st.dataframe(
        df.groupby("Country")[available].mean().round(3),
        use_container_width=True
    )

st.markdown("---")
st.subheader("📊 Visualisasi")

country_param = None if selected_country == "Semua Negara" else selected_country

st.markdown("#### Tren GDP Growth")
plot_gdp_trend(df, country=country_param)

if selected_country == "Semua Negara":
    st.markdown("#### Perbandingan Antar Negara")
    plot_country_comparison(df, countries=negara_list, metric="GDP_Growth")

st.markdown("#### Heatmap Korelasi")
plot_correlation_heatmap(df_filtered)

st.markdown("#### Scatter Plot Fitur vs GDP Growth")
fitur_scatter     = ["GDP_Per_Capita", "Life_Expectancy", "Exports_pct", "Imports_pct"]
available_scatter = [f for f in fitur_scatter if f in df.columns]
if available_scatter:
    selected_fitur = st.selectbox("Pilih Fitur:", available_scatter)