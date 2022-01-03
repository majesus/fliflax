#----------------------------------------------------#
#----------------------------------------------------#
import streamlit as st
#----------------------------------------------------#
st.set_page_config(layout="centered",
                   page_title="Fliflax",
                   page_icon=":smiley",
                   initial_sidebar_state='expanded'
                   )
#----------------------------------------------------#
st.markdown(""" <style> .font {
    font-size:50px ; font-family: 'Consolas'; color: #000000;} 
    </style> """, unsafe_allow_html=True)
#----------------------------------------------------#
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image("Avatar-con-naming-Fliflax.jpg", use_column_width=True, width = 400)
#----------------------------------------------------#
st.markdown('<p style="font-family:Consolas; color:#000000; font-size: 50px;"><b>Modelo Beta-binomial</b></p>', unsafe_allow_html=True)
#----------------------------------------------------#
st.write("Beta binomial es un método de estimación de la "
         "distribución de contactos que denominamos de Audiencia neta acumulada "
         "(o modelo de acumulación), es decir, se trabaja con un único soporte. "
         ""
         "Los datos de inicio son los siguientes: A1, es decir, la audiencia del soporte; "
         "A2, es decir, la audiencia acumulada tras la segunda inserción, y n, es decir, "
         "el número de inserciones que contratamos en el único soporte que seleccionamos."
         "")
#----------------------------------------------------#
import pandas as pd
import numpy as np
#import scipy.stats as stats
from scipy import special
#----------------------------------------------------#
st.markdown('<p style="font-family:Consolas; color:#000000; font-size: 35px;">Selección de datos:</p>', unsafe_allow_html=True)
#----------------------------------------------------#
#----------------------------------------------------#
A1_default = 500000; A2_default = 550000
A2_max = round(A1_default * 1.6)

A1 = st.number_input("Audiencia acumulada tras 1 inserción", min_value = 1, value = A1_default, step=100, key = "A1")
# st.write("Valor elegido: {:.0f}".format(A1))
A2 = st.number_input("Audiencia acumulada tras 2 inserciones", min_value = A1+1, max_value = A2_max, value = A2_default, step=100, key = "A2")
# st.write("Valor elegido: {:.0f}".format(A2))
P = st.number_input("Población", min_value = A2, value = 1000000, step=100, key = "poblacion")
# st.write("Valor elegido: {}".format(P))
#----------------------------------------------------#
inserciones = st.slider("inserciones", 2, 100, value = 5, step=1, key = "inserciones")
# st.write("Valor elegido: {}".format(inserciones))
#----------------------------------------------------#
n = inserciones
#----------------------------------------------------#
R1=A1/P;R2=A2/P
#----------------------------------------------------#
#----------------------------------------------------#
try:
    alpha=((R1)*((R2)-(R1)))/(2*(R1)-(R1)*(R1)-(R2))
    beta=(alpha*(1-R1))/(R1)
except ZeroDivisionError as e:
    # for example
    alpha = 0.125
    beta = 0.125
    n = 5
    st.markdown('<p style="font-family:Consolas; color:Red; font-size: 14px;"><b>Hay un problema con A2. Debes revisarlo, por favor.</b></p>', unsafe_allow_html=True)
#----------------------------------------------------#
x = np.arange(1,n+1)
alphas = alpha
betas = beta
# n = insertions
#----------------------------------------------------#
# https://docs.pymc.io/en/v3/api/distributions/discrete-2.py
# https://docs.scipy.org/doc/scipy/tutorial/stats/discrete_betabinom.html
def BetaBinom(a, b, n, x):
    pmf = special.binom(n, x) * (special.beta(x+a, n-x+b) / special.beta(a, b))
    return pmf

pmf = BetaBinom(alphas, betas, n, x)
# Pi:
y = pmf*1000000
# Ri:
Ri = np.flip(y); Ri = np.cumsum(Ri); Ri = np.flip(Ri)
#----------------------------------------------------#
st.markdown('<p style="font-family:Consolas; color:#000000; font-size: 35px;">Resultados:</p>', unsafe_allow_html=True)
#----------------------------------------------------#
data = {'exposiciones':  x, 'Pi': y, 'Ri': Ri}

df = pd.DataFrame(data)
df = df.head(n=n)

if df.lt(0).any().any() == True:
    st.markdown('<p style="font-family:Consolas; color:Red; font-size: 14px;"><b>Hay un problema con el valor de <b>A2</b>. Puedes observar que obtienes valores negativos en la tabla de la distribución de contactos. <b>El valor de A2 es excesivo en comparación con A1</b>, y la distribución no sabe interpretarlo correctamente.</b></p>', unsafe_allow_html=True)
else:
    st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)

#----------------------------------------------------#
st.write("Dibujamos "
         "la representación gráfica de la distribución de contactos "
         "mediante el trazado de una curva suave en Matplotlib. "
         "La curva representa Pi, es decir, el número de personas alcanzadas exclusivamente i veces."
         "")
#----------------------------------------------------#
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.interpolate import make_interp_spline
model=make_interp_spline(df.exposiciones, df.Pi)
xs=np.linspace(1, n, 500)
ys=model(xs)

rcParams['font.family'] = 'monospace'
rcParams['font.size'] = 8
#fig = plt.figure(figsize=(4, 4))
plt.grid(b=True, which='major', color='#ffffff', linestyle='-')
plt.figure(facecolor='white')
plt.ticklabel_format(style="plain")

fig, ax = plt.subplots()
ax.plot(xs,ys, label="spline")
ax.set_facecolor("white")
plt.title("Distribución de contactos")
plt.xticks(x,x)
plt.xlabel("Exclusivamente i veces")
plt.ylabel("Personas")
plt.legend()
st.pyplot(fig)
#----------------------------------------------------#
st.write("A continuación, te mostramos la tabla de valores Pi y Ri alcanzados. "
         "Pi es la distribución de contactos, y Ri la distribución de contactos acumulada. "
         "A modo de resumen, señalamos que "
         "el valor de la cobertura es igual a", round(df['Ri'].iloc[0]), "personas. "
         "Es el primer valor de Ri, es decir, las personas alcanzadas al menos una vez. "
         "A su vez, la suma de Ri es el total de impactos logrados, en este caso,", round(df['Ri'].sum())," impactos. "
         "Otro modo de calcular los impactos es mediante el producto de A1 x n, siendo n el total de inserciones. "
         "Y una vez que hemos calculado los impactos, la frecuencia media no es más que el cociente entre "
         "los impactos y la cobertura, es decir,", round(df['Ri'].sum() / df['Ri'].iloc[0]),"impactos por persona de la cobertura."
         "")

# st.write("Distribución de contactos (y acumulada):")
st.table(df.style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'}))      
#----------------------------------------------------#
#----------------------------------------------------#

