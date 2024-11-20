import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de Streamlit
st.set_page_config(
    page_title="Dashboard de Predicción de Concreto",
    layout="wide",
    initial_sidebar_state="collapsed"  # Opciones: "expanded", "collapsed"
)

# Paleta de colores
DARK_BLUE = "#072D44"
MEDIUM_BLUE = "#064469"
LIGHT_BLUE = "#5790AB"
PALE_BLUE = "#9CCCDB"
GRAY_BLUE = "#D0D7E1"
BUTTER_YELLOW = "#F3D77F"
WHITE = "#fcfbf9"

# Estilos personalizados con CSS
st.markdown(f"""
    <style>
        .main-title {{
            color: {DARK_BLUE};
            font-weight: bold;
            font-size: 28px;
            text-align: center;
            margin-bottom: 20px;
        }}
        .section-title {{
            color: {MEDIUM_BLUE};
            font-weight: bold;
            font-size: 20px;
            margin-bottom: 10px;
        }}
        .contact {{
            text-align: center;
            margin-top: 20px;
        }}
        .contact a {{
            text-decoration: none;
            color: {MEDIUM_BLUE};
            font-weight: bold;
            font-size: 16px;
            margin: 5px;
            display: block;
        }}
        .contact a:hover {{
            color: {LIGHT_BLUE};
        }}
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='main-title'>Dashboard de Predicción de Resistencia del Concreto</h1>", unsafe_allow_html=True)

# Barra lateral: Información y contacto
st.sidebar.title("Configuración")
st.sidebar.markdown("Ajusta los parámetros del modelo y explora los datos.")
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.markdown("### by Miguel Ortiz C.")
st.sidebar.markdown(f"""
<div class="contact">
    <a href="https://www.linkedin.com/in/mortizcoilla/" target="_blank">LinkedIn</a>
    <a href="https://github.com/mortizcoilla" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)

# Cargar datos
@st.cache_data
def load_data():
    data_path = "data/raw/concrete_data.csv"
    return pd.read_csv(data_path)

try:
    data = load_data()
except FileNotFoundError:
    st.error("El archivo de datos no fue encontrado. Por favor verifica la ruta.")
    st.stop()

# Layout principal
col1, col2 = st.columns([1, 1.5])

# Columna 1: Importancia de variables
with col1:
    st.markdown("<h2 class='section-title'>Importancia de Variables según SHAP</h2>", unsafe_allow_html=True)
    feature_importance = {
        'Cement': 5.56,
        'Water': 4.97,
        'Age': 3.79,
        'Blast Furnace Slag': 3.46,
        'Coarse Aggregate': 1.99,
        'Superplasticizer': 1.83,
        'Fine Aggregate': 1.73,
        'Fly Ash': 1.33
    }

    # Gráfico de barras
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.barh(
        list(feature_importance.keys()),
        list(feature_importance.values()),
        color=LIGHT_BLUE,
        edgecolor=DARK_BLUE,
        alpha=0.85
    )
    ax.set_xlabel("Importancia Promedio Absoluta", fontsize=10)
    ax.set_title("Importancia de Variables según SHAP", fontsize=12, fontweight='bold')
    ax.grid(axis='x', linestyle='--', alpha=0.6)
    ax.tick_params(labelsize=8)
    plt.tight_layout()
    st.pyplot(fig)

# Columna 2: Configuración del modelo y simulación
with col2:
    st.markdown("<h2 class='section-title'>Configuración del Modelo</h2>", unsafe_allow_html=True)
    epochs = st.slider("Número de épocas de entrenamiento", min_value=50, max_value=200, step=10, value=100)
    layers = st.slider("Número de capas ocultas", min_value=1, max_value=5, step=1, value=3)
    st.write(f"**Configuración seleccionada:** {layers} capas ocultas, {epochs} épocas")

    st.markdown("<h2 class='section-title'>Simulación de Predicción</h2>", unsafe_allow_html=True)
    cement = st.number_input("Cement (kg/m³):", min_value=0.0, value=300.0, step=10.0)
    water = st.number_input("Water (kg/m³):", min_value=0.0, value=185.0, step=5.0)
    age = st.number_input("Age (days):", min_value=1, value=28, step=1)

    # Predicción simulada
    prediction = cement * 0.2 + water * 0.1 + age * 0.5  # Fórmula ficticia para ejemplo
    st.markdown(f"""
        <div class='metric-box'>
            <h3>Resistencia Estimada (MPa): {prediction:.2f}</h3>
        </div>
    """, unsafe_allow_html=True)

# Sección independiente: Tabla de datos
st.markdown("<h2 class='section-title'>Datos del Concreto</h2>", unsafe_allow_html=True)
with st.expander("Mostrar/Ocultar tabla de datos"):
    st.dataframe(data)
  
