#----------------------------------------------------#
from PIL import Image
img=Image.open('img/fliflax-logo.jpg')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        #footer {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)
#----------------------------------------------------#
#----------------------------------------------------#
st.image('img/fliflax-logo.jpg',width=200)
st.title("Fliflax: Una plataforma de apoyo al estudio")
st.markdown("Por __*Manuel J. Sánchez Franco*__, Universidad de Sevilla.")
st.write("En **Fliflax** creamos contenidos para que tu estudio de las materias de Comportamiento y Comunicacion "
         "no dependan del lugar en que te encuentras. Nuestra obsesión es la ubicuidad, o **u-learning**, "
         "es decir, queremos ofrecerte una enseñanza en cualquier momento y lugar siempre que "
         "tengas entre tus manos un teléfono móvil o una tablet.")
st.write("Abajo te mostramos, por ejemplo, el **modelo Beta-Binomial**, y en el _sidebar_ de la izquierda una **calculadora de la Frecuencia efectiva mínima**. "
        "También abajo hemos incluido un breve **glosario** que puede ayudarte.")
#----------------------------------------------------#

import streamlit as st
# Crear una columna lateral y mostrar el logo en ella
sidebar = st.sidebar
#sidebar.image(logo, use_column_width=True)

#-----------------------------

import streamlit as st
import requests
from bs4 import BeautifulSoup

url = 'https://www.us.es/centros/departamentos/administracion-de-empresas-y-marketing'  # Reemplaza esto con la URL de la página que contiene el código fuente que proporcionaste

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")

table = soup.find("table", class_="cifrasUS")
rows = table.find_all("tr")

director_row = rows[1]
secretario_row = rows[2]

director = director_row.find_all("td")[1].text.strip()
secretario = secretario_row.find_all("td")[1].text.strip()

st.write(f"Director/a: {director}")
st.write(f"Secretario: {secretario}")

#----------------------------------------------------#
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Profesores", value = "105")
with col2:
    st.metric(label="Títulos", value = "25")
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Centros", value = "15")
with col2:
    st.metric(label="Áreas", value = "2")
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Másteres", value = "28")
with col2:
    st.metric(label="Doctorados", value = "10")  
#----------------------------------------------------#

#------------------------------#

import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup

st.title("Web Scraping de la página del investigador")

def obtener_info_departamento(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    sede_div = soup.find("div", class_="field--name-field-centro")
    sede = sede_div.find("a").text.strip() if sede_div else "No disponible"

    direccion_div = soup.find("div", class_="field--name-field-direccion")
    direccion = direccion_div.text.strip() if direccion_div else "No disponible"

    email_div = soup.find("div", class_="field--name-field-correo-electronico")
    email = email_div.text.strip() if email_div else "No disponible"

    return sede, direccion, email

url = "https://www.us.es/centros/departamentos/administracion-de-empresas-y-marketing"  # Reemplaza esto con la URL de la página que deseas extraer
sede, direccion, email = obtener_info_departamento(url)

st.write("Sede:", sede)
st.write("Dirección:", direccion)
st.write("Correo electrónico:", email)

#-------------------------------#


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
import base64
from io import BytesIO

st.title("Web Scraping de la página del investigador")

def obtener_info_investigador(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    nombre_h1 = soup.find("h1", id="nombre")
    nombre = nombre_h1.text.strip() if nombre_h1 else "No disponible"

    categoria_div = soup.find("div", id="categoria")
    categoria = categoria_div.text.strip() if categoria_div else "No disponible"

    email_div = soup.find("div", id="email")
    email = email_div.text.strip() if email_div else "No disponible"

    area_conocimiento = soup.find("span", string="Área de conocimiento: ").find_next("span").text.strip() if soup.find("span", string="Área de conocimiento: ") else "No disponible"

    departamento = soup.find("span", string="Departamento: ").find_next("a").text.strip() if soup.find("span", string="Departamento: ") else "No disponible"

    return nombre, categoria, email, area_conocimiento, departamento

def leer_urls_desde_csv(archivo_csv):
    df = pd.read_csv(archivo_csv)
    urls = df["url"].tolist()
    return urls

archivo_csv = "csv/urls.csv"
urls = leer_urls_desde_csv(archivo_csv)

data = {
    "Nombre": [],
    "Categoría": [],
    "Email": [],
    "Área de Conocimiento": [],
    "Departamento": [],
    "URL": [],
}

for url in urls:
    st.write(f"Extrayendo información del Departamento y Área de Conocimiento de: {url}")
    nombre, categoria, email, area_conocimiento, departamento = obtener_info_investigador(url)
    
    data["Nombre"].append(nombre)
    data["Categoría"].append(categoria)
    data["Email"].append(email)
    data["Área de Conocimiento"].append(area_conocimiento)
    data["Departamento"].append(departamento)
    data["URL"].append(url)

df = pd.DataFrame(data)

# Realiza la copia del DataFrame sin enlaces HTML
df_csv = df.copy()

# Convierte el nombre en un enlace HTML que apunta a la URL correspondiente
df["Nombre"] = df.apply(lambda row: f'<a href="{row["URL"]}" target="_blank">{row["Nombre"]}</a>', axis=1)

# Muestra el DataFrame en Streamlit como una tabla HTML
st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Función para descargar el DataFrame como un archivo CSV
def to_csv_download_link(df, filename):
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
    csv_b64 = base64.b64encode(csv_buffer.getvalue()).decode()
    href = f'<a href="data:file/csv;base64,{csv_b64}" download="{filename}" target="_blank">Descargar CSV</a>'
    return href

# Ofrece la opción de descargar el DataFrame como un archivo CSV
st.markdown(to_csv_download_link(df_csv, "investigadores.csv"), unsafe_allow_html=True)
