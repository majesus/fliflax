import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def mostrar_grafico_area_suavizado():
    # Cargar tus datos desde el archivo CSV
    data = pd.read_csv("csv/dep_inv_prisma.txt")

    # Calcular el número de publicaciones por año
    publications_by_year = data.groupby(['Año']).size().reset_index(name='Número de Publicaciones')

    # Crear el gráfico de área suavizado
    area_chart = go.Figure()

    area_chart.add_trace(go.Scatter(x=publications_by_year['Año'], y=publications_by_year['Número de Publicaciones'],
                                    mode='lines', line_shape='spline', fill='tozeroy', line=dict(smoothing=0.5, color='blue'), fillcolor='rgba(0, 0, 255, 0.2)'))

    area_chart.update_layout(title='Evolución del número de publicaciones por año [2000-2022]',
                             xaxis=dict(range=[2000, 2022]),
                             width=650,
                             annotations=[dict(xref='paper', yref='paper', x=0, y=-0.5,
                                               xanchor='left', yanchor='bottom',
                                               text='Fuente: PRISMA, Universidad de Sevilla',
                                               font=dict(size=12),
                                               showarrow=False)])

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(area_chart)

