import streamlit as st
import json
from utils.navigation import show_navbar

st.set_page_config(
    page_title="Prediksi — GDP ASEAN",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_navbar()

try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

st.title("🤖 Prediksi GDP Growth")
st.markdown("Masukkan indikator ekonomi untuk prediksi dari 4 model sekaligus.")
st.markdown("---")

try:
    with open("models/features.json") as f:
        FEATURES = json.load(f)
except FileNotFoundError:
    st.warning("⚠️ Menunggu models/features.json dari Dini")
    st.stop()

try:
    from utils.predictor import predict_all_models
    PREDICTOR_READY = True
except ImportError:
    PREDICTOR_READY = False

st.subheader("📝 Input Indikator Ekonomi")

col1, col2 = st.columns(2)

with col1:
    gdp_per_kapita    = st.number_input("GDP Per Kapita (USD)",       min_value=0.0,   max_value=100000.0, value=5000.0,  step=100.0)
    population_growth = st.number_input("Population Growth (%)",      min_value=-5.0,  max_value=10.0,     value=1.5,     step=0.1)
    exports_pct       = st.number_input("Exports (% of GDP)",         min_value=0.0,   max_value=200.0,    value=30.0,    step=1.0)
    imports_pct       = st.number_input("Imports (% of GDP)",         min_value=0.0,   max_value=200.0,    value=28.0,    step=1.0)

with col2:
    life_expectancy   = st.number_input("Life Expectancy (tahun)",    min_value=40.0,  max_value=90.0,     value=70.0,    step=0.5)
    gdp_growth_lag1   = st.number_input("GDP Growth Lag-1 (%)",       min_value=-20.0, max_value=20.0,     value=3.0,     step=0.1)
    gdp_growth_lag2   = st.number_input("GDP Growth Lag-2 (%)",       min_value=-20.0, max_value=20.0,     value=3.5,     step=0.1)
    gdp_lag1          = st.number_input("GDP Per Kapita Lag-1 (USD)", min_value=0.0,   max_value=100000.0, value=4800.0,  step=100.0)

input_mapping = {
    "GDP_Per_Capita":    gdp_per_kapita,
    "Population_Growth": population_growth,
    "Exports_pct":       exports_pct,
    "Imports_pct":       imports_pct,
    "Life_Expectancy":   life_expectancy,
    "GDP_Growth_lag1":   gdp_growth_lag1,
    "GDP_Growth_lag2":   gdp_growth_lag2,
    "GDP_lag1":          gdp_lag1
}
input_values = [input_mapping[f] for f in FEATURES]

st.markdown("---")

if st.button("🚀 Prediksi Sekarang", use_container_width=True, type="primary"):

    if not PREDICTOR_READY:
        st.warning("⚠️ Menunggu predictor.py dari Fajar")
        st.stop()

    with st.spinner("Menjalankan 4 model..."):
        try:
            results = predict_all_models(input_values)
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

    st.markdown("---")
    st.subheader("🎯 Hasil Prediksi GDP Growth")

    icons = {
        "Linear Regression": "📏",
        "Ridge":             "🔷",
        "Decision Tree":     "🌳",
        "Random Forest":     "🌲"
    }

    cols = st.columns(4)
    for i, (model_name, prediction) in enumerate(results.items()):
        if model_name == "best_model":
            continue
        with cols[i % 4]:
            st.metric(label=f"{icons.get(model_name, '🤖')} {model_name}", value=f"{prediction:.2f}%")

    if "best_model" in results:
        best = results["best_model"]
        st.success(f"🏆 Model Terbaik: {best} → {results[best]:.2f}%")

    with st.expander("🔍 Debug — Input yang Digunakan"):
        st.dataframe({f: [v] for f, v in zip(FEATURES, input_values)})