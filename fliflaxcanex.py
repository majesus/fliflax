import pandas as pd
import itertools
import streamlit as st
import numpy as np

def calcular_prob_conjunta(data, marginales):
    n = len(data.columns)
    medios = data.columns
    prob_conjunta = pd.DataFrame(columns=medios, index=medios)

    for medio_i, medio_j in itertools.combinations(medios, 2):
        prob_conjunta.at[medio_i, medio_j] = marginales[medio_i] * marginales[medio_j]
        prob_conjunta.at[medio_j, medio_i] = prob_conjunta.at[medio_i, medio_j]

    for medio in medios:
        prob_conjunta.at[medio, medio] = marginales[medio]

    return prob_conjunta

def calcular_alcance(marginales, prob_conjunta):
    return 1 - np.prod(1 - marginales + np.diag(prob_conjunta))

def calcular_distribucion_contactos(marginales, inserciones, alcance):
    distribucion = pd.DataFrame(index=range(1, sum(inserciones.values()) + 1), columns=['Contactos'])
    for i in range(1, sum(inserciones.values()) + 1):
        distribucion.loc[i, 'Contactos'] = np.sum(marginales * i) / alcance

    return distribucion

# Simulación de datos de exposición
np.random.seed(42)
data = pd.DataFrame({'Medio1': np.random.binomial(1, 400 / poblacion, poblacion),
                     'Medio2': np.random.binomial(1, 300 / poblacion, poblacion),
                     'Medio3': np.random.binomial(1, 500 / poblacion, poblacion)})

marginales = data.mean()
prob_conjunta = calcular_prob_conjunta(data, marginales)
alcance = calcular_alcance(marginales, prob_conjunta)
distribucion_contactos = calcular_distribucion_contactos(marginales, inserciones, alcance)

st.subheader("Probabilidades marginales")
st.write(marginales)
st.subheader("Probabilidades conjuntas")
st.write(prob_conjunta)
st.subheader("Alcance del plan de medios")
st.write(alcance)
st.subheader("Distribución de contactos")
st.write(distribucion_contactos)
