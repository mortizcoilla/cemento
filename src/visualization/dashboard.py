import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos procesados
data = pd.read_csv('data/raw/concrete_data.csv')

# Título del dashboard
st.title("Dashboard: Resistencia a la Compresión del Hormigón")

# Sección 1: Exploración de Datos
st.header("Exploración de Datos")

# Seleccionar columna para análisis
column = st.selectbox("Selecciona una característica:", data.columns[:-1])
st.write(f"Histograma para: {column}")

# Crear histograma
fig, ax = plt.subplots()
ax.hist(data[column], bins=20, color='skyblue', edgecolor='black')
ax.set_title(f"Distribución de {column}")
ax.set_xlabel(column)
ax.set_ylabel("Frecuencia")
st.pyplot(fig)

# Sección 2: Resultados del Modelo
st.header("Resultados del Modelo")

# Subir resultados de MSE
mse_values = [10, 15, 12, 14, 13]  # Ejemplo de datos
st.write("Comparación de errores cuadráticos medios (MSE) entre modelos")

# Boxplot de MSE
fig2, ax2 = plt.subplots()
ax2.boxplot(mse_values, vert=False, patch_artist=True)
ax2.set_title("Distribución de MSE entre modelos")
ax2.set_xlabel("MSE")
st.pyplot(fig2)
