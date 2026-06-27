import streamlit as st
import pandas as pd
from utils.navigation import show_navbar
# from utils.world_data import load_asean_data, get_map_data, get_country_list

try:
    from utils.world_data import load_asean_data, get_map_data, get_country_list
    WORLD_DATA_READY = True
except ModuleNotFoundError:
    WORLD_DATA_READY = False

from utils.predictor import predict_future

try:
    from streamlit_echarts import st_echarts
    ECHARTS_OK = True
except ImportError:
    ECHARTS_OK = False

st.set_page_config(
    page_title="Analisis ASEAN — GDP ASEAN",
    page_icon="🌍",
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

st.title("🌍 Analisis ASEAN")
st.markdown("Peta interaktif dan forecasting GDP Growth negara-negara ASEAN.")
st.markdown("---")

@st.cache_data
def get_data():
    return load_asean_data()

df        = get_data()
countries = get_country_list(df)

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

col_kiri, col_kanan = st.columns([1, 2])

with col_kiri:
    selected_country = st.selectbox("Pilih Negara:", countries)
    n_years          = st.slider("Jumlah Tahun Proyeksi:", 1, 10, 5)
    run_forecast     = st.button("📈 Jalankan Forecast", use_container_width=True, type="primary")

with col_kanan:
    if run_forecast:
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