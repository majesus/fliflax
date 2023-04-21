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
top_3_afinidad = df.nlargest(5, 'Afinidad')

from sklearn.preprocessing import MinMaxScaler

# Selecciona solo las columnas numéricas
numeric_columns = top_3_afinidad.select_dtypes(include=[np.number]).columns.tolist()

# Normaliza las columnas numéricas a un rango de 0 a 100
scaler = MinMaxScaler(feature_range=(0, 100))
top_3_afinidad_normalized = top_3_afinidad.copy()
top_3_afinidad_normalized[numeric_columns] = scaler.fit_transform(top_3_afinidad[numeric_columns])

# Crea una figura de plotly
fig = go.Figure()

# Agrega cada fila al gráfico de radar
for index in top_3_afinidad_normalized.index:
    fig.add_trace(go.Scatterpolar(
        r=top_3_afinidad_normalized.loc[index, numeric_columns],
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
