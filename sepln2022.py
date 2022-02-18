import streamlit as st

from collections import Counter
import pandas as pd
import re

from sentence_transformers import SentenceTransformer, util
@st.cache
model = SentenceTransformer('msmarco-MiniLM-L-12-v3')

st.write("cargado")


# Cargamos los datos de nuevos

# None para usar todas => ¡Tarda mucho!
n_top = 2000
# Decide si se enmascaran palabras o no
masking = False

from collections import Counter
import pandas as pd
import re

datos = pd.read_csv("drive/MyDrive/Colab Notebooks/Fermin/proyecto.csv")
airbnb = datos[datos.type=="airbnb"].description1 
hotel = datos[datos.type=="hotel"].description1 

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

airbnb_sents = split_sentences(airbnb)
hotel_sents = split_sentences(hotel)

print("Total sentences airbnb:", len(airbnb_sents))
print("Total sentences hotel:",len(hotel_sents))

if n_top:
    print("Encoding",n_top,"sentences...")
    text = airbnb_sents[:n_top//2] + hotel_sents[:n_top//2]
    labs = ['airbnb']*(n_top//2)+['hotel']*(n_top//2)
    emb = model.encode(text)
    print("Done")
else:
    print("Encoding all sentences...")
    text = airbnb_sents + hotel_sents
    labs = ['airbnb']*len(airbnb_sents)+['hotel']*len(hotel_sents)
    emb = model.encode(text)
    print("Done")
    
 
