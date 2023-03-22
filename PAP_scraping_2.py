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

    grupo = soup.find("span", string="Grupo: ").find_next("a").text.strip() if soup.find("span", string="Grupo: ") else "No disponible"

    instituto_inv = soup.find("span", string="Instituto de Inv.: ").find_next("a").text.strip() if soup.find("span", string="Instituto de Inv.: ") else "No disponible"

    prog_doctorado = soup.find("span", string="Prog. doctorado: ").find_next("a").text.strip() if soup.find("span", string="Prog. doctorado: ") else "No disponible"

    return nombre, categoria, email, area_conocimiento, departamento, grupo, instituto_inv, prog_doctorado

def leer_urls_desde_csv(archivo_csv):
    df = pd.read_csv(archivo_csv)
    
    df = df.head()
    
    print(df)  # Imprime el DataFrame leído desde el archivo CSV
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
    "Grupo": [],
    "Instituto de Inv.": [],
    "Prog. Doctorado": [],
    #"URL": [],
}

for url in urls:
    st.write(f"Extrayendo información del Departamento y Área de Conocimiento de: {url}")
    nombre, categoria, email, area_conocimiento, departamento, grupo, instituto_inv, prog_doctorado = obtener_info_investigador(url)
    
    data["Nombre"].append(nombre)
    data["Categoría"].append(categoria)
    data["Email"].append(email)
    data["Área de Conocimiento"].append(area_conocimiento)
    data["Departamento"].append(departamento)
    data["Grupo"].append(grupo)
    data["Instituto de Inv."].append(instituto_inv)
    data["Prog. Doctorado"].append(prog_doctorado)

try:
    st.write(data)
except Exception as e:
    st.write(f"Error: {e}")

for column, values in data.items():
    print(f"{column}: {len(values)}")

try:
    df = pd.DataFrame(data)
    st.write(df)
except Exception as e:
    st.write(f"Error: {e}")

# Realiza la copia del DataFrame sin enlaces HTML
df_csv = df.copy()

# Convierte el nombre en un enlace HTML que apunta a la URL correspondiente
#df["Nombre"] = df.apply(lambda row: f'<a href="{row["URL"]}" target="_blank">{row["Nombre"]}</a>', axis=1)

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
