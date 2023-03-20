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

    def cargar_datos():
        df = pd.read_csv("csv/investigadores.csv")
        return df

    def mostrar_datos(df):
        for index, _ in df.iterrows():
            color = ""
            if df.at[index, "Área de Conocimiento"].startswith("O"):
                color = "lightgreen"
            elif df.at[index, "Área de Conocimiento"].startswith("C"):
                color = "lightsalmon"

            with st.container():
                st.markdown(
                    f'<p style="background-color:{color}; padding:10px; font-size:10px;"><a href="{df.at[index, "URL"]}" target="_blank">{df.at[index, "Nombre"]}</a> - {df.at[index, "Categoría"]} - {df.at[index, "Email"]} - {df.at[index, "Área de Conocimiento"]}</p>',
                    unsafe_allow_html=True,
                )

    df = cargar_datos()
    # Elimina las columnas "Departamento" y "URL"
    df = df.drop(columns=["Departamento", "URL"])

    st.title("Investigadores")
    mostrar_datos(df)
    
# Contacto
elif menu == "Contacto":
    st.subheader("Contacto")
    st.markdown("Información de contacto del departamento.")
    st.markdown("Formulario de contacto (puedes usar el componente `st.form` para crear un formulario).")
