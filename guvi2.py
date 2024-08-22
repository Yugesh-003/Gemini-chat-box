import streamlit as st
import google.generativeai as genai

st.title("Welcome to gemini chat")

genai.configure(api_key="AIzaSyAQwXZ5P8o2e4DYQ65pVWxX8iEcJgHohzI")

text = st.text_input("Enter your qureies : ")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("SEARCH"):
    response = chat.send_message(text)
    st.write(response.text)