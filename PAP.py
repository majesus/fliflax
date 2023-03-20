import streamlit as st
#----------------------------------------------------#
from PIL import Image
img=Image.open('img/fliflax-logo.jpg')
st.set_page_config(#layout="centered",
                   #theme="light",
                   layout="wide",
                   page_title="Fliflax",
                   page_icon=img,
                   initial_sidebar_state='expanded'
                   )
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        #footer {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)
#----------------------------------------------------#
st.markdown(
  """ 
<style> 
.font {font-size:50px ; #font-family: 'sans-serif'; color: #ffffff;} 
</style>
""", unsafe_allow_html=True)
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
st.write("Bienvenidos al **Departamento de Administración de Empresas y Marketing** de __*la Universidad de Sevilla*__."
         "Nuestro equipo está compuesto por **105 docentes y 2 profesionales de administración**, comprometidos con la formación " 
         "académica y el desarrollo integral de nuestros estudiantes."
         "Impartimos docencia en más de **25 títulos de grado**, **10 títulos de máster** y participamos en **2 programas de** "
         "doctorado. Nuestro enfoque pedagógico se basa en metodologías avanzadas y adaptadas a las necesidades de los "
         "estudiantes, garantizando una educación de calidad.")
         
st.write("La investigación es un pilar fundamental en nuestro departamento. Participamos en más de **10 proyectos** "
         "competitivos y nuestras publicaciones cuentan con un alto nivel de impacto en el ámbito académico.")
         
st.write("Invitamos a los interesados a unirse a nuestra comunidad académica, donde encontrarán un entorno de "
         "aprendizaje y crecimiento, apoyado por **profesionales dedicados a la enseñanza y la investigación**.")
#----------------------------------------------------#
from streamlit_echarts import st_echarts

options = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}
    ],
}
st_echarts(options=options)
#----------------------------------------------------#
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)

#----------------------------------------------------#
from streamlit_echarts import st_echarts
import streamlit as st
st.set_page_config(layout="wide")
col1, col2, col3, col4, col5=st.beta_columns([0.2, 1, 0.2, 1, 0.2])
with col1:
    st.empty()
with col2:
    option = {
        "tooltip": {
            "formatter": '{a} <br/>{b} : {c}%'
        },
        "series": [{
            "name": '进度',
            "type": 'gauge',
            "startAngle": 180,
            "endAngle": 0,
            "progress": {
                "show": "true"
            },
            "radius":'100%', 

            "itemStyle": {
                "color": '#58D9F9',
                "shadowColor": 'rgba(0,138,255,0.45)',
                "shadowBlur": 10,
                "shadowOffsetX": 2,
                "shadowOffsetY": 2,
                "radius": '55%',
            },
            "progress": {
                "show": "true",
                "roundCap": "true",
                "width": 15
            },
            "pointer": {
                "length": '60%',
                "width": 8,
                "offsetCenter": [0, '5%']
            },
            "detail": {
                "valueAnimation": "true",
                "formatter": '{value}%',
                "backgroundColor": '#58D9F9',
                "borderColor": '#999',
                "borderWidth": 4,
                "width": '60%',
                "lineHeight": 20,
                "height": 20,
                "borderRadius": 188,
                "offsetCenter": [0, '40%'],
                "valueAnimation": "true",
            },
            "data": [{
                "value": 66.66,
                "name": '百分比'
            }]
        }]
    };


    st_echarts(options=option, key="1")


    option = {
    "tooltip": {
        "trigger": 'item'
    },
    "legend": {
        "top": '5%',
        "left": 'center'
    },
    "series": [
        {
            "name": '访问来源',
            "type": 'pie',
            "radius": ['40%', '75%'],
            "avoidLabelOverlap": "false",
            "itemStyle": {
                "borderRadius": "10",
                "borderColor": '#fff',
                "borderWidth": "2"
            },
            "label": {
                "show": "false",
                "position": 'center'
            },
            "emphasis": {
                "label": {
                    "show": "true",
                    "fontSize": '20',
                    "fontWeight": 'bold'
                }
            },
            "labelLine": {
                "show": "true"
            },
            "data": [
                {"value": 1048, "name": '搜索引擎'},
                {"value": 735, "name": '直接访问'},
                {"value": 580, "name": '邮件营销'},
                {"value": 484, "name": '联盟广告'},
                {"value": 300, "name": '视频广告'}
            ]
        }
    ]
};

    st_echarts(options=option, key="2")

with col3:
    st.empty()

with col4:
    option = {
    "legend": {
        "top": 'top'
    },
    "toolbox": {
        "show": "true",
        "feature": {
            "mark": {"show": "true"},
            "dataView": {"show": "true", "readOnly": "false"},
            "restore": {"show": "true"},
            
        }
    },
    "series": [
        {
            "name": '面积模式',
            "type": 'pie',
            "radius": ["30", "120"],
            "center": ['50%', '60%'],
            "roseType": 'area',
            "itemStyle": {
                "borderRadius": "8"
            },
            "data": [
                {"value": 40, "name": '苹果'},
                {"value": 38, "name": '梨子'},
                {"value": 32, "name": '香蕉'},
                {"value": 30, "name": '桃子'},
                {"value": 28, "name": '葡萄'},
                {"value": 26, "name": '芒果'},
                {"value": 22, "name": '李子'},
                {"value": 18, "name": '菠萝'}
            ]
        }
    ],
    "tooltip": {
                    "show": "true"
                },
    "label": {
        "show":"true"
    },
};


    st_echarts(options=option, key="3")

    option = {
        "toolbox": {
        "show": "true",
        "feature": {
          "dataZoom": {
            "yAxisIndex": "none"
          },
          "dataView": {
            "readOnly": "false"
          },
          "magicType": {
            "type": ["line", "bar"]
          },
          "restore": {"show":"true"},
        }
      },
        "xAxis": {
            "type": 'category',
            "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [
                {"value":900, "itemStyle":{"color":"#FF0000"}}, 
                {"value":750, "itemStyle":{"color":"#FF7D00"}},
                {"value":520, "itemStyle":{"color":"#FFFF00"}},
                {"value":350, "itemStyle":{"color":"#00FF00"}},
                {"value":200, "itemStyle":{"color":"#0000FF"}},
                {"value":130, "itemStyle":{"color":"#00FFFF"}},
                {"value":70, "itemStyle":{"color":"#FF00FF"}},
                ],
            "type": 'bar'

        }],
        "tooltip": {
                        "show": "true"
                    },
        "label": {
            "show":"true"
        },
        
                        
        };
    st_echarts(options=option, key="4")

with col5:
    st.empty()

#----------------------------------------------------#

import pandas as pd

st.markdown("""
<style>
.container {
    width: 800px !important;
}
</style>
""", unsafe_allow_html=True)

# Coordenadas de la Facultad de Estudios
latitude = 36.7277394
longitude = -4.41775599241557

# Crear un DataFrame de Pandas con las coordenadas
data = pd.DataFrame({
    "lat": [37.377777777778, 37.378888888889, 37.405277777778],
    "lon": [-5.9743055555556, -5.9733611111111, -6.0030555555556],
    "Facultad": ["Ciencias Económicas y Empresariales", "Turismo y Finanzas", "Comunicación"]
})

# Mostrar el mapa en Streamlit con las coordenadas proporcionadas
container = st.container()
with container:
    st.write(data)
    st.map(data, use_container_width=True)
#----------------------------------------------------#

import streamlit as st
# Crear una columna lateral
st.sidebar.write("## En **Fliflax** te hemos construido una calculadora de la **frecuencia efectiva mínima**.")

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
