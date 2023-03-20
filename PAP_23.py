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

    def aplicar_estilos(df):
        # Define la función para asignar colores de fondo a las filas
        def asignar_color(row):
            if row["Área de Conocimiento"].startswith("O"):
                return "background-color: lightgreen"
            elif row["Área de Conocimiento"].startswith("C"):
                return "background-color: lightsalmon"
            else:
                return ""

        # Aplica los estilos al DataFrame
        estilos = df.style.set_table_styles([
            {"selector": "th, td", "props": [("font-size", "10px")]},
        ]).applymap(asignar_color)

        # Añade enlaces a los nombres de los investigadores
        estilos = estilos.format({"Nombre": '<a href="{}" target="_blank">{}</a>'.format("{URL}", "{Nombre}")})
        return estilos

    df = cargar_datos()
    # Elimina las columnas "Departamento" y "URL"
    df = df.drop(columns=["Departamento", "URL"])

    st.title("Investigadores")

    # Aplica los estilos al DataFrame y muestra la tabla HTML
    tabla_con_estilos = aplicar_estilos(df)
    st.write(tabla_con_estilos.to_html(escape=False), unsafe_allow_html=True)

    
# Contacto
elif menu == "Contacto":
    st.subheader("Contacto")
    st.markdown("Información de contacto del departamento.")
    st.markdown("Formulario de contacto (puedes usar el componente `st.form` para crear un formulario).")
