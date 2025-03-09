# main.py

import streamlit as st
import requests
import config

API_URL = "http://127.0.0.1:8000/process"  # FastAPI backend URL

st.title("Multilingual Sentiment Chatbot")

# User input field
user_input = st.text_input("Enter your message:")

if st.button("Analyze"):
    if user_input.strip():
        response = requests.post(API_URL, json={"text": user_input})
        if response.status_code == 200:
            result = response.json()
            st.write(f"**Detected Language:** {result['language']}")
            st.write(f"**Cleaned Text:** {result['cleaned_text']}")
            st.write(f"**Tokens:** {result['tokens']}")
        else:
            st.write("Error processing input. Try again.")
