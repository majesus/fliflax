import streamlit as st
import pandas as pd

# Encabezado
st.set_page_config(page_title="Departamento de Administración de Empresas y Marketing", page_icon=":mortar_board:")
#st.image("img/fliflax-logo.jpg", width=200)
st.title("Departamento de Administración de Empresas y Marketing")
st.markdown("---")

# Menú de navegación
import streamlit as st
from streamlit_option_menu import option_menu
menu = option_menu(None, ["Acerca de", "Estudiantes", "Investigación", "Docencia", "Contacto"], 
    icons=['house', 'pesona-vcard'. 'person-plus', "person-plus-fill", 'mailbox'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "11px"}, 
        "nav-link": {"font-size": "11px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

# Inicio
if menu == "Acerca de":
    st.subheader("Bienvenidos")
    
    st.write("El Departamento de Administración de Empresas y Marketing es una destacada entidad académica dedicada a la enseñanza y la investigación universitaria. Con más de 100 miembros especializados en diversas áreas de conocimiento, nuestro departamento es un referente en el campo de la organización de empresas y el marketing.")
    st.write("El Departamento de Administración de Empresas y Marketing está comprometido con la formación de profesionales altamente cualificados y líderes en sus campos. Nuestros docentes e investigadores trabajan para transmitir conocimientos y habilidades a nuestros estudiantes y contribuir al avance científico en sus áreas de especialización.")
    st.write("El departamento se organiza en dos áreas de conocimiento principales: **Organización de Empresas**, con 69 profesores, y Comercialización e Investigación de Mercados, con 35, lo que evidencia nuestra diversidad y versatilidad académica.")
    st.write("Nuestra presencia se distribuye en cinco facultades, la Facultad de Ciencias Económicas y Empresariales, la Facultad de Turismo y Finanzas, la Facultad de Ciencias del Trabajo, la Facultad de Comunicación y la Facultad de Ciencias de la Educación. Ello refleja nuestra capacidad para contribuir en diversos campos académicos y audiencias.")
    st.write("El departamento está conformado por profesionales de distintas categorías, incluyendo catedráticos de universidad, profesores titulares de universidad, profesores titulares de escuela universitaria y catedráticos de escuela universitaria, profesores contratados doctores, profesores colaboradores, profesores ayudantes doctores, profesores asociados, profesores sustitutos interinos, miembros del programa PAIDI, predoctorales PIF VI Plan Propio, posdoctorales Marie Curie.")
    st.write("Le invitamos a explorar nuestra página web y conocer las oportunidades académicas y de investigación que ofrece nuestro departamento.")
    
    areas_data = {
    'Áreas de conocimiento': ['Organización de Empresas', 'Comercialización e Investigación de Mercados', 'Sin área de conocimiento'],
    'Miembros': [69, 35, 1],
    }

    centros_data = {
    'Centros': ['Facultad de CC. Económ. y Empresariales', 'Facultad de Turismo y Finanzas', 'Facultad de Ciencias del Trabajo', 'Facultad de Ciencias de la Educación', 'Facultad de Comunicación'],
    'Miembros': [74, 18, 11, 1, 1],
    }

    categorias_data = {
    'Categorías profesionales': ['Profesor Titular de Universidad', 'Catedrático de Universidad', 'Profesor Sustituto Interino', 'Profesor Titular Escuela Universitaria', 'Profesor Contratado Doctor', 'Profesor Asociado', 'Profesor Ayudante Doctor', 'PAIDI', 'Profesor Colaborador', 'Predoctoral PIF VI Plan Propio', 'Posdoctoral Marie Curie', 'Catedrático de Escuela Universitaria'],
    'Miembros': [35, 24, 18, 9, 5, 5, 4, 1, 1, 1, 1, 1],
    }
 
    areas_df = pd.DataFrame(areas_data)
    centros_df = pd.DataFrame(centros_data)
    categorias_df = pd.DataFrame(categorias_data)
    
    st.title('Tabla de Datos')

    st.header('Áreas de conocimiento')
    st.write(areas_df)

    st.header('Centros')
    st.write(centros_df)

    st.header('Categorías profesionales')
    st.write(categorias_df)

# Estudiantes
elif menu == "Estudiantes":
    st.subheader("Estudiantes")
    st.markdown("")
    
# Investigación
elif menu == "Investigación":
    st.subheader("Investigación")
    st.markdown("Áreas de investigación, proyectos, publicaciones y colaboraciones.")

    # Diseño de la aplicación de Streamlit
    st.title("Ficha del investigador/a")
    
    # Lectura de la tabla con los datos de perfil:
    df_result0 = pd.read_csv('csv/investigadores_perfil.csv', sep=",")
    
    # Estilos CSS personalizados
    st.markdown(
        """
        <style>
            h2.custom-header {
                color: steelblue;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Selector de profesores
    df_result = df_result0.set_index('Nombre')
    selected_indices = st.multiselect('Selecciona el nombre del investigador/a:', df_result.index.unique())

    import re
    if selected_indices:
        # Muestra la ficha del profesor seleccionado
        for index in selected_indices:
            professor_data = df_result.loc[index]

            st.markdown(f"<h2 class='custom-header'>{index}</h2>", unsafe_allow_html=True)
            st.write(f"**Categoría:** {professor_data['Categoría']}")
            st.write(f"**Email:** {professor_data['Email']}")
            st.write(f"**Área de Conocimiento:** {professor_data['Área de Conocimiento']}")
            st.write(f"**Departamento:** {professor_data['Departamento']}")

            # Comprueba si el valor de 'Grupo' no coincide con el patrón de números y guiones
            grupo_str = str(professor_data['Grupo'])
            if not re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', grupo_str):
                st.write(f"**Grupo:** {professor_data['Grupo']}")

            st.write(f"**Instituto de Inv.:** {professor_data['Instituto de Inv.']}")
            st.write(f"**Prog. Doctorado:** {professor_data['Prog. Doctorado']}")
            st.write(f"**URL:** [{professor_data['URL']}]({professor_data['URL']})")
    else:
        st.write("")

 
# Docencia
elif menu == "Docencia":
    st.subheader("Docencia")
    st.markdown("Programas académicos, cursos, horarios y recursos para estudiantes.")
    
    # Diseño de la aplicación de Streamlit
    st.title("Ficha del docente")
    
    # Lectura de la tabla con los datos de perfil:
    df_result0 = pd.read_csv('csv/profesores_perfil.csv', sep=",")
    
    # Estilos CSS personalizados
    st.markdown(
        """
        <style>
            h2.custom-header {
                color: steelblue;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Selector de profesores
    df_result = df_result0.set_index('Nombre')
    selected_indices = st.multiselect('Selecciona el nombre del docente:', df_result.index.unique())

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
        st.write("Selecciona al menos un docente.")

# Personal
elif menu == "Personal":
    st.subheader("Personal")
    st.markdown("Lista del personal académico y administrativo, roles y áreas de especialización.")

    dfg = pd.read_csv('csv/investigadores.csv', sep=",")

    dfg1 = dfg.set_index('Área de Conocimiento')
    selected_indices = st.multiselect('Selecciona al menos un área de conocimiento:', dfg1.index.unique())

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
        st.write("Selecciona al menos un área de conocimiento para ver sus componentes.")
    
# Contacto
elif menu == "Contacto":
    st.subheader("Contacto")
    st.markdown("Dirección: AVDA. RAMÓN Y CAJAL, 1, CP: 41018.")
    st.write("Localidad: SEVILLA, ESPAÑA")
    #st.markdown("Formulario de contacto (puedes usar el componente `st.form` para crear un formulario).")

    st.subheader("Secretaría del Departamento")
    st.write("Teléfono: 954557575")
    st.write("Correo electrónico: empresa@us.es")
    st.write("Horario de atención al público:")
    st.write("Lunes – Viernes: 12 a 14 horas")
    
    st.write("Buzón de quejas y sugerencias")
    st.write("+ Enlace a Expón@US")
    
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
