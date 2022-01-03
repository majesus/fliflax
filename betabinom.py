#----------------------------------------------------#
#----------------------------------------------------#
import streamlit as st
#----------------------------------------------------#
st.set_page_config(layout="centered",
                   page_title="Fliflax",
                   page_icon=":smiley"
                   #initial_sidebar_state='expanded'
                   )
#----------------------------------------------------#
st.markdown(""" <style> .font {
    font-size:50px ; 
    #font-family: 'Consolas'; 
    color: #000000;} 
    </style> """, unsafe_allow_html=True)
#----------------------------------------------------#
col1, col2, col3 = st.columns([2.5, 5, 0.2])
col1.image("Avatar-con-naming-Fliflax.jpg", use_column_width=True, width = 400)
with col2:
    st.markdown('<div style="text-align:center"><p style="font-family:sans-serif; color:#000000; font-size: 50px;"><b>Modelo<br>Beta-Binomial</b></p></div>', unsafe_allow_html=True)
#----------------------------------------------------#

#----------------------------------------------------#
st.write("Beta binomial es un método de estimación de la "
         "distribución de contactos que denominamos de Audiencia neta acumulada "
         "(o modelo de acumulación), es decir, se trabaja con un único soporte. ")
st.write("Los datos de inicio son los siguientes: A1, es decir, la audiencia del soporte; "
         "A2, es decir, la audiencia acumulada tras la segunda inserción, y n, es decir, "
         "el número de inserciones que contratamos en el único soporte que seleccionamos.")
#----------------------------------------------------#
import pandas as pd
import numpy as np
#import scipy.stats as stats
from scipy import special
#----------------------------------------------------#
# st.markdown('<p style="font-family:Consolas; color:#000000; font-size: 35px;">Selección de datos:</p>', unsafe_allow_html=True)
st.write("### Selección de datos:")
#----------------------------------------------------#
A1_default = 500000

col1, col2 = st.columns([5,5])
with col1:
    A1 = st.number_input("Audiencia acumulada tras 1 inserción", min_value = 1, max_value = pow(10, 10), value = A1_default, step=100, key = "A1")
    # st.write("Valor elegido: {:.0f}".format(A1))
with col2:
    A2 = st.number_input("Audiencia acumulada tras 2 inserciones", min_value = 1, max_value = pow(10, 10), value = 550000, step=100, key = "A2")
    # st.write("Valor elegido: {:.0f}".format(A2))

col1, col2 = st.columns([5,5])
with col1:
    P = st.number_input("Población", min_value = 1, max_value = pow(10, 10), value = 1000000, step=100, key = "poblacion")
    # st.write("Valor elegido: {}".format(P))
with col2:    
    Precio = st.number_input("Precio de una inserción €", min_value = 1, max_value = pow(10, 10), value = 1000000, step=100, key = "precio")
    # st.write("Valor elegido: {}".format(P))
#----------------------------------------------------#
inserciones = st.slider("inserciones", 2, 100, value = 5, step=1, key = "inserciones")
# st.write("Valor elegido: {}".format(inserciones))
#----------------------------------------------------#
n = inserciones
#----------------------------------------------------#
R1=A1/P;R2=A2/P
#----------------------------------------------------#
try:
    alpha=((R1)*((R2)-(R1)))/(2*(R1)-(R1)*(R1)-(R2))
    beta=(alpha*(1-R1))/(R1)
except ZeroDivisionError as e:
    # for example
    alpha = 0.125
    beta = 0.125
    n = 5
    st.markdown('<p style="font-family:Consolas; color:Red; font-size: 14px;">Se ha producido una excepción al proponerse un valor de A2 que provoca una división por 0. Debes revisarlo antes de continuar.</p>', unsafe_allow_html=True)
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
data = {'exposiciones':  x, 'Pi': y, 'Ri': Ri}

df = pd.DataFrame(data)
df = df.astype(int)
pd.options.display.float_format = '{:,}'.format
df = df.head(n=n)

if df.lt(0).any().any() == True:
  st.write("### Observaciones:")
  st.markdown('<p style="font-family:Consolas; color:Red; font-size: 14px;"><b>En este momento el valor de <b>A2</b> es inferior a A1. No olvides corregirlo antes de continuar.</p>', unsafe_allow_html=True)
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)
    
if P < A2:
  st.write("### Observaciones:")
  st.markdown('<p style="font-family:Consolas; color:Red; font-size: 14px;"><b>En este momento el valor de <b>P</b> es inferior a A2. No olvides corregirlo antes de continuar.</p>', unsafe_allow_html=True)
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)
#----------------------------------------------------#
# st.markdown('<p style="font-family:Consolas; color:#000000; font-size: 35px;">Resultados:</p>', unsafe_allow_html=True)
st.write("### Resultados:")
#----------------------------------------------------#
st.write("A modo de resumen, y como te mostramos en los sliders de resultados, "
         "con los datos correctos de arriba, el valor de la cobertura es igual a", f"{round(df['Ri'].iloc[0]):,.0f}", "personas. "
         "Es decir,", f"{round(df['Ri'].iloc[0]):,.0f}", "personas se exponen al menos 1 vez. " 
         "La cobertura es pues el primer valor de Ri (distribución de contactos acumulada). "
         "Te recordamos que Pi hace referencia a las personas alcanzadas exclusivamente i veces, y "
         "Ri a las personas alcanzadas al menos i veces.")
