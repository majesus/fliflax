#----------------------------------------------------#
import streamlit as st
#----------------------------------------------------#
# @st.cache(suppress_st_warning=False, allow_output_mutation=True)
#----------------------------------------------------#
from PIL import Image
img=Image.open('img/fliflax-logo.jpg')
st.set_page_config(#layout="centered",
                   #theme="light",
                   layout="wide",
                   page_title="Fliflax",
                   page_icon=img,
                   initial_sidebar_state='expanded'
                   )
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        #footer {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)
#----------------------------------------------------#
st.markdown(
  """ 
<style> 
.font {font-size:50px ; #font-family: 'sans-serif'; color: #ffffff;} 
</style>
""", unsafe_allow_html=True)
#----------------------------------------------------#
st.sidebar.write("## En **Fliflax** te hemos construido una calculadora de la **frecuencia efectiva mínima**.")
LC = 1
# https://discuss.streamlit.io/t/form-and-submit-button-in-sidebar/12436/3
with st.sidebar.form(key ='FormFEM'):
    st.write("## **Frec. efectiva mínima [FEM]**")
    
    values6=['Sí', 'No']
    options6=[1,2]
    dic6 = dict(zip(options6, values6))
    Lider = st.radio('¿Soy líder?', options6, format_func=lambda x: dic6[x], key = "Lider")
    
    with st.expander("Si no soy líder, clica el signo +."):
      
      values5=['No soy líder']
      options5=[1]
      dic5 = dict(zip(options5, values5))
      # No_Lider = st.selectbox('',  options5, format_func=lambda x: dic5[x], key = "No_Lider")
      
      Lider_LC = st.number_input("¿Cuál es la FEM del líder?", min_value = 0, max_value = 99, value = 4, step=1, key = "Lider_LC")
      
      values7=['Alto', 'Bajo']
      options7=[1,2]
      dic7 = dict(zip(options7, values7))
      Lider_VA = st.radio('¿El líder emplea un medio de alto o bajo valor de atención?',  options7, format_func=lambda x: dic7[x], key = "Lider_VA")
    
    values0=['Alto', 'Bajo']
    options0=[1,2]
    dic0 = dict(zip(options0, values0))
    VA = st.radio('¿Cuál es el valor de atención del medio que elijo?', options0, format_func=lambda x: dic0[x], key = "VA")
    
    values1=['Leal a mi marca', 'Favorable a mi marca', 'Leal a otra marca', 'No usuario']
    options1=[0, 1, 2, 3]
    dic1 = dict(zip(options1, values1))
    PO = st.radio('¿Cuál es la población a que me dirijo?', options1, format_func=lambda x: dic1[x], key = "PO")
    
    values2=['Reconocimiento', 'Recuerdo']
    options2=[0, LC + 1]
    dic2 = dict(zip(options2, values2))
    NM = st.selectbox('¿Cuál es mi objetivo de memoria?', options2, format_func=lambda x: dic2[x], key = "NM")
   
    values3=['Informativa', 'Transformativa']
    options3=[0, LC + 1]
    dic3 = dict(zip(options3, values3))
    ACT = st.selectbox('¿Cuál es mi estrategia comunicativa?', options3, format_func=lambda x: dic3[x], key = "ACT")
    
    values4=['Baja', 'Alta']
    options4=[0,-1]
    dic4 = dict(zip(options4, values4))
    IP = st.radio('¿Hay influencia personal positiva de otros agentes?', options4, format_func=lambda x: dic4[x], key = "IP")
    
    submitted = st.form_submit_button(label = "Calcular")

if VA == 2 and Lider_VA == 2:
  Lider_LC = Lider_LC / 2
else:
  Lider_LC = Lider_LC
   
if Lider == 1:
  if PO == 3:
    PO_cor = 2
    FEM = 1 + VA * (PO_cor + NM + ACT + IP)
  else:
    FEM = 1 + VA * (PO + NM + ACT + IP)
else:
  if PO != 3 and NM != 2 and ACT != 2:
    FEM = 1 + VA * (PO + NM + ACT + IP)
  elif PO == 3 and NM == 2 and ACT == 2:
    PO_cor = 1; NM_cor = 1; ACT_cor = 1
    FEM = 1 + VA * (PO_cor + NM_cor + ACT_cor + IP + Lider_LC)
    
  elif PO == 3 and NM != 2 and ACT != 2:
    PO_cor = 1
    FEM = 1 + VA * (PO_cor + NM + ACT + IP + Lider_LC)
  elif PO != 3 and NM == 2 and ACT != 2:
    NM_cor = 1
    FEM = 1 + VA * (PO + NM_cor + ACT + IP + Lider_LC)
  elif PO != 3 and NM != 2 and ACT == 2:
    ACT_cor = 1
    FEM = 1 + VA * (PO + NM + ACT_cor+ IP + Lider_LC)
    
  elif PO == 3 and NM == 2 and ACT != 2:
    PO_cor = 1; NM_cor = 1
    FEM = 1 + VA * (PO_cor + NM_cor + ACT + IP + Lider_LC)
  elif PO == 3 and NM != 2 and ACT == 2:
    PO_cor = 1; ACT_cor = 1
    FEM = 1 + VA * (PO_cor + NM + ACT_cor + IP + Lider_LC)
  elif PO != 3 and NM == 2 and ACT == 2:
    NM_cor = 1; ACT_cor = 1
    FEM = 1 + VA * (PO + NM_cor+ ACT_cor + IP + Lider_LC)
  else:
    st.sidebar.write("")

