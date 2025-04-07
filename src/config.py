import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="Traductor a Gallego Normativo",
        page_icon="🇬🇦",
        layout="wide"
    )

def inject_css():
    st.markdown("""
    <style>
    /* Fondo principal suave con textura sutil */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Barra lateral estilizada */
    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    
    /* Títulos modernos con degradado */
    h1, h2, h3 {
        color: #2d3436;
        background: linear-gradient(45deg, #2d3436, #0984e3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    /* Botones con diseño moderno */
    div.stButton > button {
        background: linear-gradient(45deg, #0984e3, #00cec9);
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11);
    }
    
    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1);
        opacity: 0.9;
    }
    
    /* Área de texto mejorada */
    textarea {
        border: 2px solid #dfe6e9 !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        font-size: 1rem !important;
        transition: border-color 0.3s ease;
    }
    
    textarea:focus {
        border-color: #0984e3 !important;
        box-shadow: 0 0 0 3px rgba(9, 132, 227, 0.1) !important;
    }
    
    /* Tarjetas con efecto de profundidad */
    .card {
        background: #ffffff;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        margin: 1.5rem 0;
        border: 1px solid #f0f0f0;
    }
    
    /* Iconos y elementos decorativos */
    .decorative-line {
        height: 4px;
        background: linear-gradient(90deg, #0984e3, #00cec9);
        border-radius: 2px;
        margin: 1.5rem 0;
    }
    
    /* Mensajes de estado */
    .stAlert {
        border-radius: 12px !important;
        padding: 1rem !important;
    }
    
    /* Footer personalizado */
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        padding: 1rem;
        text-align: center;
        color: #636e72;
        background: rgba(255,255,255,0.9);
        border-top: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Añadir fuente Inter
    st.markdown('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">', unsafe_allow_html=True)