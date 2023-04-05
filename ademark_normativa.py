import requests
from bs4 import BeautifulSoup
import csv
import streamlit as st

url = "https://www.us.es/laUS/secretaria-general/normativas"

# Realizar una solicitud HTTP a la página web y obtener el contenido
response = requests.get(url)
content = response.content

# Analizar el contenido HTML utilizando BeautifulSoup
soup = BeautifulSoup(content, "html.parser")
dl_elements = soup.find_all("dl", class_="ckeditor-accordion")

# Recorrer los elementos dl y extraer la información relevante
data = []
for dl in dl_elements:
    dt_elements = dl.find_all("dt")
    dd_elements = dl.find_all("dd")

    for dt, dd in zip(dt_elements, dd_elements):
        title = dt.get_text(strip=True)
        links = dd.find_all("a")
        for link in links:
            normativa = link.get_text(strip=True)
            url = link["href"]
            importance = "PE"  # Por defecto, asumimos que es importante para ambos

            if "profesorado" in normativa.lower():
                importance = "P"
            elif "estudiantes" in normativa.lower():
                importance = "E"

            data.append([normativa, url, importance])

# Crear y descargar el archivo CSV
csv_file = "normativas.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Normativa", "URL", "Importancia"])
    writer.writerows(data)

st.markdown("### Descargar archivo CSV")
st.markdown(f"[{csv_file}]({csv_file})")
