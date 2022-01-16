import tweepy as tw
import streamlit as st
import pandas as pd
from transformers import pipeline

st.write("consumerKey:", st.secrets["consumerKey"])
st.write("consumerSecret:", st.secrets["consumerSecret"])
st.write("access_token:", st.secrets["access_token"])
st.write("access_token_secret:", st.secrets["access_token_secret"])

import os
st.write("Has environment variables been set:", os.environ["db_username"] == st.secrets["db_username"])

auth = tw.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

classifier = pipeline('sentiment-analysis')

st.title('Live Twitter Sentiment Analysis with Tweepy and HuggingFace Transformers')
st.markdown("This app uses tweepy to get tweets from twitter based on the input name/phrase. "
            "It then processes the tweets through HuggingFace transformers pipeline function for sentiment analysis. "
            "The resulting sentiments and corresponding tweets are then put in a dataframe for display which is what you see as result.")
