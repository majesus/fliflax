import streamlit as st
#------------------------------------------------#
from PIL import Image
img=Image.open('img/fliflax-logo.jpg')
st.set_page_config(#layout="centered",
                   #theme="light",
                   #layout="wide",
                   page_title="Fliflax",
                   page_icon=img,
                   #initial_sidebar_state='expanded'
                   )
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        #footer {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)
#------------------------------------------------#
# Separador estético personalizado
def separador(color):
    st.markdown(
        f'<hr style="border: 1px solid {color};">', unsafe_allow_html=True
    )
#------------------------------------------------#
custom_title = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 25px; line-height: 1.5; color: #B30A1B; font-weight: bold;"
custom_subtitle = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 18px; line-height: 1.5; color: #B30A1B;"
custom_subtitle_black = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 18px; line-height: 1.5;"
custom_style_black = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 15px; line-height: 1.5;"
custom_style = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 14px; line-height: 1.5;"

# Aplicar estilos CSS personalizados a toda la página
st.write("""
<style>
    * {
        font-family: Bahnschrift Light, Segoe UI, Arial;
        font-size: 18px;
        line-height: 1.5;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)
#------------------------------------------------#
# Título y descripción de la aplicación
# Función para descargar y almacenar imágenes en caché
@st.cache
def cargar_imagen(url):
    image = Image.open(url_imagen)
    return image
  
# URL de la imagen
url_imagen = "img/fliflax-logo.jpg"
# Descargar imagen
imagen = cargar_imagen(url_imagen)
# Crear dos columnas con anchos ajustados
col1, col2 = st.beta_columns([1, 3])  # La primera columna tendrá un ancho proporcional de 1, y la segunda un ancho proporcional de 3
# Añadir imagen en la primera columna
col1.image(imagen, width=150)
# Añadir título en la segunda columna
col2.title("")
#------------------------------------------------#
st.markdown(f"<p style='{custom_subtitle_black}'>Por Manuel J. Sánchez Franco, Universidad de Sevilla.</p>", unsafe_allow_html=True)
with st.expander("Notas del autor:"):
  st.markdown(f"<p style='{custom_style}'>Es esencial señalar que esta herramienta se ha construido exclusivamente para uso docente, con la que ilustrar a los estudiantes sobre los usos, su buena y mala praxis, de los modelos de lenguaje de gran tamaño (LLMs). Con la herramienta se busca evidenciar los errores propios de este tipo de modelos de lenguaje, así como advertir en relación con las alucinaciones que se derivan de su concepto y diseño.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>La programación ha sido asistida por el modelo: GPT-4.</p>", unsafe_allow_html=True)
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_subtitle}'>Bloque 0</p>", unsafe_allow_html=True)
st.markdown(f"<p style='{custom_style_black}'>Con esta herramienta puedes crear tus propios prompts, y ajustar los principales parámetros e instrucciones dados al modelo para alinear las respuestas a tus deseos. Los parámetros e instrucciones están orientados a GPT4. No obstante, antes de comenzar debes saber las ventajas e desventajas del uso de los modelos LLMs.</p>", unsafe_allow_html=True)

with st.expander("Advertencias:"):
  st.markdown(f"<p style='{custom_subtitle}'>Ventajas:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Acceso rápido a información: GPT-4 puede proporcionar respuestas rápidas y relevantes a preguntas, lo que permite a los estudiantes investigar temas y obtener información de manera eficiente.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Generación de ideas: GPT-4 puede ayudar a los estudiantes a explorar nuevas perspectivas y generar ideas para sus proyectos de investigación o tareas.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Desarrollo de habilidades de redacción: GPT-4 puede servir como una herramienta para mejorar las habilidades de redacción de los estudiantes al proporcionar ejemplos de escritura de alta calidad y ayudar a mejorar el estilo y la gramática.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Facilitar el aprendizaje de idiomas: GPT-4 puede ser útil para estudiantes que aprenden nuevos idiomas al proporcionar traducciones, ejemplos de uso de vocabulario y práctica en la construcción de frases.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Soporte para la enseñanza: GPT-4 puede ser utilizado como un recurso adicional para profesores, proporcionando ejemplos, explicaciones y material adicional para apoyar la enseñanza.</p>", unsafe_allow_html=True)
  
  st.markdown(f"<p style='{custom_subtitle}'>Desventajas:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Confiabilidad de la información: GPT-4 puede generar respuestas incorrectas o desactualizadas, lo que podría llevar a los usuarios a obtener información errónea. GPT-4 puede generar información falsa sin previo aviso, en ocasiones en medio de un texto que, por lo demás, es preciso</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Integridad académica: La facilidad con la que GPT-4 puede generar contenido bien redactado puede fomentar la dependencia excesiva por parte de los estudiantes en el trabajo generado por la IA, en lugar de desarrollar y demostrar sus habilidades y conocimientos originales, lo que socava la integridad académica.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Falta de pensamiento crítico: La dependencia excesiva de GPT-4 puede disuadir a los estudiantes de desarrollar habilidades de pensamiento crítico y análisis independiente.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Sesgo y discriminación: GPT-4 puede reflejar y perpetuar sesgos y estereotipos presentes en los datos de entrenamiento, lo que podría llevar a conclusiones incorrectas o discriminatorias.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Falta de habilidades de comunicación: El uso excesivo de GPT-4 puede limitar las oportunidades de los estudiantes para desarrollar habilidades de comunicación interpersonal, ya que pueden depender en exceso del modelo en lugar de interactuar directamente con profesores y compañeros de clase.</p>", unsafe_allow_html=True)
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_subtitle}'>Bloque 1</p>", unsafe_allow_html=True)
st.markdown(f"<p style='{custom_style}'>En este primer bloque deseamos conocer algunos aspectos clave que deben ser establecidos al inicio para guiar la respuesta.</p>", unsafe_allow_html=True)

# Comienza el prompt y elementos adicionales
with st.expander("3 preguntas:"):
    omit = st.radio("1. ¿Deseas que olvide todas las instrucciones y restricciones dadas en los prompts anteriores?",('No', 'Sí'))
    confirm = st.radio("2. ¿Deseas confirmar que el modelo ha comprendido el prompt que vamos a diseñar, y las instrucciones y restricciones adicionales?",('Sí', 'No'))
    detail = st.radio("3. ¿Cómo debe ser la respuesta del modelo?",('equilibrada', 'precisa', 'creativa'))
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_subtitle}'>Bloque 2</p>", unsafe_allow_html=True)
st.markdown(f"<p style='{custom_style}'>Te exponemos 5 conceptos básicos para la generación de un prompt que genere una respuesta relevante.</p>", unsafe_allow_html=True)

# Conceptos clave para la generación de un prompt que generen una respuesta relevante
with st.expander("Conceptos básicos:"):
  st.markdown(f"<p style='{custom_subtitle}'>Contexto:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: Información adicional, detalles o antecedentes que ayudan a aclarar o especificar la situación, tema o propósito del prompt.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: El contexto proporciona la base para comprender el prompt y es necesario para establecer una conexión clara entre el tema y la respuesta esperada.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: La empresa ABC ha lanzado recientemente un producto innovador en el mercado de dispositivos electrónicos.</p>", unsafe_allow_html=True)

  st.markdown(f"<p style='{custom_subtitle}'>Prompt:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: La pregunta o instrucción central que se presenta al modelo de lenguaje, diseñada para obtener una respuesta específica o iniciar una discusión sobre un tema.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: El prompt es la parte principal de la interacción, y su contenido determina en gran medida la calidad y relevancia de la respuesta.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: Analice el impacto potencial de la campaña de marketing de la empresa ABC en las ventas de su nuevo producto.</p>", unsafe_allow_html=True)

  st.markdown(f"<p style='{custom_subtitle}'>Material complementario:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: Recursos adicionales, como estudios, gráficos, datos o referencias que pueden ayudar a enriquecer y respaldar la respuesta del modelo de lenguaje.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: El material complementario no forma parte del prompt en sí, pero puede ser útil para proporcionar información adicional o aclaraciones que el modelo podría utilizar en su respuesta.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: Incluya en su análisis datos de la siguiente investigación de mercado: [enlace al estudio].</p>", unsafe_allow_html=True)

  st.markdown(f"<p style='{custom_subtitle}'>Objetivos:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: Los propósitos específicos que se esperan lograr con la respuesta del modelo, como informar, persuadir, analizar o resolver un problema.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: Los objetivos guían el enfoque y el tono de la respuesta, y deben estar alineados con las necesidades y expectativas de la audiencia.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: El objetivo principal de este análisis es identificar oportunidades de mejora en la estrategia de marketing y proponer acciones específicas para incrementar las ventas.</p>", unsafe_allow_html=True)

  st.markdown(f"<p style='{custom_subtitle}'>Tareas:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: Acciones concretas o pasos que el modelo debe llevar a cabo para cumplir con los objetivos y responder adecuadamente al prompt.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: Las tareas son instrucciones claras y específicas que facilitan la estructuración y el enfoque de la respuesta.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: a) Identifique los principales canales de marketing utilizados por la empresa ABC, b) Evalúe la efectividad de cada canal en función de los datos proporcionados, y c) Proponga al menos tres acciones de marketing para mejorar el rendimiento de la campaña actual.</p>", unsafe_allow_html=True)#------------------------------------------------#
#------------------------------------------------#
contexto = st.text_area("Facilita, si lo deseas, un CONTEXTO para que la respuesta adquiera mayor relevancia. En el contexto precisa el rol que tú juegas en la conversación; más adelante te preguntaremos por el rol específico que asignas al modelo:", "")
#------------------------------------------------#
# Campos de entrada para el prompt y elementos adicionales
prompt1 = st.text_area("Escribe tu cadena de entrada (o PROMPT) para guiar la generación de texto del modelo.", "")
with st.expander("Si deseas estructurar tu prompt en módulos o pasos, aquí dispones de tres módulos o pasos adicionales:"):
    prompt2 = st.text_input("Escribe tu segundo módulo o paso", "")
    prompt3 = st.text_input("Escribe tu tercer módulo o paso:", "")
    prompt4 = st.text_input("Escribe tu cuarto módulo o paso:", "")
    step = st.radio("¿Deseas que la respuesta siga secuencialmente cada paso (o módulo) que has señalado?",('No', 'Sí'))
#------------------------------------------------#
# Añadir material complementario (por ejemplo, códigos)
anexo = st.text_area("MATERIAL complementario (ejemplos, código, etc.):", "")
#------------------------------------------------#
# Añadir objetivos y tareas
objectives_tasks = st.text_area("¿Cuáles son los OBJETIVOS que persigues en tu respuesta, y las TAREAS que crees necesarias para lograr los objetivos?", "")
#------------------------------------------------#
st.markdown(f"<p style='{custom_subtitle}'>Bloque 3</p>", unsafe_allow_html=True)
st.markdown(f"<p style='{custom_style}'>A continuación, te proponemos un conjunto de instrucciones para dotar de mayor relevancia a la respuesta esperada del modelo.</p>", unsafe_allow_html=True)

audience = st.text_input("¿Quiénes son los DESTINATARIOS de la respuesta esperada?", "")
rol = st.multiselect("¿Qué ROL específico deseas que asuma el modelo para generar la respuesta?", ["académico", "analista de datos", "analista de marketing", "analista de negocios", "analista de sistemas", "asesor financiero", "asesor legal", "asistente de investigación", "asistente personal", "biólogo", "científico de datos", "coach de vida", "cocinero", "comentarista deportivo", "consultor de recursos humanos", "consultor de ventas", "corrector de estilo / ortográfico", "crítico de cine", "crítico literario", "desarrollador de aplicaciones móviles", "desarrollador frontend", "desarrollador backend", "diseñador de experiencia de usuario (UX)", "diseñador de interfaz de usuario (UI)", "diseñador de moda", "diseñador gráfico", "diseñador multimedia", "diseñador web", "director de arte", "director de cine", "director de fotografía", "editor de revista académica", "educador", "escritor", "especialista en animación", "especialista en efectos visuales", "estadístico", "experto en marketing", "fotógrafo", "físico", "generador de prompts", "gestor de proyectos", "guía de viaje", "historiador", "informático", "ingeniero civil", "ingeniero de sonido", "interiorista", "instrucciones de uso", "matemático", "médico", "nutricionista", "periodista", "productor musical", "programador", "programador de R", "programador de Python", "programador de videojuegos", "psicólogo", "químico", "redactor publicitario", "revisor de artículos académicos", "screenwriter", "sociólogo", "sonidista", "storyteller", "técnico de soporte", "traductor", "tutor", "videógrafo"], default=[])
tone = st.multiselect("¿Cuál debe ser el TONO (de la conversación) empleado por el modelo en la respuesta?", ["experto", "amigable", "asertivo", "cercano", "divertido", "duro", "enfadado", "entusiasta", "faltón", "formal", "grosero", "informativo", "insultante", "optimista", "persuasivo", "preocupado", "profesional", "relajado", "romántico", "rudo", "serio"], default=[])
author = st.text_input("El modelo debe responder con el ESTILO del siguiente autor/a:", "")
language = st.selectbox("¿En qué IDIOMA deseas que se genere la respuesta?", ["", "español", "alemán", "francés", "inglés americano", "inglés británico", "italiano", "portugués"])
formato = st.selectbox("¿Cuál debe ser el FORMATO de la respuesta esperada?", ["", "texto", "bullet points", "tabla"])
tipo = st.selectbox("¿Qué TIPO de texto estás redactando?", ["", "artículo académico", "artículo de opinión", "definición", "diario personal/reflexión", "ejemplo", "email", "entrada de blog o redes sociales", "entrevista", "preguntas frecuentes", "guía paso a paso", "ideas", "lista de verificación (checklist)", "párrafo", "resumen ejecutivo", "script de vídeo/animación"])
extension = st.selectbox("¿Qué EXTENSIÓN o duración deseas que tenga la respuesta esperada?", ["", "corto", "medio", "largo"])
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_style}'>Si deseas que el modelo consulte en algún SITE particular para generar su respuesta, indícalo, por favor.</p>", unsafe_allow_html=True)
site = st.selectbox("Site:", ["", "scholar.google.com", "pubmed.ncbi.nlm.nih.gov", "elicit.org"])
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_style}'>Si deseas que la respuesta tenga una estructura muy específica, debes ingresar algunos ejemplos de cómo te gustaría que fueran, separados por comas. Te animo a consultar: few-shot prompting.</p>", unsafe_allow_html=True)
with st.expander("Few-Shot:"):
  st.markdown(f"<p style='{custom_style}'>La táctica few-shot prompting en prompt engineering consiste en proporcionar al modelo ejemplos limitados de preguntas y respuestas en el contexto de entrada, lo que permite que el modelo generalice y genere respuestas relevantes a nuevas preguntas similares, sin necesidad de reentrenamiento específico.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>3 + 3 = 6. La explicación es ...</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>5 + 5 = 10. La explicación es ...</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>2 + 2 = ...</p>", unsafe_allow_html=True)
st.markdown(f"<p style='{custom_style}'>A continuación, propón en el siguiente campo de texto una batería de ejemplos que ilustren el modo en que deseas que el modelo estructure tu respuesta.</p>", unsafe_allow_html=True)
shot = st.text_area("Ejemplos:", "")
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_style}'>A continuación, te proponemos un conjunto de instrucciones para agregar información de entrada (start) y también adicional (restart) en la respuesta para guiar al modelo.</p>", unsafe_allow_html=True)
with st.expander("Inject start text (texto de inicio para guiar la respuesta desde el principio):"):
  st.markdown(f"<p style='{custom_style}'>Inject start text es un parámetro utilizado para agregar texto específico al inicio de la respuesta generada como, por ejemplo: ¿Qué es la inflación? Este parámetro se utiliza para controlar el inicio de la respuesta generada y para agregar contexto específico al inicio de la respuesta.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se establece un texto de inicio como: En respuesta a su pregunta sobre el clima..., el modelo generará una respuesta que comienza con esa frase para indicar que se está respondiendo a una pregunta específica.</p>", unsafe_allow_html=True)
inject_start_text = st.text_input("Inject start text:", "")
separador("#B30A1B")

with st.expander("Inject restart text (texto de reinicio para cambiar o reorientar la dirección del flujo de la conversación):"):
  st.markdown(f"<p style='{custom_style}'>Inject restart text es un parámetro utilizado para agregar texto específico al reinicio de la respuesta generada. Este parámetro se utiliza para controlar el reinicio de la respuesta generada y para agregar contexto específico al reinicio de la respuesta.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se establece un texto de reinicio como: Me gustaría saber más sobre la inflación subyacente..., el modelo generará una respuesta que comienza con esa frase para indicar que se está retomando una conversación anterior y agregar contexto a la respuesta.</p>", unsafe_allow_html=True)
inject_restart_text = st.text_input("Inject restart text:", "")
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_subtitle}'>Bloque 4</p>", unsafe_allow_html=True)
st.markdown(f"<p style='{custom_style}'>A continuación, te proponemos un conjunto de parámetros de control de generación de texto. Estos parámetros influyen en cómo los modelos de lenguaje generan texto, afectando factores como la diversidad, la longitud y la coherencia de las respuestas.</p>", unsafe_allow_html=True)

with st.expander("Temperature (ajuste de la variabilidad -o creatividad y diversidad- en la respuesta generada):"):
  st.markdown(f"<p style='{custom_style}'>La temperatura es un parámetro utilizado en los modelos de lenguaje generativos para controlar la variabilidad en las respuestas generadas. Se refiere a la cantidad de aleatoriedad que se permite en la respuesta generada. Un valor más alto de temperatura genera respuestas más creativas y diversas, mientras que un valor más bajo produce respuestas más predecibles y cercanas a lo que ya ha sido visto en los datos de entrenamiento.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se utiliza una temperatura alta en la generación de un texto, se pueden obtener respuestas como: El cielo es de color rosa, o Los gatos vuelan. Por otro lado, si se utiliza una temperatura baja, es más probable que la respuesta generada sea coherente y realista, como: El cielo es azul, o Los gatos no pueden volar.</p>", unsafe_allow_html=True)
temperature =st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
separador("#B30A1B")

with st.expander("logit-bias (ajuste de las probabilidades de determinados tokens para ser seleccionados):"):
  st.markdown(f"<p style='{custom_style}'>El logit bias es un parámetro utilizado en los modelos de lenguaje generativos para ajustar las probabilidades de ciertos tokens antes de aplicar la función softmax, lo que afecta la selección de tokens durante la generación de texto. Al ajustar el logit bias, puedes hacer que ciertos tokens sean más o menos probables en la salida generada.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si deseas que el modelo genere más contenido relacionado con gatos, puedes aumentar el logit bias de tokens relacionados con gatos, como gato, felino o gatito. Por otro lado, si deseas reducir la probabilidad de que aparezcan palabras negativas en la salida, puedes disminuir el logit bias de tokens como triste, malo o negativo.</p>", unsafe_allow_html=True)
logit_bias_tokens = st.text_input("Tokens:", "")
logit_bias =st.slider("logit-bias:", min_value=-2.0, max_value=2.0, value=0.0, step=0.1)
separador("#B30A1B")

with st.expander("Maximum tokens (extensión en número de tokens):"):
  st.markdown(f"<p style='{custom_style}'>La longitud máxima es el número máximo de tokens (palabras) permitidos en la respuesta generada. Este parámetro se utiliza para controlar la longitud de las respuestas generadas y evitar que sean demasiado largas o demasiado cortas.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se establece una longitud máxima de 50 palabras, el modelo generará una respuesta que no supere esa cantidad.</p>", unsafe_allow_html=True)
max_length = st.slider("Maximum tokens:", min_value=10, max_value=4096, value=1024, step=10)
separador("#B30A1B")

with st.expander("Top P (ajuste de la diversidad de respuestas basado en la probabilidad acumulativa de tokens):"):
  st.markdown(f"<p style='{custom_style}'>Top P es un parámetro utilizado para controlar la cantidad de opciones que el modelo tiene para elegir la siguiente palabra en una respuesta generada. Ayuda a controlar la creatividad de las respuestas generadas al elegir palabras en función de su probabilidad. Si se elige un valor de Top P más bajo, la respuesta será más conservadora y probable, mientras que un valor más alto dará lugar a respuestas más creativas y diversas, aunque potencialmente menos coherentes.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si estableces Top P en 0.9, se combinan palabras hasta que su probabilidad acumulada alcance el 90 %. Esto permitirá que el modelo elija entre un conjunto diverso de palabras, creando respuestas más creativas y variadas, pero aún coherentes y relevantes para el contexto.</p>", unsafe_allow_html=True)
top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
separador("#B30A1B")

with st.expander("Stop sequence (expresión que, cuando el modelo la genera, detiene inmediatamente la generación de texto adicional):"):
  st.markdown(f"<p style='{custom_style}'>El parámetro Stop sequence es un parámetro utilizado en GPT-4 para indicar el final anticipado de una respuesta generada. Este parámetro permite especificar una secuencia de palabras o caracteres que, cuando el modelo los genera, detiene inmediatamente la generación de texto adicional. De esta manera, se puede controlar la longitud de la respuesta y asegurar que termine de manera coherente y apropiada.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se establece una secuencia de parada como: Fin de la explicación, el modelo generará una respuesta y, una vez que encuentre la frase: Fin de la explicación, detendrá la generación de texto adicional. Esto puede ser útil para garantizar que la respuesta se complete con una conclusión adecuada o para limitar su extensión a un contexto específico.</p>", unsafe_allow_html=True)
stop_sequence = st.text_input("Stop sequence:", "")
separador("#B30A1B")

with st.expander("Frequency penalty (valor con que penalizamos la reiteración de palabras o tokens en la respuesta):"):
  st.markdown(f"<p style='{custom_style}'>La penalización de frecuencia es un parámetro utilizado para controlar la repetición de palabras en las respuestas generadas. Este parámetro penaliza la repetición de palabras que ya han sido utilizadas en la respuesta generada.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se establece una penalización de frecuencia, el modelo evitará generar respuestas que contengan muchas repeticiones de las mismas palabras.</p>", unsafe_allow_html=True)
frequency_penalty = st.slider("Frequency penalty:", min_value=-2.0, max_value=2.0, value=0.6, step=0.1)
separador("#B30A1B")

with st.expander("Presence penalty (valor con que penalizamos la aparición de un texto en la respuesta):"):
  st.markdown(f"<p style='{custom_style}'>La penalización de presencia es un parámetro utilizado para controlar la aparición de ciertas palabras o frases en las respuestas generadas. Este parámetro penaliza la aparición de ciertas palabras o frases en la respuesta generada.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se establece una penalización de presencia para la palabra: política, el modelo evitará generar respuestas que contengan esa palabra o frases relacionadas con ese tema.</p>", unsafe_allow_html=True)
word_presence_penalty = st.text_input("Texto:", "</p>", unsafe_allow_html=True)
presence_penalty = st.slider("Presence penalty:", min_value=-2.0, max_value=2.0, value=0.5, step=0.1)
separador("#B30A1B")

with st.expander("Best of (número de respuestas solicitadas):"):
  st.markdown(f"<p style='{custom_style}'>Best of se refiere a la cantidad de respuestas generadas que se presentan al usuario. Este parámetro permite seleccionar el número de respuestas más adecuadas a presentar al usuario.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se establece un valor Best of de 5, el modelo generará 5 respuestas distintas y luego se presentarán las 5 opciones al usuario para que elija la que más le guste o la que mejor se ajuste a sus necesidades.</p>", unsafe_allow_html=True)
best_of = st.slider("Best of:", min_value=1, max_value=5, value=1, step=1)
separador("#B30A1B")

with st.expander("n-gram size (no repetir n-gramas de tamaño n):"):
  st.markdown(f"<p style='{custom_style}'>El parámetro repeat n-gram es un parámetro utilizado para controlar la repetición de secuencias de palabras (n-gramas) en la respuesta generada. Este parámetro ayuda a reducir la redundancia y a mejorar la calidad de la respuesta, asegurando que la información no se repita innecesariamente.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Por ejemplo, si se establece el valor de repeat n-gram en 3, el modelo evitará repetir cualquier secuencia de tres palabras consecutivas que ya haya aparecido en la respuesta. Esto ayuda a mantener la coherencia y la relevancia del texto generado, evitando redundancias y mejorando la legibilidad de la respuesta.</p>", unsafe_allow_html=True)
repeat_ngram = st.slider("No repeat n-gram size:", min_value=0, max_value=5, value=0, step=1)
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_subtitle}'>Bloque 5</p>", unsafe_allow_html=True)
st.markdown(f"<p style='{custom_style}'>Aquí puedes consultar el texto del prompt para su inclusión en la consolo de ChatGPT.</p>", unsafe_allow_html=True)
# Construye el prompt completo
def build_full_prompt(contexto, step, omit, confirm, anexo, extension, detail, author, prompt1, prompt2, prompt3, prompt4, audience, rol, tone, objectives_tasks, language, formato, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text, repeat_ngram, site, tipo):
    full_prompt = f"Por favor, {omit} debes olvidar las restricciones e instruccionesdadas anteriormente de comenzar a responder a este nuevo prompt. Y {step} debes seguir secuencialmente en tu respuesta los distintos prompts (o pasos) que en la cadena de pensamiento te he facilitado (Let's think step-by-step!). Es importante que recuerdes que la respuesta debe ser altamente {detail}. \n\nPor favor, incluye solo referencias bibliográficas que hayas verificado y encontrado en {site} (site/{site}) antes de incluirlas en la respuesta. \n\nA continuación, te facilito las siguientes instrucciones que debes seguir, por favor: \n\nContexto de la pregunta: \n\n{contexto} \n\nComienza la respuesta con el siguiente texto de inicio para guiar la respuesta desde el principio (o parámetro: inject_start_text): {inject_start_text} \n\nIncluye el siguiente texto (o parámetro: inject_restart_text) para reorientar la dirección de la respuesta anterior: {inject_restart_text} \n\nA continuación, se indica cómo debe estructurarse la respuesta en pasos o módulos: \n\nPrimer paso (o primer módulo): {prompt1} \n\nSegundo paso (o segundo módulo): {prompt2} \n\nTercer paso (o tercer módulo): {prompt3} \n\nCuarto paso (o cuarto módulo): {prompt4}. \n\nMaterial complementario: \n\n{anexo} \n\nObjetivos y tareas: \n\n{objectives_tasks} \n\nEjemplos de respuestas deseadas: \n\n{shot} \n\nNúmero de respuestas (parámetro: best_of): {best_of} \n\nNo repetir grupos (o n-gramas) de: {repeat_ngram} gramas (o tokens). \n\nTe doy más instrucciones que se acumulan a las anteriores: \n\nAudiencia de la respuesta: {audience} \n\nActúa como: {rol} \n\nTono de la respuesta: {tone} \n\nEstilo de la respuesta: {author} \n\nIdioma de la respuesta: {language} \n\nFormato de la respuesta: {formato} \n\nTipo de la respuesta: {tipo} \n\nParámetro temperatura (parámetro: temperature) o aleatoriedad: {temperature} \n\nExtensión (o duración) de la respuesta (parámetro: max_tokens) inferior a: {max_length} tokens \n\nLa respuesta debe ser de extensión en tokens: {extension} \n\nAl generar la respuesta se deben elegir las 'palabras (o tokens) siguientes' con probabilidades de al menos: {top_p} \n\nSi te encuentras la siguiente cadena de texto (o parámetro: stop_sequence): {stop_sequence}, ¡debes parar de escribir, por favor! \n\nDe 0 (mayor repetición) a 2 (menor repetición) repite (aproximándose el valor a 0) o evita repetir (aproximándose a el valor a 2) palabras en tu respuesta; el valor (parámetro: frequency_penalty) es: {frequency_penalty} \n\nDe 0 (mayor repetición) a 2 (menor repetición) emplea repetidamente (aproximándose el valor a 0) o evita usar en tu respuesta (aproximándose el valor a 2) el siguiente texto: {word_presence_penalty}, con un valor (o parámetro: presence_penalty) de: {presence_penalty} \n\nFinalmente, dime claramente (con un Sí o un No) si has comprendido las instrucciones: {confirm} \n\nEn caso de sí haber comprendido las instrucciones, y en formato bullet points indica, por favor, los puntos clave de mis instrucciones, y acto seguido comienza a responder potenciando la relevancia y ajustado a las instrucciones dadas (por ejemplo, contexto, prompts, material, objetivos y tareas, site, y todas las demás instrucciones que te he dado, no las olvides). En caso de no haber comprendido alguna instrucción, dime qué no has comprendido para aclararla."
    return full_prompt

full_prompt = build_full_prompt(contexto, step, omit, confirm, anexo, extension, detail, author, prompt1, prompt2, prompt3, prompt4, audience, rol, tone, objectives_tasks, language, formato, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text, repeat_ngram, site, tipo)

if __name__ == '__main__': 
    with st.expander("Prompt"):
        text_area = st.text_area("", full_prompt, key="prompt_text_area", height=300)
            
        st.markdown("1. Haz clic dentro del área de texto.")
        st.markdown("2. Utiliza `Ctrl+A` o `Cmd+A` para seleccionar todo el texto.")
        st.markdown("3. Copia el texto seleccionado con `Ctrl+C` o `Cmd+C`.")
        st.markdown("4. Pega el texto seleccionado con `Ctrl+V` o `Cmd+V` en [ChatGPT](http://ai.com).")