st.write("A su vez, la suma de los valores de Ri (desde 1 hasta n), "
         "siendo n el total de inserciones, es igual al total de impactos. "
         "Otro modo inmediato para calcular los impactos es mediante el producto de A1 x n, "
         "en este caso,", f"{A1 * n:,.0f}"," impactos")
st.write("Y una vez que hemos calculado los impactos, la frecuencia media no es más que el cociente entre "
         "los impactos y la cobertura, es decir, la frecuencia es igual a", f"{round(df['Ri'].sum() / df['Ri'].iloc[0]):,.0f}","impactos por persona de la cobertura.")
st.write("Los resultados que te mostramos abajo, son los derivados de los datos que nos has facilitado en el bloque: Selección de datos.")

col1, col2 = st.columns([5,5])
with col1:
    st.slider("Cobertura", 1, max_value= P, value = round(df['Ri'].iloc[0]), step=None, key = "cobertura")
with col2:
    st.slider("Frecuencia media", 1, max_value= n, value = round(df['Ri'].sum() / df['Ri'].iloc[0]), step=None, key = "frecuencia")
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
st.write("Junto a lo anterior, y también en los sliders de arriba, te mostramos el valor GRP "
         "(número medio de impactos por cada 100 personas de la población). "
         "Y junto a los GRP te mostramos el valor CPP (coste por punto de rating), es decir, el coste monetario de alcanzar a un 1 % de la población. El valor CPP "
         "es el resultado de divir el presupuesto (el coste asociado al plan propuesto, i.e., Precio de una inserción x n) "
         "y el volumen de GRP a contratar.")
st.write("También te dibujamos "
         "la representación gráfica de la distribución de contactos (y acumulada) "
         "mediante el trazado de una curva suave (spline) en Matplotlib. "
         "La curva representa los valores de Pi "
         "y también los valores de Ri."
         "")
#----------------------------------------------------#
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.interpolate import make_interp_spline
model1=make_interp_spline(df.exposiciones, df.Pi)
xs1=np.linspace(1, n, 500)
ys1=model1(xs1)
model2=make_interp_spline(df.exposiciones, df.Ri)
xs2=np.linspace(1, n, 500)
ys2=model2(xs2)

rcParams['font.family'] = 'monospace'
rcParams['font.size'] = 8
#fig = plt.figure(figsize=(4, 4))
plt.grid(b=True, which='major', color='#ffffff', linestyle='-')
plt.figure(facecolor='white')
plt.ticklabel_format(style="plain")

fig, ax = plt.subplots()
ax.plot(xs1,ys1, label="Pi, spline")
ax.plot(xs2,ys2, label="Ri, spline")
ax.set_facecolor("white")
plt.title("Distribución de contactos")
#plt.xticks(x,x)

if n < 20:
    plt.xticks(np.arange(1, n+1, 1))
else:
    plt.xticks(np.arange(1, n+1, 5))

plt.xlabel("i veces")
plt.ylabel("Personas")
plt.legend()
st.pyplot(fig)
 
#----------------------------------------------------#
st.write("### Frecuencia efectiva mínima")
st.write("A continuación, puedes seleccionar los valores de Pi y Ri cuyo valor desees conocer de modo preciso. "
         "El valor i elegido puede corresponderse, por ejemplo, con la frecuencia efectiva mínima que has prupuesto como objetivo en tu plan de medios y soportes. "
         "Recuerda que la frecuencia efectiva mínima es el mínimo número de impactos por persona de la cobertura efectiva para alcanzar "
         "los objetivos de comunicación por encima de un determinado nivel crítico.")
pd.options.display.float_format = '{:,}'.format
df = df.set_index('exposiciones')
selected_indices = st.multiselect('Selecciona el/los valor/es i:', df.index)
selected_indices = map(lambda selected_indices:selected_indices, selected_indices)
selected_rows = df.loc[selected_indices]
st.write('##### Filas seleccionadas')
st.table(selected_rows)
#----------------------------------------------------#
st.write("### Referencias:")
st.write("Finalmente, para profundizar en estos materiales, te recomendamos consultar la tesis doctoral de "
         "Joaquín Aldás Manzano de 1998, Catedrático actualmente en la Universidad de Valencia. ")

st.write("También, te recomendamos visitar el siguiente enlace: https://es.wikipedia.org/wiki/Distribuci%C3%B3n_beta-binomial")
#----------------------------------------------------#
st.write("### Anexo")
st.write("Como datos complentarios te mostramos el detalle de la tabla de valores Pi y Ri alcanzados. "
         "Como hemos señalado arriva, la columna Pi representa la distribución de contactos, "
         "que se relaciona con la frecuencia efectiva, y Ri es la distribución de contactos acumulada, "
         "que se relaciona con la frecuencia efectiva mínima. ")
# st.write("Distribución de contactos (y acumulada):")
#df = df.set_index('exposiciones')
st.table(df.style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'}))    
#----------------------------------------------------#
