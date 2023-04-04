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
st.write("La temperatura es como la del horno. Al igual que un chef necesita ajustar el horno a la temperatura adecuada para hornear el pastel a la perfección, GPT necesita ajustar la temperatura al nivel adecuado para generar la historia más realista y coherente.")
temperature =st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.8, step=0.1)
st.write("La longitud máxima es como el tamaño del molde. Del mismo modo que un chef debe elegir el molde adecuado para hornear la tarta, GPT debe establecer la longitud máxima para garantizar que la historia tenga la longitud adecuada y no se eternice.")
max_length = st.slider("Maximum length:", min_value=10, max_value=4096, value=100, step=10)
st.write("La P superior es como el tipo de molde. Al igual que un chef debe decidir el tipo de molde (redondo, cuadrado, etc.) en el que horneará el pastel, GPT debe establecer la p superior para generar la historia de la forma que considere más adecuada.")
top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=0.9, step=0.1)

st.write("La secuencia de parada es como el orden de los ingredientes. Al igual que un chef necesita añadir los ingredientes en el orden correcto, GPT necesita seguir la secuencia de pasos para generar la historia en el orden correcto.")
stop_sequence = st.text_input("Stop sequence:", "")
st.write("La penalización por frecuencia es como utilizar demasiada sal. Al igual que un chef debe tener cuidado de no utilizar demasiada sal, GPT debe utilizar la penalización por frecuencia para evitar repetir palabras o frases con demasiada frecuencia en la historia.")
frequency_penalty = st.slider("Frequency penalty:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)
st.write("La penalización por presencia es como utilizar demasiado azúcar. Al igual que un chef debe tener cuidado de no utilizar demasiado azúcar, GPT necesita utilizar la penalización por presencia para evitar tener palabras o frases que no encajen en la historia.")
presence_penalty = st.slider("Presence penalty:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)

st.write("El best of es como la presentación final del pastel. Al igual que un chef quiere presentar el pastel de la mejor manera posible, GPT quiere generar la mejor historia posible.")
best_of = st.slider("Best of:", min_value=1, max_value=20, value=1, step=1)

st.write("Son como decorar el pastel. Al igual que un chef puede añadir decoraciones para que la tarta tenga un aspecto más atractivo, GPT puede añadir texto para que la historia sea más interesante.")
inject_start_text = st.text_input("Inject start text:", "")
st.write("Es como la prueba de sabor del pastel. Al igual que un chef puede probar el pastel para ver si necesita más azúcar o sal, GPT puede mostrar las probabilidades para ver si el texto generado es coherente y realista.")
inject_restart_text = st.text_input("Inject restart text:", "")
# show_probabilities = st.checkbox("Show probabilities:")
#------------------------------------------------#
# Construye el prompt completo
def build_full_prompt(prompt, audience, tone, objectives_tasks, language, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text):
    full_prompt = f"{prompt} [Audiencia: {audience}, Tono: {tone}, Objetivos y tareas: {objectives_tasks}, Idioma: {language}, Temperatura: {temperature}, Longitud máxima: {max_length}, Top P: {top_p}, Secuencia de parada: {stop_sequence}, Penalización de frecuencia: {frequency_penalty}, Penalización de presencia: {presence_penalty}, Mejor de: {best_of}, Texto inicial a inyectar: {inject_start_text}, Texto de reinicio a inyectar: {inject_restart_text}]"
    return full_prompt

full_prompt = build_full_prompt(prompt, audience, tone, objectives_tasks, language, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text)

if __name__ == '__main__':
    st.write("Prompt completo para ChatGPT:")
    st.write(full_prompt)
