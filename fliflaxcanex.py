import streamlit as st
import pandas as pd
import numpy as np

# Función para generar datos de exposición basados en inserciones
def generate_exposure_data(n, p, inserciones):
    data = np.zeros((n, len(p)))
    for i in range(len(p)):
        for j in range(inserciones[i]):
            random_data = np.random.binomial(1, p[i], n)
            data[:, i] = np.logical_or(data[:, i], random_data).astype(int)
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
M = st.slider('Número de medios', min_value=2, max_value=10, value=4)

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
contact_distribution = contact_distribution.sort_index()  # Agrega esta línea
st.write('Distribución de contactos:')
st.dataframe(contact_distribution)
st.write(f'Total: {contact_distribution["Frecuencia"].sum()}')

import matplotlib.pyplot as plt
import seaborn as sns

def plot_contact_distribution(contact_distribution):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=contact_distribution.index, y=contact_distribution["Frecuencia"])
    plt.xlabel("Contactos")
    plt.ylabel("Frecuencia")
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

plot_covariance_matrix(cov_matrix)

#------------------------------------------#

import streamlit as st

import networkx as nx
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator

def create_bayesian_network(df):
    # Crear el grafo y agregar los nodos
    G = nx.DiGraph()
    G.add_nodes_from(df.columns)

    # Agregar los arcos entre nodos (aquí se puede modificar la estructura del grafo)
    for i in range(len(df.columns) - 1):
        G.add_edge(df.columns[i], df.columns[i + 1])

    # Crear el modelo Bayesiano
    bn_model = BayesianModel(G.edges)

    # Estimar las CPT usando el estimador de máxima verosimilitud
    bn_model.fit(df, estimator=MaximumLikelihoodEstimator)
    
    return bn_model

bn_model = create_bayesian_network(df)

def get_marginal_and_joint_probabilities(bn_model, nodes=None):
    if nodes is None:
        nodes = bn_model.nodes()

    # Calcular las probabilidades marginales y conjuntas
    marginal_probabilities = {}
    for node in nodes:
        marginal_probabilities[node] = bn_model.get_cpds(node).marginalize_all_but([node]).values

    joint_probabilities = bn_model.get_joint_distribution(nodes).values

    return marginal_probabilities, joint_probabilities

marginal_probabilities, joint_probabilities = get_marginal_and_joint_probabilities(bn_model)

st.write("Probabilidades marginales:")
for node, prob in marginal_probabilities.items():
    st.write(f"{node}: {prob}")

st.write("Probabilidad conjunta:")
st.write(joint_probabilities)

#-------------------------------------------#
