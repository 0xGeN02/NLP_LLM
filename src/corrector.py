import language_tool_python
import streamlit as st

@st.cache_resource(show_spinner=False)
def obtener_corrector():
    """
    Inicializa LanguageTool para gallego ('gl').
    """
    try:
        herramienta = language_tool_python.LanguageTool('gl')
        return herramienta
    except Exception as e:
        st.error(f"Error inicializando la herramienta de corrección: {e}")
        return None

def corregir_texto(texto, herramienta):
    """
    Corrige el texto utilizando LanguageTool.
    """
    try:
        matches = herramienta.check(texto)
        return language_tool_python.server.correct(texto, matches)
    except Exception as e:
        st.error(f"Error durante la corrección: {e}")
        return texto
