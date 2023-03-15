import streamlit as st
import pandas as pd
import plotly.express as px

import requests

# Título de la aplicación
st.title("Aplicación Streamlit para leer, filtrar y visualizar datos CSV")

# Carga el archivo CSV
uploaded_file = st.file_uploader("Sube un archivo CSV", type="csv")

if uploaded_file is not None:
    # Lee el archivo CSV y lo convierte en un DataFrame de Pandas
    data = pd.read_csv(uploaded_file)
    st.markdown("### Datos cargados correctamente")

    # Muestra las primeras filas del DataFrame
    st.markdown("### Vista previa de los datos")
    st.write(data.head())

    # Selecciona la columna para filtrar
    st.markdown("### Selecciona la columna para filtrar")
    column_to_filter = st.selectbox("Columna", data.columns)

    # Ingresa el valor para filtrar
    st.markdown(f"### Ingresa el valor para filtrar en la columna '{column_to_filter}'")
    # Obtén los valores únicos de la columna seleccionada
    unique_values = data[column_to_filter].unique()
    # Crea un desplegable con los valores únicos de la columna
    value_to_filter = st.selectbox("Valor", unique_values)

    # Filtra el DataFrame
    filtered_data = data[data[column_to_filter] == value_to_filter]

    # Muestra la tabla filtrada de manera elegante
    if not filtered_data.empty:
        st.markdown("### Datos filtrados")
        st.dataframe(filtered_data)
    else:
        st.warning("No hay datos que coincidan con el filtro")

else:
    st.warning("Por favor, sube un archivo CSV")

    
    
#------------------------------------------#
    
    
# Carga el archivo CSV
csv_url = st.text_input("Ingresa la URL del archivo CSV")

if csv_url:
    try:
        # Lee el archivo CSV desde la URL y lo convierte en un DataFrame de Pandas
        data = pd.read_csv(csv_url)
        st.markdown("### Datos cargados correctamente")

        # Muestra las primeras filas del DataFrame
        st.markdown("### Vista previa de los datos")
        st.write(data.head())

        # Selecciona la columna para filtrar
        st.markdown("### Selecciona la columna para filtrar")
        column_to_filter = st.selectbox("Columna", data.columns)

        # Ingresa el valor para filtrar
        st.markdown(f"### Ingresa el valor para filtrar en la columna '{column_to_filter}'")
        # Obtén los valores únicos de la columna seleccionada
        unique_values = data[column_to_filter].unique()
        # Crea un desplegable con los valores únicos de la columna
        value_to_filter = st.selectbox("Valor", unique_values)

        # Filtra el DataFrame
        filtered_data = data[data[column_to_filter] == value_to_filter]

        # Muestra la tabla filtrada de manera elegante
        if not filtered_data.empty:
            st.markdown("### Datos filtrados")
            st.dataframe(filtered_data)
        else:
            st.warning("No hay datos que coincidan con el filtro")

        
        
    except pd.errors.ParserError:
        st.error("No se pudo leer el archivo CSV desde la URL proporcionada. Asegúrate de que la URL sea válida y accesible.")
else:
    st.warning("Por favor, ingresa la URL de un archivo CSV")
    
    
    
