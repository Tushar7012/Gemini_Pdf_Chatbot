import streamlit as st
from main import generate_response

st.title("Chatbot using Gemini")

user_input = st.text_input("Enter your Question")

# Button to Generate Response
if st.button("Ask Gemini"):
    if user_input.strip():
        with st.spinner("Its Loading"):
            response = generate_response(user_input)
        st.success(response)

    else:
        st.warning("Please enter a valid Question")
