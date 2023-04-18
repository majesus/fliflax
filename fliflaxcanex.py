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

def canex_probability(audiencias, inserciones, contacts):
    prob = 0
    for subset in itertools.combinations(range(len(audiencias)), contacts):
        subset = list(subset)
        prob_subset = 1
        for i in range(len(audiencias)):
            if i in subset:
                prob_subset *= 1 - (1 - audiencias[i] / n) ** inserciones[i]
            else:
                prob_subset *= (1 - audiencias[i] / n) ** inserciones[i]
        prob += prob_subset
    return prob

contact_distribution = pd.DataFrame(columns=['Contactos', 'Personas'])
total_prob = 0

for contacts in range(1, M+1):
    prob = canex_probability(audiencias, inserciones, contacts)
    total_prob += prob
    contact_distribution.loc[len(contact_distribution)] = [contacts, round(prob * n)]

st.write('Distribución de contactos:')
st.dataframe(contact_distribution)
st.write(f'Total: {contact_distribution["Personas"].sum()}')
