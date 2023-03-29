import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar tus datos desde el archivo CSV
data = pd.read_csv("csv/dep_inv_prisma.txt")
st.write(data)

# Calcular el número de publicaciones por año
publications_by_year = data.groupby(['Año']).size().reset_index(name='Número de Publicaciones')

# Crear el gráfico de área
area_chart = px.area(publications_by_year, x='Año', y='Número de Publicaciones',
                     title='Evolución del Número de Publicaciones por Año',
                     range_x=[2000, 2023], width=1200)

# Mostrar el gráfico en Streamlit
st.plotly_chart(area_chart)
