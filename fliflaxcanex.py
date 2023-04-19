import pandas as pd
import itertools
import streamlit as st
import numpy as np

# ... (aquí van las funciones: calcular_segundo_orden, calcular_alcance, calcular_distribucion_contactos)

# Configuración de la aplicación Streamlit
st.set_page_config(page_title="Planificación de Medios", page_icon="📊", layout="centered")

st.title("Planificación de Medios")
st.write("Cálculo del alcance del plan de medios y la distribución de contactos utilizando el modelo CANEX")

# Crear un DataFrame ficticio
np.random.seed(42)  # Fijar una semilla para obtener resultados consistentes

data_ficticia = pd.DataFrame({
    'Medio1': np.random.choice([0, 1], size=100, p=[0.6, 0.4]),
    'Medio2': np.random.choice([0, 1], size=100, p=[0.7, 0.3]),
    'Medio3': np.random.choice([0, 1], size=100, p=[0.5, 0.5])
})

data = data_ficticia.copy()

# Solicitar el tamaño de la población
poblacion = st.sidebar.number_input("Población total", value=1000, min_value=1, step=1)

# Solicitar las audiencias de cada soporte
audiencias = {}
for medio in data.columns:
    audiencias[medio] = st.sidebar.number_input(f"Audiencia de {medio}", value=100, min_value=1, step=1)

# Calcular las probabilidades marginales
marginales = pd.Series(audiencias) / poblacion
primer_orden = data.corr()
segundo_orden = calcular_segundo_orden(data)

# Solicitar el número de inserciones por medio
inserciones = {}
for medio in data.columns:
    inserciones[medio] = st.sidebar.number_input(f"Inserciones en {medio}", value=1, min_value=1, step=1)

alcance = calcular_alcance(marginales, pd.Series(inserciones))
distribucion_contactos = calcular_distribucion_contactos(marginales, pd.Series(inserciones))
st.subheader("Alcance del plan de medios")
st.write(alcance)
st.subheader("Distribución de contactos")
st.write(distribucion_contactos)
