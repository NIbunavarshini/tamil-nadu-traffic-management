import streamlit as st
from utils.translations import get_text
import streamlit.components.v1 as components

st.set_page_config(
    page_title="TN Traffic Management",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
with open('assets/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Language selector
language = st.sidebar.selectbox(
    "भाषा / Language / மொழி",
    ["தமிழ்", "English"],
    index=1,
    key="language_selector"
)

st.title(get_text("main_title", language))

# Main page layout
col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1526148653006-c95760000cc0", 
             caption=get_text("traffic_caption", language))
    st.header(get_text("features_header", language))
    st.markdown(get_text("features_list", language))

with col2:
    st.image("https://images.unsplash.com/photo-1422765732560-d03723b2c6b1",
             caption=get_text("transport_caption", language))
    st.header(get_text("quick_actions", language))

    if st.button(get_text("report_accident", language), key="report_accident_btn"):
        st.session_state.page = "emergency"
        st.experimental_rerun()

    if st.button(get_text("find_parking", language), key="find_parking_btn"):
        st.session_state.page = "parking"
        st.experimental_rerun()

    if st.button(get_text("ev_charging", language), key="ev_charging_btn"):
        st.session_state.page = "ev_stations"
        st.experimental_rerun()_page("pages/ev_stations.py")

# Footer
st.markdown("---")
st.markdown(get_text("footer_text", language), unsafe_allow_html=True)