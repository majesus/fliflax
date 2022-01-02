import streamlit as st
#----------------------------------------------------#
st.set_page_config(layout="centered",
                   page_title="Fliflax",
                   page_icon="🧊",
                   menu_items={
                       'Ayuda': 'https://www.us.es',
                       '¿Algún error?': "https://www.us.es",
                       '¿QUuiénes somos?': "# Fliflax"
                       })
#st.set_page_config(page_title="Fliflax")
#st.set_page_config(page_icon="🧊")
#----------------------------------------------------#
st.markdown(""" <style> .font {
    font-size:50px ; font-family: 'Consolas'; color: #000000;} 
    </style> """, unsafe_allow_html=True)
#----------------------------------------------------#

st.markdown('<p style="font-family:Consolas; color:#000000; font-size: 50px;"><b>Modelo Beta-binomial</b></p>', unsafe_allow_html=True)

#----------------------------------------------------#
st.image(
    ".png",
    width=100,
)
#----------------------------------------------------#
import matplotlib.pyplot as plt
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
    st.markdown('<p style="font-family:Consolas; color:Red; font-size: 20px;"><b>Hay un problema con A2. Debes revisarlo, por favor.</b></p>', unsafe_allow_html=True)
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
# To make all your floats show comma separators by default in pandas versions 0.23 through 0.25 set the following:
#pd.options.display.float_format = '{:,}'.format
data = {'exposiciones':  x, 'Pi': y, 'Ri': Ri}

df = pd.DataFrame(data)
df = df.head(n=n)

if df.lt(0).any().any() == True:
    st.markdown('<p style="font-family:Consolas; color:Red; font-size: 20px;"><b>Hay un problema con A2. Debes revisarlo, por favor. Puedes comprobar que obtienes valores negativos; es muy probable que se deba a que el valor de A2 es excesivo en comparación con A1</b></p>', unsafe_allow_html=True)
else:
    st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;">A continuación, te mostramos los principales resultados.</p>', unsafe_allow_html=True)

#----------------------------------------------------#
st.write("Por un lado, se dibuja "
         "la representación gráfica de la distribución de contactos,"
         "es decir, el número de personas alcanzadas exclusivamente i veces. En nuestro ejemplo,"
         "el valor de la cobertura es ", round(df['Ri'].iloc[0]),
         "Por otro lado, se muestra también la tabla de valores de Pi y Ri alcanzados. "
         "En ella localizas algunos de los valores citados anteriormente.")
#----------------------------------------------------#
from scipy.interpolate import make_interp_spline
model=make_interp_spline(df.exposiciones, df.Pi)
xs=np.linspace(1, n, 500)
ys=model(xs)

from matplotlib import rcParams
rcParams['font.family'] = 'monospace'
rcParams['font.size'] = 8
#plt.style.use('seaborn-darkgrid')
fig = plt.figure(figsize=(4, 4))
plt.grid(b=True, which='major', color='#ffffff', linestyle='-')

plt.figure(facecolor='white')
plt.ticklabel_format(style="plain")
#fig = plt.plot(df.exposiciones,df.Pi, label="original")
fig = plt.plot(xs,ys, label="spline")


plt.title("Distribución de contactos")
plt.xlabel("Exclusivamente i veces")
plt.ylabel("Personas")
plt.legend()

ax = plt.axes()
ax.set_facecolor("white")

st.pyplot(plt)
#----------------------------------------------------#
st.write("Distribución de contactos (y acumulada):")
st.table(df.style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'}))
             
#----------------------------------------------------#
#----------------------------------------------------#
