
#-----------------------------------------------------------------#
import pandas as pd
import streamlit as st
import altair as alt
import snscrape.modules.twitter as sntwitter
import itertools

import twint
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
#-----------------------------------------------------------------#
with st.form(key='Twitter_form'):
  search_term = st.text_input('What do you want to search for?', value = 'zara_es)
  limit = st.slider('How many tweets do you want to get?', min_value=1, max_value=100, value=2, step=10)
  output_csv = st.radio('Save a CSV file?', ['Yes', 'No'])
  file_name = st.text_input('Name the CSV file:')
  submit_button = st.form_submit_button(label='Search')
if submit_button:
  # Configure
  c = twint.Config()
  c.Limit = 1
  c.Username = search_term

  # Run
  twint.run.Search(c)
  
  c.Pandas = True
  Tweets_df = twint.storage.panda.Tweets_df
  st.table(Tweets_df)
  

#-----------------------------------------------------------------#

