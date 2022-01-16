import pandas as pd
import streamlit as st
import tweepy as tw
from transformers import pipeline

import os

# https://huggingface.co/spaces/lewtun/twitter-sentiments/blob/aa8bd7daee9993846d1a2330b163aa76b6690023/app.py

st.write("Has environment variables been set:", os.environ["consumerKey"] == st.secrets["consumerKey"])
st.write("Has environment variables been set:", os.environ["consumerSecret"] == st.secrets["consumerSecret"])
st.write("Has environment variables been set:", os.environ["access_token"] == st.secrets["access_token"])
st.write("Has environment variables been set:", os.environ["access_token_secret"] == st.secrets["access_token_secret"])

auth = tw.OAuthHandler(st.secrets["consumerKey"], st.secrets["consumerSecret"])
auth.set_access_token(st.secrets["access_token"], st.secrets["access_token_secret"])
api = tw.API(auth)

@st.cache(allow_output_mutation=True)
def load_model():
    pipe = pipeline(task="sentiment-analysis", model="bhadresh-savani/distilbert-base-uncased-emotion")
    return pipe


"""
# Twitter Emotion Analyser
"""


pipe = load_model()
twitter_handle = st.sidebar.text_input("Twitter handle:", "huggingface")
twitter_count = st.sidebar.selectbox("Number of tweets:", (10, 100, 500, 1000, 3200))

def get_sentiment(texts):
    preds = pipe(texts)

    response = dict()
    response["labels"] = [pred["label"] for pred in preds]
    response["scores"] = [pred["score"] for pred in preds]
    return response

if st.sidebar.button("Get tweets!"):
    tweets = tw.Cursor(api.search,
              q=twitter_handle,
              lang="en",
              since=date_since).items(twitter_count)
    df = pd.DataFrame(tweets)
    st.table(df)
