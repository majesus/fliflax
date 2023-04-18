import streamlit as st
import pandas as pd
import numpy as np

# Función para generar datos de exposición basados en inserciones
def generate_exposure_data(n, p, inserciones):
    data = np.zeros((n, len(p)))
    for i in range(len(p)):
        for j in range(inserciones[i]):
            data[:, i] |= np.random.binomial(1, p[i], n)
    return data

# Función iterativa para calcular la suma de productos M-duples de covarianzas y probabilidades marginales
def calc_mduple_sum_iterative(cov_matrix, p):
    sum_mduple = 0
    indices = range(len(p))
    for depth in range(len(p)):
        prod_p = np.prod(p[indices])
        sum_cov = np.sum(cov_matrix[indices, :][:, indices])
        sum_mduple += (-1) ** depth * prod_p * sum_cov
        indices = indices[1:]
    return sum_mduple

# Generar datos ficticios de exposición a los medios para M medios
M = st.slider('Número de medios', min_value=4, max_value=10, value=4)

n = st.number_input('Número de individuos', value=1000)

p_labels = [f"Probabilidad marginal medio {i+1}" for i in range(M)]
p = [st.slider(p_labels[i], min_value=0.0, max_value=1.0, value=1.0/M, step=0.01) for i in range(M)]

inserciones_labels = [f"Número de inserciones en el medio {i+1}" for i in range(M)]
inserciones = [st.slider(inserciones_labels[i], min_value=1, max_value=10, value=i+1) for i in range(M)]

p = np.array(p[:M])
inserciones = np.array(inserciones[:M])

data = generate_exposure_data(n, p, inserciones)

df = pd.DataFrame(data)
df.columns = [f'Medio{i}' for i in range(1, M+1)]

# Calcular las probabilidades conjuntas de exposición a los medios usando la expansión canónica truncada
cov_matrix = np.cov(data.T)
joint_prob = np.prod(p)
for depth in range(1, M+1):
    joint_prob += (-1) ** depth * calc_mduple_sum_iterative(cov_matrix, p)

st.write(f'La probabilidad conjunta de exposición a los {M} medios es {joint_prob:.4f}')

# Función para calcular la distribución de contactos
def calculate_contact_distribution(data):
    contact_freq = data.sum(axis=1)
    freq_table = pd.DataFrame(contact_freq.value_counts())
    freq_table.columns = ['Frecuencia']
    freq_table.index.name = 'Contactos'
    return freq_table

# Calcular e imprimir la distribución de contactos
contact_distribution = calculate_contact_distribution(df)
st.write('Distribución de contactos:')
st.dataframe(contact_distribution)
st.write(f'Total: {contact_distribution["Frecuencia"].sum()}')

