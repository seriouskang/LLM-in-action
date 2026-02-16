import streamlit as st
import os
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(
    api_key=os.getenv("API_KEY")
)

def get_ai_response(messages):
    return client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=st.session_state.messages
    ).text

st.title("Chatbot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "model", "parts": [{"text": "How can I help you?"}]}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["parts"][0]["text"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "parts": [{"text": prompt}]})    
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_ai_response(st.session_state.messages)        
    with st.chat_message("model"):
        message_placeholder = st.empty()
        full_response = ""

        # Simulate stream of response with milliseconds delay
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.03)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "model", "parts": [{"text": response}]})