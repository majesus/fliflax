import streamlit as st
import pandas as pd
from PIL import Image
#----------------------------------------#
# Encabezado
st.set_page_config(page_title="Departamento de Administración de Empresas y Marketing", page_icon=":mortar_board:")
#st.image("img/fliflax-logo.jpg", width=200)
#st.title("Departamento de Administración de Empresas y Marketing")
#----------------------------------------#
custom_title = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 25px; line-height: 1.5; color: #B30A1B; font-weight: bold;"
custom_subtitle = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 18px; line-height: 1.5; color: #B30A1B;"
custom_style_15 = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 15px; line-height: 1.5;"
custom_style = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 14px; line-height: 1.5;"
#----------------------------------------#
st.markdown(
    """
    <style>
    .custom-download-button {
        font-family: 'Bahnschrift Light', Segoe UI, sans-serif;
        font-size: 14px;
        color: #B30A1B;
        background-color: #FFFFFF;
        border: 1px solid #FFFFFF;
        border-radius: 5px;
        padding: 0px;
        margin: 0px 0;
        width: 600px;
        height: 40px;
    }
    .custom-download-button:hover {
        color: #FFFFFF;
        background-color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# multiselect
change_text = """
<style>
div.st-cs.st-c5.st-bc.st-ct.st-cu {visibility: hidden;}
div.st-cs.st-c5.st-bc.st-ct.st-cu:before {content: "Wähle eine Option"; visibility: visible;}
</style>
"""
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
# st.markdown("---")
#----------------------------------------#
# Separador estético personalizado
def separador(color):
    st.markdown(
        f'<hr style="border: 1px solid {color};">', unsafe_allow_html=True
    )
#----------------------------------------#
# Menú de navegación
st.markdown(
    """
    <style>
    [data-baseweb="select"] {
        margin-top: -50px;
        font-family: 'Bahnschrift Light', sans-serif;
        font-size: 16px;
        color: #B30A1B;
        background-color: #FFFFFF;
        border: 1px solid #B30A1B;
        border-radius: 5px;
        padding: 5px;
        margin: 5px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
options = ["Inicio", "Oferta académica", "Estudiantes", "Profesorado", "Investigación", "Contacto", "Noticias"]
menu = st.selectbox("", options, key="custom_selectbox", label_visibility = "collapsed")
separador("#B30A1B")
#----------------------------------------#
# Inicio
if menu == "Inicio":
    # URL de la imagen
    url_imagen = "img/uni_about.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>BIENVENIDOS</p>", unsafe_allow_html=True)
        
    st.markdown(f"<p style='{custom_style}'>El Departamento de Administración de Empresas y Marketing de la Universidad de Sevilla es una prestigiosa entidad académica que se dedica al fomento y la promoción de la enseñanza y la investigación universitaria en los ámbitos de la gestión empresarial y el marketing. Con una plantilla de más de 100 expertos, nuestro departamento se centra en la formación de profesionales altamente capacitados y líderes en sus respectivas disciplinas.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Nos dividimos en dos áreas principales: Organización de Empresas (69 profesores) y Comercialización e Investigación de Mercados (Marketing) (35 profesores), lo que refleja nuestra diversidad y versatilidad académica. Nuestro equipo incluye académicos y profesionales que trabajan en múltiples áreas de investigación avanzada y docencia en los campos de la gestión empresarial y el marketing. Estamos presentes en trece facultades de la Universidad de Sevilla, lo que demuestra nuestro compromiso con la excelencia académica y la colaboración interdisciplinaria.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Le invitamos a explorar nuestra página web para conocer las oportunidades académicas y de investigación que ofrece nuestro departamento.</p>", unsafe_allow_html=True)

    separador("#B30A1B")

    # Título de la aplicación
    st.markdown(f"<p style='{custom_title}'>Datos de interés</p>", unsafe_allow_html=True)

    # Lista de elementos
    equipo_directivo = [
        "Director: Sánchez Franco, Manuel Jesús (majesus-us.es)",
        "Secretario: Calvo de Mora Schmidt, Arturo (schmidt-us.es)",
        "Gestora: Martínez Medina, Silvia (empresa-us.es)",
        "Administrativa: Fernández Delgado, Ana (empresa-us.es)",
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
        "Facultad de Turismo y Finanzas",
    ]
    
    centros_docencia_url = [
        "http://eip.us.es/",
        "https://etsie.us.es/",
        "https://www.informatica.us.es/",
        "https://educacion.us.es/",
        "https://fct.us.es/",
        "https://fceye.us.es/",
        "https://fcom.us.es/",
        "Facultad de Derecho",
        "https://derecho.us.es/",
        "http://farmacia.us.es/portal/",
        "https://filosofia.us.es/",
        "https://ftf.us.es/",
    ]

    st.markdown(f"<p style='{custom_subtitle}'>Dirección</p>", unsafe_allow_html=True)
    # Establecer estilos personalizados para los elementos de la lista
    # Crear una lista utilizando la etiqueta <p>
    for item in equipo_directivo:
        st.markdown(f"<p style='{custom_style}'>{item}</p>", unsafe_allow_html=True)

    with st.expander("Localización"):
        st.markdown(f"<p style='{custom_style}'><a href='http://fceye.us.es' target='_blank' style='text-decoration:none; color:inherit;'>Facultad de Ciencias Económicas y Empresariales</a></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{custom_style}'>Avda. Ramón y Cajal, n1, 41018, Sevilla, España</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{custom_style}'>Teléfono: 954557575</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{custom_style}'>Correo electrónico: empresa-us.es</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
    st.markdown(f"<p style='{custom_subtitle}'>Áreas de conocimiento</p>", unsafe_allow_html=True)
    for item in areas_conocimiento:
        st.markdown(f"<p style='{custom_style}'>{item}</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
    st.markdown(f"<p style='{custom_subtitle}'>Centros en los que impartimos docencia (por orden alfabético)</p>", unsafe_allow_html=True)
    # Utilizar la función enumerate para obtener el índice y el valor del elemento en la lista 'centros_docencia'
    for index, item in enumerate(centros_docencia):
        # Concatenar el nombre del centro de docencia con su respectiva URL
        st.markdown(f"<p style='{custom_style}'><a href='{centros_docencia_url[index]}' target='_blank' style='text-decoration:none; color:inherit;'>{item}</a></p>", unsafe_allow_html=True)
        
    separador("#B30A1B")

# Estudiantes
elif menu == "Estudiantes":
    # URL de la imagen
    # url_imagen = "img/uni_student.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>ESTUDIANTES</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='{custom_style}'>Nuestro departamento se enorgullece de contar con un cuerpo estudiantil talentoso y diverso, dedicado al estudio de las ciencias sociales con énfasis en la gestión empresarial y el marketing. Los estudiantes de nuestra institución tienen la oportunidad de participar en actividades académicas y extracurriculares que enriquecen su experiencia educativa y fomentan su crecimiento personal y profesional.</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
    # Normativa_interés
    # Leer el archivo CSV
    normativas = pd.read_csv("csv/normativas.csv")
    options = ['E'] 
    # Seleccionar las filas que cumplen la condición: E
    normativas = normativas[normativas['Codigo'].isin(options)]
    st.markdown(f"<p style='{custom_title}'>Normativa de interés</p>", unsafe_allow_html=True)
    with st.expander("Normativas"):
        # Iterar sobre las noticias y mostrarlas
        for _, normativa in normativas.iterrows():
            complete_url = f"https://www.us.es{normativa['URL']}"
            st.markdown(f"<p style='{custom_style}'><a href='{complete_url}' target='_blank' style='text-decoration:none; color:inherit;'>{normativa['Normativa']}</a></p>", unsafe_allow_html=True)

    # Documentos_interés
    st.markdown(f"<p style='{custom_title}'>Documentos de interés</p>", unsafe_allow_html=True)
    with st.expander("Documentos"):
    #---------------------------
        # Asegúrate de cambiar la ruta del archivo a la ubicación de tu archivo PDF
        import base64
        with open("csv/Tutorías.xlsb", "rb") as pdf_file: # img/tutorias_cuarta_planta_fceye.pdf
            PDFbyte = pdf_file.read()
        base64_pdf = base64.b64encode(PDFbyte).decode("utf-8")
        html_button = f'<a download="tutorias.xlsb" href="data:application/octet-stream;base64,{base64_pdf}" class="custom-download-button" target="_blank" style="text-decoration:none; color:inherit;">Descargar aquí las horas de tutorías del profesorado</a>'
        st.write(html_button, unsafe_allow_html=True)
    #---------------------------
        st.markdown(f"<p style='{custom_style}', color: #B30A1B>AVISO: En cada centro puedes consultar la normativa específica de los TFE.</p>", unsafe_allow_html=True)
    #---------------------------
    separador("#B30A1B")
    
    # Leer el archivo CSV
    noticias = pd.read_csv("csv/noticias_estudiantes.csv")
    noticias = noticias.head(n = 3)

    # Mostrar título de la sección
    st.markdown(f"<p style='{custom_title}'>Avisos</p>", unsafe_allow_html=True)

    # Iterar sobre las noticias y mostrarlas
    for _, noticia in noticias.iterrows():
        st.markdown(f"<p style='{custom_subtitle}'><b>Título:</b> {noticia['titulo']} ({noticia['fecha']})</p>", unsafe_allow_html=True)
        #st.markdown(f"<p style='{custom_style}'><b>Fecha:</b> {noticia['fecha']}</p>", unsafe_allow_html=True)
        #st.markdown(f"<p style='{custom_style}'><b>Autor:</b> {noticia['autor']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{custom_style}'><b>Resumen:</b> {noticia['resumen']}</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
# Investigación
elif menu == "Investigación":
    # URL de la imagen
    # url_imagen = "img/uni_research.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>INVESTIGACIÓN</p>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='{custom_style}'>La investigación es un componente fundamental de la misión de nuestro departamento. Nuestros académicos y estudiantes colaboran en proyectos de investigación innovadores y de vanguardia en el campo de la administración de empresas y el marketing. Estos proyectos contribuyen al avance del conocimiento en nuestras áreas de especialización y ofrecen a nuestros estudiantes la oportunidad de desarrollar habilidades de investigación y aplicar sus conocimientos en contextos prácticos. Además, el departamento mantiene relaciones de colaboración con instituciones y organizaciones nacionales e internacionales, lo que fomenta el intercambio de ideas y el enriquecimiento mutuo de nuestras líneas de investigación.</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
    # Ficha del investigador
    st.markdown(f"<p style='{custom_subtitle}'>Datos de nuestros/as investigadores/as</p>", unsafe_allow_html=True)
    
    # Lectura de la tabla con los datos de perfil:
    df_result0 = pd.read_csv('csv/investigadores_perfil.csv', sep=",")

    # Selector de profesores
    df_result = df_result0.set_index('Nombre')
    st.markdown(f"<p style='{custom_style}'>Selecciona su nombre:</p>", unsafe_allow_html=True)
    st.markdown(change_text, unsafe_allow_html=True)
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
                st.write(f"<p style='{custom_style}'><b>Grupo:</b> <a href='{professor_data['URL_grupo']}' target='_blank'>{professor_data['Grupo']}</a></p>", unsafe_allow_html=True)

            st.markdown(f"<p style='{custom_style}'><b>Instituto de Inv.:</b> {professor_data['Instituto de Inv.']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Prog. Doctorado:</b> {professor_data['Prog. Doctorado']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{custom_style}'><b>Publicaciones:</b> <a href='{professor_data['URL']}' target='_blank'>{professor_data['URL']}</a></p>", unsafe_allow_html=True)
            separador("#B30A1B")
    else:
        st.write("")

    separador("#B30A1B")

    # Título de la aplicación
    st.markdown(f"<p style='{custom_subtitle}'>Líneas de investigación</p>", unsafe_allow_html=True)
    
    from ademark_KG import knowledge_graph_app
    # Llama a la función en la parte apropiada de tu aplicación Streamlit.
    knowledge_graph_app()
    
    st.markdown("---")
    
    # Título de la aplicación
    st.markdown(f"<p style='{custom_style_15}'><b>Evolución de nuestras publicaciones</b></p>", unsafe_allow_html=True)
    
    from ademark_graphs_research import mostrar_grafico_area_suavizado
    with st.expander("Evolución"):
        mostrar_grafico_area_suavizado()
        
    st.markdown("---")
        
    # Lista de titulares
    titulares = [
        "Turismo y sostenibilidad",
        "Transformación digital y tecnologías de la información",
        "Marketing digital y redes sociales",
        "Big data y aprendizaje automático (machine learning)",
        "Inteligencia Artificial: retos y soluciones",
        "Innovación y emprendimiento",
        "Comportamiento del consumidor y valor en instituciones",
        "Estudio de demanda con incertidumbre",
    ]

    # Título de la aplicación
    st.markdown(f"<p style='{custom_style_15}'><b>Principales líneas de investigación en Marketing</b></p>", unsafe_allow_html=True)

    # Mostrar titulares como una lista con interlineado ajustado
    for titular in titulares:
        st.markdown(f"<p style='{custom_style}'>{titular}</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
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
    st.markdown(f"<p style='{custom_style_15}'><b>Principales líneas de investigación en Organización</b></p>", unsafe_allow_html=True)

    # Mostrar titulares como una lista con interlineado ajustado
    for titular in titulares:
        st.markdown(f"<p style='{custom_style}'>{titular}</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
    st.markdown(f"<p style='{custom_subtitle}'>Grupos de investigación</p>", unsafe_allow_html=True)
    with st.expander("Ver Grupos de investigación"):
        # Lectura de la tabla de Grupos con los datos de perfil:
        df_result0 = pd.read_csv('csv/investigadores_perfil.csv', sep=",")
        # Filtramos los grupos que finalizan con un paréntesis y un código alfanumérico y eliminamos duplicados
        grupos = df_result0.loc[df_result0['Grupo'].str.endswith(')'), ['Grupo', 'URL_grupo']].drop_duplicates()
        # Convertir los nombres de los grupos en mayúsculas
        grupos['Grupo'] = grupos['Grupo'].str.upper()
        
        # Crear una lista utilizando la etiqueta <p> y enlazar cada grupo con su URL correspondiente
        # Crear una lista utilizando la etiqueta <p> y enlazar cada grupo con su URL correspondiente
        for index, row in grupos.iterrows():
            st.markdown(f"<p style='{custom_style}'><a href='{row['URL_grupo']}' target='_blank' style='text-decoration:none; color:inherit;'>{row['Grupo']}</a></p>", unsafe_allow_html=True)

    separador("#B30A1B")
    
    # Instituto de investigación:
    st.markdown(f"<p style='{custom_subtitle}'>Instituto de investigación</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'><a href='http://centro.us.es/iusen/' target='_blank' style='text-decoration:none; color:inherit;'>Instituto de Economía y Negocios de la Universidad de Sevilla</a></p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
# Docencia
elif menu == "Profesorado":
    # URL de la imagen
    # url_imagen = "img/uni_teacher.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>PROFESORADO</p>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='{custom_style}'>El departamento cuenta con un destacado equipo de profesionales altamente cualificados y experimentados en los campos de la administración de empresas y el marketing. Nuestro profesorado se dedica a proporcionar una educación excepcional basada en investigaciones y prácticas actuales, y está comprometido con el éxito académico y profesional de nuestros estudiantes.</p>", unsafe_allow_html=True)

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
    else:
        st.write("")

    separador("#B30A1B")
    
    # Normativa_interés
    # Leer el archivo CSV
    normativas = pd.read_csv("csv/normativas.csv")
    options = ['P'] 
    # Seleccionar las filas que cumplen la condición: P
    normativas = normativas[normativas['Codigo'].isin(options)]
    st.markdown(f"<p style='{custom_title}'>Normativa de interés</p>", unsafe_allow_html=True)
    with st.expander("Normativas"):
        # Iterar sobre las noticias y mostrarlas
        for _, normativa in normativas.iterrows():
            complete_url = f"https://www.us.es{normativa['URL']}"
            st.markdown(f"<p style='{custom_style}'><a href='{complete_url}' target='_blank' style='text-decoration:none; color:inherit;'>{normativa['Normativa']}</a></p>", unsafe_allow_html=True)

    # Documentos_interés
    st.markdown(f"<p style='{custom_title}'>Documentos de interés</p>", unsafe_allow_html=True)
    with st.expander("Documentos"):
    #---------------------------
        # Asegúrate de cambiar la ruta del archivo a la ubicación de tu archivo PDF
        import base64
        with open("csv/Tutorías.xlsb", "rb") as pdf_file: # img/tutorias_cuarta_planta_fceye.pdf
            PDFbyte = pdf_file.read()
        base64_pdf = base64.b64encode(PDFbyte).decode("utf-8")
        html_button = f'<a download="tutorias.xlsb" href="data:application/octet-stream;base64,{base64_pdf}" class="custom-download-button" target="_blank" style="text-decoration:none; color:inherit;">Descargar aquí las horas de tutorías del profesorado</a>'
        st.write(html_button, unsafe_allow_html=True)
    #---------------------------
        st.markdown(f"<p style='{custom_style}', color: #B30A1B>AVISO: En cada centro puedes consultar la normativa específica de los TFE.</p>", unsafe_allow_html=True)
    #---------------------------
    separador("#B30A1B")

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
    # URL de la imagen
    # url_imagen = "img/uni_contact.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>CONTACTO</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='{custom_subtitle}'>Secretaría</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Avda. Ramón y Cajal, n1, 41018, Sevilla, España</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Teléfono: 954557575</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='{custom_style}'>Correo electrónico: empresa-us.es</p>", unsafe_allow_html=True)
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

    separador("#B30A1B")

# Noticias
elif menu == "Noticias":
    # URL de la imagen
    # url_imagen = "img/uni_teacher.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>NOTICIAS</p>", unsafe_allow_html=True)
    
    #st.markdown(f"<p style='{custom_style}'>El Departamento de Administración de Empresas y Marketing es una reconocida entidad académica, dedicada a la enseñanza e investigación universitaria en organización de empresas y marketing. Con más de 100 miembros expertos, nuestro departamento se enfoca en la formación de profesionales altamente cualificados y líderes en sus respectivos campos.</p>", unsafe_allow_html=True)

    #separador("#B30A1B")
    
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

# Oferta académica
elif menu == "Oferta académica":
    # URL de la imagen
    # url_imagen = "img/uni_student.png"
    # Insertar imagen
    # imagen = cargar_imagen(url_imagen)
    # st.image(imagen, caption='')
    
    st.markdown(f"<p style='{custom_title}'>OFERTA ACADÉMICA</p>", unsafe_allow_html=True)

    st.markdown(f"<p style='{custom_style}'>El departamento ofrece una amplia gama de programas y cursos de grado en ciencias sociales, con especial énfasis en la administración de empresas y el marketing. Nuestra metodología académica combina el rigor teórico con la formación práctica y el desarrollo de habilidades transferibles, lo que permite a nuestros estudiantes enfrentar los desafíos del mundo laboral con éxito y eficacia.</p>", unsafe_allow_html=True)
    
    separador("#B30A1B")
    
    #st.markdown(f"<p style='{custom_title}'>Normativa universitaria</p>", unsafe_allow_html=True)
    #st.markdown(f"<p style='{custom_style}'><a href='https://www.us.es/laUS/secretaria-general/normativas' target='_blank' style='text-decoration:none; color:inherit;'>Se recomienda hacer CLIC para consultar la normativa universitaria.</a></p>", unsafe_allow_html=True)
    
    #separador("#B30A1B")
    
    # Mostrar el título "Grados"
    st.markdown(f"<p style='{custom_subtitle}'>Principales <b>GRADOS</b> en que participamos</p>", unsafe_allow_html=True)
    
    datos = [("Facultad de Ciencias Económicas y Empresariales", "https://fceye.us.es/",          
              [("Grado en Economía", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-economia"),           
               ("Grado en Administración y Dirección de Empresas", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-administracion-y-direccion-de-empresas#edit-group-plani"),           ("Grado en Marketing e Investigación de Mercados", "https://departamento.us.es/daeep/docencia-facultad-de-ciencias-economicas-y-empresariales/#"),           ("Doble Grado en Derecho y en Economía", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/doble-grado-en-derecho-y-en-economia"),           ("Doble Grado en Administración y Dirección de Empresas y en Derecho", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/doble-grado-en-administracion-y-direccion-de-empresas-y-en")]),
             ("Facultad de Turismo y Finanzas", "https://ftf.us.es/",
              [("Grado en Turismo", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-turismo"),
               ("Grado en Finanzas y Contabilidad", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-finanzas-y-contabilidad")]),
             ("Facultad de Ciencias del Trabajo", "https://fct.us.es/",
              [("Grado en Relaciones laborales y Recursos Humanos", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-relaciones-laborales-y-recursos-humanos")]),
             ("Facultad de Comunicación", "https://fcom.us.es/",
              [("Grado en Publicidad y Relaciones Públicas", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-publicidad-y-relaciones-publicas"),
               ("Grado en Periodismo", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-periodismo"),
               ("Grado en Comunicación Audiovisual", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-comunicacion-audiovisual")]),
             ("Facultad de Ciencias de la Educación", "https://educacion.us.es/",
              [("Grado en Ciencias de la Actividad Física y del Deporte", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-ciencias-de-la-actividad-fisica-y-del-deporte")]),
             ("Facultad de Filosofía", "https://filosofia.us.es/",
              [("Grado en Estudios de Asia Oriental por la Universidad de Sevilla", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-estudios-de-asia-oriental-por-la-universidad-de")]),
             ("Facultad de Derecho", "https://derecho.us.es/",
              [("Grado en Derecho", "https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-derecho")])]
    # Mostrar los datos
    for facultad in datos:
        # Mostrar el título de la facultad con su enlace
        st.markdown(f"<p style='{custom_subtitle}'><a href='{facultad[1]}' target='_blank' style='color: #B30A1B; text-decoration: none;'>{facultad[0]}</a></p>", unsafe_allow_html=True)
        # Mostrar los títulos en los que participa la facultad
        for titulo in facultad[2]:
            st.markdown(f"<p style='{custom_style}'><a href='{titulo[1]}' target='_blank' style='color: black; text-decoration: none;'>{titulo[0]}</a></p>", unsafe_allow_html=True)   
        
    separador("#B30A1B")
    
    # Leer el archivo masteres.csv:
    df_maestrias = pd.read_csv('csv/masteres.csv', encoding='utf-8')

    # Mostrar el título "Másteres"
    st.markdown(f"<p style='{custom_subtitle}'>Principales <b>MÁSTERES</b> en que participamos</p>", unsafe_allow_html=True)

    # Iterar sobre las filas del DataFrame y crear enlaces HTML
    for _, row in df_maestrias.iterrows():
        nombre_master = row['master']
        url_master = row['url']

        st.markdown(f"<p style='{custom_style}'><a href='{url_master}' style='color: black; text-decoration: none;'>{nombre_master}</a></p>", unsafe_allow_html=True)
        
    separador("#B30A1B")
    
    # Leer el archivo doctorados.csv:
    df_maestrias = pd.read_csv('csv/doctorados.csv', encoding='utf-8')

    # Mostrar el título "Doctorasdos"
    st.markdown(f"<p style='{custom_subtitle}'>Principales <b>DOCTORADOS</b> en que participamos</p>", unsafe_allow_html=True)

    # Iterar sobre las filas del DataFrame y crear enlaces HTML
    for _, row in df_maestrias.iterrows():
        nombre_master = row['doctorado']
        url_master = row['url']

        st.markdown(f"<p style='{custom_style}'><a href='{url_master}' style='color: black; text-decoration: none;'>{nombre_master}</a></p>", unsafe_allow_html=True)

    separador("#B30A1B")
     

        
#---------------------------------------------------------#

