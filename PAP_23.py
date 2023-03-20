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
        df = pd.read_csv("investigadores.csv")
        return df

    def filtrar_datos(df, categorias, areas_conocimiento):
        df_filtrado = df[df['categoría'].isin(categorias) & df['area_conocimiento'].isin(areas_conocimiento)]
        return df_filtrado

    def crear_tabla(df):
        for index, row in df.iterrows():
            color = ""
            if row["area_conocimiento"] == "Organización de Empresas":
                color = "lightgreen"
            elif row["area_conocimiento"] == "Comercialización e Investigación de Mercados":
                color = "lightsalmon"

            with st.container():
                st.markdown(
                    f'<p style="background-color:{color}; padding:10px;"><a href="{row["url"]}" target="_blank">{row["nombre"]}</a> - {row["categoría"]} - {row["email"]} - {row["area_conocimiento"]} - {row["departamento"]}</p>',
                    unsafe_allow_html=True,
                )

    st.title("Investigadores")

    df = cargar_datos()

    categorias = [
        "Catedrática de Escuela Universitaria",
        "Catedrática de Universidad",
        "Catedrático de Universidad",
        "Posdoctoral Marie Curie",
        "Predoctoral PIF VI Plan Propio",
        "Profesor Asociado",
        "Profesor Ayudante Doctor",
        "Profesor Contratado Doctor",
        "Profesor Sustituto Interino",
        "Profesor Titular de Universidad",
        "Profesor Titular Escuela Universitaria",
        "Profesora Asociada",
        "Profesora Ayudante Doctora",
        "Profesora Colaboradora",
        "Profesora Contratada Doctora",
        "Profesora Sustituta Interina",
        "Profesora Titular de Universidad",
        "Profesora Titular Escuela Universitaria",
    ]

    areas_conocimiento = [
        "Comercialización e Investigación de Mercados",
        "Organización de Empresas",
    ]

    categorias_seleccionadas = st.multiselect("Selecciona categorías", categorias)
    areas_seleccionadas = st.multiselect("Selecciona áreas de conocimiento", areas_conocimiento)

    if categorias_seleccionadas and areas_seleccionadas:
        df_filtrado = filtrar_datos(df, categorias_seleccionadas, areas_seleccionadas)
        crear_tabla(df_filtrado)
    else:
        st.warning("Por favor, selecciona al menos una categoría y un área de conocimiento.")


# Contacto
elif menu == "Contacto":
    st.subheader("Contacto")
    st.markdown("Información de contacto del departamento.")
    st.markdown("Formulario de contacto (puedes usar el componente `st.form` para crear un formulario).")
