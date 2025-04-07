import streamlit as st

def set_page_config():
    st.set_page_config(page_title="Traductor a Gallego Normativo", page_icon="🇬🇦", layout="wide")

def inject_css():
    st.markdown("""
    <style>
    /* Fondo principal: azul celeste */
    [data-testid="stAppViewContainer"] {
        background-color: #87CEFA;
    }
    /* Títulos en rojo */
    h1, h2, h3, h4, h5, h6 {
        color: #FF0000;
    }
    /* Barra lateral en blanco */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
    }
    /* Estilo para los botones */
    div.stButton > button {
        background-color: #FF0000;
        color: #FFFFFF;
        border: none;
        padding: 0.5em 1em;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
