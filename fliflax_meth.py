import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

# 1) Sliders para Ai, ni y P
st.sidebar.header("Configuración de parámetros")
M = st.sidebar.slider("Número de medios (M)", 1, 10, 3)

# Inicializar listas para almacenar Ai y ni
A_list = []
n_list = []

for i in range(M):
    A_list.append(st.sidebar.slider(f"Audiencia del Medio {i+1} (A{i+1})", 0, 100000, 10000))
    n_list.append(st.sidebar.slider(f"Inserciones en el Medio {i+1} (n{i+1})", 0, 100, 10))

# Población superior a la mayor de las audiencias
max_audience = max(A_list)
P = st.sidebar.number_input("Población (P)", value=max_audience+1, min_value=max_audience+1)

# 2) Tabla de duplicaciones del Medio i con i, y el Medio i con j
with st.expander("Duplicaciones"):
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

# Valores redondeados
C1_rounded = round(C1, 4)
D_rounded = round(D, 4)
C2_rounded = round(C2, 4)

# Cálculo de alphas y betas para la distribución Beta Binomial
R1 = C1 / P
R2 = C2 / P

try:
    alpha = (R1 * (R2 - R1)) / (2 * R1 - R1 * R1 - R2)
    beta = (alpha * (1 - R1)) / R1
except ZeroDivisionError as e:
    alpha = 0.125
    beta = 0.125
    st.error("Se ha producido una excepción al proponerse un valor de C2 que provoca una división por 0. "
             "Recuerda que los parámetros de forma deben ser superiores a 0 ."
             "Debes pues revisar los valores de C1 y C2. "
             "Mientras tanto, los resultados que ves abajo, se corresponden con valores por defecto.")

# Definición de la función BetaBinom
def BetaBinom(a, b, n, x):
    pmf = special.binom(n, x) * (special.beta(x+a, n-x+b) / special.beta(a, b))
    return pmf

# Inserciones
n = sum(n_list)
x = np.arange(1, n+1)

if alpha > 0 and beta > 0 and P > C2:
    pmf = BetaBinom(alpha, beta, n, x)
else:
    C1 = 500000
    C2 = 550000
    P = 1000000
    alpha = 0.125
    beta = 0.125
    pmf = BetaBinom(alpha, beta, n, x)

# Pi:
y = pmf * P

# Ri:
Ri = np.flip(y)
Ri = np.cumsum(Ri)
Ri = np.flip(Ri)

# Distribución de frecuencias en porcentaje sobre la población
freq_population_pct = y / P * 100

# Distribución de frecuencias en porcentaje sobre la cobertura
freq_coverage_pct = y / sum(y[1:]) * 100

# Distribución de frecuencias en personas
freq_people = y

# Construcción de la tabla de contactos
contacts_df = pd.DataFrame({"% Población": freq_population_pct,
                            "% Cobertura": freq_coverage_pct,
                            "Personas": freq_people},
                            index=range(n+1))
contacts_df.index.name = "Contactos"

st.write(contacts_df)

# Gráfica de la tabla de contactos
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(contacts_df.index, contacts_df["% Población"], label="% Población")
ax.plot(contacts_df.index, contacts_df["% Cobertura"], label="% Cobertura")
ax.plot(contacts_df.index, contacts_df["Personas"], label="Personas")
ax.set_xlabel("Contactos")
ax.set_ylabel("Frecuencia")
ax.set_title("Distribución de frecuencias")
ax.legend()

st.pyplot(fig)


# Construcción de la tabla de contactos
contacts_df = pd.DataFrame({"% Población": freq_population_pct,
                            "% Cobertura": freq_coverage_pct,
                            "Personas": freq_people},
                            index=range(n+1))
contacts_df.index.name = "Contactos"

st.write(contacts_df)

# Gráfica de la tabla de contactos
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(contacts_df.index, contacts_df["% Población"], label="% Población")
ax.plot(contacts_df.index, contacts_df["% Cobertura"], label="% Cobertura")
ax.plot(contacts_df.index, contacts_df["Personas"], label="Personas")
ax.set_xlabel("Contactos")
ax.set_ylabel("Frecuencia")
ax.set_title("Distribución de frecuencias")
ax.legend()

st.pyplot(fig)
