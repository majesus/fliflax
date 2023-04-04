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
temperature =st.slider("Temperatura:", min_value=0.0, max_value=1.0, value=0.8, step=0.1)
max_length = st.slider("Longitud máxima:", min_value=10, max_value=4096, value=100, step=10)
top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=0.9, step=0.1)

stop_sequence = st.slider("Secuencia de parada:", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
frequency_penalty = st.slider("Penalización de frecuencia:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)
presence_penalty = st.slider("Penalización de presencia:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)

best_of = st.slider("Mejor de:", min_value=1, max_value=20, value=1, step=1)

inject_start_text = st.text_input("Texto inicial a inyectar:", "")
inject_restart_text = st.text_input("Texto de reinicio a inyectar:", "")
# show_probabilities = st.checkbox("Mostrar probabilidades:")
#------------------------------------------------#
# Construye el prompt completo
def build_full_prompt(prompt, audience, tone, objectives_tasks, language, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text, show_probabilities):
    full_prompt = f"{prompt} [Audiencia: {audience}, Tono: {tone}, Objetivos y tareas: {objectives_tasks}, Idioma: {language}, Temperatura: {temperature}, Longitud máxima: {max_length}, Top P: {top_p}, Secuencia de parada: {stop_sequence}, Penalización de frecuencia: {frequency_penalty}, Penalización de presencia: {presence_penalty}, Mejor de: {best_of}, Texto inicial a inyectar: {inject_start_text}, Texto de reinicio a inyectar: {inject_restart_text}]"
    return full_prompt

full_prompt = build_full_prompt(prompt, audience, tone, objectives_tasks, language, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text)
#------------------------------------------------#
st.write("Prompt completo para ChatGPT:")
st.write(full_prompt)
#------------------------------------------------#
