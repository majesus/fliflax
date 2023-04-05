import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Realizamos la petición GET a la URL y obtenemos el contenido
url = "https://www.us.es/laUS/secretaria-general/normativas"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

# Buscamos el elemento que contiene todas las normativas
normativas_element = soup.find("dl", class_="ckeditor-accordion")

# Creamos una lista vacía para ir almacenando las normativas
normativas = []

# Iteramos por cada normativa y extraemos su nombre, URL y código
for normativa in normativas_element.find_all("a"):
    nombre = normativa.text
    url = normativa.get("href")
    cod = url.split("/")[-1]
    normativas.append({"Normativa": nombre, "URL": url, "COD": cod})

# Creamos un dataframe con las normativas
df = pd.DataFrame(normativas)

# Mostramos la tabla en pantalla
st.dataframe(df)

# Añadimos un enlace para descargar la tabla en formato CSV
st.markdown(
    f'<a href="data:application/octet-stream,{df.to_csv(index=False)}" download="normativas.csv">Descargar como CSV</a>',
    unsafe_allow_html=True,
)
