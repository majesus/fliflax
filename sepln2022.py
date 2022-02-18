import streamlit as st

from collections import Counter
import pandas as pd
import re
#---------------------------------------------------------#
from sentence_transformers import SentenceTransformer, util
#@st.cache
model = SentenceTransformer('msmarco-MiniLM-L-12-v3')
st.write("cargado")
#---------------------------------------------------------#
# Decide si se enmascaran palabras o no
masking = False
#---------------------------------------------------------#
datos = pd.read_csv("csv/proyecto.csv")
airbnb = datos[datos.type=="airbnb"].description1 
hotel = datos[datos.type=="hotel"].description1 
#---------------------------------------------------------#
def split_sentences(reviews):
    res = []
    for r in reviews:
        sts = [mask(s.strip())+"." for s in r.split(".") if s.strip()!=""]
        res+= sts
    return res

def mask(s):
    if masking:
        res = []
        for w in re.split(r"\b", s):
            if w.lower() in masking_set:
                w = "HMKD"
            res.append(w.strip())
        return ' '.join(res)
    else:
        return s
#---------------------------------------------------------#
airbnb_sents = split_sentences(airbnb)
hotel_sents = split_sentences(hotel)
#---------------------------------------------------------#
n_top = 10
query = 'enduring relationship'

with st.form(key='my_form'):
    n_top = st.text_input(label='número de frases')
    query = st.text_input(label='frase objetivo')
    form1 = st.form_submit_button(label='Calcular')

if n_top:
    st.write("Codificando",n_top,"frases...")
    text = airbnb_sents[:n_top//2] + hotel_sents[:n_top//2]
    labs = ['airbnb']*(n_top//2)+['hotel']*(n_top//2)
    emb = model.encode(text)
    st.write("Done")
else:
    st.write("Codificando todas las frases...")
    text = airbnb_sents + hotel_sents
    labs = ['airbnb']*len(airbnb_sents)+['hotel']*len(hotel_sents)
    emb = model.encode(text)
    st.write("Done")
    
#---------------------------------------------------------#
#st.table(datos.head())
#---------------------------------------------------------#
if query is not None:
    query_emb = model.encode(query)
    
    sims = util.cos_sim(query_emb, emb)
    sims = [(float(s),i) for i, s in enumerate(sims[0])]
    sims.sort(reverse=True)
    
    for s, i in sims[:10]:
        st.write(str(s)+"\t"+labs[i]+": "+ text[i])
    Counter(labs[i] for _,i in sims[:100])
    
else:
    st.write("falta query")


#---------------------------------------------------------#
