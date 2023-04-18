import streamlit as st
import pandas as pd
import numpy as np


def CANEX(audience, insertion):
    """
    Calcular el alcance de un medio.

    audience: el tamaño de la audiencia del medio
    insertion: el número de inserciones en el medio
    return: el alcance del medio
    """
    return audience * (1 - np.exp(-insertion / audience))


def CSD(audiences, insertions, order, form):
    """
    Calcular el alcance y la distribución de exposición de una campaña.

    audiences: una lista con los tamaños de las audiencias de los medios
    insertions: una lista con los números de inserciones en los medios
    order: un criterio para ordenar los medios (por ejemplo, "audience", "insertion" o "random")
    form: una forma de agregación secuencial (por ejemplo, "normal", "inverse" o "mixed")
    return: el alcance y la distribución de exposición de la campaña
    """

    df = pd.DataFrame({"audience": audiences, "insertion": insertions})

    if order == "audience":
        df = df.sort_values(by="audience", ascending=False)
    elif order == "insertion":
        df = df.sort_values(by="insertion", ascending=False)
    elif order == "random":
        df = df.sample(frac=1)

    reach = 0
    exposure = [0]

    for i in range(len(df)):
        r = CANEX(df["audience"].iloc[i], df["insertion"].iloc[i])

        if form == "normal":
            reach = reach + r * (1 - reach)
            exposure.append(reach)
        elif form == "inverse":
            reach = r + reach * (1 - r)
            exposure.insert(0, reach)
        elif form == "mixed":
            if i % 2 == 0:
                reach = reach + r * (1 - reach)
                exposure.append(reach)
            else:
                reach = r + reach * (1 - r)
                exposure.insert(0, reach)

    return reach, exposure


def main():
    st.title("Calcular el alcance y la distribución de exposición de una campaña")

    # Configuración inicial de la página
    st.sidebar.title("Configuración de la campaña")
    st.sidebar.markdown("Ingrese los datos de la campaña:")
    st.sidebar.subheader("Tamaños de audiencia")
    a1 = st.sidebar.number_input("Medio 1", value=125, min_value=0)
    a2 = st.sidebar.number_input("Medio 2", value=748, min_value=0)
    a3 = st.sidebar.number_input("Medio 3", value=250, min_value=0)
    a4 = st.sidebar.number_input("Medio 4", value=312, min_value=0)

    st.sidebar.subheader("Número de inserciones")
    i1 = st.sidebar.number_input("Medio 1", value=10, min_value=0)
    i2 = st.sidebar.number_input("Medio 2", value=2, min_value=0)
i3 = st.sidebar.number_input("Medio 3", value=3, min_value=0)
i4 = st.sidebar.number_input("Medio 4", value=4, min_value=0)

order = st.sidebar.selectbox("Ordenar medios por", ["audience", "insertion", "random"])
form = st.sidebar.selectbox("Forma de agregación secuencial", ["normal", "inverse", "mixed"])

# Calcular el alcance y la distribución de exposición de la campaña
audiences = [a1, a2, a3, a4]
insertions = [i1, i2, i3, i4]
reach, exposure = CSD(audiences, insertions, order, form)

# Mostrar los resultados
st.subheader("Resultados")
st.write(f"El alcance de la campaña es {reach:.4f}")
st.write("La distribución de exposición de la campaña es:")
st.line_chart(exposure)

if name == "main":
main()
