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

def get_tweets(username, count):
    tweets = tw.Cursor(
        api.user_timeline,
        screen_name=username,
        tweet_mode="extended",
        exclude_replies=True,
        include_rts=False,
    ).items(count)

    tweets = list(tweets)
    response = {
        "tweets": [tweet.full_text.replace("\n", "").lower() for tweet in tweets],
        "timestamps": [str(tweet.created_at) for tweet in tweets],
        "retweets": [tweet.retweet_count for tweet in tweets],
        "likes": [tweet.favorite_count for tweet in tweets],
    }
    return response
   

with st.sidebar.form(key='my_form'):
	twitter_handle = st.text_input(label='Username', key = "twitter_handle")
    twitter_count = st.slider(label='Tweets', min_value=0, max_value=100, key="twitter_count")
	submit_button = st.form_submit_button(label='Submit')
    
tweets = get_tweets(twitter_handle, twitter_count)
preds = get_sentiment(tweets["tweets"])
# neutralise_sentiment(preds)
tweets.update(preds)
# dataframe creation + preprocessing
df = pd.DataFrame(tweets)
df["timestamps"] = pd.to_datetime(df["timestamps"])
# plots
agg_period = get_aggregation_period(df)
ts_sentiment = (
        df.groupby(["timestamps", "labels"])
        .count()["likes"]
        .unstack()
        .resample(agg_period)
        .count()
        .stack()
        .reset_index())
ts_sentiment.columns = ["timestamp", "label", "count"]
