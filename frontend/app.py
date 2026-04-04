import streamlit as st
import requests

st.title("Sentiment Analysis AI")

st.write("Enter a sentence to check sentiment")

text = st.text_input("Enter text")

if st.button("Predict"):

    url = "http://127.0.0.1:8000/predict"

    response = requests.post(url, params={"text": text})

    result = response.json()

    st.success(result["prediction"])