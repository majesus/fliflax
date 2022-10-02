
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

with st.sidebar.form("my_form"):
    st.write("**Buscador de Tweets**:")
    
    tipo = st.radio("¿Qué deseas descargar?", ('Usuario', 'Tema'), key = "type")
    username = st.text_input(label="Indica el numbre del usuario, o las palabras clave:", value = "BMWEspana")
    count = st.slider("Hasta un máximo de ...", min_value=1, max_value=100, value=2, step=10)
    desde_fecha = st.date_input('¿Desde qué fecha?',value = dt.datetime.now(), key ="date_min")
    hasta_fecha = st.date_input('¿Hasta qué fecha?',value = dt.datetime.now(), key ="date_max")
    
    st.markdown("----")
    st.write("Si deseas descargar tweets de un usuario, indicanos:")
    
    values1=['Yes','No']
    options1=[True,False]
    dic1 = dict(zip(options1, values1))
    retweets = st.radio('¿Quieres descargar los retweets?',  options1, format_func=lambda x: dic1[x], key = "retweets_1", disabled = True)
    
    values2=['Yes','No']
    options2=[True,False]
    dic2 = dict(zip(options2, values2))
    replies = st.radio('¿Quieres descargar los replies?',  options2, format_func=lambda x: dic2[x], key = "retweets_2", disabled = True)

    output_csv = st.radio('¿Grabar como CSV?', ['Yes', 'No'])
    file_name = st.text_input('Nombre del CSV:')
      
    submitted = st.form_submit_button(label = "Descargar")
#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
with st.form(key=’Twitter_form’):
      search_term = st.text_input('What do you want to search for?')
      limit = st.slider('How many tweets do you want to get?', 
                         min, 
                         max, 
                         step=int)
      output_csv = st.radio('Save a CSV file?', 
                             ['Yes', 'No'])
      file_name = st.text_input('Name the CSV file:')
      submit_button = st.form_submit_button(label='Search')
if submit_button:
        c = twint.Config()
        c.Search = search_term
        c.Limit = limit
        c.Store_csv = True
        if c.Store_csv:
            c.Output = f'{file_name}.csv'
        twint.run.Search(c)
data = pd.read_csv(f'{file_name}.csv', usecols=['date','tweet'])
st.table(data)
#-----------------------------------------------------------------#
#-----------------------------------------------------------------#

# IMPORTANTE: https://github.com/JustAnotherArchivist/snscrape/blob/master/snscrape/modules/twitter.py

# sd = desde_fecha.strftime("%Y-%m-%d")
# st.write(sd)

# Creating list to append tweet data to
tweets_list2 = []
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(username).get_items()):
    if i>count:
        break
    tweets_list2.append([tweet.date, tweet.content, tweet.username])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2)
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Text', 'Username'])
st.table(tweets_df2)

@st.cache
def convert_df(df):
   return df.to_csv(sep="|").encode('utf-8')

csv = convert_df(tweets_df2)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
#-----------------------------------------------------------------#

# IMPORTANTE: https://github.com/JustAnotherArchivist/snscrape/blob/master/snscrape/modules/twitter.py

tweets_list1 = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+username).get_items()):
  if i>count:
    break
  tweets_list1.append([tweet.id,
                       tweet.content,
                       tweet.date])

tweets_df1 = pd.DataFrame(tweets_list1)
st.table(tweets_df1)
#-----------------------------------------------------------------#

tweets_list1 = []
users_name = 'futbol'
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pizza near:"Madrid" within:10km').get_items()):
  if i>count:
    break
  tweets_list1.append([tweet.id,
                       tweet.content,
                       tweet.date])

tweets_df1 = pd.DataFrame(tweets_list1)
st.table(tweets_df1)
#-----------------------------------------------------------------#

loc = '34.052235, -118.243683, 10km'
tweets_list1 = []
users_name = 'futbol'
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pizza geocode:"{}"'.format(loc)).get_items()):
  if i>count:
    break
  tweets_list1.append([tweet.id,
                       tweet.content,
                       tweet.date])

tweets_df1 = pd.DataFrame(tweets_list1)
st.table(tweets_df1)
#-----------------------------------------------------------------#

import os

sd = desde_fecha.strftime("%Y-%m-%d")
ed = hasta_fecha.strftime("%Y-%m-%d")
city = "Madrid"

query = 'snscrape --jsonl --max-results 10 twitter-search "(("covid" OR "corona" OR "coronavirus" OR "positive" OR "ve") AND ' + '"{}"'.format(city) + ') AND (("Available" AND ' + 'vantilator' + ') AND ("contact" OR "mobile" OR "call" OR "number" OR "91" OR "message" OR "phone" OR "num" OR "tel")) since:' + sd + " until:" + ed + '" > COVID_data.json'
os.system(query)
df = pd.read_json('COVID_data.json', lines=True)
st.table(df)
#-----------------------------------------------------------------#

st.markdown('''
## Contáctame con cualqueir duda:
- [LinkedIn](https://www.linkedin.com/in/.../)
- [Mail](https://mail.google.com/mail/u/0/...) 
- [GitHub](https://github.com/...) (Source code will be updated soon)
''', unsafe_allow_html=False)
