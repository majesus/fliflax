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
custom_title_black = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 40px; line-height: 1.5; color: #000000; font-weight: bold;"
custom_title = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 25px; line-height: 1.5; color: #B30A1B; font-weight: bold;"
custom_subtitle = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 18px; line-height: 1.5; color: #B30A1B;"
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
separador("#B30A1B")
st.write("Crea tus propios prompts, y ajusta los parámetros para obtener respuestas precisas y relevantes. A continuación, te formulamos distintas preguntas para alinear tu prompt con tus deseos.")
separador("#B30A1B")
#------------------------------------------------#
# Comienza el prompt y elementos adicionales
with st.expander("Preguntas prescindibles"):
    omit = st.radio("¿Deseas que olvide lo anteriormente preguntado?",('No', 'Sí'))
    confirm = st.radio("¿Deseas que confirme que ha comprendido el prompt y los elementos adicionales?",('No', 'Sí'))
    detail = st.radio("La respuesta debe ser:",('Precisa', 'Creativa', 'Equilibrada'))
separador("#B30A1B")
#------------------------------------------------#
# Campos de entrada para el prompt y elementos adicionales
st.write("Escribe tu prompt que puede contener distintos pasos si lo deseas.", "")
prompt1 = st.text_area("Primer prompt (o único):", "")
with st.expander("Pasos adicionales:"):
    prompt2 = st.text_input("Escribe tu segundo paso", "")
    prompt3 = st.text_input("Escribe tu tercer paso:", "")
    prompt4 = st.text_input("Escribe tu cuarto paso:", "")
    step = st.radio("¿Deseas que la respuesta siga cada paso por orden?",('No', 'Sí'))
