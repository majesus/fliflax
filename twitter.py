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
