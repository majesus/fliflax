import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define la URL de la página web que contiene la información que queremos extraer.
url = 'https://www.us.es/laUS/secretaria-general/normativas'

# Realiza una petición a la página web y obtiene el código HTML como respuesta.
response = requests.get(url)

# Parsea el código HTML con BeautifulSoup y extrae la lista de normativas.
soup = BeautifulSoup(response.content, 'html.parser')
normativas_list = soup.select_one('dl.ckeditor-accordion')

# Crea listas vacías para almacenar los datos de la tabla.
normativas = []
urls = []
codigos = []

# Extrae la información de cada normativa de la lista y la añade a las listas.
for item in normativas_list.select('dt'):
    normativas.append(item.text.strip())
    
    link = item.find_next('a')
    urls.append(link['href'])
    
    codigos.append("")

# Crea un DataFrame con los datos extraídos.
data = {'Normativa': normativas, 'URL': urls, 'COD': codigos}
df = pd.DataFrame(data)

# Muestra la tabla en pantalla.
st.write(df)

# Agrega un enlace para descargar la tabla en formato CSV.
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="tabla_normativas.csv">Descargar tabla en CSV</a>'
st.markdown(href, unsafe_allow_html=True)
