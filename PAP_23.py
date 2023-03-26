import streamlit as st
import pandas as pd
from PIL import Image
#----------------------------------------#
# Encabezado
st.set_page_config(page_title="Departamento de Administración de Empresas y Marketing", page_icon=":mortar_board:")
#st.image("img/fliflax-logo.jpg", width=200)
#st.title("Departamento de Administración de Empresas y Marketing")
#----------------------------------------#
custom_title = "font-family: Bahnschrift Light; font-size: 23px; line-height: 1.5; color: #B30A1B; font-weight: bold;"
custom_subtitle = "font-family: Bahnschrift Light; font-size: 16px; line-height: 1.5; color: #B30A1B;"
custom_style = "font-family: Bahnschrift Light; font-size: 12px; line-height: 1.5;"
#----------------------------------------#
# Función para descargar y almacenar imágenes en caché
@st.cache
def cargar_imagen(url):
    image = Image.open(url_imagen)
    return image

# URL de la imagen
url_imagen = "img/uni_logo_ademark.png"
# Descargar imagen
imagen = cargar_imagen(url_imagen)
# Crear dos columnas con anchos ajustados
col1, col2 = st.beta_columns([1, 3])  # La primera columna tendrá un ancho proporcional de 1, y la segunda un ancho proporcional de 3
# Añadir imagen en la primera columna
col1.image(imagen, width=150)
# Añadir título en la segunda columna
col2.title("Administración de Empresas y Marketing")
#----------------------------------------#
st.markdown("---")
#----------------------------------------#
# Separador estético personalizado
def separador(color):
    st.markdown(
        f'<hr style="border: 1px solid {color};">', unsafe_allow_html=True
    )
