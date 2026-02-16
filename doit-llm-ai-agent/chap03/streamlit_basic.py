import streamlit as st
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(
    api_key=os.getenv("API_KEY")
)

def get_ai_response(messages):
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=st.session_state.messages
    ).text

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "model", "parts": [{"text": "How can I help you?"}]}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["parts"][0]["text"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "parts": [{"text": prompt}]})    
    st.chat_message("user").write(prompt)

    response = get_ai_response(st.session_state.messages)
    st.session_state.messages.append({"role": "model", "parts": [{"text": response}]})
    st.chat_message("model").write(response)