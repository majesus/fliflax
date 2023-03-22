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
    
    st.write("El Departamento de Administración de Empresas y Marketing es una destacada entidad académica dedicada a la enseñanza y la investigación universitaria. Con más de 100 miembros especializados en diversas áreas de conocimiento, nuestro departamento es un referente en el campo de la organización de empresas y el marketing.")
    st.write("El Departamento de Administración de Empresas y Marketing está comprometido con la formación de profesionales altamente cualificados y líderes en sus campos. Nuestros docentes e investigadores trabajan para transmitir conocimientos y habilidades a nuestros estudiantes y contribuir al avance científico en sus áreas de especialización.")
    st.write("El departamento se organiza en dos áreas principales: Organización de Empresas, con 69 profesores, y Comercialización e Investigación de Mercados, con 35, lo que evidencia nuestra diversidad y versatilidad académica.")
    st.write("Nuestra presencia se distribuye en cinco facultades, la Facultad de Ciencias Económicas y Empresariales, la Facultad de Turismo y Finanzas, la Facultad de Ciencias del Trabajo, la Facultad de Comunicación y la Facultad de Ciencias de la Educación. Ello refleja nuestra capacidad para contribuir en diversos campos académicos y audiencias.")
    st.write("El departamento está conformado por profesionales de distintas categorías, incluyendo catedráticos de universidad, profesores titulares de universidad, profesores titulares de escuela universitaria y catedra´ticos de escuela universitaria, profesores contratados doctores, profesores colaboradores, profesores ayudantes doctores, profesores asociados, profesores sustitutos interinos, miembros del programa PAIDI, predoctorales PIF VI Plan Propio, posdoctorales Marie Curie.")
    st.write("Le invitamos a explorar nuestra página web y conocer las oportunidades académicas y de investigación que ofrece nuestro departamento.")
    
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
    
    # Estilos CSS personalizados
    st.markdown(
        """
        <style>
            h2.custom-header {
                color: red;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Selector de profesores
    df_result = df_result0.set_index('Nombre')
    selected_indices = st.multiselect('Selecciona el nombre del profesor:', df_result.index.unique())

    if selected_indices:
        # Muestra la ficha del profesor seleccionado
        for index in selected_indices:
            professor_data = df_result.loc[index]

            st.markdown(f"<h2 class='custom-header'>{index}</h2>", unsafe_allow_html=True)
            st.write(f"**Categoría:** {professor_data['Categoría']}")
            st.write(f"**Perfil de Prisma:** [{professor_data['Perfil de Prisma']}]({professor_data['Perfil de Prisma']})")
            st.write(f"**Teléfono:** {professor_data['Teléfono']}")
            st.write(f"**Email:** {professor_data['Email']}")
            st.write(f"**Departamento:** {professor_data['Departamento']}")
            st.write(f"**Área de Conocimiento:** {professor_data['Área de Conocimiento']}")
            st.write(f"**Centros:** {professor_data['Centros']}")
            st.write(f"**Asignaturas:** {professor_data['Asignaturas']}")

    else:
        st.write("Selecciona al menos un área de conocimiento para ver la tabla.")


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
    st.markdown("Dirección: AVDA. RAMÓN Y CAJAL, 1, CP: 41018.")
    st.write("Localidad: SEVILLA, ESPAÑA")
    st.write("Teléfono: 954557575")
    st.write("Correo electrónico: empresa@us.es")
    #st.markdown("Formulario de contacto (puedes usar el componente `st.form` para crear un formulario).")

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
        #st.write(data)
        st.map(data, use_container_width=True)                                      
