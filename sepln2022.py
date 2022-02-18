from sentence_transformers import SentenceTransformer, util
import streamlit as st
import pandas as pd
#-----------------------------------------------------------------------------#
data = pd.read_csv("model/emb.csv") #path folder of the data file
st.write(data) #displays the table of data
#-----------------------------------------------------------------------------#
#spectra = st.file_uploader("upload file", type={"csv", "txt"})
#-----------------------------------------------------------------------------#

# None para usar todas => ¡Tarda mucho!
n_top = 2000
# Decide si se enmascaran palabras o no
masking = False

from collections import Counter
import pandas as pd
import re

# datos = pd.read_csv("csv/proyecto.csv")
datos = pd.read_csv("csv/proyecto.csv") #path folder of the data file
st.write("datos")
st.write(datos)

airbnb = datos[datos.type=="airbnb"].description1 
hotel = datos[datos.type=="hotel"].description1 

def split_sentences(reviews):
    res = []
    for r in reviews:
        sts = [mask(s.strip())+"." for s in r.split(".") if s.strip()!=""]
        res.append('. '.join(sts))
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

print("Total reviews airbnb:", len(airbnb_sents))
print("Total reviews hotel:",len(hotel_sents))
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
    
