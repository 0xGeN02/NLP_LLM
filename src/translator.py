import ollama
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

@st.cache_resource(show_spinner=False)
def traducir_con_ollama(texto):
    """
    Usa Ollama 3.1 con un modelo local específico.
    """
    prompt = f"Por favor, traduce o seguinte texto a galego normativo:\n{texto}\n"
    try:
        respuesta = ollama.generate(
            prompt,
            model="C:\\Users\\manue\\.ollama\\models\\blobs\\sha256-948af2743fc78a328dcb3b0f5a31b3d75f415840fdb699e8b1235978392ecf85"
        )
        return respuesta
    except Exception as e:
        st.error(f"Error invocando Ollama: {e}")
        return texto
