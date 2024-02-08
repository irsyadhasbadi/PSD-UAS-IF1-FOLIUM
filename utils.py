from streamlit_extras.app_logo import add_logo

@st.cache_data
def init():
    add_logo(
        "logo.png"
    )