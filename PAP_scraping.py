import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
import base64
from io import BytesIO

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

    data.append({"Nombre": nombre, "URL": url, "URL_abs": url_abs})

df = pd.DataFrame(data)

# Realiza la copia del DataFrame sin enlaces HTML
df_csv = df.copy()

# Convierte el nombre en un enlace HTML que apunta a la URL correspondiente
df["Nombre"] = df.apply(lambda row: f'<a href="{row["URL_abs"]}" target="_blank">{row["Nombre"]}</a>', axis=1)

# Muestra el DataFrame en Streamlit como una tabla HTML
# st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
# st.write(f'<div style="font-size: 12;">{df.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)
st.dataframe(df, 200, 100)

# Función para descargar el DataFrame como un archivo CSV
def to_csv_download_link(df, filename):
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
    csv_b64 = base64.b64encode(csv_buffer.getvalue()).decode()
    href = f'<a href="data:file/csv;base64,{csv_b64}" download="{filename}" target="_blank">Descargar CSV</a>'
    return href

# Ofrece la opción de descargar el DataFrame como un archivo CSV
st.markdown(to_csv_download_link(df_csv, "profesores.csv"), unsafe_allow_html=True)
