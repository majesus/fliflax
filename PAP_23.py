import streamlit as st
import pandas as pd

# Encabezado
st.set_page_config(page_title="Departamento de Administración de Empresas y Marketing", page_icon=":mortar_board:")
st.image("img/fliflax-logo.jpg", width=200)
st.title("Departamento de Administración de Empresas y Marketing")
st.markdown("---")

# Menú de navegación
menu = st.sidebar.selectbox("Menú de navegación", ("Inicio", "Acerca de", "Investigación", "Docencia", "Personal", "Contacto"))

# Inicio
if menu == "Inicio":
    st.subheader("Bienvenidos")
    st.markdown("Texto de bienvenida y descripción del departamento.")
    #st.image("img/fliflax-logo.jpg", caption="Imagen destacada")

# Acerca de
elif menu == "Acerca de":
    st.subheader("Acerca de")
    st.markdown("Historia, misión y objetivos del departamento.")

# Investigación
elif menu == "Investigación":
    st.subheader("Investigación")
    st.markdown("Áreas de investigación, proyectos, publicaciones y colaboraciones.")

# Docencia
elif menu == "Docencia":
    st.subheader("Docencia")
    st.markdown("Programas académicos, cursos, horarios y recursos para estudiantes.")

# Personal
elif menu == "Personal":
    st.subheader("Personal")
    st.markdown("Lista del personal académico y administrativo, roles y áreas de especialización.")

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
    
# Contacto
elif menu == "Contacto":
    st.subheader("Contacto")
    st.markdown("Información de contacto del departamento.")
    st.markdown("Formulario de contacto (puedes usar el componente `st.form` para crear un formulario).")