#----------------------------------------#
# Menú de navegación
import streamlit as st
from streamlit_option_menu import option_menu
menu = option_menu(None, ["Inicio", "Investigar", "Enseñar", "Contactar", "Noticias"], 
    icons=['house', 'person-video', 'person-plus', "person-plus-fill", 'mailbox'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "12px"}, 
        "nav-link": {"font-size": "11px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)
#----------------------------------------#
# Inicio
if menu == "Inicio":
    # URL de la imagen
    url_imagen = "img/uni_about.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>BIENVENIDOS</p>", unsafe_allow_html=True)
        
    st.markdown(f"<p style='{custom_style}'>El Departamento de <b>Administración de Empresas y Marketing</b> es una reconocida entidad académica, dedicada a la enseñanza e investigación universitaria en organización de empresas y marketing. Con más de 100 miembros expertos, nuestro departamento se enfoca en la formación de profesionales altamente cualificados y líderes en sus respectivos campos.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Nos organizamos en dos áreas principales: <b>Organización de Empresas</b> (69 profesores) y <b>Comercialización e Investigación de Mercados (Marketing)</b> (35 profesores), reflejando nuestra diversidad y versatilidad académica. Nuestro equipo incluye profesionales que practican diversas líneas docentes y de investigación avanzadas en los campos de la organización de empresas y el marketing. Estamos presentes en <b>trece facultades</b>, lo que demuestra nuestra capacidad para contribuir en distintos campos y audiencias.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Le invitamos a explorar nuestra página web para conocer las oportunidades académicas y de investigación que ofrece nuestro departamento.</p>", unsafe_allow_html=True)

    separador("#B30A1B")

    # Título de la aplicación
    st.markdown(f"<p style='{custom_title}'>Datos de interés</p>", unsafe_allow_html=True)

    # Lista de elementos
    equipo_directivo = [
        "Director: Sánchez Franco, Manuel Jesús",
        "Secretario: Calvo de Mora Schmidt, Arturo",
        "Gestora: Martínez Medina, Silvia",
        "Administrativa: Fernández Delgado, Ana",
    ]

    areas_conocimiento = [
        "Organización de Empresas",
        "Comercialización e Investigación de Mercados",
    ]

    centros_docencia = [
        "Escuela Internacional de Posgrado (EIP)",
        "Escuela Técnica Superior de Ingeniería de Edificación",
        "Escuela Técnica Superior de Ingeniería Informática",
        "Facultad de Ciencias de la Educación",
        "Facultad de Ciencias del Trabajo",
        "Facultad de Ciencias Económicas y Empresariales",
        "Facultad de Comunicación",
        "Facultad de Derecho",
        "Facultad de Enfermería, Fisioterapia y Podología",
        "Facultad de Farmacia",
        "Facultad de Filosofía",
        "Facultad de Medicina",
        "Facultad de Turismo y Finanzas",
    ]

    st.markdown(f"<p style='{custom_subtitle}'>Dirección</p>", unsafe_allow_html=True)
    # Establecer estilos personalizados para los elementos de la lista
    # Crear una lista utilizando la etiqueta <p>
    for item in equipo_directivo:
        st.markdown(f"<p style='{custom_style}'>{item}</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='{custom_subtitle}'>Áreas de conocimiento</p>", unsafe_allow_html=True)
    for item in areas_conocimiento:
        st.markdown(f"<p style='{custom_style}'>{item}</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='{custom_subtitle}'>Centros en los que imparte docencia</p>", unsafe_allow_html=True)
    for item in centros_docencia:
        st.markdown(f"<p style='{custom_style}'>{item}</p>", unsafe_allow_html=True)

# Estudiantes
elif menu == "Estudiar":
    # URL de la imagen
    # url_imagen = "img/uni_student.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.subheader("Estudiar")
    
    st.write("El Departamento de **Administración de Empresas y Marketing** es una reconocida entidad académica, dedicada a la enseñanza e investigación universitaria en organización de empresas y marketing. Con más de 100 miembros expertos, nuestro departamento se enfoca en la formación de profesionales altamente cualificados y líderes en sus respectivos campos.")
    st.markdown("")
    
# Investigación
elif menu == "Investigar":
    # URL de la imagen
    url_imagen = "img/uni_research.png"
    # Insertar imagen
    imagen = cargar_imagen(url_imagen)
    st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>INVESTIGAR</p>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='{custom_style}'>El Departamento de Administración de Empresas y Marketing es una reconocida entidad académica, dedicada a la enseñanza e investigación universitaria en organización de empresas y marketing. Con más de 100 miembros expertos, nuestro departamento se enfoca en la formación de profesionales altamente cualificados y líderes en sus respectivos campos.</p>", unsafe_allow_html=True)

    separador("#B30A1B")
    
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
    st.markdown(f"<p style='{custom_subtitle}'>Líneas de investigación en Marketing</p>", unsafe_allow_html=True)

    # Mostrar titulares como una lista con interlineado ajustado
    for titular in titulares:
        st.markdown(f"<p style='{custom_style}'>{titular}</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
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
    st.markdown(f"<p style='{custom_subtitle}'>Líneas de investigación en Organización</p>", unsafe_allow_html=True)

    # Mostrar titulares como una lista con interlineado ajustado
    for titular in titulares:
        st.markdown(f"<p style='{custom_style}'>{titular}</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
    # Ficha del investigador
    st.markdown(f"<p style='{custom_subtitle}'>Datos de nuestros/as investigadores/as</p>", unsafe_allow_html=True)
    
    # Lectura de la tabla con los datos de perfil:
    df_result0 = pd.read_csv('csv/investigadores_perfil.csv', sep=",")

    # Selector de profesores
    df_result = df_result0.set_index('Nombre')
    st.markdown(f"<p style='{custom_style}'>Selecciona su nombre:</p>", unsafe_allow_html=True)
    selected_indices = st.multiselect('', df_result.index.unique())
        
    import re
    if selected_indices:
        # Muestra la ficha del profesor seleccionado
        for index in selected_indices:
            professor_data = df_result.loc[index]

            st.markdown(f"<p style='{custom_subtitle}', color = '#8DB4ED'><b>{index}</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Categoría:</b> {professor_data['Categoría']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Email:</b> {professor_data['Email']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Área de Conocimiento:</b> {professor_data['Área de Conocimiento']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Departamento:</b> {professor_data['Departamento']}</p>", unsafe_allow_html=True)

            # Comprueba si el valor de 'Grupo' no coincide con el patrón de números y guiones
            grupo_str = str(professor_data['Grupo'])
            if not re.fullmatch(r'\d{4}-\d{4}-\d{4}-\d{4}', grupo_str):
                st.write(f"<p style='{custom_style}'><b>Grupo:</b> {professor_data['Grupo']}</p>", unsafe_allow_html=True)

            st.markdown(f"<p style='{custom_style}'><b>Instituto de Inv.:</b> {professor_data['Instituto de Inv.']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Prog. Doctorado:</b> {professor_data['Prog. Doctorado']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Publicaciones:</b> <a href='{professor_data['URL']}' target='_blank'>{professor_data['URL']}</a></p>", unsafe_allow_html=True)
            separador("#B30A1B")
    else:
        st.write("")

 
# Docencia
elif menu == "Enseñar":
    # URL de la imagen
    # url_imagen = "img/uni_teacher.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>ENSEÑAR</p>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='{custom_style}'>El Departamento de Administración de Empresas y Marketing es una reconocida entidad académica, dedicada a la enseñanza e investigación universitaria en organización de empresas y marketing. Con más de 100 miembros expertos, nuestro departamento se enfoca en la formación de profesionales altamente cualificados y líderes en sus respectivos campos.</p>", unsafe_allow_html=True)

    separador("#B30A1B")
    
    # Ficha del docente
    st.markdown(f"<p style='{custom_subtitle}'>Datos de nuestros/as docentes</p>", unsafe_allow_html=True)
    
    # Lectura de la tabla con los datos de perfil:
    df_result0 = pd.read_csv('csv/profesores_perfil.csv', sep=",")
    
    # Selector de profesores
    df_result = df_result0.set_index('Nombre')
    st.markdown(f"<p style='{custom_style}'>Selecciona su nombre:</p>", unsafe_allow_html=True)
    selected_indices = st.multiselect('', df_result.index.unique())
        
    import re
    # Función para reemplazar "nan" por "No disponible"
    def replace_nan(value):
        if pd.isna(value):
            return "No disponible"
        return value

    if selected_indices:
        for index in selected_indices:
            professor_data = df_result.loc[index]

            for key in professor_data.keys():
                professor_data[key] = replace_nan(professor_data[key])

            # El resto del código sigue igual
            st.markdown(f"<p style='{custom_subtitle}', color = '#8DB4ED'>{index}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Categoría:</b> {professor_data['Categoría']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Publicaciones:</b> <a href='{professor_data['Perfil de Prisma']}' target='_blank'>{professor_data['Perfil de Prisma']}</a></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Email:</b> {professor_data['Email']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Teléfono:</b> {professor_data['Teléfono']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Área de Conocimiento:</b> {professor_data['Área de Conocimiento']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Departamento:</b> {professor_data['Departamento']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Centros:</b> {professor_data['Centros']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Asignaturas:</b> {professor_data['Asignaturas']}</p>", unsafe_allow_html=True)
            separador("#B30A1B")
    else:
        st.write("")

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
elif menu == "Contactar":
    # URL de la imagen
    # url_imagen = "img/uni_contact.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>CONTACTAR</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='{custom_subtitle}'>Secretaría</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Avda. Ramón y Cajal, n1, 41018, Sevilla, España</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Teléfono: 954557575</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Correo electrónico: empresa@us.es</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_subtitle}', color = '#B30A1B'>Horario de atención al público:</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Lunes – Viernes: 12 a 14 horas</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='{custom_style}'>Buzón de quejas y sugerencias: <a href='https://www.us.es/expon-us'>Expón@US</a></p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
   
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

# Noticias
elif menu == "Noticias":
    # URL de la imagen
    # url_imagen = "img/uni_teacher.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>NOTICIAS</p>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='{custom_style}'>El Departamento de Administración de Empresas y Marketing es una reconocida entidad académica, dedicada a la enseñanza e investigación universitaria en organización de empresas y marketing. Con más de 100 miembros expertos, nuestro departamento se enfoca en la formación de profesionales altamente cualificados y líderes en sus respectivos campos.</p>", unsafe_allow_html=True)

    separador("#B30A1B")
    
    # Leer el archivo CSV
    noticias = pd.read_csv("csv/noticias.csv")
    noticias = noticias.head(n = 10)

    # Mostrar título de la sección
    st.markdown(f"<p style='{custom_subtitle}'>Principales noticias</p>", unsafe_allow_html=True)

    # Iterar sobre las noticias y mostrarlas
    for _, noticia in noticias.iterrows():
        st.markdown(f"<p style='{custom_subtitle}'><b>Título:</b> {noticia['titulo']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{custom_style}'><b>Fecha:</b> {noticia['fecha']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{custom_style}'><b>Autor:</b> {noticia['autor']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{custom_style}'><b>Resumen:</b> {noticia['resumen']}</p>", unsafe_allow_html=True)
        separador("#B30A1B")
