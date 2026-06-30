import streamlit as st
import pandas as pd

try:
    from streamlit_echarts import st_echarts
    ECHARTS_OK = True
except ImportError:
    ECHARTS_OK = False

from utils.navigation import show_navbar
from utils.world_data import load_asean_data, get_map_data, get_country_list

st.set_page_config(
    page_title="Analisis ASEAN — GDP ASEAN",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

show_navbar()

try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

st.title("🌍 Analisis ASEAN")
st.markdown("Peta interaktif dan forecasting GDP Growth negara-negara ASEAN.")
st.markdown("---")

try:
    @st.cache_data
    def get_data():
        return load_asean_data()
    df        = get_data()
    countries = get_country_list(df)
except FileNotFoundError:
    st.warning("⚠️ Menunggu dataset_asean.csv dari Mochamad")
    st.stop()

st.subheader("🗺️ Peta GDP Growth ASEAN")

year_min      = int(df["Year"].min())
year_max      = int(df["Year"].max())
selected_year = st.slider("Pilih Tahun:", min_value=year_min, max_value=year_max, value=2020)

if ECHARTS_OK:
    map_data = get_map_data(df, selected_year)
    options  = {
        "backgroundColor": "#0D1117",
        "title": {"text": f"GDP Growth ASEAN — {selected_year}", "textStyle": {"color": "#E6EDF3"}},
        "tooltip": {"trigger": "item", "formatter": "{b}: {c}%"},
        "visualMap": {
            "min": -10, "max": 15,
            "text": ["Tinggi", "Rendah"],
            "realtime": False, "calculable": True,
            "inRange": {"color": ["#313695", "#4F8EF7", "#00D4AA", "#FFB347"]}
        },
        "series": [{
            "name": "GDP Growth (%)", "type": "map", "map": "world",
            "roam": True, "emphasis": {"label": {"show": True}},
            "data": map_data
        }]
    }
    st_echarts(options=options, height="500px")
else:
    st.warning("⚠️ Install dulu: pip install streamlit-echarts")
    df_year = df[df["Year"] == selected_year][["Country", "GDP_Growth"]]\
        .sort_values("GDP_Growth", ascending=False).round(2)
    st.dataframe(df_year, use_container_width=True)

st.markdown("---")
st.subheader(f"📊 Ranking Negara — {selected_year}")

df_rank = df[df["Year"] == selected_year][["Country", "GDP_Growth"]]\
    .sort_values("GDP_Growth", ascending=False).reset_index(drop=True)
df_rank.index += 1
df_rank.columns = ["Negara", "GDP Growth (%)"]
df_rank["GDP Growth (%)"] = df_rank["GDP Growth (%)"].round(2)
st.dataframe(df_rank, use_container_width=True)

st.markdown("---")
st.subheader("📈 Forecasting GDP Growth")

try:
    from utils.predictor import predict_future
    FORECAST_READY = True
except ImportError:
    FORECAST_READY = False

col_kiri, col_kanan = st.columns([1, 2])

with col_kiri:
    selected_country = st.selectbox("Pilih Negara:", countries)
    n_years          = st.slider("Jumlah Tahun Proyeksi:", 1, 10, 5)
    run_forecast     = st.button("📈 Jalankan Forecast", use_container_width=True, type="primary")

with col_kanan:
    if run_forecast:
        if not FORECAST_READY:
            st.warning("⚠️ Menunggu predict_future() dari Fajar")
        else:
            with st.spinner(f"Proyeksi {n_years} tahun untuk {selected_country}..."):
                try:
                    forecast = predict_future(selected_country, n_years)
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                    st.stop()
            st.success(f"✅ Proyeksi {selected_country} — {n_years} tahun ke depan")
            st.line_chart(forecast)
            with st.expander("Lihat Data Numerik"):
                st.dataframe(forecast, use_container_width=True)
    else:
        st.info("👈 Pilih negara dan tahun, lalu klik Jalankan Forecast")