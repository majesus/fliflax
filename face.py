# https://medium.com/pythoneers/detect-face-emotions-with-10-lines-of-code-3a2ef507fd34

from fer import FER
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image, ImageOps
st.write('''
#  Emotion Detector
''')
st.write("A Image Classification Web App That Detects the Emotions Based On An Image")
file = st.file_uploader("Please Upload an image of Person With Face", type=['jpg','png'])
