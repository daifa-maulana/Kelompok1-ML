import streamlit as st

def show_navbar():
    cols = st.columns(7)
    pages = [
        ("app.py", "🏠 Home"),
        ("pages/01_Home.py", "📖 Info"),
        ("pages/02_Dataset.py", "📁 Dataset"),
        ("pages/03_Visualisasi.py", "📊 Visualisasi"),
        ("pages/04_Prediksi.py", "🔮 Prediksi"),
        ("pages/05_Kesimpulan.py", "📝 Kesimpulan"),
        ("pages/06_Forecasting.py", "📡 Forecasting"),
    ]
    for col, (path, label) in zip(cols, pages):
        with col:
            st.page_link(path, label=label, use_container_width=True)

# Alias
show_navigation = show_navbar