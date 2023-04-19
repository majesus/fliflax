import pandas as pd
import itertools
import streamlit as st
import numpy as np

def calcular_prob_conjunta(marginales):
    medios = marginales.index
    prob_conjunta = pd.DataFrame(columns=medios, index=medios)

    for medio_i, medio_j in itertools.combinations(medios, 2):
        prob_conjunta.at[medio_i, medio_j] = marginales[medio_i] * marginales[medio_j]
        prob_conjunta.at[medio_j, medio_i] = prob_conjunta.at[medio_i, medio_j]

    for medio in medios:
        prob_conjunta.at[medio, medio] = marginales[medio]

    return prob_conjunta

def calcular_alcance(prob_conjunta):
    prob_no_contacto = np.prod(1 - np.diag(prob_conjunta))
    return 1 - prob_no_contacto

def calcular_distribucion_contactos(marginales, inserciones, alcance):
    distribucion = pd.DataFrame(index=range(1, sum(inserciones.values()) + 1), columns=['Contactos'])
    for i in range(1, sum(inserciones.values()) + 1):
        distribucion.loc[i, 'Contactos'] = np.sum(marginales ** i) / alcance

    return distribucion

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

marginales = pd.Series(audiencias).div(poblacion)
prob_conjunta = calcular_prob_conjunta(marginales)
alcance = calcular_alcance(prob_conjunta)
distribucion_contactos = calcular_distribucion_contactos(marginales, inserciones, alcance)

st.subheader("Probabilidades marginales")
st.write(marginales)
st.subheader("Probabilidades conjuntas")
st.write(prob_conjunta)
st.subheader("Alcance del plan de medios")
st.write(alcance)
st.subheader("Distribución de contactos")
st.write(distribucion_contactos)
