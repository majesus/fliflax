import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import base64

# Función para descargar archivo CSV
def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'


# Realizar scraping
url = "https://www.example.com"  # Cambiar esta URL a la URL real del sitio web
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
items = soup.select("dl.ckeditor-accordion dd ul li a")

normativas = []
urls = []

for item in items:
    normativas.append(item.text)
    urls.append(url + item["href"])

tabla = pd.DataFrame({"Normativa": normativas, "URL": urls, "Columna adicional": [""] * len(normativas)})

# Mostrar y descargar la tabla usando Streamlit
st.title("Tabla de Normativas")
st.write(tabla)

if st.button("Descargar tabla en formato CSV"):
    tmp_download_link = download_link(tabla, "tabla_normativas.csv", "Haz clic aquí para descargar la tabla en formato CSV")
    st.markdown(tmp_download_link, unsafe_allow_html=True)
