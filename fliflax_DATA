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

# Función para crear el Radar Chart
def radar_chart(data, columns, title):
    num_vars = len(columns)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for index, row in data.iterrows():
        values = row[columns].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=index)
        ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(columns)
    ax.set_yticklabels([])

    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title='Soportes')
    plt.title(title, size=20, color='blue', y=1.1)

    return fig

# Crear el Radar Chart
variables = ['Afinidad', 'rating', 'GRP', 'Reach_pct', 'CPP']
chart_title = 'Top 3 Soportes con Mayor Afinidad'
radar_fig = radar_chart(top_3_afinidad, variables, chart_title)

# Mostrar la tabla y el Radar Chart en Streamlit
st.write(df)
st.pyplot(radar_fig)
