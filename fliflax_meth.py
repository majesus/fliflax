
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import streamlit as st
#------------------------------------------#
def create_dataset(num_media, num_individuals):
    np.random.seed(42)
    data = np.random.randint(0, 2, size=(num_individuals, num_media))
    return pd.DataFrame(data, columns=[f'Medio {i+1}' for i in range(num_media)])

def calculate_phi_correlation_matrix(dataframe):
    num_media = dataframe.shape[1]
    correlation_matrix = np.zeros((num_media, num_media))

    for i in range(num_media):
        for j in range(num_media):
            if i == j:
                correlation_matrix[i, j] = 1
            else:
                contingency_table = pd.crosstab(dataframe.iloc[:, i], dataframe.iloc[:, j])
                chi2, _, _, _ = chi2_contingency(contingency_table)
                n = contingency_table.sum().sum()
                phi = np.sqrt(chi2 / n)
                correlation_matrix[i, j] = phi
                
    return pd.DataFrame(correlation_matrix, index=dataframe.columns, columns=dataframe.columns)

def adjust_correlation_matrix(correlation_matrix, min_audience_matrix):
    num_media = correlation_matrix.shape[0]
    adjusted_matrix = correlation_matrix.copy()

    for i in range(num_media):
        for j in range(num_media):
            if i != j:
                adjusted_matrix.iat[i, j] *= min_audience_matrix[i, j]
                
    return adjusted_matrix

def create_min_audience_matrix(audience_list):
    num_media = len(audience_list)
    min_audience_matrix = np.zeros((num_media, num_media))

    for i in range(num_media):
        for j in range(num_media):
            if i != j:
                min_audience_matrix[i, j] = min(audience_list[i], audience_list[j])

    return min_audience_matrix
#------------------------------------------#
#------------------------------------------#

#------------------------------------------#
#M = num_media
#------------------------------------------#
#------------------------------------------#
#------------------------------------------#
#------------------------------------------#
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

# 1) Sliders para Ai, ni y P
st.sidebar.header("Configuración de parámetros")
M = st.sidebar.slider("Número de medios (M)", 1, 5, 3)

# Inicializar listas para almacenar Ai y ni
A_list = []
n_list = []

for i in range(M):
    A_list.append(st.sidebar.slider(f"Audiencia del Medio {i+1} (A{i+1})", 1, 1000, 10))
    n_list.append(st.sidebar.slider(f"Inserciones en el Medio {i+1} (n{i+1})", 0, 10, 1))

# Población superior a la mayor de las audiencias, y Precio
max_audience = max(A_list)
min_audience = min(A_list)
P = st.sidebar.number_input("Población (P)", value=pow(10,4), min_value=max_audience+min_audience)
Precio = st.sidebar.number_input("Precio", value=5000, min_value=1000, max_value = 10000)

#----------------------------------------------#
data = create_dataset(M, P)
#----------------------------------------------#

st.title("Correlación Phi entre medios")

correlation_matrix_0 = calculate_phi_correlation_matrix(data)
min_audience_matrix = create_min_audience_matrix(A_list)
correlation_matrix = adjust_correlation_matrix(correlation_matrix_0, min_audience_matrix)

st.table(data.head())
st.table(correlation_matrix)
#----------------------------------------------#

st.title("BBD - estimación Duplicaciones")

import numpy as np
from scipy import special
import scipy.stats as stats

def BetaBinom(a, b, n, x):
    pmf = special.binom(n, x) * (special.beta(x+a, n-x+b) / special.beta(a, b))
    return pmf

def calculate_Dii(data, P, i):
    n = data.shape[0]
    y = np.sum(data.iloc[:, i] == 1)  # Número de 1 en el medio i

    p = y / n # Probailidad de exposición en el medio i: número de 1 / número de 1 y 0
    s2 = p * (1 - p) / n
    a = p * (p * (1 - p) / s2 - 1)
    b = (1 - p) * (p * (1 - p) / s2 - 1)

    n = 2
    x = np.array([1, 2])
    dc = BetaBinom(a, b, n, x)
    z = dc * P
    reach = np.sum(z)
    Dii = 2 * y - reach

    return Dii, reach, y  # Devolver reach y Ai además de Dii

