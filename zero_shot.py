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
    options = st.multiselect('What are your favorite colors',['location', 'price'])
    form1 = st.form_submit_button(label='Calcular')
#---------------------------------------------------------#
datos = datos.groupby('type').apply(lambda x: x.sample(n=n_top, replace = False, random_state=123)).reset_index(drop = True)
#---------------------------------------------------------#
#---------------------------------------------------------#
st.markdown("""---""")
#---------------------------------------------------------#
candidate_labels = ["location", "price"]
candidate_results = [0, 0]
datos1 = datos.head(10)
for sent in datos1['description1'].values:
    # To do multi-class classification, simply pass multi_class=True.
    # In this case, the scores will be independent, but each will fall between 0 and 1.
    res = classifier(sent, candidate_labels)

    SCORES = res["scores"]
    CLASSES = res["labels"]
    BEST_INDEX = argmax(SCORES)
    predicted_class = CLASSES[BEST_INDEX]
    predicted_score = SCORES[BEST_INDEX]

    if predicted_class == 'renewable' and predicted_score > 0.5:
        candidate_results[0] = candidate_results[0] + 1
    if predicted_class == 'politics' and predicted_score > 0.5:
        candidate_results[1] = candidate_results[1] + 1
    
    if res['scores'][0] > 0.5:
        print(sent)
        print(res['labels'])
        print(res['scores'])
        print()

st.wirte(candidate_results)
#---------------------------------------------------------#





