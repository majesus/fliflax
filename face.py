from fer import FER
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image, ImageOps
st.write('''
#  Emotion Detector
''')
st.write("A Image Classification Web App That Detects the Emotions Based On An Image")
file = st.file_uploader("Please Upload an image of Person With Face", type=['jpg','png'])
if file is None:
  st.text("Please upload an image file")
else:
  image = Image.open(file)
  detector = FER(mtcnn=True)
  result = detector.detect_emotions(image)
  st.write(result)
  st.image(image, use_column_width=True)
