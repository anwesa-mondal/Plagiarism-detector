import streamlit as st
import requests

st.title("Plagiarism detector")

text = st.text_input("Enter text to check for plagiarism")

if st.button("Predict"):
    response = requests.post('http://localhost:5000/predict', json={'text': text})
    if response.status_code == 200:
        result = response.json().get('prediction')
        st.write(f"{result}")
    else:
        st.error("Error: Could not get a response from the backend.")