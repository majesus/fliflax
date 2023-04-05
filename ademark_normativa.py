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

df = pd.DataFrame(data, columns=["Normativa", "URL", "Codigo"])

# st.write(df)

# csv = df.to_csv(index=False, encoding="utf-8")
# st.download_button(label="Descargar CSV", data=csv, file_name="normativas.csv", mime="text/csv")

# data = pd.read_csv("csv/normativas.csv") #path folder of the data file
# st.write(data) #displays the table of data
#-------------------------------------------------------#
# Crear el vector de valores proporcionados
vector_valores = [
    'P', 'E', 'PE', 'PE', 'E', 'PE', 'PE', 'E', 'E', 'E', 'PE', 'E', 'PE',
    'E', 'PE', 'PE', 'E', 'PE', 'E', 'PE', 'PE', 'P', 'PE', 'P', 'E', 'PE',
    'PE', 'PE', 'PE', 'E', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE',
    'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'E', 'P', 'P',
    'P', 'P', 'PE', 'P', 'P', 'P', 'P', 'PE', 'PE', 'P', 'P', 'P', 'P', 'PE',
    'PE', 'PE', 'PE', 'PE', 'P', 'E', 'E', 'E', 'PE', 'PE', 'PE', 'PE', 'PE',
    'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'E'
]

# Asegurarse de que el vector tenga la misma longitud que el número de filas en el DataFrame
assert len(vector_valores) == len(df)

# Agregar la columna con el vector de valores al DataFrame
df['Codigo'] = vector_valores
st.write(df)

# Guardar el DataFrame actualizado en un nuevo archivo CSV
csv = df.to_csv(index=False, encoding="utf-8")
st.download_button(label="Descargar CSV", data=csv, file_name="normativas.csv", mime="text/csv")
