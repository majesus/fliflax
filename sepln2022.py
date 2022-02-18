import streamlit as st

from collections import Counter
import pandas as pd
import re

from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('msmarco-MiniLM-L-12-v3')

st.write("cargado")
