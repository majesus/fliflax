import streamlit as st
import pandas as pd
import plotly.express as px

import requests

# Título de la aplicación
st.title("Aplicación Streamlit para leer, filtrar y visualizar datos CSV")

# Carga el archivo CSV
uploaded_file = st.file_uploader("Sube un archivo CSV", type="csv")

if uploaded_file is not None:
    # Lee el archivo CSV y lo convierte en un DataFrame de Pandas
    data = pd.read_csv(uploaded_file)
    st.markdown("### Datos cargados correctamente")

    # Muestra las primeras filas del DataFrame
    st.markdown("### Vista previa de los datos")
    st.write(data.head())

    # Selecciona la columna para filtrar
    st.markdown("### Selecciona la columna para filtrar")
    column_to_filter = st.selectbox("Columna", data.columns)

    # Ingresa el valor para filtrar
    st.markdown(f"### Ingresa el valor para filtrar en la columna '{column_to_filter}'")
    # Obtén los valores únicos de la columna seleccionada
    unique_values = data[column_to_filter].unique()
    # Crea un desplegable con los valores únicos de la columna
    value_to_filter = st.selectbox("Valor", unique_values)

    # Filtra el DataFrame
    filtered_data = data[data[column_to_filter] == value_to_filter]

    # Muestra la tabla filtrada de manera elegante
    if not filtered_data.empty:
        st.markdown("### Datos filtrados")
        st.dataframe(filtered_data)
    else:
        st.warning("No hay datos que coincidan con el filtro")

else:
    st.warning("Por favor, sube un archivo CSV")

    
    
#------------------------------------------#
    
    
# Carga el archivo CSV
csv_url = st.text_input("Ingresa la URL del archivo CSV")

if csv_url:
    try:
        # Lee el archivo CSV desde la URL y lo convierte en un DataFrame de Pandas
        data = pd.read_csv(csv_url)
        st.markdown("### Datos cargados correctamente")

        # Muestra las primeras filas del DataFrame
        st.markdown("### Vista previa de los datos")
        st.write(data.head())

        # Selecciona la columna para filtrar
        st.markdown("### Selecciona la columna para filtrar")
        column_to_filter = st.selectbox("Columna", data.columns)

        # Ingresa el valor para filtrar
        st.markdown(f"### Ingresa el valor para filtrar en la columna '{column_to_filter}'")
        # Obtén los valores únicos de la columna seleccionada
        unique_values = data[column_to_filter].unique()
        # Crea un desplegable con los valores únicos de la columna
        value_to_filter = st.selectbox("Valor", unique_values)

        # Filtra el DataFrame
        filtered_data = data[data[column_to_filter] == value_to_filter]

        # Muestra la tabla filtrada de manera elegante
        if not filtered_data.empty:
            st.markdown("### Datos filtrados")
            st.dataframe(filtered_data)
        else:
            st.warning("No hay datos que coincidan con el filtro")

        
        
    except pd.errors.ParserError:
        st.error("No se pudo leer el archivo CSV desde la URL proporcionada. Asegúrate de que la URL sea válida y accesible.")
else:
    st.warning("Por favor, ingresa la URL de un archivo CSV")
    
    
#----------------------------#

import streamlit as st
import pandas as pd

# Cabecera corporativa con imagen
st.markdown("# Título del Departamento")
st.markdown("![Imagen Corporativa](URL_DE_IMAGEN)")

# Breve resumen del departamento
st.markdown("## Resumen del departamento")
st.write("Aquí puedes incluir un breve resumen sobre el departamento, sus objetivos, áreas de investigación, etc.")

# Cargar y mostrar los datos del profesorado
st.markdown("## Profesorado")
profesorado_url = "https://raw.githubusercontent.com/majesus/fliflax/master/csv/libro_pap1.csv"
profesorado_data = pd.read_csv(profesorado_url)
st.write(profesorado_data.head(5))  # Muestra solo los primeros 5 registros

# Cargar y mostrar los datos de los títulos en que participamos
st.markdown("## Títulos en que participamos")
titulos_url = "https://raw.githubusercontent.com/majesus/fliflax/master/csv/libro_pap1.csv"
titulos_data = pd.read_csv(titulos_url)
st.write(titulos_data.head(5))  # Muestra solo los primeros 5 registros

# Cargar y mostrar los datos de los centros
st.markdown("## Datos de los centros")
centros_url = "https://raw.githubusercontent.com/majesus/fliflax/master/csv/libro_pap1.csv"
centros_data = pd.read_csv(centros_url)
st.write(centros_data.head(5))  # Muestra solo los primeros 5 registros

#--------------------------------

import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup

st.title("Web Scraping de la página del investigador")

url = "https://bibliometria.us.es/prisma/investigador/14"
st.write(f"Extrayendo información del Departamento y Área de Conocimiento de: {url}")

def obtener_info_investigador(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    nombre_h1 = soup.find("h1", id="nombre")
    nombre = nombre_h1.text.strip() if nombre_h1 else "No disponible"

    categoria_div = soup.find("div", id="categoría")
    categoria = categoria_div.text.strip() if categoria_div else "No disponible"

    email_div = soup.find("div", id="email")
    email = email_div.text.strip() if email_div else "No disponible"

    return nombre, categoria, email

nombre, categoria, email = obtener_info_investigador(url)

data = {
    "Nombre": [nombre],
    "Categoría": [categoria],
    "Email": [email],
}

df = pd.DataFrame(data)
st.write(df)
