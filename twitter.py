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

# https://github.com/pysentimiento/pysentimiento
from pysentimiento import create_analyzer
analyzer = create_analyzer(task="sentiment", lang="es")
results = analyzer.predict("Qué gran jugador es Messi")

data_items = results.probas.items()
data_list = list(data_items)
df = pd.DataFrame(data_list)
st.table(df)
