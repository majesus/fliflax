import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import base64

def download_csv(dataframe):
    csv = dataframe.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="normativa.csv">Descargar tabla en formato CSV</a>'
    return href

html_doc = """
# Aquí deberías pegar el código HTML que proporcionaste anteriormente
"""

soup = BeautifulSoup(html_doc, 'html.parser')

normativas = []
urls = []

for link in soup.find_all('a'):
    normativas.append(link.get_text())
    urls.append(link.get('href'))

codigos = [
    # Aquí debes agregar los códigos correspondientes (A P, E, PE) para cada normativa
]

data = {
    "Normativa": normativas,
    "URL": urls,
    "Código": codigos
}

df = pd.DataFrame(data)

st.title("Normativas de la Universidad")
st.write(df)

st.markdown(download_csv(df), unsafe_allow_html=True)
