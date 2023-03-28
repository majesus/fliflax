import pandas as pd
import altair as alt

# Cargar tus datos desde el archivo CSV
data = pd.read_csv("csv/departmento_inv_prisma.csv")

# Calcular el número de publicaciones por año para Cód. WOS y Cód. Scopus
publications_by_year_wos = data[data['Cód. WOS'].notna()].groupby('Año de Publicación').size().reset_index(name='Número de Publicaciones WOS')
publications_by_year_scopus = data[data['Cód. Scopus'].notna()].groupby('Año de Publicación').size().reset_index(name='Número de Publicaciones Scopus')

# Crear el gráfico de la función de densidad para Cód. WOS
density_chart_wos = alt.Chart(publications_by_year_wos).transform_density(
    density='Número de Publicaciones WOS',
    groupby=['Año de Publicación'],
    as_=['Año de Publicación', 'Número de Publicaciones']
).mark_area(
    opacity=0.3,
    color='darkblue'
).encode(
    alt.X('Año de Publicación:Q', axis=alt.Axis(format='d')),
    alt.Y('Número de Publicaciones:Q')
).properties(
    title='Funciones de Densidad por Año para Cód. WOS y Cód. Scopus'
)

# Crear el gráfico de la función de densidad para Cód. Scopus
density_chart_scopus = alt.Chart(publications_by_year_scopus).transform_density(
    density='Número de Publicaciones Scopus',
    groupby=['Año de Publicación'],
    as_=['Año de Publicación', 'Número de Publicaciones']
).mark_area(
    opacity=0.3,
    color='darkgreen'
).encode(
    alt.X('Año de Publicación:Q'),
    alt.Y('Número de Publicaciones:Q')
)

# Combinar las dos funciones de densidad en un solo gráfico
combined_chart = density_chart_wos + density_chart_scopus

# Mostrar el gráfico combinado en Streamlit
st.altair_chart(combined_chart, use_container_width=True)
