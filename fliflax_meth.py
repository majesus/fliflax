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

#----------------------------------------------------#
A1 = C1
A2 = C2
n = sum(n_list)

st.write(A1); st.write(A2); st.write(n)
#----------------------------------------------------#
R1=A1/P;R2=A2/P  
alpha=((R1)*((R2)-(R1)))/(2*(R1)-(R1)*(R1)-(R2))
beta=(alpha*(1-R1))/(R1)
#----------------------------------------------------#
try:
  alpha=((R1)*((R2)-(R1)))/(2*(R1)-(R1)*(R1)-(R2))
  beta=(alpha*(1-R1))/(R1)
except ZeroDivisionError as e:
  # st.write("#### Observaciones:")
  # datos de muestra:
  alpha = 0.125
  beta = 0.125
  n = 5
  st.error("Se ha producido una excepción al proponerse un valor de A2 que provoca una división por 0. "
           "Recuerda que los parámetros de forma deben ser superiores a 0 ."
           "Debes pues revisar los valores de A1 y A2. "
           "Mientras tanto, los resultados que ves abajo, se corresponden con valores por defecto.")
#----------------------------------------------------#
x = np.arange(1,n+1)
alphas = alpha
betas = beta
#----------------------------------------------------#
# https://docs.pymc.io/en/v3/api/distributions/discrete-2.py
# https://docs.scipy.org/doc/scipy/tutorial/stats/discrete_betabinom.html
def BetaBinom(a, b, n, x):
    pmf = special.binom(n, x) * (special.beta(x+a, n-x+b) / special.beta(a, b))
    return pmf

# eliminar primer elemento de la lista pmf que hace referencia a los individuos no expuestos:
dc = BetaBinom(alphas, betas, n, x); 
  
if alphas > 0 and betas > 0 and P > A2:
  pmf = BetaBinom(alphas, betas, n, x)
else:
  st.error("Se ha producido un error catastrófico. Los valores alfa y beta generan un error debido a los valores arriba elegidos. "
           "Debes revisar la elección de A1 y A2 o de la población. "
           "Recuerda que A2 debe ser superior a A1, y nunca más del doble, y que la población debe ser superior a A2.")
  st.error("Asimismo, valores excesivos de A2 producen errores graves que impiden a la distribución ofrecer valores consistentes.")
  st.error("Mientras tanto, los resultados que te mostramos abajo corresponden a un valor de A1 igual a 500,000 y "
           "un valor de A2 igual a 550,000 personas, y una población igual a 1,000,000, con el número de inserciones que hayas elegido.")

  A1 = 500000
  A2 = 550000
  P = 1000000
  alphas = 0.125
  betas = 0.125
  pmf = BetaBinom(alphas, betas, n, x)
  
# Pi:
y = pmf * P
# Ri:
Ri = np.flip(y); Ri = np.cumsum(Ri); Ri = np.flip(Ri)
#----------------------------------------------------#
data = {'exposiciones':  x, 'Pi': y, 'Ri': Ri}

df = pd.DataFrame(data)
df = df.astype(int)
pd.options.display.float_format = '{:,}'.format
df = df.head(n=n)
#----------------------------------------------------#
if df['Ri'].iloc[0] > P:
  st.error("La cobertura es superior a la población, y es imposible; puedes verlo en los resultados de abajo. "
           "Igual el número de inserciones es excesivo.")
else:
  st.write("")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
