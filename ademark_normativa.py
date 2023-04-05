import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# función para obtener el contenido de una url
def get_url_content(url):
    response = requests.get(url)
    content = response.content
    return content

# url de la página a hacer scraping
url = 'https://www.us.es/laUS/secretaria-general/normativas'

# hacer scraping del contenido de la página
soup = BeautifulSoup(get_url_content(url), 'html.parser')

# encontrar el elemento de la página que contiene la lista de normativas
lista_normativas = soup.find('dl', class_='ckeditor-accordion')

# inicializar una lista vacía para almacenar las filas de la tabla
rows = []

# iterar sobre cada elemento de la lista de normativas
for normativa in lista_normativas.find_all('a'):

    # obtener el título de la normativa y la url
    title = normativa.text.strip()
    url = normativa['href']
    
    # obtener el código de la normativa a partir de la url
    cod = url.split('/')[-1]
    
    # agregar una nueva fila a la tabla
    rows.append({'Normativa': title, 'URL': url, 'COD': cod})

# convertir la lista de filas en un DataFrame de pandas
df = pd.DataFrame(rows)

# mostrar la tabla en pantalla
st.dataframe(df)

# agregar un enlace para descargar la tabla en formato CSV
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="tabla_normativas.csv">Descargar CSV</a>'
st.markdown(href, unsafe_allow_html=True)