st.sidebar.write("La frecuencia efectiva mínima es", f"**{FEM:,.1f}**", "impactos por persona de la cobertura efectiva.")
#----------------------------------------------------#
st.image('img/fliflax-logo.jpg',width=200)
st.title("Fliflax: Una plataforma de apoyo al estudio")
st.markdown("Por __*Manuel J. Sánchez Franco*__, Universidad de Sevilla.")
st.write("En **Fliflax** creamos contenidos para que tu estudio de las materias de Comportamiento y Comunicacion "
         "no dependan del lugar en que te encuentras. Nuestra obsesión es la ubicuidad, o **u-learning**, "
         "es decir, queremos ofrecerte una enseñanza en cualquier momento y lugar siempre que "
         "tengas entre tus manos un teléfono móvil o una tablet.")
st.write("Abajo te mostramos, por ejemplo, el **modelo Beta-Binomial**, y en el _sidebar_ de la izquierda una **calculadora de la Frecuencia efectiva mínima**. "
        "También abajo hemos incluido un breve **glosario** que puede ayudarte.")
#----------------------------------------------------#
st.sidebar.markdown("""---""")
#----------------------------------------------------#
from streamlit_tags import st_tags, st_tags_sidebar
keyword = st_tags_sidebar(
    label='## Palabras clave:',
    text='Clica enter para añadir alguna más.',
    value=['publicidad', 'comportamiento', 'marketing',
          'advertising', 'behaviour'],
    suggestions=['media', 'planning'],
    maxtags = 10,
    key='1')
st.sidebar.write(keyword)
#----------------------------------------------------#
st.sidebar.markdown("""---""")
#----------------------------------------------------#
st.sidebar.write("Mi valoración, pon la cara que se ha quedado después de consultar estos contenidos ...")
img_file = st.sidebar.camera_input("")
if img_file is not None:
    st.sidebar.image(img_file)
    
#----------------------------------------------------#
st.sidebar.markdown("""---""")
#----------------------------------------------------#
#----------------------------------------------------#
#----------------------------------------------------#
st.write("### Modelo Beta-Binomial")
st.write("Beta binomial es un método de estimación de la "
         "distribución de contactos que denominamos de **Audiencia neta acumulada** "
         "(o modelo de acumulación), es decir, se programan las inserciones en un único soporte.")
st.markdown(
    '''
    La definición de cada uno de los datos de partida son los siguientes:
- **Audiencia A1**: personas que frecuentan el soporte.
- **Audiencia A2**: personas alcanzadas al menos una vez tras 2 inserciones.
- **Población P**: grupo de personas con características comunes _que contiene_ a las audiencias.
- **Inserciones n**: número de inserciones programadas para lograr los objetivos.
    '''
)
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
if st.checkbox("Si deseas ver la expresión matemática empleada, marca la casilla.", False):
    st.image('img/beta_binomial_expresion.png')
    st.warning("**A** y **B** son los parámetros de forma alpha y beta, y **n** es el número de inserciones contratadas; "
               "**i** es el valor de la distribución de contactos que pudiere interesarnos, "
               "por ejemplo, **P3** (siendo i = 3) estima la **probabilidad de exponerse exclusivamente 3 veces** contratando **n** inserciones.")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
# st.info("En nuestra calculadora, "
         # "hemos restringido los valores posibles para evitar **bugs** "
         # "relacionados con los parámetros de forma alfa y beta. "
         # "En nuestra calculadora, la Población es superior a 1.000.000 de personas, "
         # "y las audiencias inferiores a 1.000.000. "
         # "**Por su naturaleza A1 debe ser inferior a A2 y la Población superior a ambas**.")
#----------------------------------------------------#
# st.markdown("""---""")
#----------------------------------------------------#
import pandas as pd
import numpy as np
#import scipy.stats as stats
from scipy import special
#----------------------------------------------------#
st.write("### Selección de datos:")
#----------------------------------------------------#

