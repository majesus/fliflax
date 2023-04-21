import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Datos ficticios de ejemplo
data = {
    'population': [10000, 20000, 15000, 25000, 12000],
    'audiencia': [500, 1500, 1200, 800, 600],
    'audiencia_target': [400, 1200, 1000, 700, 500],
    'spots': [10, 20, 15, 25, 12],
    'Precio': [2000, 5000, 4000, 6000, 3000]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Calcular las columnas adicionales
df['rating'] = (df['audiencia'] * 100) / df['population']
df['rating_target'] = (df['audiencia_target'] * 100) / df['population']
df['Afinidad'] = df['rating_target'] / df['rating']
df['impressions'] = df['audiencia'] * df['spots']
df['GRP'] = (df['impressions'] / df['population']) * 100
df['CPP'] = df['Precio'] / df['rating']
df['CPM'] = (df['Precio'] / df['audiencia']) * 1000
df['Reach_pct'] = 1 - (1 - (df['rating'] / 100))**df['spots']
df['Reach_personas'] = df['population'] * df['Reach_pct']

# Redondear los valores a 2 decimales
df = df.round(2)

# Seleccionar los tres soportes con mayor afinidad
top_3_afinidad = df.nlargest(3, 'Afinidad')

# Seleccione solo las columnas numéricas
numeric_columns = top_3_afinidad.select_dtypes(include=[np.number]).columns.tolist()

# Each attribute we'll plot in the radar chart.
labels = numeric_columns

# Number of variables we're plotting.
num_vars = len(labels)

import plotly.graph_objects as go

# Asegúrate de que el DataFrame `top_3_afinidad` tenga columnas que coincidan con las etiquetas del gráfico de radar.
# Elimina las columnas que no sean numéricas en `top_3_afinidad` antes de trazar el gráfico de radar.

# Seleccione solo las columnas numéricas
numeric_columns = top_3_afinidad.select_dtypes(include=[np.number]).columns.tolist()

# Crea una figura de plotly
fig = go.Figure()

# Agrega cada fila al gráfico de radar
for index in top_3_afinidad.index:
    fig.add_trace(go.Scatterpolar(
        r=top_3_afinidad.loc[index, numeric_columns],
        theta=numeric_columns,
        fill='toself',
        name=index
    ))

# Establece el diseño del gráfico
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
    showlegend=True,
    title="Comparing Top 3 Support by Affinity Across Dimensions"
)

# Muestra el gráfico en Streamlit
st.plotly_chart(fig)
