import pandas as pd
import streamlit as st
import tweepy as tw
from transformers import pipeline
import os

# https://huggingface.co/spaces/lewtun/twitter-sentiments/blob/aa8bd7daee9993846d1a2330b163aa76b6690023/app.py

# st.write("Has environment variables been set:", os.environ["consumerKey"] == st.secrets["consumerKey"])
# st.write("Has environment variables been set:", os.environ["consumerSecret"] == st.secrets["consumerSecret"])
# st.write("Has environment variables been set:", os.environ["access_token"] == st.secrets["access_token"])
# st.write("Has environment variables been set:", os.environ["access_token_secret"] == st.secrets["access_token_secret"])

auth = tw.OAuthHandler(st.secrets["consumerKey"], st.secrets["consumerSecret"])
auth.set_access_token(st.secrets["access_token"], st.secrets["access_token_secret"])
api = tw.API(auth)

from PIL import Image
img=Image.open('img/fliflax-logo.jpg')
st.set_page_config(#layout="centered",
                   #theme="light",
                   layout="wide",
                   page_title="Fliflax",
                   page_icon=img,
                   initial_sidebar_state='expanded'
                   )

with st.sidebar.form("my_form"):
    st.write("Buscador de **tweets**:")
    username = st.text_input(label="Cuenta a buscar ...", value = "JoeBiden")
    count = st.slider("Hasta un máximo de ...", min_value=10, max_value=100, value=10, step=10)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Descargar")
    
tweets = tw.Cursor(
        api.user_timeline,
        screen_name=username,
        tweet_mode="extended",
        exclude_replies=True,
        include_rts=False,).items(count)

tweets = list(tweets)
response = {
  "tweets": [tweet.full_text.replace("\n", "").lower() for tweet in tweets],
  "timestamps": [str(tweet.created_at) for tweet in tweets],
  "retweets": [tweet.retweet_count for tweet in tweets],
  "likes": [tweet.favorite_count for tweet in tweets],
    
   #"id": [tweet.id_str for tweet in tweets],
}
  
results = pd.DataFrame(response)
if st.checkbox("Si deseas ver los tweets descargados por fecha.", False):
  st.table(results)

# https://altair-viz.github.io/user_guide/times_and_dates.html
if st.checkbox("Si deseas ver la representación gráfica de 'likes' por fecha.", False):
  import altair as alt
  chart = alt.Chart(results).mark_line().encode(
    x=alt.X('timestamps:T', axis=alt.Axis(labelOverlap="greedy",grid=False)),
    y=alt.Y('likes'))
  st.altair_chart(chart, use_container_width=True)
