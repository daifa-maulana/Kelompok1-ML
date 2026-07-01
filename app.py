import streamlit as st
import pandas as pd
import json
from utils.navigation import show_navbar

st.set_page_config(
    page_title="Prediksi GDP Growth Asia Tenggara",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_navbar()

try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

st.title("🌏 Prediksi GDP Growth Asia Tenggara")
st.markdown("Dashboard analisis dan prediksi pertumbuhan ekonomi negara-negara ASEAN.")
st.markdown("---")

try:
    @st.cache_data
    def load_data():
        return pd.read_csv("data/processed/dataset_asean.csv")

    @st.cache_data
    def load_report():
        with open("models/model_report.json") as f:
            return json.load(f)

    df     = load_data()
    report = load_report()
    DATA_READY = True
except FileNotFoundError:
    DATA_READY = False
    st.warning("⚠️ Menunggu dataset_asean.csv dari Mochamad dan model_report.json dari Dini")

if DATA_READY:
    st.subheader("📈 Ringkasan Dataset & Model")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📋 Total Observasi", f"{len(df):,}")
    with col2:
        st.metric("🌍 Jumlah Negara", df["Country"].nunique())
    with col3:
        st.metric("🤖 Jumlah Model", "4")
    with col4:
        st.metric("🏆 Model Terbaik", report.get("best_model", "N/A"))

    st.markdown("---")
    st.subheader("🗺️ Negara yang Tercakup")

    countries = df["Country"].unique().tolist()
    cols = st.columns(5)
    for i, country in enumerate(countries):
        cols[i % 5].success(f"✅ {country}")

    st.markdown("---")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info(f"📅 Rentang Tahun: {int(df['Year'].min())} – {int(df['Year'].max())}")
    with col_b:
        st.info("📊 Jumlah Fitur Model: 8 fitur ASEAN")