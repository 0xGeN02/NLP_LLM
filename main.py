import streamlit as st
from src.config import set_page_config, inject_css
from src.translator import detectar_idioma, obtener_traductor
from src.corrector import obtener_corrector, corregir_texto

# Configuración inicial de la página y aplicación de estilos
set_page_config()
inject_css()

# Título y descripción principal
st.title("Traductor a Gallego Normativo y Corrector de Estilo")
st.markdown("Introduce un texto en cualquier idioma para traducirlo a gallego normativo y aplicar correcciones gramaticales y sugerencias de estilo.")

# Área de entrada para el texto
texto_entrada = st.text_area("Introduce el texto a traducir:")

if st.button("Traducir y Corregir") and texto_entrada:
    # Detección del idioma de entrada
    idioma_detectado = detectar_idioma(texto_entrada)
    st.write(f"Idioma detectado: **{idioma_detectado}**")

    # Traducción a gallego
    traductor = obtener_traductor(idioma_detectado)
    if traductor:
        resultado_traduccion = traductor(texto_entrada)
        texto_traducido = resultado_traduccion[0]['translation_text']
        st.subheader("Texto traducido a gallego:")
        st.write(texto_traducido)

        # Corrección del texto traducido
        corrector = obtener_corrector()
        if corrector:
            texto_corregido = corregir_texto(texto_traducido, corrector)
            st.subheader("Texto corregido:")
            st.write(texto_corregido)
        else:
            st.warning("No se pudo inicializar la herramienta de corrección.")
    else:
        st.warning("No se pudo cargar el modelo de traducción para el idioma detectado.")
