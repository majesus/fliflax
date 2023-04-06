import streamlit as st

import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])

st.write(text)
