
#-----------------------------------------------------------------#
import pandas as pd
import streamlit as st
import random
import string

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
# customize form
with st.sidebar.form(key='Twitter_form'):
    #search_term = st.text_input('¿Qué deseas buscar?', value = "unisevilla")
    search_term = st.selectbox("¿Qué deseas buscar?", ('zara_es','RealBetis','SevillaFC','JoeBiden'))
    limit = st.slider('¿Cuántos tweets deseas descargar?', 20, 200, step=20)
    
    #output_csv = st.radio('Save a CSV file?', ['Si', 'No'])
    #desde_fecha = st.date_input('¿Desde qué fecha?',value = dt.datetime.now(), key ="date_min")
    
    file_name = ''.join(random.choices(string.ascii_uppercase, k = 10))  
    file_name = st.text_input('Nombre del CSV:', value = file_name)

    submit_button = st.form_submit_button(label='Buscar tweets')

if submit_button:
  c = twint.Config()
  c.Username = search_term
  #c.Search = search_term
  c.Limit = limit
  #c.Since = desde_fecha
  c.Store_csv = True
  c.Store_object = True
  c.Custom_csv = ['date', 'tweet', 'replies_count', 'retweets_count', 'likes_count']
  c.Output = f'{file_name}.csv'
  
  twint.run.Search(c)
  
  #Tweets_df  = twint.storage.panda.Tweets_df
  Tweets_df = pd.DataFrame()
  Tweets_df = pd.read_csv(f'{file_name}.csv')
  Tweets_df = Tweets_df[['date', 'tweet', 'replies_count', 'retweets_count', 'likes_count']]
  
  len_df = len(Tweets_df.index)
  st.write('Número de tweets ', len_df)
  st.write('Limit ', limit)
  
  @st.cache
  def convert_df(df):
    return df.to_csv(sep="|").encode('utf-8')
  csv = convert_df(Tweets_df)
  st.download_button(
     "Descargar CSV",
     csv,
     "file.csv",
     "text/csv",
     key='download-csv'
  )
  
  st.table(Tweets_df)
#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
st.markdown('''
## Contáctame con cualquier duda:
- [LinkedIn](https://www.linkedin.com/in/.../) (la cuenta será actualizada en breve)
- [Mail](https://mail.google.com/mail/u/0/...) (el correo será actualizado en breve)
- [GitHub](https://github.com/...) (el código será actualizado en breve)
''', unsafe_allow_html=False)
#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