def update_correlation_matrix_with_Dii(correlation_matrix, data, P):
    num_media = correlation_matrix.shape[0]

    for i in range(num_media):
        Dii, reach, y = calculate_Dii(data, P, i)
        #st.write(f"Reach para el medio {i + 1}: {reach}")
        #st.write(f"A1 para el medio {i + 1}: {y}")

        correlation_matrix.iat[i, i] = Dii

    return correlation_matrix

data = create_dataset(M, P)
st.table(data.head())
#correlation_matrix_0 = calculate_phi_correlation_matrix(data)
#min_audience_matrix = create_min_audience_matrix(A_list)
#correlation_matrix = adjust_correlation_matrix(correlation_matrix_0, min_audience_matrix)

data = data.sample(n=150, random_state=42)
P = data.shape[0] # Cambia esto por el valor real de la población
correlation_matrix_with_Dii = update_correlation_matrix_with_Dii(correlation_matrix, data, P)

st.table(data.head())
st.table(correlation_matrix_with_Dii)

reach_list = []
Ai_list = []

for i in range(data.shape[1]):
    Dii, reach, Ai = calculate_Dii(data, P, i)
    reach_list.append(reach)
    Ai_list.append(Ai)

result_df = pd.DataFrame({'Media': range(1, data.shape[1] + 1), 'Reach': reach_list, 'Ai': Ai_list})
st.table(result_df)
#----------------------------------------------#

st.title("Duplicaciones propuestas por el usuario")
    
# 2) Tabla de duplicaciones del Medio i con i, y el Medio i con j

with st.expander("Duplicaciones"):
    duplication_df = pd.DataFrame(index=range(M), columns=range(M))
    duplication_input = []

    for i in range(M):
        for j in range(i, M):
            default_value = correlation_matrix.iat[i, j]
            duplication_input.append(st.number_input(f"Duplicación del Medio {i+1} con {j+1}", value=default_value, key=f"{i},{j}"))

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

st.title("Matriz nii y nij")
st.write(options_df)

# 4) Matriz de multiplicación de la duplicación ii x nii, duplicación ij por nij
multiplication_df = duplication_df * options_df

st.title("Matriz de multiplicación de la duplicación ii x nii, duplicación ij por nij")
st.write(multiplication_df)

# 5) Cálculo de C1
C1 = sum(np.array(A_list) * np.array(n_list)) / sum(n_list)

# 6) Cálculo de D
if M == 1:
    D = duplication_df.at[0, 0]
else:
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

st.title("Parámetros y número de inserciones")
st.write(A1); st.write(A2); st.write(n)
#----------------------------------------------------#
R1=A1/P;R2=A2/P  
alpha=((R1)*((R2)-(R1)))/(2*(R1)-(R1)*(R1)-(R2))
beta=(alpha*(1-R1))/(R1)
st.write(alpha); st.write(beta)
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
#----------------------------------------------------#
st.write("Derivado de tus datos y siempre que se ajusten a las premisas del modelo Beta-Binomial, "
         "con una audiencia de", f"**{A1:,.0f}**", "y una audiencia acumulada tras la segunda inserción de", f"**{A2:,.0f}**", 
         ", el valor de la cobertura alcanzada es igual a", f"**{round(df['Ri'].iloc[0]):,.0f}**", "personas. "
         "Es decir,", f"**{round(df['Ri'].iloc[0]):,.0f}**", "personas se exponen al menos 1 vez. "
         "Los impactos logrados con", f"**{n:,.0f}**", "inserciones son", f"**{A1 * n:,.0f}**"," impactos. "
         "La frecuencia media es pues igual a", f"**{df['Ri'].sum() / df['Ri'].iloc[0]:,.0f}**","impactos por persona de la cobertura.")
