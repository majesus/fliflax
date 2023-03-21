import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

url_base = "http://alojawebapps.us.es/centrosdptos/departamentos/listpdi.php?dpto=I0G7"
url_pagina = "http://alojawebapps.us.es/centrosdptos/departamentos/listpdi.php?dpto=I0G7"

# Obtener contenido HTML con requests
response = requests.get(url_pagina)
html_content = response.text

# Extraer información con Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")
profesores = soup.find_all("li")

# Crear DataFrame y añadir la información extraída
data = []

for profesor in profesores:
    link = profesor.find("a")
    nombre = link.text
    url = link["href"]
    url_abs = url_base + url

    data.append({"Nombre del profesor": nombre, "URL": url, "URL_abs": url_abs})

df = pd.DataFrame(data)

# Crear app Streamlit
st.title("Profesores y sus URLs")
st.write(df)

if st.button("Descargar CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="profesores.csv">Descargar CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
