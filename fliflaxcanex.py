import streamlit as st
import pandas as pd
import numpy as np

# Función para simular la distribución conjunta de probabilidad completa para los medios dados
def simulate_joint_distribution(n, p, inserciones):
    joint_prob = np.zeros((n, len(p)))
    for i in range(len(p)):
        effective_p = 1 - (1 - p[i]) ** inserciones[i]
        joint_prob[:, i] = np.random.binomial(1, effective_p, n)
    return joint_prob

# Función para calcular la matriz de covarianza ajustada en función de las correlaciones entre los medios
def adjusted_covariance_matrix(cov_matrix, correlations, p):
    adjusted_cov_matrix = cov_matrix.copy()
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            adjusted_cov_matrix[i, j] = correlations[i, j] * np.sqrt(p[i] * p[j] * (1 - p[i]) * (1 - p[j]))
            adjusted_cov_matrix[j, i] = adjusted_cov_matrix[i, j]
    return adjusted_cov_matrix

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
M = st.slider('Número de medios', min_value=2, max_value=10, value=4)

n = st.number_input('Número de individuos', value=1000)

audiencia_labels = [f"Audiencia medio {i+1}" for i in range(M)]
audiencias = [st.slider(audiencia_labels[i], min_value=0, max_value=n, value=n//(2*M)+(i*(n//M)//M)) for i in range(M)]

inserciones_labels = [f"Número de inserciones en el medio {i+1}" for i in range(M)]
inserciones = [st.slider(inserciones_labels[i], min_value=0, max_value=10, value=(i%M)+1) for i in range(M)]

audiencias = np.array(audiencias[:M])
inserciones = np.array(inserciones[:M])

exposure_ratios = 1 - np.power(1 - audiencias/n, inserciones)
exposure_ratios = np.array(exposure_ratios[:M])

marginal_probabilities = exposure_ratios / np.sum(exposure_ratios)

st.write('Probabilidades marginales de cada medio:', dict(zip(audiencia_labels, marginal_probabilities)))

joint_prob = simulate_joint_distribution(n, exposure_ratios, inserciones)

cov_matrix = np.cov(joint_prob.T)
correlations = np.identity(M)  # Asumimos que no hay correlaciones entre los medios
adjusted_cov_matrix = adjusted_covariance_matrix(cov_matrix, correlations, marginal_probabilities)

joint_prob = np.prod(marginal_probabilities)
for depth in range(1, M+1):
    joint_prob += (-1) ** depth * calc_mduple_sum_iterative(adjusted_cov_matrix, marginal_probabilities)

st.write(f'La probabilidad conjunta de exposición a los {M} medios es {joint_prob:.4f}')

# Función para calcular la distribución de contactos
def calculate_contact_distribution(data):
    contact_freq = data.sum(axis=1)
    freq_table = pd.DataFrame(contact_freq.value_counts())
    freq_table.columns = ['Personas']
    freq_table.index.name = 'Contactos'
    return freq_table

# Calcular e imprimir la distribución de contactos
simulated_joint_dist = simulate_joint_distribution(n, exposure_ratios, inserciones)
simulated_joint_dist_df = pd.DataFrame(simulated_joint_dist)  # Convertir la matriz en un DataFrame de Pandas
contact_distribution = calculate_contact_distribution(simulated_joint_dist_df)
contact_distribution = contact_distribution.sort_index()
st.write('Distribución de contactos:')
st.dataframe(contact_distribution)
st.write(f'Total: {contact_distribution["Personas"].sum()}')

import matplotlib.pyplot as plt
import seaborn as sns

def plot_contact_distribution(contact_distribution):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=contact_distribution.index, y=contact_distribution["Personas"])
    plt.xlabel("Contactos")
    plt.ylabel("Personas")
    plt.title("Distribución de contactos")
    st.pyplot()

plot_contact_distribution(contact_distribution)

def plot_covariance_matrix(cov_matrix):
    plt.figure(figsize=(10, 6))
    sns.heatmap(cov_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.xlabel("Medios")
    plt.ylabel("Medios")
    plt.title("Matriz de covarianzas entre medios")
    st.pyplot()

plot_covariance_matrix(adjusted_cov_matrix)