st.write("Junto a lo anterior, el valor GRP es igual a", f"**{round(df['Ri'].sum() * 100 / P):,.0f}**","impactos por cada 100 personas de la población "
         "que en nuestro caso es igual a", f"{P:,.0f}", "personas. "
         "Y junto a los GRP te mostramos el valor CPP (coste por punto de rating), en este caso "
         "el coste monetario de alcanzar a un 1 % de la población es igual a", f"**{round(Precio * n / (df['Ri'].sum() * 100 / P)):,.0f}**","€. "
         "El valor CPP es el resultado de divir un presupuesto de", f"**{Precio * n:,.0f}**", "€ "
         "y los GRP logrados con la programación de inserciones.")
st.write('Finalmente, te mostramos los parámetros de forma que obtenemos: alfa: ',f"{alphas:,.3f}",'y beta: ',f"{betas:,.3f}")
st.write("A continuación, te ofrecemos un breve resumen de las principales cifras.")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Cobertura", value = f"{round(df['Ri'].iloc[0]):,.0f}")
with col2:
    st.metric(label="Frecuencia media", value = f"{df['Ri'].sum() / df['Ri'].iloc[0]:,.3f}")
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Impactos", value = f"{A1 * n:,.0f}")
with col2:
    st.metric(label="GRP", value = f"{round(df['Ri'].sum() * 100 / P):,.0f}")
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Presupuesto €", value = f"{Precio * n:,.0f}")
with col2:
    st.metric(label="CPP", value = f"{round(Precio * n / (df['Ri'].sum() * 100 / P)):,.0f}")  
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#    
# https://github.com/PablocFonseca/streamlit-aggrid  # --> Para el futuro.
#----------------------------------------------------#
# Mostrar la tabla de Pi y Ri:
# Convierto en index columna de exposiciones, y vuelco en otra tabla porque si no, me genera arror en Matplotlib.
df1 = df.set_index('exposiciones')
if st.checkbox("Si deseas ver los primeros 5 valores de Pi y Ri alcanzados, marca la casilla.", False):
    st.write('###### Tabla 1. Distribución de contactos Pi (y acumulada Ri)')
    st.table(df1.head(n).style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'})) 
    st.info("En nuestro Anexo de abajo, puedes ver todos los valores de Pi y Ri.")
    #st.balloons()
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
#----------------------------------------------------#
import numpy as np
from scipy import special
import scipy.stats as stats

def BetaBinom(a, b, n, x):
    pmf = special.binom(n, x) * (special.beta(x+a, n-x+b) / special.beta(a, b))
    return pmf

def calculate_Dii(data, P, i):
    n = data.shape[0]
    y = np.sum(data.iloc[:, i] == 1)  # Cambiar esta línea

    p = y / n
    s2 = p * (1 - p) / n
    a = p * (p * (1 - p) / s2 - 1)
    b = (1 - p) * (p * (1 - p) / s2 - 1)

    Ai = y
    n = 2
    x = np.array([1, 2])
    dc = BetaBinom(a, b, n, x)
    z = dc * P
    reach = np.sum(z)
    Dii = 2 * Ai - reach

    return Dii, reach, Ai  # Devolver reach y Ai además de Dii

def update_correlation_matrix_with_Dii(correlation_matrix, data, P):
    num_media = correlation_matrix.shape[0]

    for i in range(num_media):
        Dii, reach, Ai = calculate_Dii(data, P, i)
        st.write(f"Reach para el medio {i + 1}: {reach}")
        st.write(f"Ai para el medio {i + 1}: {Ai}")

        correlation_matrix.iat[i, i] = Dii

    return correlation_matrix

data = create_dataset(M, 150)
correlation_matrix_0 = calculate_phi_correlation_matrix(data)
min_audience_matrix = create_min_audience_matrix(A_list)
correlation_matrix = adjust_correlation_matrix(correlation_matrix_0, min_audience_matrix)
st.table(correlation_matrix)


P = 150 # Cambia esto por el valor real de la población
correlation_matrix_with_Dii = update_correlation_matrix_with_Dii(correlation_matrix, data, P)
st.table(correlation_matrix)

reach_list = []
Ai_list = []

for i in range(data.shape[1]):
    Dii, reach, Ai = calculate_Dii(data, P, i)
    reach_list.append(reach)
    Ai_list.append(Ai)

result_df = pd.DataFrame({'Media': range(1, data.shape[1] + 1), 'Reach': reach_list, 'Ai': Ai_list})
st.table(result_df)


