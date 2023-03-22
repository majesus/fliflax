import streamlit as st
import pandas as pd

# Encabezado
st.set_page_config(page_title="Departamento de Administración de Empresas y Marketing", page_icon=":mortar_board:")
#st.image("img/fliflax-logo.jpg", width=200)
st.title("Departamento de Administración de Empresas y Marketing")
st.markdown("---")

# Menú de navegación
menu = st.sidebar.selectbox("Menú de navegación", ("Inicio", "Acerca de", "Investigación", "Docencia", "Personal", "Contacto"))

# Inicio
if menu == "Inicio":
    st.subheader("Bienvenidos")
    st.markdown("Texto de bienvenida y descripción del departamento.")
    
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

# Acerca de
elif menu == "Acerca de":
    st.subheader("Acerca de")
    st.markdown("Historia, misión y objetivos del departamento.")

# Investigación
elif menu == "Investigación":
    st.subheader("Investigación")
    st.markdown("Áreas de investigación, proyectos, publicaciones y colaboraciones.")

    # Diseño de la aplicación de Streamlit
    st.title("Ficha del profesor")
    
    # Lectura de la tabla con los datos de perfil:
    df_result0 = pd.read_csv('csv/profesores_perfil.csv', sep=",")

    # Selector de profesores
    df_result = df_result0.set_index('Nombre')
    selected_indices = st.multiselect('Selecciona el nombre del profesor:', df_result.index.unique())

    # Muestra la ficha del profesor seleccionado
    selected_indices = map(lambda selected_indices:selected_indices, selected_indices)
    professor_data = df_result.loc[selected_indices]

    st.header(professor_data["Nombre"])
    st.write(f"**Categoría:** {professor_data['Categoría']}")
    st.write(f"**Perfil de Prisma:** [{professor_data['Perfil de Prisma']}]({professor_data['Perfil de Prisma']})")
    st.write(f"**Teléfono:** {professor_data['Teléfono']}")
    st.write(f"**Email:** {professor_data['Email']}")
    st.write(f"**Departamento:** {professor_data['Departamento']}")
    st.write(f"**Área de Conocimiento:** {professor_data['Área de Conocimiento']}")
    st.write(f"**Centros:** {professor_data['Centros']}")
    st.write(f"**Asignaturas:** {professor_data['Asignaturas']}")

# Docencia
elif menu == "Docencia":
    st.subheader("Docencia")
    st.markdown("Programas académicos, cursos, horarios y recursos para estudiantes.")
    
    # Diseño de la aplicación de Streamlit
    st.title("Ficha del profesor")
    
    # Lectura de la tabla con los datos de perfil:
    df_result = pd.read_csv('csv/profesores_perfil.csv', sep=",")

    # Selector de profesores
    selected_professor = st.selectbox("Selecciona un profesor:", df_result["Nombre"])

    # Muestra la ficha del profesor seleccionado
    professor_data = df_result[df_result["Nombre"] == selected_professor].squeeze()

    st.header(professor_data["Nombre"])
    st.write(f"**Categoría:** {professor_data['Categoría']}")
    st.write(f"**Perfil de Prisma:** [{professor_data['Perfil de Prisma']}]({professor_data['Perfil de Prisma']})")
    st.write(f"**Teléfono:** {professor_data['Teléfono']}")
    st.write(f"**Email:** {professor_data['Email']}")
    st.write(f"**Departamento:** {professor_data['Departamento']}")
    st.write(f"**Área de Conocimiento:** {professor_data['Área de Conocimiento']}")
    st.write(f"**Centros:** {professor_data['Centros']}")
    st.write(f"**Asignaturas:** {professor_data['Asignaturas']}")

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
        st.write(f'<div style="font-size: 12px;">{selected_rows.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)
    else:
        st.write("Selecciona al menos un área de conocimiento para ver la tabla.")
   
# Contacto
elif menu == "Contacto":
    st.subheader("Contacto")
    st.markdown("Información de contacto del departamento.")
    st.markdown("Formulario de contacto (puedes usar el componente `st.form` para crear un formulario).")
