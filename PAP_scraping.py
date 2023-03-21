import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

url_base = "http://alojawebapps.us.es/"
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

# Función para descargar el DataFrame como un archivo CSV
# Realiza la copia del DataFrame sin enlaces HTML
df_csv = df.copy()
def to_csv_download_link(df, filename):
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
    csv_b64 = base64.b64encode(csv_buffer.getvalue()).decode()
    href = f'<a href="data:file/csv;base64,{csv_b64}" download="{filename}" target="_blank">Descargar CSV</a>'
    return href

# Ofrece la opción de descargar el DataFrame como un archivo CSV
st.markdown(to_csv_download_link(df_csv, "profesores.csv"), unsafe_allow_html=True)
