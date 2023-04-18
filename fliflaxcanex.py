import itertools
import math
import numpy as np
import pandas as pd
import streamlit as st

M = st.slider('Número de medios', min_value=2, max_value=10, value=4)

n = st.number_input('Número de individuos', value=1000)

audiencia_labels = [f"Audiencia medio {i+1}" for i in range(M)]
audiencias = [st.slider(audiencia_labels[i], min_value=0, max_value=n, value=n//(2*M)+(i*(n//M)//M)) for i in range(M)]

inserciones_labels = [f"Número de inserciones en el medio {i+1}" for i in range(M)]
inserciones = [st.slider(inserciones_labels[i], min_value=0, max_value=10, value=(i%M)+1) for i in range(M)]

audiencias = np.array(audiencias[:M])
inserciones = np.array(inserciones[:M])

def calculate_corr(audiencias, n):
    num_medios = len(audiencias)
    corr_matrix = np.zeros((num_medios, num_medios))

    for i in range(num_medios):
        for j in range(i + 1, num_medios):
            p1 = audiencias[i] / n
            p2 = audiencias[j] / n
            p11 = (audiencias[i] * audiencias[j]) / (n * n)
            corr = (p11 - p1 * p2) / (math.sqrt(p1 * (1 - p1) * p2 * (1 - p2)))
            corr_matrix[i, j] = corr
            corr_matrix[j, i] = corr

    return corr_matrix

def canex_probability(audiencias, inserciones, contacts, corr_matrix):
    prob = 0
    for subset in itertools.combinations(range(len(audiencias)), contacts):
        subset = list(subset)
        prob_subset = 1
        for i in range(len(audiencias)):
            p1 = audiencias[i] / n
            if i in subset:
                prob_subset *= 1 - (1 - p1) ** inserciones[i]
            else:
                prob_subset *= (1 - p1) ** inserciones[i]

        # Combinar las correlaciones de Pearson para los medios en el subconjunto
        for i, j in itertools.combinations(subset, 2):
            corr = corr_matrix[i, j]
            prob_subset *= (1 + corr)

        prob += prob_subset

    return prob

# Calcular la matriz de correlación de Pearson
corr_matrix = calculate_corr(audiencias, n)

# Cálculo de la probabilidad conjunta
for contacts in range(1, M+1):
    prob = canex_probability(audiencias, inserciones, contacts, corr_matrix)
    total_prob += prob
    contact_distribution.loc[len(contact_distribution)] = [contacts, round(prob * n)]

st.write('Distribución de contactos:')
st.dataframe(contact_distribution)
st.write(f'Total: {contact_distribution["Personas"].sum()}')