with st.form(key ='Form1'):
  col1, col2 = st.columns([5,5])
  with col1:
    A1 = st.number_input("Audiencia acumulada tras 1 inserción:", min_value = 1, max_value = pow(10, 10), value = 500000, step=100, key = "A1")
  with col2:
    A2 = st.number_input("Audiencia acumulada tras 2 inserciones:", min_value = 1, max_value = pow(10, 10), value = 550000, step=100, key = "A2")
  col1, col2 = st.columns([5,5])
  with col1:
    P = st.number_input("Población:", min_value = 1, max_value = pow(10, 10), value = 1000000, step=100, key = "poblacion")
  with col2:
    Precio = st.number_input("Precio de una inserción €:", min_value = 1, max_value = pow(10, 10), value = 1000, step=100, key = "precio")
  
  inserciones = st.slider("Inserciones:", 2, 50, value = 5, step=1, key = "inserciones")
    
  submitted = st.form_submit_button("Calcular")

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
n = inserciones
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
st.write("### Resultados:")
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
    st.table(df1.head().style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'})) 
    st.info("En nuestro Anexo de abajo, puedes ver todos los valores de Pi y Ri.")
    #st.balloons()
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
import altair as alt

df1 = df.set_index('exposiciones')
df1 = pd.DataFrame(df1)

if st.checkbox("Si deseas ver la representación gráfica de la distribución de contactos Pi (y acumulada Ri), marca la casilla.", False):
    st.write('###### Figura 1. Distribución de contactos Pi')
    
    g = alt.Chart(df).mark_area().encode(
      x=alt.Y('exposiciones', axis=alt.Axis(tickCount=n)),
      y='Pi'
    ).configure_mark(
      opacity=0.5,
      color='red'
    ).configure_axis(
      grid=False
    )
    st.altair_chart(g, use_container_width = True)
    #st.balloons()
    
    st.markdown("""---""")
    
    st.write('###### Figura 2. Distribución de contactos acumulada Ri')
    g = alt.Chart(df).mark_area().encode(
      x=alt.Y('exposiciones', axis=alt.Axis(tickCount=n)),
      y='Ri'
    ).configure_mark(
      opacity=0.5,
      color='blue'
    ).configure_axis(
      grid=False
    )
    st.altair_chart(g, use_container_width = True)
    #st.balloons()
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Frecuencia efectiva mínima")
#----------------------------------------------------#
if df.lt(0).any().any() == True:
  st.write("#### Observaciones:")
  st.error("Puedes comprobar que en la tabla se muestran valores extraños, por ejemplo, valores negativos. "
            "Debes revisar los valores de A1 y A2. "
            "Corrígelo antes de seleccionar ningún valor de i.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)

st.write("En este apartado puedes seleccionar los valores de Pi y Ri cuyo valor desees conocer de modo preciso. "
         "El valor i que elijas, puede corresponderse, por ejemplo, con la frecuencia efectiva mínima que "
         "has prupuesto como objetivo en tu plan de medios y soportes. "
         "Recuerda que **la frecuencia efectiva mínima es el mínimo número de impactos por persona de la cobertura efectiva para alcanzar** "
         "**(por encima de un determinado nivel crítico)** "
         "**los objetivos de comunicación**.")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
pd.options.display.float_format = '{:,}'.format
df1 = df.set_index('exposiciones')
selected_indices = st.multiselect('Selecciona el/los valor/es i:', df1.index)
selected_indices = map(lambda selected_indices:selected_indices, selected_indices)
selected_rows = df1.loc[selected_indices]
st.markdown("""---""")
st.write('###### Tabla 2. Valores de Pi y Ri seleccionados')
# st.table(selected_rows)
st.table(selected_rows.style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'})) 
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Referencias:")
#----------------------------------------------------#
st.info("Finalmente, para profundizar en estos materiales, te recomendamos consultar la tesis doctoral de "
         "**Joaquín Aldás Manzano** de 1998, Catedrático actualmente en la Universidad de Valencia. ")
st.info("También, te recomendamos visitar el siguiente enlace: [Wikipedia: Beta-Binomial](https://es.wikipedia.org/wiki/Distribuci%C3%B3n_beta-binomial)")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Anexos")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
if df.lt(0).any().any() == True:
  st.write("#### Observaciones:")
  st.error("Puedes comprobar que en la tabla se muestran valores extraños, por ejemplo, valores negativos. "
            "Es debido probablemente a que el valor de A2 es superior a A1, y eso no es posible.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)

st.write('###### Anexo 1. Distribución de contactos Pi (y acumulada Ri)')
#df = df.set_index('exposiciones')
if st.checkbox("Si deseas ver la tabla completa de valores de Pi y Ri alcanzados, marca la casilla.", False):
    st.write('###### Distribución de contactos Pi (y acumulada Ri)')
    st.table(df1.style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'})) 
    st.write('Parámetros de forma: alfa: ',f"{alphas:,.3f}",'y beta: ',f"{betas:,.3f}")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write('###### Anexo 2. Glosario')
dfg = pd.read_csv('csv/conceptos_basicos_planificacion.txt', sep=",")
dfg1 = dfg.set_index('concepto')
selected_indices = st.multiselect('Selecciona el/los concepto/es:', dfg1.index)
selected_indices = map(lambda selected_indices:selected_indices, selected_indices)
selected_rows = dfg1.loc[selected_indices]
st.write('###### Glosario')
st.table(selected_rows.definicion)
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
