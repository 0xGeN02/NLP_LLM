import streamlit as st
from src.config import set_page_config, inject_css
from src.translator import detectar_idioma, obtener_traductor
from src.corrector import obtener_corrector, corregir_texto

# Configuración inicial
set_page_config()
inject_css()

# Header con logo
st.markdown("""
<div class="card">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Galicia.svg" width="60" style="border-radius: 8px;">
        <div>
            <h1 style="margin: 0;">GalegoPro</h1>
            <p style="color: #636e72; margin: 0; font-size: 1.1rem;">Tradución e corrección lingüística avanzada</p>
        </div>
    </div>
    <div class="decorative-line"></div>
</div>
""", unsafe_allow_html=True)

# Área de entrada principal
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    texto_entrada = st.text_area(
        "Introduce o texto:",
        height=180,
        placeholder="✍️ Escribe ou pega aquí o texto que desexas traducir...",
        key="input_text",
        help="Texto en calquera idioma para traducir a galego normativo"
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button(
            "🚀 Procesar texto",
            type="primary",
            use_container_width=True,
            help="Iniciar a tradución e corrección"
        ):
            if texto_entrada:
                # Mostrar spinner durante o procesamento
                with st.spinner("Procesando..."):
                    try:
                        # Detectar idioma
                        idioma_detectado = detectar_idioma(texto_entrada)
                        
                        # Traducir texto
                        traductor = obtener_traductor(idioma_detectado)
                        if traductor:
                            resultado_traduccion = traductor(texto_entrada)
                            texto_traducido = resultado_traduccion[0]['translation_text']
                            
                            # Corregir texto
                            corrector = obtener_corrector()
                            if corrector:
                                texto_corregido = corregir_texto(texto_traducido, corrector)
                                st.session_state.resultados = {
                                    'traduccion': texto_traducido,
                                    'correccion': texto_corregido,
                                    'idioma': idioma_detectado
                                }
                            else:
                                st.error("Erro ao cargar o corrector gramatical")
                        else:
                            st.error(f"Non se atopou tradutor para {idioma_detectado}")
                    except Exception as e:
                        st.error(f"Erro no proceso: {str(e)}")
            else:
                st.warning("Por favor, introduce un texto para procesar")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Mostrar resultados si existen
if 'resultados' in st.session_state:
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        
        # Tabs para resultados
        tab_trad, tab_corr = st.tabs(["📄 Tradución", "✅ Corrección"])
        
        with tab_trad:
            st.markdown(f"""
            <div style="margin-bottom: 1rem; color: #636e72;">
                Idioma orixinal: <strong>{st.session_state.resultados['idioma']}</strong>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="
                background: #f8f9fa;
                padding: 1.5rem;
                border-radius: 12px;
                border: 1px solid #e0e0e0;
                line-height: 1.6;
            ">
                {st.session_state.resultados['traduccion']}
            </div>
            """, unsafe_allow_html=True)
        
        with tab_corr:
            st.markdown(f"""
            <div style="
                background: #000000;
                padding: 1.5rem;
                border-radius: 12px;
                border: 1px solid #e0e0e0;
                line-height: 1.6;
            ">
                {st.session_state.resultados['correccion']}
            </div>
            """, unsafe_allow_html=True)
        
        # Botón de limpar
        if st.button("🔄 Novo texto", use_container_width=True):
            del st.session_state.resultados
            del st.session_state.input_text
            st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    🏆 Dev [oxGeN02] • v0.1.0
</div>
""", unsafe_allow_html=True)