import streamlit as st

def show_navbar():
    st.markdown("""
        <style>
            [data-testid="collapsedControl"] { display: none; }
            section[data-testid="stSidebar"] { display: none; }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])

    with col1:
        st.markdown("### 🌏 GDP ASEAN")
    with col2:
        st.page_link("pages/02_EDA.py", label="📊 EDA", use_container_width=True)
    with col3:
        st.page_link("pages/03_Prediksi.py", label="🤖 Prediksi", use_container_width=True)
    with col4:
        st.page_link("pages/04_Analisis_Global.py", label="🌍 Analisis ASEAN", use_container_width=True)
    with col5:
        st.page_link("pages/05_Kesimpulan.py", label="📝 Kesimpulan", use_container_width=True)

    st.divider()