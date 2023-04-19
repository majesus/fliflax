import streamlit as st

# Datos de entrada 
tv_audience = 2000000  
tv_insertions = 3
radio_audience = 1000000  
radio_insertions = 2
press_audience = 500000  
press_insertions = 1 
total_population = 10000000

# Duplicación entre medios
tv_radio_dup = 0.10  
tv_press_dup = 0.05
radio_press_dup = 0.02

# Función para calcular alcance 
def get_reach(audience, insertions, duplication):
  reach = audience * (1 - duplication)
  for i in range(2, insertions + 1):
    reach += audience * (duplication ** (i - 1)) * (1 - duplication)
  return reach

# Función para calcular distribución de frecuencias
def get_frequency_dist(audience, insertions, duplication):
  frequency_dist = {1: 0}
  for i in range(2, insertions + 1):
    frequency_dist[i] = audience * (duplication ** (i - 1)) * (1 - duplication)
  return frequency_dist

# Interfaz de Streamlit
st.title('Modelo de cobertura CANEX')
st.subheader('Datos de entrada')
col1, col2 = st.beta_columns(2)
with col1:
  st.write('Audiencia TV: ', tv_audience)
  st.write('Inserciones TV: ', tv_insertions)
with col2:  
  st.write('Audiencia Radio: ', radio_audience)
  st.write('Inserciones Radio: ', radio_insertions)  
st.write('Audiencia Prensa: ', press_audience)  
st.write('Inserciones Prensa: ', press_insertions)
st.write('Población Total: ', total_population)
st.write('Duplicación TV-Radio: ', tv_radio_dup) 
st.write('Duplicación TV-Prensa: ', tv_press_dup)
st.write('Duplicación Radio-Prensa: ', radio_press_dup)

# Cálculo de alcance 
tv_reach = get_reach(tv_audience, tv_insertions, tv_radio_dup + tv_press_dup) 
radio_reach = get_reach(radio_audience, radio_insertions, radio_press_dup)
press_reach = get_reach(press_audience, press_insertions, 0)  
total_reach = tv_reach + radio_reach + press_reach - (tv_reach*radio_reach*press_reach)/total_population

# Cálculo de distribución de frecuencias
tv_freq_dist = get_frequency_dist(tv_audience, tv_insertions, tv_radio_dup + tv_press_dup)
radio_freq_dist = get_frequency_dist(radio_audience, radio_insertions, radio_press_dup) 
press_freq_dist = get_frequency_dist(press_audience, press_insertions, 0)
total_freq_dist = {k: tv_freq_dist.get(k, 0) + radio_freq_dist.get(k, 0) + press_freq_dist.get(k, 0) for k in set(tv_freq_dist) | set(radio_freq_dist) | set(press_freq_dist)}

# Mostrar resultados 
st.subheader('Resultados')
st.write('Alcance Total: ', total_reach)
st.write('Distribución de Frecuencias: ', total_freq_dist) 