separador("#B30A1B")
#------------------------------------------------#
contexto = st.text_area("Contexto:", "")
separador("#B30A1B")
#------------------------------------------------#
# Añadir material complementario (por ejemplo, códigos)
anexo = st.text_area("Material complementario", "")
separador("#B30A1B")
#------------------------------------------------#
audience = st.text_input("¿A quién te diriges?", "")
rol = st.multiselect("¿Qué rol deseas que asuma ChatGPT?", ["Académico", "Analista de datos", "Asesor financiero", "Asistente personal", "Cocinero", "Corrector de estilo / ortográfico", "Diseñador gráfico", "Diseñador web", "Diseñador multimedia", "Director de arte", "Editor de revista académica", "Escritor", "Estadístico", "Generador de prompts", "Guía de viaje", "Informático", "Interiorista", "Instrucciones de uso", "Matemático", "Nutricionista", "Programador", "Redactor publicitario", "Revisor de artículos académicos", "Screenwriter", "Storyteller", "Traductor"], default=[])
tone = st.selectbox("¿Cuál debe ser el tono de la respuesta?", ["", "Experto", "Formal", "Profesional", "Informativo", "Relajado", "Cercano", "Divertido", "Serio", "Persuasivo", "Entusiasta"])
author = st.text_input("Responde con el estilo de un/a autor/a conocido/a:", "")
objectives_tasks = st.text_area("¿Cuáles son los objetivos que persigues preguntando, y las tareas necesarias para lograrlos?", "")
language = st.selectbox("¿En qué idoma deseas la respuesta?", ["", "Español", "Inglés", "Alemán", "Francés", "Italiano", "Portugués"])
formato = st.selectbox("¿Cuál debe ser el formato de la respuesta?", ["", "Texto", "Bullet points", "Tabla"])
extension = st.selectbox("¿Qué longitud deseas que tenga la respuesta?", ["", "Corto", "Medio", "Largo"])
separador("#B30A1B")
#------------------------------------------------#
with st.expander("Más parámetros:"):
    st.write("La temperatura es un parámetro utilizado en los modelos de lenguaje generativos para controlar la variabilidad en las respuestas generadas. Se refiere a la cantidad de aleatoriedad que se permite en la respuesta generada. Un valor más alto de temperatura genera respuestas más creativas y diversas, mientras que un valor más bajo produce respuestas más predecibles y cercanas a lo que ya ha sido visto en los datos de entrenamiento.")
    st.write("Por ejemplo, si se utiliza una temperatura alta en la generación de un texto, se pueden obtener respuestas como: El cielo es de color rosa, o Los gatos vuelan. Por otro lado, si se utiliza una temperatura baja, es más probable que la respuesta generada sea coherente y realista, como: El cielo es azul, o Los gatos no pueden volar.")
    temperature =st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.8, step=0.1)
    separador("#B30A1B")
    st.write("La longitud máxima es el número máximo de tokens (palabras) permitidos en la respuesta generada. Este parámetro se utiliza para controlar la longitud de las respuestas generadas y evitar que sean demasiado largas o demasiado cortas.")
    st.write("Por ejemplo, si se establece una longitud máxima de 50 palabras, el modelo generará una respuesta que no supere esa cantidad.")
    max_length = st.slider("Maximum length:", min_value=10, max_value=4096, value=100, step=10)
    separador("#B30A1B")
    st.write("Top P es un parámetro utilizado para controlar la cantidad de opciones que el modelo tiene para elegir la siguiente palabra en una respuesta generada. Se refiere al porcentaje de las opciones más probables que el modelo considera para la siguiente palabra.")
    st.write("Por ejemplo, si se establece un valor Top P de 0.8, el modelo considerará las palabras con las 80% de mayor probabilidad para la siguiente palabra.")
    top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=0.9, step=0.1)
    separador("#B30A1B")
    st.write("La secuencia de parada se refiere a una cadena de texto que el modelo utilizará para detener la generación de texto. Es útil para controlar el tema o el enfoque de las respuestas generadas.")
    st.write("Por ejemplo, si se establece una secuencia de parada como: Fin del texto, el modelo generará respuestas hasta que encuentre la secuencia: Fin del texto, luego dejará de generar texto.")
    stop_sequence = st.text_input("Stop sequence:", "")
    separador("#B30A1B")
    st.write("La penalización de frecuencia es un parámetro utilizado para controlar la repetición de palabras en las respuestas generadas. Este parámetro penaliza la repetición de palabras que ya han sido utilizadas en la respuesta generada.")
    st.write("Por ejemplo, si se establece una penalización de frecuencia, el modelo evitará generar respuestas que contengan muchas repeticiones de las mismas palabras.")
    frequency_penalty = st.slider("Frequency penalty:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)
    separador("#B30A1B")
    st.write("La penalización de presencia es un parámetro utilizado para controlar la aparición de ciertas palabras o frases en las respuestas generadas. Este parámetro penaliza la aparición de ciertas palabras o frases en la respuesta generada.")
    st.write("Por ejemplo, si se establece una penalización de presencia para la palabra: política, el modelo evitará generar respuestas que contengan esa palabra o frases relacionadas con ese tema.")
    word_presence_penalty = st.text_input("Word/s:", "")
    presence_penalty = st.slider("Presence penalty:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)
    separador("#B30A1B")
    st.write("Best of se refiere a la cantidad de respuestas generadas que se presentan al usuario. Este parámetro permite seleccionar el número de respuestas más adecuadas a presentar al usuario.")
    st.write("Por ejemplo, si se establece un valor Best of de 5, el modelo generará 5 respuestas distintas y luego se presentarán las 5 opciones al usuario para que elija la que más le guste o la que mejor se ajuste a sus necesidades.")
    best_of = st.slider("Best of:", min_value=1, max_value=20, value=1, step=1)
    separador("#B30A1B")
    st.write("Inject start text es un parámetro utilizado para agregar texto específico al inicio de la respuesta generada. Este parámetro se utiliza para controlar el inicio de la respuesta generada y para agregar contexto específico al inicio de la respuesta.")
    st.write("Por ejemplo, si se establece un texto de inicio como: En respuesta a su pregunta sobre el clima..., el modelo generará una respuesta que comienza con esa frase para indicar que se está respondiendo a una pregunta específica.")
    inject_start_text = st.text_input("Inject start text:", "")
    separador("#B30A1B")
    st.write("Inject restart text es un parámetro utilizado para agregar texto específico al reinicio de la respuesta generada. Este parámetro se utiliza para controlar el reinicio de la respuesta generada y para agregar contexto específico al reinicio de la respuesta.")
    st.write("Por ejemplo, si se establece un texto de reinicio como: Continuando nuestra conversación anterior..., el modelo generará una respuesta que comienza con esa frase para indicar que se está retomando una conversación anterior y agregar contexto a la respuesta.")
    inject_restart_text = st.text_input("Inject restart text:", "")

separador("#B30A1B")
#------------------------------------------------#
# Construye el prompt completo
def build_full_prompt(contexto, step, omit, confirm, anexo, extension, detail, author, prompt1, prompt2, prompt3, prompt4, audience, rol, tone, objectives_tasks, language, formato, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text):
    full_prompt = f"[{omit} olvida (u olvides) todo lo anterior. Y {step} sigue (o sigas) los distintos prompts (o pasos) que te he facilitado en tu respuesta. Importante: la respuesta debe ser altamente {detail}. \n\nTe facilito el contexto de mi prompt: {contexto}. El primer paso (o prompt) es: {prompt1}. El segundo paso (o prompt adicional) es: {prompt2}. El tercer paso (o prompt) es: {prompt3}. El cuarto paso (o prompt) es: {prompt4}. \n\nTambién te adjunto material complementario: {anexo}, para que la respuesta sea muy relevante y ajustada a mis prompts.] \n\n[La audiencia a que se dirige la respuesta es: {audience}. Actúa como: {rol}, y emplea un tono: {tone}. Además, la respuesta debe seguir el estilo de: {author}. Los objetivos y tareas que te asigno en tu respuesta, son: {objectives_tasks}. El idioma a emplear es: {language}. El formato de la respuesta debe ser: {formato}.] \n\n[El parámetro temperatura (parámetro: temperature) debe ser igual a: [{temperature}]. La extensión y duración de la respuesta (parámetro: maximum_length) NUNCA debe ser superior a: [{max_length}] tokens. La extensión y duración de la respuesta debe ser pues: {extension}.] \n\n[Al generar tu respuesta ve eligiendo las siguientes palabras con probabilidades de al menos: [{top_p}]. Si te encuentras la siguiente cadena de texto: [{stop_sequence}], ¡debes parar de escribir!] \n\n[De 0 (mayor repetición) a 2 (menor repetición) repite (aproximándose a 0) o evita repetir (aproximándose a 2) palabras en tu respuesta; el valor es: [{frequency_penalty}]. De 0 (mayor repetición) a 2 (menor repetición) emplea repetidamente (aproximándose a 0) o evita usar en tu respuesta (aproximándose a 2) las siguientes palabras: [{word_presence_penalty}], con un valor de: [{presence_penalty}].] \n\n[Y finalmente, e importante, comienza la respuesta con las siguientes palabras: [{inject_start_text}], y finaliza cada respuesta -independientemente de cuántas respuestas te haya pedido- con las siguientes palabras: [{inject_restart_text}] \n\n[Debes darme un número de respuestas igual a: [{best_of}].] \n\n[¿Me has comprendido? {confirm}. \n\nEn caso de Sí haberme comprendido en relación con todo lo anterior, antes de tu respuesta señala con formato bullet points los puntos clave de mi prompt, y comienza a responder con relevancia y ajustado a todos los requisitos que te he facilitado. En caso contrario, dime qué no has comprendido.]"
    return full_prompt

full_prompt = build_full_prompt(contexto, step, omit, confirm, anexo, extension, detail, author, prompt1, prompt2, prompt3, prompt4, audience, rol, tone, objectives_tasks, language, formato, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text)

if __name__ == '__main__':
    with st.expander("Consulta aquí el prompt completo para ChatGPT."):
        text_area = st.text_area("", full_prompt, key="prompt_text_area", height=300)
            
        st.markdown("1. Haz clic dentro del área de texto.")
        st.markdown("2. Utiliza `Ctrl+A` o `Cmd+A` para seleccionar todo el texto.")
        st.markdown("3. Copia el texto seleccionado con `Ctrl+C` o `Cmd+C`.")
        st.markdown("4. Pega el texto seleccionado con `Ctrl+V` o `Cmd+V` en [ChatGPT](http://ai.com).")
        
