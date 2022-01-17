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

with st.sidebar.form("my_form"):
    st.write("Buscador de **tweets**:")
    username = st.text_input(label="Cuenta a buscar ...", value = "zara_es")
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
st.table(results)


import matplotlib.pyplot as plt
ylabels = ["favorite_count","retweet_count"]
fig = plt.figure(figsize=(13,3))
fig.subplots_adjust(hspace=0.01,wspace=0.01)
n_row = len(ylabels)
n_col = 1
for count, ylabel in enumerate(ylabels):
    ax = fig.add_subplot(n_row,n_col,count+1)
    ax.plot(df["created_at"],df[ylabel])
    ax.set_ylabel(ylabel)
plt.show()

st.pyplot(fig)
