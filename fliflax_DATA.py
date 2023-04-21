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

# Split the circle into even parts and save the angles
# so we know where to put each axis.
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is a circle, so we need to "complete the loop"
# and append the start value to the end.
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Helper function to plot each row on the radar chart.
def add_to_radar(row, color):
    values = top_3_afinidad.loc[row, numeric_columns].tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=1, label=row)
    ax.fill(angles, values, color=color, alpha=0.25)

# Add each row to the chart using different colors.
colors = ['#1aaf6c', '#429bf4', '#d42cea']
for index, color in zip(top_3_afinidad.index, colors):
    add_to_radar(index, color)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw axis lines for each angle and label.
ax.set_thetagrids(np.degrees(angles), labels)

for label, angle in zip(ax.get_xticklabels(), angles):
    if angle in (0, np.pi):
        label.set_horizontalalignment('center')
    elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
    else:
        label.set_horizontalalignment('right')

ax.set_ylim(0, 100)

ax.set_rlabel_position(180 / num_vars)

ax.tick_params(colors='#222222')
ax.tick_params(axis='y', labelsize=8)
ax.grid(color='#AAAAAA')
ax.spines['polar'].set_color('#222222')
ax.set_facecolor('#FAFAFA')

ax.set_title('Comparing Top 3 Support by Affinity Across Dimensions', y=1.08)

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.show()

