import pandas as pd
import itertools
import streamlit as st
import numpy as np

def calcular_prob_conjunta(data):
    n = len(data)
    medios = data.columns
    prob_conjunta = pd.DataFrame(columns=medios, index=medios)
    
    for medio_i, medio_j in itertools.combinations(medios, 2):
        prob_conjunta.at[medio_i, medio_j] = data[(data[medio_i] == 1) & (data[medio_j] == 1)].shape[0] / n
        prob_conjunta.at[medio_j, medio_i] = prob_conjunta.at[medio_i, medio_j]
        
    return prob_conjunta

def calcular_alcance(marginales, prob_conjunta):
    return 1 - np.prod(1 - marginales + np.diag(prob_conjunta))

def calcular_distribucion_contactos(data, inserciones, alcance):
    distribucion = pd.DataFrame(index=range(1, inserciones.sum() + 1), columns=['Contactos'])
    for i in range(1, inserciones.sum() + 1):
        distribucion.loc[i, 'Contactos'] = np.sum(data ** i) / alcance

    return distribucion

st.set_page_config(page_title="Planificación de Medios", page_icon="📊", layout="centered")

st.title("Planificación de Medios")
st.write("Cálculo del alcance del plan de medios y la distribución de contactos utilizando el modelo CANEX")

np.random.seed(42)

# Sidebar
st.sidebar.title("Parámetros del Plan de Medios")
poblacion = st.sidebar.number_input("Población", value=1000, min_value=1)
audiencias = {
    'Medio1': st.sidebar.number_input("Audiencia Medio1", value=400, min_value=0, max_value=poblacion),
    'Medio2': st.sidebar.number_input("Audiencia Medio2", value=300, min_value=0, max_value=poblacion),
    'Medio3': st.sidebar.number_input("Audiencia Medio3", value=500, min_value=0, max_value=poblacion)
}
inserciones = {
    'Medio1': st.sidebar.number_input("Inserciones Medio1", value=1, min_value=0),
    'Medio2': st.sidebar.number_input("Inserciones Medio2", value=1, min_value=0),
    'Medio3': st.sidebar.number_input("Inserciones Medio3", value=1, min_value=0)
}

data = pd.DataFrame(audiencias, index=[0]).div(poblacion)

marginales = data.mean()
prob_conjunta = calcular_prob_conjunta(data)
alcance = calcular_alcance(marginales, prob_conjunta)
distribucion_contactos = calcular_distribucion_contactos(data, pd.Series(inserciones), alcance)

st.subheader("Probabilidades marginales")
st.write(marginales)
st.subheader("Probabilidades conjuntas")
st.write(prob_conjunta)
st.subheader("Alcance del plan de medios")
st.write(alcance)
st.subheader("Distribución de contactos")
st.write(distribucion_contactos)
