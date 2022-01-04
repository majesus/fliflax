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
    #font-family: 'sans-serif'; 
    color: #000000;} 
    </style> """, unsafe_allow_html=True)
#----------------------------------------------------#
col1, col2, col3 = st.columns([2.5, 5, 0.2])
col1.image("Avatar-con-naming-Fliflax.jpg", use_column_width=True, width = 400)
with col2:
    st.markdown('<div style="text-align:center"><p style="font-family:sans-serif; color:#000000; font-size: 50px;"><b>Modelo<br>Beta-Binomial</b></p></div>', unsafe_allow_html=True)
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("Beta binomial es un método de estimación de la "
         "distribución de contactos que denominamos de Audiencia neta acumulada "
         "(o modelo de acumulación), es decir, se trabaja con un único soporte. ")
st.write("Los datos de inicio son los siguientes: A1 (la audiencia del soporte); "
         "A2 (la audiencia acumulada tras la segunda inserción); n "
         "(el número de inserciones que contratamos en el único soporte que seleccionamos), "
         "y la población.")
#----------------------------------------------------#
# st.markdown("""---""")
#----------------------------------------------------#
st.info("Es importante señalar que en nuestra aplicación Fliflax, "
         "hemos restringido los valores para evitar los bugs "
         "relacionados con los parámetros de forma alfa y beta. "
         "La Población debe ser superior o igual a 1.000.000 de personas, "
         "y las audiencias, A1 y A2, deben ser inferiores a 1.000.000. "
         "Por su naturaleza A1 debe ser inferior a A2.")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
import pandas as pd
import numpy as np
#import scipy.stats as stats
from scipy import special
#----------------------------------------------------#
st.write("### Selección de datos:")
#----------------------------------------------------#
col1, col2 = st.columns([5,5])
with col1:
    A1 = st.number_input("Audiencia acumulada tras 1 inserción:", min_value = 1, max_value = pow(10, 6), value = 500000, step=100, key = "A1")
    # st.write("Valor elegido: {:.0f}".format(A1))
with col2:
    A2 = st.number_input("Audiencia acumulada tras 2 inserciones:", min_value = 1, max_value = pow(10, 6), value = 550000, step=100, key = "A2")
    # st.write("Valor elegido: {:.0f}".format(A2))

if A1 > A2:
  st.write("##### Observaciones:")
  st.warning("El valor de A2 es inferior a A1. No olvides corregirlo antes de continuar.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)  
    
col1, col2 = st.columns([5,5])
with col1:
    P = st.number_input("Población:", min_value = pow(10, 6), max_value = pow(10, 10), value = 1000000, step=100, key = "poblacion")
    # st.write("Valor elegido: {}".format(P))
with col2:    
    Precio = st.number_input("Precio de una inserción €:", min_value = 1, max_value = pow(10, 10), value = 1000000, step=100, key = "precio")
    # st.write("Valor elegido: {}".format(P))

if P < A2:
  st.write("##### Observaciones:")
  st.warning("El valor de la Población es inferior a A2. No olvides corregirlo antes de continuar.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)    
#----------------------------------------------------#
inserciones = st.slider("Inserciones:", 2, 100, value = 5, step=1, key = "inserciones")
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
  st.write("#### Observaciones:")
  # datos de muestra:
  alpha = 0.125
  beta = 0.125
  n = 5
  st.warning("Se ha producido una excepción al proponerse un valor de A2 que provoca una división por 0. "
             "Puede ser debido a varias razones, por ejemplo, que el valor A2 esté muy próximo al valor de la población "
             "y se produzca un bug al no poderlo modelizar la distribución Beta-Binomial. "
             "Debes pues revisarlo antes de continuar. Mientras tanto, "
             "los resultados que ves abajo, se corresponden con valores ficticios de los parámetros de forma.")
if alpha, beta <= 0:
  st.write("##### Observaciones:")
  st.warning("Los parámetros de forma alfa y beta son negativos, y violan un presupuesto de partida.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)  
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
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Resultados:")
#----------------------------------------------------#
st.write("Derivado de tus datos y siempre que se ajuesten a las premisas del modelo Beta-Binomial, "
         "el valor de la cobertura alcanzada es igual a", f"{round(df['Ri'].iloc[0]):,.0f}", "personas. "
         "Es decir,", f"{round(df['Ri'].iloc[0]):,.0f}", "personas se exponen al menos 1 vez."
         "Los impactos logrados son", f"{A1 * n:,.0f}"," impactos. "
         "La frecuencia media es pues igual a", f"{round(df['Ri'].sum() / df['Ri'].iloc[0]):,.0f}","impactos por persona de la cobertura.")
st.write("Junto a lo anterior, el valor GRP es igual a", f"{round(df['Ri'].sum() * 100 / P):,.0f}","impactos por cada 100 personas de la población. "
         "Y junto a los GRP te mostramos el valor CPP (coste por punto de rating), en este caso "
         "el coste monetario de alcanzar a un 1 % de la población es igual a", f"{round(Precio * n / (df['Ri'].sum() * 100 / P)):,.0f}","€. "
         "El valor CPP es el resultado de divir el presupuesto (el coste asociado al plan propuesto "
         "y los GRP a contratar.")
st.write("A continuación, te ofrecemos un breve resumen.")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Cobertura", value = f"{round(df['Ri'].iloc[0]):,.0f}")
with col2:
    st.metric(label="Frecuencia media", value = f"{round(df['Ri'].sum() / df['Ri'].iloc[0]):,.0f}")
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
st.write("A continuación, también te dibujamos "
         "la representación gráfica de la distribución de contactos Pi (y acumulada Ri) "
         "mediante el trazado de una curva suave (spline) en Matplotlib. ")

#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write('###### Figura 1. Distribución de contactos Pi (y acumulada Ri)')

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
#plt.title("Distribución de contactos")
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
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Frecuencia efectiva mínima")
#----------------------------------------------------#
if df.lt(0).any().any() == True:
  st.write("#### Observaciones:")
  st.warning("Puedes comprobar que en la tabla se muestran valores extraños, por ejemplo, valores negativos. "
            "Es debido probablemente a que el valor de A2 es superior a A1, y eso no es posible. "
            "Corrígelo antes de seleccionar ningún valor de i.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)

st.write("En este apartado puedes seleccionar los valores de Pi y Ri cuyo valor desees conocer de modo preciso. "
         "El valor i que elijas, puede corresponderse, por ejemplo, con la frecuencia efectiva mínima que "
         "has prupuesto como objetivo en tu plan de medios y soportes. "
         "Recuerda que la frecuencia efectiva mínima es el mínimo número de impactos por persona de la cobertura efectiva para alcanzar "
         "(por encima de un determinado nivel crítico) "
         "los objetivos de comunicación.")
pd.options.display.float_format = '{:,}'.format
df = df.set_index('exposiciones')
selected_indices = st.multiselect('Selecciona el/los valor/es i:', df.index)
selected_indices = map(lambda selected_indices:selected_indices, selected_indices)
selected_rows = df.loc[selected_indices]
st.write('###### Tabla 1. Valores de Pi y Ri seleccionados')
st.table(selected_rows)
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Referencias:")
#----------------------------------------------------#
st.write("Finalmente, para profundizar en estos materiales, te recomendamos consultar la tesis doctoral de "
         "Joaquín Aldás Manzano de 1998, Catedrático actualmente en la Universidad de Valencia. ")
st.write("También, te recomendamos visitar el siguiente enlace:","[Wikipedia: Beta-Binomial](https://es.wikipedia.org/wiki/Distribuci%C3%B3n_beta-binomial)")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Anexo")
#----------------------------------------------------#
if df.lt(0).any().any() == True:
  st.write("#### Observaciones:")
  st.warning("Puedes comprobar que en la tabla se muestran valores extraños, por ejemplo, valores negativos. "
            "Es debido probablemente a que el valor de A2 es superior a A1, y eso no es posible.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)

st.write('###### Anexo 1. Distribución de contactos Pi (y acumulada Ri)')
# st.write("Distribución de contactos (y acumulada):")
#df = df.set_index('exposiciones')
st.table(df.style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'})) 
st.write('Parámetros de forma: alfa: ',f"{alpha:,.3f}",'y beta: ',f"{alpha:,.3f}")
#----------------------------------------------------#
