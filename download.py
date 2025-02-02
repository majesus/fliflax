import streamlit as st

# Asegúrate de cambiar el usuario, el repositorio y la rama por los tuyos
GITHUB_USER = 'majesus'
GITHUB_REPO = 'fliflax'
GITHUB_BRANCH = 'master'
DIR_NAME = 'csv'

# Lista de archivos PDF
pdf_files = ['zs.pdf']  # Actualizar con los nombres reales de los archivos

# Crear una lista de enlaces para descargar los archivos PDF
for file in pdf_files:
    file_url = f'https://github.com/{GITHUB_USER}/{GITHUB_REPO}/raw/{GITHUB_BRANCH}/{DIR_NAME}/{file}'
    st.markdown(f'[{file}]({file_url})', unsafe_allow_html=True)
