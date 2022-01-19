import pandas as pd
import streamlit as st
import tweepy as tw
import altair as alt
from transformers import pipeline
import os

from PIL import Image
img=Image.open('img/fliflax-logo.jpg')
st.set_page_config(#layout="centered",
                   #theme="light",
                   layout="wide",
                   page_title="Fliflax",
                   page_icon=img,
                   initial_sidebar_state='expanded'
                   )

# https://huggingface.co/spaces/lewtun/twitter-sentiments/blob/aa8bd7daee9993846d1a2330b163aa76b6690023/app.py

# st.write("Has environment variables been set:", os.environ["consumerKey"] == st.secrets["consumerKey"])
# st.write("Has environment variables been set:", os.environ["consumerSecret"] == st.secrets["consumerSecret"])
# st.write("Has environment variables been set:", os.environ["access_token"] == st.secrets["access_token"])
# st.write("Has environment variables been set:", os.environ["access_token_secret"] == st.secrets["access_token_secret"])

auth = tw.OAuthHandler(st.secrets["consumerKey"], st.secrets["consumerSecret"])
auth.set_access_token(st.secrets["access_token"], st.secrets["access_token_secret"])
api = tw.API(auth)


with st.sidebar.form("my_form"):
    st.write("**Tweet Finder**:")
    username = st.text_input(label="Query ...", value = "JoeBiden")
    count = st.slider("Hasta un máximo de ...", min_value=1, max_value=600, value=20, step=10)
    
    values1=['Yes','No']
    options1=[True,False]
    dic1 = dict(zip(options1, values1))
    retweets = st.radio('Do you want to download retweets?',  options1, format_func=lambda x: dic1[x], key = "retweets", disabled = False)
    
    values2=['Yes','No']
    options2=[True,False]
    dic2 = dict(zip(options2, values2))
    replies = st.radio('Do you want to download replies?',  options2, format_func=lambda x: dic2[x], key = "retweets", disabled = False)

    submitted = st.form_submit_button("Download")
  
#@st.cache(suppress_st_warning=False)
def get_tweets(username, count):
    tweets = tw.Cursor(
      api.user_timeline,
      screen_name=username,
      #api.search,
      #q=username,
      tweet_mode="extended",
      exclude_replies=replies,
      include_rts=retweets,
    ).items(count)

    tweets = list(tweets)
    response = {
      "tweets": [tweet.full_text.replace("\n", "").lower() for tweet in tweets],
      "timestamps": [str(tweet.created_at) for tweet in tweets],
      "retweets": [tweet.retweet_count for tweet in tweets],
      "likes": [tweet.favorite_count for tweet in tweets],
      
      #"retweet_text": [tweet.retweeted_status.full_text.replace("\n", "").lower() for tweet in tweets],
      "screen_name": [tweet.user.screen_name for tweet in tweets],
      #"query": [query for tweet in tweets],
      #"hashtags": [tweet.hashtags for tweet in tweets],
      #"status_count": [tweet.status_count for tweet in tweets],
      #"location": [tweet.location for tweet in tweets],
      #"source_device": [tweet.source_device for tweet in tweets],
    }
    
    results = pd.DataFrame(response) 

    return results 

      
results = get_tweets(username, count)


if st.checkbox("If you want to see the tweets downloaded by date, click here.", False):
  st.markdown("----")
  st.table(results)
  
st.markdown("----")

# https://altair-viz.github.io/user_guide/times_and_dates.html

if st.checkbox("If you want to see the graphical representation of the **retweets**, click here.", False):
  #import altair as alt
  st.markdown("----")
  results.loc[results.likes == 0, 'likes'] = 0.001 # log
  chart = alt.Chart(results).mark_area(color = "lightblue", interpolate = "step-after", line = True, opacity=0.3,).encode(
    x=alt.X('timestamps:T', title='', axis=alt.Axis(labelOverlap="greedy",grid=False)),
    y=alt.Y('likes', scale=alt.Scale(type='log')))
  st.altair_chart(chart, use_container_width=True)

st.markdown("----")

if st.checkbox("If you want to see the graphical representation of the **likes**, click here.", False):
  #import altair as alt
  st.markdown("----")
  results.loc[results.retweets == 0, 'retweets'] = 0.001 # log
  chart = alt.Chart(results).mark_area(color = "lightblue", interpolate = "step-after", line = True, opacity=0.3,).encode(
    x=alt.X('timestamps:T', title='', axis=alt.Axis(labelOverlap="greedy",grid=False)),
    y=alt.Y('retweets', scale=alt.Scale(type='log')))
  st.altair_chart(chart, use_container_width=True)
  
st.markdown("----")

st.write("### A continuación, te mostramos la evolución semanal de retweets y likes.")

st.markdown("----")

results['date'] = pd.to_datetime(results['timestamps']) - pd.to_timedelta(7, unit='d')
df = results.resample('W-Mon', on='date').sum().reset_index().sort_values(by='date')
st.table(df)

st.markdown("----")

st.write("### Here are the main performance metrics.")

#value1 = df['retweets'].iloc[-1]
value1 = df['retweets'].iloc[len(df) - 2]
value2 = df['retweets'].iloc[len(df) - 3]
#st.write("", f"**{value2:,.0f}**", "")
delta = round((value2 - value1) / value2)
delta = "{:.0%}".format(delta)
st.metric(label="retweets", value='{:,}'.format(value1), delta=delta, delta_color="inverse")
