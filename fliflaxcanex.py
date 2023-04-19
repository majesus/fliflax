import pandas as pd
import itertools
import streamlit as st
import numpy as np

def calcular_prob_conjunta(data, marginales):
    medios = data.columns
    prob_conjunta = pd.DataFrame(columns=medios, index=medios)
    
    for medio_i, medio_j in itertools.combinations(medios, 2):
        prob_conjunta.at[medio_i, medio_j] = data[(data[medio_i] == 1) & (data[medio_j] == 1)].shape[0] / len(data)
        prob_conjunta.at[medio_j, medio_i] = prob_conjunta.at[medio_i, medio_j]
    
    for medio_i in medios:
        prob_conjunta.at[medio_i, medio_i] = marginales[medio_i]
    
    return prob_conjunta

def calcular_alcance(prob_conjunta):
    alcance = 1 - prob_conjunta.at['Ninguno', 'Ninguno']
    return alcance

def calcular_distribucion_contactos(prob_conjunta):
    medios = prob_conjunta.columns[:-1]  # Excluir la columna 'Ninguno'
    distribucion_contactos = prob_conjunta.loc[medios, 'Ninguno'] * -1
    return distribucion_contactos

st.set_page_config(page_title="Planificación de Medios", page_icon="📊", layout="centered")

st.title("Planificación de Medios")
st.write("Cálculo del alcance del plan de medios y la distribución de contactos utilizando el modelo CANEX")

np.random.seed(42)

data_ficticia = pd.DataFrame({
    'Medio1': np.random.choice([0, 1], size=100, p=[0.6, 0.4]),
    'Medio2': np.random.choice([0, 1], size=100, p=[0.7, 0.3]),
    'Medio3': np.random.choice([0, 1], size=100, p=[0.5, 0.5])
})

data = data_ficticia.copy()

# Agregar una columna 'Ninguno' para calcular el alcance y la distribución de contactos
data['Ninguno'] = (~data.any(axis=1)).astype(int)

# Sidebar para ingresar datos
st.sidebar.title("Ingrese los datos del plan de medios")
inserciones = {
    medio: st.sidebar.number_input(f"Inserciones en {medio}", min_value=0, value=1)
    for medio in data.columns[:-1]
}

poblacion = st.sidebar.number_input("Población", min_value=1, value=100)

# Aplicar las inserciones en el plan de medios
for medio, num_inserciones in inserciones.items():
    data.loc[data[medio] == 1, medio] = num_inserciones

marginales = data.mean()
prob_conjunta = calcular_prob_conjunta(data, marginales)
alcance = calcular_alcance(prob_conjunta)
distribucion_contactos = calcular_distribucion_contactos(prob_conjunta)

st.subheader("Probabilidades marginales")
st.write(marginales)
st.subheader("Probabilidades conjuntas")
st.write(prob_conjunta)
st.subheader("Alcance del plan de medios")
st.write(alcance)
st.subheader("Distribución de contactos")
st.write(distribucion_contactos)
