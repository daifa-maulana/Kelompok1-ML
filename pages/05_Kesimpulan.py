import streamlit as st
import json
import pandas as pd
from utils.navigation import show_navbar

st.set_page_config(
    page_title="Kesimpulan — GDP ASEAN",
    page_icon="📝",
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

st.title("📝 Kesimpulan")
st.markdown("---")

try:
    with open("models/model_report.json") as f:
        report = json.load(f)
except:
    report = {}
    st.warning("⚠️ model_report.json tidak ditemukan")

st.subheader("📌 Ringkasan Proyek")
st.markdown("""
Proyek ini menganalisis dan memprediksi **GDP Growth negara-negara ASEAN**
menggunakan pendekatan Machine Learning berbasis data historis dari World Bank.

Model dilatih menggunakan data dari **9 negara ASEAN**: Indonesia, Malaysia,
Singapura, Thailand, Filipina, Vietnam, Myanmar, Kamboja, dan Laos —
mencakup rentang tahun **1990–2024**.
""")

st.subheader("🤖 Perbandingan Performa Model")
if report:
    models_data = report.get("models", {})
    if models_data:
        df_report = pd.DataFrame(models_data).T
        st.dataframe(df_report, use_container_width=True)
    best = report.get("best_model", "N/A")
    st.success(f"🏆 Model Terbaik: {best}")

st.subheader("📋 Catatan")
st.info("""
- Model dilatih pada data 9 negara ASEAN
- Menggunakan 8 fitur: GDP Per Kapita, Population Growth, Exports (% GDP),
  Imports (% GDP), Life Expectancy, dan 3 lag features
- Evaluasi: Time-Series Split 80/20 per negara + KFold 5-fold
- Sumber data: World Bank Open Data
""")