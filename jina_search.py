import streamlit as st
from streamlit_jina import jina
st.set_page_config(page_title="Jina Text Search",)

endpoint = "http://0.0.0.0:45678/api/search" # This is Jina's default endpoint. If your Flow uses something different, switch it out

st.title("Jina Text Search")

jina.text_search(endpoint=endpoint)
