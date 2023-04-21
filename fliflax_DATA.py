import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Datos ficticios de ejemplo
data = {
    'population': [10000, 10000, 10000, 10000, 10000],
    'audiencia': [500, 1500, 1200, 800, 600],
    'indice_utilidad': [0.8, 0.4, 0.7, 0.4, 0.3],
    'spots': [10, 20, 15, 25, 12],
    'Precio': [2000, 5000, 4000, 3000, 2200]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Calcular las columnas adicionales
df['audiencia_target'] = df['audiencia'] * df['indice_utilidad']
df['rating'] = (df['audiencia'] * 100) / df['population']
df['rating_target'] = (df['audiencia_target'] * 100) / df['population']
df['Afinidad'] = df['rating_target'] / df['rating']
df['impressions'] = df['audiencia'] * df['spots']
df['GRP'] = (df['impressions'] / df['population']) * 100
df['TRP'] = (df['impressions'] / df['population']) * 100
df['CPP'] = df['Precio'] / df['rating']
df['CPM'] = (df['Precio'] / df['audiencia']) * 1000
df['Reach_pct'] = 1 - (1 - (df['rating'] / 100))**df['spots']
df['Reach_personas'] = df['population'] * df['Reach_pct']
df['Reach_target_pct'] = 1 - (1 - (df['rating_target'] / 100))**df['spots']
df['Reach_target_personas'] = df['population'] * df['Reach_target_pct']

# Seleccionar los tres soportes con mayor afinidad
top_3_afinidad = df.nlargest(5, 'Afinidad')

# Redondear los valores a 2 decimales
top_3_afinidad = top_3_afinidad.round(2)
top_3_afinidad = top_3_afinidad[["rating_target", "Reach_target_pct", "Reach_pct", "TRP", "GRP"]]

from sklearn.preprocessing import MinMaxScaler

# Selecciona solo las columnas numéricas
numeric_columns = top_3_afinidad.select_dtypes(include=[np.number]).columns.tolist()

# Normaliza las columnas numéricas a un rango de 0 a 100
scaler = MinMaxScaler(feature_range=(0, 100))
top_3_afinidad_normalized = top_3_afinidad.copy()
top_3_afinidad_normalized[numeric_columns] = scaler.fit_transform(top_3_afinidad[numeric_columns])

# Crea una figura de plotly
import plotly.graph_objects as go

fig = go.Figure()

# Agrega cada fila al gráfico de radar
for index in top_3_afinidad_normalized.index:
    fig.add_trace(go.Scatterpolar(
        r=top_3_afinidad_normalized.loc[index, numeric_columns],
        theta=numeric_columns,
        fill='toself',
        name=index,
        opacity=0.4
    ))

# Establece el diseño del gráfico
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
    showlegend=True,
    title="Comparing Top Support by Affinity Across Dimensions"
)

# Muestra el gráfico en Streamlit
st.plotly_chart(fig)
