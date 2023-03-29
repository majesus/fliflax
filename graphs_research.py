import pandas as pd
import altair as alt

# Cargar tus datos desde el archivo CSV
data = pd.read_excel("csv/departamento_inv_prisma.xlsx")
st.write(data.columns)

# Calcular el número de publicaciones por año
publications_by_year = data.groupby(['Año de Publicación']).size().reset_index(name='Número de Publicaciones')


# Crear el gráfico de área apilada
area_chart = alt.Chart(publications_by_year).mark_area(
    opacity=0.5,
    line={'color': 'darkblue'}
).encode(
    alt.X('Año de Publicación:Q', axis=alt.Axis(format='d')),
    alt.Y('Número de Publicaciones:Q', stack=None)
).properties(
    title='Evolución del Número de Publicaciones por Año'
)

# Crear el gráfico de la función de densidad
density_chart = alt.Chart(publications_by_year).transform_density(
    density='Número de Publicaciones',
    groupby=['Año de Publicación'],
    as_=['Año de Publicación', 'Número de Publicaciones']
).mark_area(
    opacity=0.3,
    color='darkgreen'
).encode(
    alt.X('Año de Publicación:Q'),
    alt.Y('Número de Publicaciones:Q')
)

# Combinar los dos gráficos
combined_chart = area_chart + density_chart

# Mostrar el gráfico combinado en Streamlit
st.altair_chart(combined_chart, use_container_width=True)
