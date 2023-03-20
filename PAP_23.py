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

    dfg = pd.read_csv('csv/investigadores.csv', sep=",")

    dfg1 = dfg.set_index('Área de Conocimiento')
    selected_indices = st.multiselect('Selecciona el área de conocimiento:', dfg1.index.unique())

    if selected_indices:
        selected_indices = map(lambda selected_indices:selected_indices, selected_indices)
        selected_rows = dfg1.loc[selected_indices]

        # Convierte el nombre en un enlace HTML que apunta a la URL correspondiente
        selected_rows["Nombre"] = selected_rows.apply(lambda row: f'<a href="{row["URL"]}" target="_blank">{row["Nombre"]}</a>', axis=1)
        # Muestra el DataFrame en Streamlit como una tabla HTML
        selected_rows = selected_rows.drop(['Departamento', 'URL'], axis=1)
        #st.write(selected_rows.to_html(escape=False, index=False), unsafe_allow_html=True)
        st.write(f'<div style="font-size: 10px;">{selected_rows.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)
    else:
        st.write("Selecciona al menos un área de conocimiento para ver la tabla.")

   
# Contacto
elif menu == "Contacto":
    st.subheader("Contacto")
    st.markdown("Información de contacto del departamento.")
    st.markdown("Formulario de contacto (puedes usar el componente `st.form` para crear un formulario).")
