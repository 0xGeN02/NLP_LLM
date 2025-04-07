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