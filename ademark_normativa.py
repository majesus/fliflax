import streamlit as st
import requests
import pandas as pd
import io

# Hacer la petición HTTP para obtener el HTML
url = "https://www.us.es/centro/secretariageneral/normativa"
response = requests.get(url)

# Cargar el HTML en BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Buscar la tabla y convertirla en un objeto DataFrame de Pandas
table = soup.find("dl", {"class": "ckeditor-accordion"})
df = pd.read_html(str(table))[0]
df.columns = ["Normativa", "URL"]

# Crear un objeto de memoria para escribir el archivo CSV
buffer = io.StringIO()
df.to_csv(buffer, index=False)

# Descargar el archivo CSV
b64 = base64.b64encode(buffer.getvalue().encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="normativas.csv">Descargar archivo CSV</a>'
st.markdown(href, unsafe_allow_html=True)

# Mostrar la tabla en pantalla
st.write(df)
