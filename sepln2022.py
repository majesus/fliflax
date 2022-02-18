import streamlit as st

from collections import Counter
import pandas as pd
import re
#---------------------------------------------------------#
nombres_set ={
    "abraham","africa","agustin","alba","alberto","albertos","alejandro","alex","alfonso","alfredo","alicia","alvaro",
    "ana","anas","andres","angel","angela","angeles","anna","anne","anselma","antonio","asun","august","aurora","avelina",
    "barbara","bea","beatriz","belen","belinda","benito","bernardo","berta","bibi","blanca","blas","brunilda","caesar",
    "camille","carlos","carmen","carmens","carmona","celia","cesar","charo","chio","christina","clotilde","consuelo","corina",
    "cristina","cristinas","cristobal","curo","curro","daniel","david","diego","dolores","dominic","dominique","dylan","elena",
    "elio","elisa","emilio","encarna","encarnacion","enrique","esther","eugenio","eva","fatima","federico","felix","fernando",
    "fidel","fran","francisco","frederico","gabriel","gabriela","gary","gavidia","gerardo","giulia","giuseppe","gloria",
    "gonzalo","guadalupe","guilia","guille","guillermo","guiseppe","gulia","ignacio","ildefonso","immaculate","ines","inma",
    "inmaculada","irene","isabel","isabelle","isobel","jacinto","jara","javi","javier","jeanne","jeannie","jesus","joaquin",
    "jolee","jon","jorge","jose","joses","juan","juanjo","judith","julian","karina","laura","lauras","leo","leonardo","leonor",
    "lidia","lola","lolas","lorena","lorenzo","louisa","louise","lucila","luis","luisa","luz","macarena","magdalena","maite",
    "manolo","manu","manual","manue","manuel","manuela","manuels","mar","marc","march","marco","marcos","margarita","mari",
    "maria","marias","maribel","marie","marina","mario","martin","matthias","mercedes","miguel","miren","moises","mr","mrs",
    "myriam","nacho","nachos","nani","natalia","natalie","nemesia","nemesio","nikita","oscar","oscars","otto","owner","pablo",
    "paco","pacqui","paloma","paqui","paquita","pastora","patricia","paul","paula","pedro","pepe","pepi","pilar","piroska",
    "rafa","ramon","ramos","raquel","raul","rebeca","rebecca","reyes","ricardo","rocio","rosa","rosalia","ruperto","ruth",
    "salvador","santiago","sara","sebastian","sergio","silvia","sofia","sophia","sophie","sylvia","telmo","teresa","teresas",
    "teressa","theresa","tirso","valentin","valentina","vero","veronica","vicente","vicentes","victoria","vincent","vincente",
    "virginia","yolanda"    
}
masking_set ={
    'hotel', 'hotels',
    "air", "airb&b", "airbnb", "airbnbs", "b&b", "bnb",
    'apartment', 'appartment', 'apartments', 'appartments',
    'staff',
    'host', 'hosts',
    'room', 'rooms',
    'reception', 'desk',
    'buffet',
    'shuttle',
    'lobby'
} | nombres_set
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
#---------------------------------------------------------#
datos = pd.read_csv("csv/proyecto.csv")

with st.form(key='my_form'):
    masking = st.radio("¿masking?", (True,False))
    n_top = st.slider(label='número de frases a emplear por tipo de alojamiento:', value=10, max_value= len(datos), min_value = 1)
    query = st.text_input(label='frase objetivo con que comparar similitudes [coseno]:', value = "enduring relationship")
    form1 = st.form_submit_button(label='Calcular')
#---------------------------------------------------------#
# datos = pd.read_csv("csv/proyecto.csv")
# st.write(n_top)
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

st.markdown("""---""")

st.write("*Resultados:*")

st.markdown("""---""")

data = pd.DataFrame()
for s, i in sims[:10]:
    #st.write(str(s)+"\t"+labs[i]+": "+ text[i])  
    data = [str(s), labs[i], text[i]]
    st.table(data)

st.markdown("""---""")

st.write("Proporción de frases [100] por tipo de alojamiento ordenadas de mayor a menor similitud:")
st.write(Counter(labs[i] for _,i in sims[:100]))

st.markdown("""---""")
#---------------------------------------------------------#
