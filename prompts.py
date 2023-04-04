import streamlit as st

# Título y descripción de la aplicación
st.title("Asistente de Marketing con ChatGPT")
st.write("Crea tus propios prompts y ajusta los parámetros para obtener respuestas precisas y relevantes.")
#------------------------------------------------#
# Campos de entrada para el prompt y elementos adicionales
prompt = st.text_input("Escribe tu prompt:", "")
#------------------------------------------------#
audience = st.text_input("Audiencia:", "")
tone = st.selectbox("Tono de la respuesta:", ["", "Formal", "Informal", "Divertido", "Serio", "Persuasivo"])
objectives_tasks = st.text_input("Objetivos y tareas:", "")
language = st.selectbox("Idioma:", ["", "Español", "Inglés", "Alemán", "Francés", "Italiano", "Portugués"])
#------------------------------------------------#
st.write("La temperatura es un parámetro utilizado en los modelos de lenguaje generativos para controlar la variabilidad en las respuestas generadas. Se refiere a la cantidad de aleatoriedad que se permite en la respuesta generada. Un valor más alto de temperatura genera respuestas más creativas y diversas, mientras que un valor más bajo produce respuestas más predecibles y cercanas a lo que ya ha sido visto en los datos de entrenamiento.")
st.write("Por ejemplo, si se utiliza una temperatura alta en la generación de un texto, se pueden obtener respuestas como: El cielo es de color rosa, o Los gatos vuelan. Por otro lado, si se utiliza una temperatura baja, es más probable que la respuesta generada sea coherente y realista, como: El cielo es azul, o Los gatos no pueden volar.")
temperature =st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.8, step=0.1)

st.write("La longitud máxima es el número máximo de tokens (palabras) permitidos en la respuesta generada. Este parámetro se utiliza para controlar la longitud de las respuestas generadas y evitar que sean demasiado largas o demasiado cortas.")
st.write("Por ejemplo, si se establece una longitud máxima de 50 palabras, el modelo generará una respuesta que no supere esa cantidad.")
max_length = st.slider("Maximum length:", min_value=10, max_value=4096, value=100, step=10)

st.write("Top P es un parámetro utilizado para controlar la cantidad de opciones que el modelo tiene para elegir la siguiente palabra en una respuesta generada. Se refiere al porcentaje de las opciones más probables que el modelo considera para la siguiente palabra.")
st.write("Por ejemplo, si se establece un valor Top P de 0.8, el modelo considerará las palabras con las 80% de mayor probabilidad para la siguiente palabra.")
top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=0.9, step=0.1)

st.write("La secuencia de parada se refiere a una cadena de texto que el modelo utilizará para detener la generación de texto. Es útil para controlar el tema o el enfoque de las respuestas generadas.")
st.write("Por ejemplo, si se establece una secuencia de parada como: Fin del texto, el modelo generará respuestas hasta que encuentre la secuencia: Fin del texto, luego dejará de generar texto.")
stop_sequence = st.text_input("Stop sequence:", "")

st.write("La penalización por frecuencia es como utilizar demasiada sal. Al igual que un chef debe tener cuidado de no utilizar demasiada sal, GPT debe utilizar la penalización por frecuencia para evitar repetir palabras o frases con demasiada frecuencia en la historia.")
st.write("Por ejemplo, si se establece una penalización de frecuencia, el modelo evitará generar respuestas que contengan muchas repeticiones de las mismas palabras.")
frequency_penalty = st.slider("Frequency penalty:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)

st.write("La penalización de presencia es un parámetro utilizado para controlar la aparición de ciertas palabras o frases en las respuestas generadas. Este parámetro penaliza la aparición de ciertas palabras o frases en la respuesta generada.")
st.write("Por ejemplo, si se establece una penalización de presencia para la palabra: política, el modelo evitará generar respuestas que contengan esa palabra o frases relacionadas con ese tema.")
word_presence_penalty = st.text_input("Word/s:", "")
presence_penalty = st.slider("Presence penalty:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)

st.write("Best of se refiere a la cantidad de respuestas generadas que se presentan al usuario. Este parámetro permite seleccionar el número de respuestas más adecuadas a presentar al usuario.")
st.write("Por ejemplo, si se establece un valor Best of de 5, el modelo generará 5 respuestas distintas y luego se presentarán las 5 opciones al usuario para que elija la que más le guste o la que mejor se ajuste a sus necesidades.")
best_of = st.slider("Best of:", min_value=1, max_value=20, value=1, step=1)

st.write("Inject start text es un parámetro utilizado para agregar texto específico al inicio de la respuesta generada. Este parámetro se utiliza para controlar el inicio de la respuesta generada y para agregar contexto específico al inicio de la respuesta.")
st.write("Por ejemplo, si se establece un texto de inicio como: En respuesta a su pregunta sobre el clima..., el modelo generará una respuesta que comienza con esa frase para indicar que se está respondiendo a una pregunta específica.")
inject_start_text = st.text_input("Inject start text:", "")

st.write("Inject restart text es un parámetro utilizado para agregar texto específico al reinicio de la respuesta generada. Este parámetro se utiliza para controlar el reinicio de la respuesta generada y para agregar contexto específico al reinicio de la respuesta.")
st.write("Por ejemplo, si se establece un texto de reinicio como: Continuando nuestra conversación anterior..., el modelo generará una respuesta que comienza con esa frase para indicar que se está retomando una conversación anterior y agregar contexto a la respuesta.")
inject_restart_text = st.text_input("Inject restart text:", "")
# show_probabilities = st.checkbox("Show probabilities:")
#------------------------------------------------#
# Construye el prompt completo
def build_full_prompt(prompt, audience, tone, objectives_tasks, language, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text):
    full_prompt = f"{prompt} [Audiencia: {audience}, Tono: {tone}, Objetivos y tareas: {objectives_tasks}, Idioma: {language}, Temperature: {temperature}, Maximum length: {max_length}, Top P: {top_p}, Stop sequence: {stop_sequence}, Frequency penalty: {frequency_penalty}, [Presence penalty: {presence_penalty}, Word presence penalty: {word_presence_penalty}], Best of: {best_of}, Inject start text: {inject_start_text}, Inject restart text: {inject_restart_text}]"
    return full_prompt

full_prompt = build_full_prompt(prompt, audience, tone, objectives_tasks, language, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text)

if __name__ == '__main__':
    st.write("Prompt completo para ChatGPT:")
    st.write(full_prompt)
