import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import betabinom

# 1) Sliders para Ai, ni y P
st.sidebar.header("Configuración de parámetros")
M = st.sidebar.slider("Número de medios (M)", 1, 5, 1)

# Inicializar listas para almacenar Ai y ni
A_list = []
n_list = []

for i in range(M):
    A_list.append(st.sidebar.slider(f"Audiencia del Medio {i+1} (A{i+1})", 0, 1000, 10))
    n_list.append(st.sidebar.slider(f"Inserciones en el Medio {i+1} (n{i+1})", 0, 100, 5))

P = st.sidebar.slider("Población (P)", 0, 1100000, 1000)

# 2) Tabla de duplicaciones del Medio i con i, y el Medio i con j
st.header("Duplicaciones")
duplication_df = pd.DataFrame(index=range(M), columns=range(M))
duplication_input = []

for i in range(M):
    for j in range(i, M):
        duplication_input.append(st.number_input(f"Duplicación del Medio {i+1} con {j+1}", key=f"{i},{j}"))

duplication_input = iter(duplication_input)

for i in range(M):
    for j in range(i, M):
        value = next(duplication_input)
        duplication_df.at[i, j] = value
        duplication_df.at[j, i] = value

st.write(duplication_df)

# 3) Matriz de opciones de duplicación i con i, e i con j
options_df = pd.DataFrame(index=range(M), columns=range(M))

for i in range(M):
    for j in range(M):
        if i == j:
            options_df.at[i, j] = n_list[i] * (n_list[i] - 1) / 2
        else:
            options_df.at[i, j] = n_list[i] * n_list[j]

st.write(options_df)

# 4) Matriz de multiplicación de la duplicación ii x nii, duplicación ij por nij
multiplication_df = duplication_df * options_df
st.write(multiplication_df)

# 5) Cálculo de C1
C1 = sum(np.array(A_list) * np.array(n_list)) / sum(n_list)

# 6) Cálculo de D
D = np.triu(multiplication_df).sum() / np.triu(options_df).sum()

# 7) Cálculo de C2
C2 = 2 * C1 - D

# Distribución de frecuencias o contactos desde 0 hasta N
N = sum(n_list)
frequencies = betabinom(N, C1 / C2, (P - C1) / C2).pmf(range(N + 1))

# Mostrar resultados
st.header("Resultados")
st.write("C1:", C1)
st.write("D:", D)
st.write("C2:", C2)
st.write("Distribución de frecuencias:")
st.write(pd.DataFrame({"Contactos": range(N + 1), "Frecuencia": frequencies}))
