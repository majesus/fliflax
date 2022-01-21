"""Interactive interface for Twitter Search API.
Twitter - datasets
"""

__author__    = "Manuel J. Sánchez-Franco"
__copyright__ = "Copyright 2022, @majesus"
__credits__   = ["@majesus"]
__license__   = ""
__version__   = "0.1"
__email__     = "majesus@us.es"
#-----------------------------------------------------------------#
import pandas as pd
import streamlit as st
import altair as alt
import snscrape.modules.twitter as sntwitter
import itertools
#-----------------------------------------------------------------#
from PIL import Image
img=Image.open('img/fliflax-logo.jpg')
st.set_page_config(#layout="centered",
                   #theme="light",
                   layout="wide",
                   page_title="Fliflax",
                   page_icon=img,
                   initial_sidebar_state='expanded'
                   )
#-----------------------------------------------------------------#
st.image('img/fliflax-logo.jpg',width=200)
st.title("Fliflax: Una plataforma de apoyo al estudio")
st.markdown("Por __*Manuel J. Sánchez Franco*__, Universidad de Sevilla.")
st.write("En **Fliflax** creamos contenidos para que tu estudio de las materias de Comportamiento y Comunicacion "
         "no dependan del lugar en que te encuentras. Nuestra obsesión es la ubicuidad, o **u-learning**, "
         "es decir, queremos ofrecerte una enseñanza en cualquier momento y lugar siempre que "
         "tengas entre tus manos un teléfono móvil o una tablet.")
st.write("Abajo te mostramos, por ejemplo, unas métricas sencillas de Twitter, y en el _sidebar_ de la izquierda un **cuadro para elegir qué tipo de descarga prefieres**. ")

st.markdown("----")
#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
import datetime as dt

with st.sidebar.form("my_form"):
    st.write("**Buscador de Tweets**:")
    
    tipo = st.radio("¿Qué deseas descargar?", ('Usuario', 'Tema'), key = "type")
    username = st.text_input(label="Indica el numbre del usuario, o las palabras clave:", value = "currovillarejo")
    count = st.slider("Hasta un máximo de ...", min_value=1, max_value=600, value=20, step=10)
    fecha = st.date_input('¿Desde qué fecha?',value = dt.datetime.now())
    
    st.markdown("----")
    st.write("Si deseas descargar tweets de un usuario, indicanos:")
    
    values1=['Yes','No']
    options1=[True,False]
    dic1 = dict(zip(options1, values1))
    retweets = st.radio('¿Quieres descargar los retweets?',  options1, format_func=lambda x: dic1[x], key = "retweets", disabled = True)
    
    values2=['Yes','No']
    options2=[True,False]
    dic2 = dict(zip(options2, values2))
    replies = st.radio('¿Quieres descargar los replies?',  options2, format_func=lambda x: dic2[x], key = "retweets", disabled = True)

    submitted = st.form_submit_button("Descargar")
#-----------------------------------------------------------------#
# our search term, using syntax for Twitter's Advanced Search
search = username

# the scraped tweets, this is a generator
scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

#-----------------------------------------------------------------#

#-----------------------------------------------------------------#
