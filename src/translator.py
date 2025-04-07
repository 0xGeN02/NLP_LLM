from langdetect import detect
from transformers import pipeline
import streamlit as st

def detectar_idioma(texto):
    try:
        return detect(texto)
    except Exception as e:
        st.error(f"Error detectando el idioma: {e}")
        return "unknown"

@st.cache_resource(show_spinner=False)
def obtener_traductor(idioma_origen):
    model_name = f"Helsinki-NLP/opus-mt-{idioma_origen}-gl"
    try:
        traductor = pipeline("translation", model=model_name)
        return traductor
    except Exception as e:
        st.error(f"Error cargando el modelo de traducción para '{idioma_origen}': {e}")
        return None
