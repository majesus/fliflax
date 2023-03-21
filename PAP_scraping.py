#--------------------------------------------#
# PROFESORES:
#--------------------------------------------#

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

# Muestra el DataFrame en Streamlit como una tabla HTML
df_csv = df_csv.drop(['URL'], axis=1)
# Convierte el nombre en un enlace HTML que apunta a la URL correspondiente
df_csv["Nombre"] = df_csv.apply(lambda row: f'<a href="{row["URL_abs"]}" target="_blank">{row["Nombre"]}</a>', axis=1)
# Muestra el DataFrame en Streamlit como una tabla HTML
st.write(f'<div style="font-size: 12px;">{df_csv.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)

# Función para descargar el DataFrame como un archivo CSV
def to_csv_download_link(df, filename):
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
    csv_b64 = base64.b64encode(csv_buffer.getvalue()).decode()
    href = f'<a href="data:file/csv;base64,{csv_b64}" download="{filename}" target="_blank">Descargar CSV</a>'
    return href

# Ofrece la opción de descargar el DataFrame como un archivo CSV
st.markdown(to_csv_download_link(df_csv, "profesores.csv"), unsafe_allow_html=True)

#--------------------------------------------#
# PROFESORES PERFIL:
#--------------------------------------------#

import pandas as pd
from bs4 import BeautifulSoup
import streamlit as st
import requests
import time

# Asumiendo que ya tienes un DataFrame llamado df_csv con una columna llamada URL_abs

# La función para extraer la información de una URL
def extract_info_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extrae la información requerida como antes
    nombre = soup.h2.text.strip()
    categoria = soup.find("h3", text="Categoría:").find_next("p").text.strip()
    perfil_prisma = soup.find("h3", text="Perfil de PRISMA:").find_next("a")["href"]
    telefono = soup.find("h4", text="Teléfono:").find_next("p").text.strip()
    email = soup.find("h4", text="Correo electrónico personal:").find_next("p").text.strip()
    departamento = soup.find("h3", text="Departamento:").find_next("a").text.strip()
    area_conocimiento = soup.find("h3", text="Area de Conocimiento:").find_next("p").text.strip()
    centros = [centro.text.strip() for centro in soup.find("h3", text="Centro(s):").find_next("ul").find_all("a")]
    asignaturas = [asignatura.text.strip() for asignatura in soup.find("h3", text="Asignaturas:").find_next("ul").find_all("a")]

    return {
        "Nombre": nombre,
        "Categoría": categoria,
        "Perfil de Prisma": perfil_prisma,
        "Teléfono": telefono,
        "Email": email,
        "Departamento": departamento,
        "Área de Conocimiento": area_conocimiento,
        "Centros": ", ".join(centros),
        "Asignaturas": ", ".join(asignaturas)
    }

# Crea un data frame vacío para almacenar los resultados
df_result = pd.DataFrame(columns=["Nombre", "Categoría", "Perfil de Prisma", "Teléfono", "Email", "Departamento", "Área de Conocimiento", "Centros", "Asignaturas"])

# Itera sobre las URL en df_csv y extrae la información de cada una
for url in df_csv["URL_abs"]:
    info = extract_info_from_url(url)
    df_result = df_result.append(info, ignore_index=True)
    time.sleep(1)

# Muestra la tabla en Streamlit
st.title("Información extraída")
st.write(df_result)

# Función para descargar el DataFrame como un archivo CSV
def to_csv_download_link(df, filename):
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
    csv_b64 = base64.b64encode(csv_buffer.getvalue()).decode()
    href = f'<a href="data:file/csv;base64,{csv_b64}" download="{filename}" target="_blank">Descargar CSV</a>'
    return href

# Ofrece la opción de descargar el DataFrame como un archivo CSV
st.markdown(to_csv_download_link(df_result, "profesores_perfil.csv"), unsafe_allow_html=True)

#--------------------------------------------#
# INVESTIGADORES:
#--------------------------------------------#

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
