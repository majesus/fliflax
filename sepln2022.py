import streamlit as st

from collections import Counter
import pandas as pd
import re
#---------------------------------------------------------#
from sentence_transformers import SentenceTransformer, util
#@st.cache
#model = SentenceTransformer('msmarco-MiniLM-L-12-v3')
#st.write("cargado")

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def init_retriever():
    # initialize retriever model
    return SentenceTransformer('msmarco-MiniLM-L-12-v3')
model = init_retriever()
#---------------------------------------------------------#
# Decide si se enmascaran palabras o no
masking = False
#---------------------------------------------------------#
datos = pd.read_csv("csv/proyecto.csv")

with st.form(key='my_form'):
    n_top = st.slider(label='número de frases a emplear', value=10, max_value= len(datos))
    query = st.text_input(label='frase objetivo', value = "enduring relationship")
    form1 = st.form_submit_button(label='Calcular')
#---------------------------------------------------------#
# datos = pd.read_csv("csv/proyecto.csv")
datos = datos.groupby('type').apply(lambda x: x.sample(n=n_top)).reset_index(drop = True)
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
#st.write("Codificando todas las frases...")
text = airbnb_sents + hotel_sents
labs = ['airbnb']*len(airbnb_sents)+['hotel']*len(hotel_sents)
emb = model.encode(text)   
#---------------------------------------------------------#
#st.table(datos.head())
#---------------------------------------------------------#
query_emb = model.encode(query)
    
sims = util.cos_sim(query_emb, emb)
sims = [(float(s),i) for i, s in enumerate(sims[0])]
sims.sort(reverse=True)
    
for s, i in sims[:10]:
    st.write(str(s)+"\t"+labs[i]+": "+ text[i])

st.write(Counter(labs[i] for _,i in sims[:100]))
#---------------------------------------------------------#
