import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargar tus datos desde el archivo CSV
data = pd.read_csv("csv/dep_inv_prisma.txt")
st.write(data)

# Calcular el número de publicaciones por año
publications_by_year = data.groupby(['Año']).size().reset_index(name='Número de Publicaciones')

# Crear el gráfico de área suavizado
area_chart = go.Figure()

area_chart.add_trace(go.Scatter(x=publications_by_year['Año'], y=publications_by_year['Número de Publicaciones'],
                                mode='lines', line_shape='spline', fill='tozeroy', line=dict(smoothing=0.5)))

area_chart.update_layout(title='Evolución del número de publicaciones por año [2000-2022]',
                         xaxis=dict(range=[2000, 2022]), width=800)

# Mostrar el gráfico en Streamlit
st.plotly_chart(area_chart)
