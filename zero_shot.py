import streamlit as st

from collections import Counter
import pandas as pd
import re
from transformers import pipeline
#---------------------------------------------------------#
datos = pd.read_csv("csv/proyecto.csv")
#---------------------------------------------------------#
# Decide si se enmascaran palabras o no

with st.sidebar.form(key='my_form'):
    options = st.multiselect('What are your favorite colors',['location', 'price'],['satisfaction', 'trust'])
    form1 = st.form_submit_button(label='Calcular')
#---------------------------------------------------------#
datos = datos.groupby('type').apply(lambda x: x.sample(n=n_top, replace = False, random_state=123)).reset_index(drop = True)
#---------------------------------------------------------#
#---------------------------------------------------------#
st.markdown("""---""")
#---------------------------------------------------------#
submit_zero = form.form_submit_button('Calcular')
if form1:
    classifier = pipeline("zero-shot-classification")

    candidate_labels = ["location", "price"]
    res = classifier(sent, candidate_labels)

    datos_head = datos.head(n_top)
    for sent in datos_head['description1'].values:
        # To do multi-class classification, simply pass multi_class=True.
        # In this case, the scores will be independent, but each will fall between 0 and 1.
        res = classifier(sent, candidate_labels)

        SCORES = res["scores"]
        CLASSES = res["labels"]
        BEST_INDEX = argmax(SCORES)
        predicted_class = CLASSES[BEST_INDEX]
        predicted_score = SCORES[BEST_INDEX]

        if predicted_class == 'location' and predicted_score > 0.5:
            candidate_results[0] = candidate_results[0] + 1
        if predicted_class == 'price' and predicted_score > 0.5:
            candidate_results[1] = candidate_results[1] + 1

        if res['scores'][0] > 0.5:
            print(sent)
            print(res['labels'])
            print(res['scores'])
            print()

    st.write(candidate_results)

    data = {'labels': candidate_labels,'values': candidate_results}
    df_chart = pd.DataFrame(data, columns=['labels','values'])
    st.table(df_chart.head(10))
#---------------------------------------------------------#





