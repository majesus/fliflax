
#-----------------------------------------------------------------#
import pandas as pd
import streamlit as st
import random
import string

from datetime import datetime, timedelta
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
    #search_term = st.selectbox("¿Qué deseas buscar?", ('NetflixES','PlayStationES','adidas_ES','NintendoES','VideojuegosGAME','Iberia','Ubisoft_Spain'))
    search_term = st.text_input('¿Qué deseas buscar?', value = "universidad")
    
    limit = st.slider('¿Cuántos tweets deseas descargar?', 20, 200, step=20)
    
    retweets = st.radio('¿Deseas descargar los retweets?', [False, True])
    verified = st.radio('¿Deseas descargar tweets verificados?', [False, True])
    
    last_24_date_time = st.date_input('¿Desde qué fecha?',value = datetime.now() - timedelta(days = 7), key ="date_min")
    today = last_24_date_time.strftime('%Y-%m-%d')
    date = str(today)
        
    file_name = ''.join(random.choices(string.ascii_uppercase, k = 10))  
    file_name = st.text_input('Nombre del CSV:', value = file_name)

    submit_button = st.form_submit_button(label='Buscar tweets')

if submit_button:
  c = twint.Config()
  
  c.Since = date
   
  c.Verified = verified
  c.Retweets = retweets
  #c.Filter_retweets = True 
  c.Hide_output = False
  #c.Lang = 'es'
  #c.Links = "exclude"
  
  if search_term != '':
    #c.Username = search_term
    c.Search = search_term
  else:
    #c.Username = 'BarackObama'
    c.Search = 'universidad'
    
  #c.Search = search_term
  c.Limit = limit
  c.Store_csv = True
  c.Store_object = True
  c.Custom_csv = ['date', 'username', 'tweet', 'replies_count', 'retweets_count', 'likes_count', 'retweet']
  c.Output = f'{file_name}.csv'
  
  twint.run.Search(c)
  
  #Tweets_df  = twint.storage.panda.Tweets_df
  Tweets_df = pd.DataFrame()
  
  for i in range(0,len(f'{file_name}.csv')):
   try:
    Tweets_df_ = pd.read_csv(f'{file_name}.csv', encoding='utf-8')
    ### Do Some Stuff
   except:
    Tweets_df_ = pd.DataFrame(columns = ['date', 'username', 'tweet', 'replies_count', 'retweets_count', 'likes_count', 'retweet'])
    #continue
  
  Tweets_df_ = Tweets_df_[['date', 'username', 'tweet', 'replies_count', 'retweets_count', 'likes_count', 'retweet']]
  
  len_df = len(Tweets_df_.index)
  st.write('Número de tweets descargados: ', len_df)
  st.write('Limite: ', limit)
  st.write('Retweets: ', retweets)
  st.write('Verificado: ', verified)
  
  @st.cache
  def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(sep="|").encode('utf-8')
  csv = convert_df(Tweets_df_)
  
  #csv = Tweets_df_.to_csv(sep="|")
  st.download_button(
     "Descargar CSV",
     csv,
     #"file.txt",
     f'{file_name}.txt',
     "text/csv",
     key='download-csv'
  )

  st.table(Tweets_df_)

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
