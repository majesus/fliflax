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
    icons=['house', 'person-video', 'person-plus', "person-plus-fill", 'mailbox'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "12px"}, 
        "nav-link": {"font-size": "11px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

# Inicio
if menu == "Acerca de":
    st.subheader("Bienvenidos")
    
    st.write("El Departamento de Administración de Empresas y Marketing es una reconocida entidad académica, dedicada a la enseñanza e investigación universitaria en organización de empresas y marketing. Con más de 100 miembros expertos, nuestro departamento se enfoca en la formación de profesionales altamente cualificados y líderes en sus respectivos campos.")
    st.write("Nos organizamos en dos áreas principales: Organización de Empresas (69 profesores) y Comercialización e Investigación de Mercados (35 profesores), reflejando nuestra diversidad y versatilidad académica. Nuestro equipo incluye profesionales que practican diversas líneas docentes y de investigación avanzadas en los campos de la organización de empresas y el marketing. Estamos presentes en cinco facultades, lo que demuestra nuestra capacidad para contribuir en distintos campos y audiencias.")
    st.write("Le invitamos a explorar nuestra página web para conocer las oportunidades académicas y de investigación que ofrece nuestro departamento.")
    
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

    # Separador estético personalizado
    def separador(color):
        st.markdown(
            f'<hr style="border: 1px solid {color};">', unsafe_allow_html=True
        )
    
    # Lista de titulares
    titulares = [
        "Turismo y sostenibilidad",
        "Transformación digital y tecnologías de la información",
        "Marketing digital y redes sociales",
        "Big data y aprendizaje automático (machine learning)",
        "Innovación y emprendimiento",
        "Comportamiento del consumidor y valor en instituciones",
        "Estudio de demanda con incertidumbre",
    ]

    # Título de la aplicación
    st.subheader("Líneas de investigación en el área científica de Marketing")

    # Mostrar titulares como una lista con interlineado ajustado
    st.subheader("Principales categorías:")
    st.markdown("<ul style='padding-left: 20px; line-height: 1.5;'>", unsafe_allow_html=True)
    for i, titular in enumerate(titulares, 1):
        st.markdown(f"<li>{i}. {titular}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    
    separador("#4f8bf9")
    
    # Lista de titulares
    titulares = [
        "Emprendimiento y creación de empresas",
        "Comunicación y periodismo",
        "Cultura organizacional y cambio cultural",
        "Gestión de la calidad e innovación",
        "Análisis de redes sociales y comunidades virtuales",
        "Estrategia y dirección internacional de empresas",
        "Coaching y desarrollo personal",
    ]

    # Título de la aplicación
    st.subheader("Líneas de investigación en el área científica de Organización de Empresas")

    # Mostrar titulares como una lista
    st.markdown("Principales categorías:")
    for i, titular in enumerate(titulares, 1):
        st.write(f"{i}. {titular}")
    
    separador("#4f8bf9")
    
    # Ficha del investigador
    st.subheader("Ficha del investigador/a")
    
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
            st.write(f"**Publicaciones:** [{professor_data['URL']}]({professor_data['URL']})")
    else:
        st.write("")

 
# Docencia
elif menu == "Docencia":
    st.subheader("Docencia")
    st.markdown("Programas académicos, cursos, horarios y recursos para estudiantes.")
    
    # Diseño de la aplicación de Streamlit
    st.subheader("Ficha del docente")
    
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
    import streamlit as st

    st.subheader("Dirección")
    st.markdown("AVDA. RAMÓN Y CAJAL, 1, 41018.")
    st.markdown("SEVILLA, ESPAÑA", unsafe_allow_html=True)

    st.subheader("Secretaría")
    st.markdown("<p style='font-size: 14px; line-height: 1;'>Teléfono: 954557575</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; line-height: 1;'>Correo electrónico: empresa@us.es</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; line-height: 1;'>Horario de atención al público:</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; line-height: 1;'>Lunes – Viernes: 12 a 14 horas</p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size: 14px; line-height: 1.2;'>Buzón de quejas y sugerencias: <a href='https://www.us.es/expon-us'>Expón@US</a></p>", unsafe_allow_html=True)

   
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
