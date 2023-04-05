import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

url = "https://www.us.es/laUS/secretaria-general/normativas"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

elements = soup.select("dl.ckeditor-accordion li a")

data = []

for elem in elements:
    normativa = elem.text
    normativa_url = elem["href"]
    data.append([normativa, normativa_url, ""])

df = pd.DataFrame(data, columns=["Normativa", "URL", "Columna Adicional"])

st.write(df)

csv = df.to_csv(index=False, encoding="utf-8")
st.download_button(label="Descargar CSV", data=csv, file_name="normativas.csv", mime="text/csv")
