import streamlit as st

from collections import Counter
import pandas as pd
import numpy as np
import re
#---------------------------------------------------------#
st.title('Estimación de la similitud mediante queries:')
st.write("En estos experimentos usamos un modelo que sirve para hacer retrieval: mandas una query, te devuelve la oración que mejor responde a la query. "
         "Se trata de búsquedas semánticas, en las que la query puede ser una palabra, una pregunta, o cualquier enunciado. "
         "El modelo que usamos sirve para búsquedas asimétricas (la query es mucho más corta que los documentos). "
         "Podría servir para definir una serie de queries relacionadas con las dimensiones SATISFACCIÓN, CONFIANZA y COMPROMISO, "
         "o con otros conceptos que nos parezcan interesantes. Y permitiría también hacer representaciones de las fuentes (airbnb/hotel) "
         "con respecto a las dimensiones elegidas.")
st.write("J.A. Troyano / Fermín Cruz / Manuel J. Sánchez-Franco, Universidad de Sevilla")

st.success("Precisamos que aún no hemos determinado la valencia de la simlitud, es decir, "
           "el embedding no detecta de modo sensible la diferencia entre satisfacción e insatisfacción, por ejemplo.")
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

#@st.cache(suppress_st_warning=True, allow_output_mutation=False)
@st.experimental_memo
def init_retriever():
    # initialize retriever model
    return SentenceTransformer('msmarco-MiniLM-L-12-v3')
model = init_retriever()

st.markdown("""---""")

if st.button("Borrar caché"):
    #init_retriever.clear()
    st.experimental_memo.clear()
#---------------------------------------------------------#
#---------------------------------------------------------#
datos = pd.read_csv("csv/proyecto.csv")
#---------------------------------------------------------#
masking = "No"
with st.sidebar.form(key='my_form'):
    masking = st.radio("¿masking?", ("Sí","No"))
    material = st.radio("¿material?", ("oraciones","revisiones"))
    n_top = st.slider(label='número de revisiones a emplear por tipo de alojamiento:', value=10, max_value= 1000, min_value = 1)
    target = st.text_input(label='query a comparar su similitud [coseno] con material:', value = "I am satisfied with this stay.")
    form1 = st.form_submit_button(label='Calcular')
#---------------------------------------------------------#
datos = datos.groupby('type').apply(lambda x: x.sample(n=n_top, replace = False, random_state=123)).reset_index(drop = True)
airbnb = datos[datos.type=="airbnb"].description1 
hotel = datos[datos.type=="hotel"].description1 
#---------------------------------------------------------#
If masking == "Sí":
         masking = True
else:
         masking = False
#---------------------------------------------------------#
@st.experimental_memo
def split_sentences(reviews):
    res = []
    for r in reviews:
        sts = [mask(s.strip())+"." for s in r.split(".") if s.strip()!=""]
        res+= sts
    return res

@st.experimental_memo
def split_sentences_join(reviews):
    res = []
    for r in reviews:
        sts = [mask(s.strip())+"." for s in r.split(".") if s.strip()!=""]
        res.append('. '.join(sts))
    return res

@st.experimental_memo
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
if material == "oraciones":
    airbnb_sents = split_sentences(airbnb)
    hotel_sents = split_sentences(hotel)
else:
    airbnb_sents = split_sentences_join(airbnb)
    hotel_sents = split_sentences_join(hotel)
#---------------------------------------------------------#
#text = airbnb_sents[:n_top] + hotel_sents[:n_top]
#labs = ['airbnb']*(n_top)+['hotel']*(n_top)
text = airbnb_sents + hotel_sents
labs = ['airbnb']*len(airbnb_sents)+['hotel']*len(hotel_sents)
emb = model.encode(text)   
#---------------------------------------------------------#
query_emb = model.encode(target)
    
sims = util.cos_sim(query_emb, emb)
sims = [(float(s),i) for i, s in enumerate(sims[0])]
sims.sort(reverse=True)

st.markdown("""---""")

st.write("### Resultados:")

st.markdown("""---""")

L = []
#for s, i in sims[:n_top*2]:   
for s, i in sims:
    dat= [(s), labs[i], text[i]]
    L.append(dat)
df = pd.DataFrame(L, columns = ['similitud', 'tipo', 'material'])

st.success("Material ordenado de mayor a menor similitud con la query con que comparamos:")
df1 = df.copy()
df1.set_index('tipo', inplace=True)
df1['similitud'].round(decimals = 3)
st.write(target)
#st.table(df1.head())
#---------------------------------------------------------#

from transformers import pipeline
classifier = pipeline("sentiment-analysis")
df2 = df1.copy()

df2 = (
    df2
    .assign(sentiment = lambda x: x['material'].apply(lambda s: classifier(s)))
    .assign(
         label = lambda x: x['sentiment'].apply(lambda s: (s[0]['label'])),
         score = lambda x: x['sentiment'].apply(lambda s: (s[0]['score']))
    )
)
del df2['sentiment']
st.table(df2.head(10))

#---------------------------------------------------------#

st.markdown("""---""")

st.write("Materiales por tipo de alojamiento:")
st.success(Counter(labs[i] for _,i in sims))
#---------------------------------------------------------#
st.markdown("""---""")
#---------------------------------------------------------#
st.write("#### Plot de densidad de la similitud:")

import altair as alt
g = alt.Chart(df).transform_density(
         'similitud',
         groupby=['tipo'],
         as_=['similitud', 'density'],
         extent=[0, 1],
).mark_area().encode(
         x="similitud:Q",
         y='density:Q',
).facet(
    'tipo:N',
    columns=1
)
st.altair_chart(g, use_container_width = True)
#---------------------------------------------------------#
st.markdown("""---""")
#---------------------------------------------------------#
# import streamlit as st
from transformers import pipeline

st.title('Estimación de sentimientos:')
st.write('Esta app-streamlit emplea Hugging Face Transformers [sentiment analyser] para clasificar el texto como positivo o negativo.')

form = st.form(key='sentiment-form')
phrase = form.text_area('texto', value = df.material[0])
submit = form.form_submit_button('Calcular')

st.markdown("""---""")

if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(phrase)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')
#---------------------------------------------------------#

#---------------------------------------------------------#
