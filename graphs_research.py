import streamlit as st
import pandas as pd
import altair as alt

# Cargar tus datos desde el archivo CSV
data = pd.read_csv("csv/dep_inv_prisma.txt")

# Calcular el número de publicaciones por año
publications_by_year = data.groupby(['Año']).size().reset_index(name='Número de Publicaciones')

# Crear el gráfico de área apilada
area_chart = alt.Chart(publications_by_year).mark_area(
    opacity=0.5,
    line={'color': 'darkblue'}
).encode(
    alt.X('Año:Q', axis=alt.Axis(format='d'), scale=alt.Scale(domain=[2000, 2023])),
    alt.Y('Número de Publicaciones:Q', stack=None)
).properties(
    title='Evolución del Número de Publicaciones por Año',
    width=1800,
    height=300
)

# Crear el gráfico de líneas
line_chart = alt.Chart(publications_by_year).mark_line(
    color='darkgreen'
).encode(
    alt.X('Año:Q', scale=alt.Scale(domain=[2000, 2023])),
    alt.Y('Número de Publicaciones:Q')
).properties(
    width=1800,
    height=300
)

# Combinar los dos gráficos
combined_chart = area_chart + line_chart

# Mostrar el gráfico combinado en Streamlit
st.altair_chart(combined_chart, use_container=True)
