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
import pandas as pd
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
# Creating list to append tweet data 
tweets_list1 = []
# https://github.com/JustAnotherArchivist/snscrape/blob/master/snscrape/modules/twitter.py
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(username).get_items()): 
  if i>count: #number of tweets you want to scrape
    break
  tweets_list1.append([tweet.date, 
                       tweet.id, 
                       tweet.content, 
                       tweet.user.username,
                       tweet.retweetCount,
                       tweet.retweetedTweet,
                       tweet.renderedContent,
                       tweet.outlinks,
                       tweet.tcooutlinks,
                       tweet.replyCount,
                       tweet.likeCount,
                       tweet.quoteCount,
                       tweet.conversationId,
                       tweet.lang,
                       tweet.source,
                       tweet.sourceUrl,
                       tweet.sourceLabel,
                       tweet.media,
                       tweet.quotedTweet,
                       tweet.mentionedUsers,
                       tweet.url,
                       tweet.coordinates,
                       tweet.place,
                       tweet.hashtags,
                       tweet.cashtags,
                       tweet.inReplyToTweetId,
                       tweet.inReplyToUser
                      ]) 

# Creating a dataframe from the tweets list above 
results = pd.DataFrame(tweets_list1, 
                          columns=['Datetime',
                                   'Tweet Id',
                                   'Text',
                                   'Username',
                                   'retweetCount',
                                   'retweetedTweet',
                                   'renderedContent',
                                   'outlinks',
                                   'tcooutlinks',
                                   'replyCount',
                                   'likeCount',
                                   'quoteCount',
                                   'conversationId',
                                   'lang',
                                   'source',
                                   'sourceUrl',
                                   'sourceLabel',
                                   'media',
                                   'quotedTweet',
                                   'mentionedUsers',
                                   'url',
                                   'coordinates',
                                   'place',
                                   'hashtags',
                                   'cashtags',
                                   'inReplyToTweetId',
                                   'inReplyToUser'
                                   ])
#-----------------------------------------------------------------#

if st.checkbox("If you want to see the tweets downloaded by date, click here.", False):
  st.markdown("----")
  st.table(results)
  
st.markdown("----")

# https://altair-viz.github.io/user_guide/times_and_dates.html

if st.checkbox("Si deseas ver la representación gráfica de los retweets, haz clic aquí.", False):
  #import altair as alt
  st.markdown("----")
  results.loc[results.retweetCount == 0, 'retweetCount'] = 0.001 # log
  chart = alt.Chart(results).mark_area(color = "lightblue", interpolate = "step-after", line = True, opacity=0.3,).encode(
    x=alt.X('timestamps:T', title='', axis=alt.Axis(labelOverlap="greedy",grid=False)),
    y=alt.Y('retweetCount', scale=alt.Scale(type='log')))
  st.altair_chart(chart, use_container_width=True)

st.markdown("----")

if st.checkbox("Si deseas ver la representación gráfica de los likes, haz clic aquí.", False):
  #import altair as alt
  st.markdown("----")
  results.loc[results.likeCount == 0, 'likeCount'] = 0.001 # log
  chart = alt.Chart(results).mark_area(color = "lightblue", interpolate = "step-after", line = True, opacity=0.3,).encode(
    x=alt.X('timestamps:T', title='', axis=alt.Axis(labelOverlap="greedy",grid=False)),
    y=alt.Y('likeCount', scale=alt.Scale(type='log')))
  st.altair_chart(chart, use_container_width=True)
  
st.markdown("----")
#-----------------------------------------------------------------#

st.write("#### A continuación, te mostramos la evolución semanal de retweets y likes.")

st.markdown("----")

results['start_date'] = pd.to_datetime(results['Datetime']) - pd.to_timedelta(7, unit='d')
df = results.resample('W-Mon', on='start_date').sum().reset_index().sort_values(by='start_date')
st.table(df)

st.markdown("----")
#-----------------------------------------------------------------#

st.write("#### Aquí te presentamos las principales métricas.")

value1 = df['retweetCount'].iloc[len(df) - 2]
value2 = df['retweetCount'].iloc[len(df) - 3]
delta = round((value2 - value1) / (value2 + 1)) # división por 0
delta = "{:.0%}".format(delta)

col1, col2 = st.columns([5,5])
with col1:
  value1 = df['retweetCount'].iloc[len(df) - 2]
  if df['retweetCount'].iloc[len(df) - 3] == 0:
    value2 = df['retweetCount'].iloc[len(df) - 3] + 1
  else:
    value2 = df['retweetCount'].iloc[len(df) - 3]
  delta = round((value2 - value1) / (value2), 1) 
  delta = "{:.0%}".format(delta)
  st.write("", f"**{value2:,.3f}**", "")
  st.metric(label="retweetCount", value='{:,}'.format(value1), delta=delta, delta_color="inverse")
with col2:
  value3 = df['likeCount'].iloc[len(df) - 2]
  if df['likeCount'].iloc[len(df) - 3] == 0:
    value4 = df['likeCount'].iloc[len(df) - 3] + 1
  else:
    value4 = df['likeCount'].iloc[len(df) - 3]
  delta = round((value4 - value3) / (value4 ), 1) 
  delta = "{:.0%}".format(delta)
  st.write("", f"**{value2:,.3f}**", "")
  st.metric(label="likeCount", value='{:,}'.format(value3), delta=delta, delta_color="inverse")
#-----------------------------------------------------------------#
