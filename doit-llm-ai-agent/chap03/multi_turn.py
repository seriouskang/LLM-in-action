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
        config=types.GenerateContentConfig(
            system_instruction="너는 사용자를 도와주는 상담사야.",
            temperature=0.9
        ),
        contents=messages
    ).text

messages = []
while True:
    user_input = input("사용자: ")
    
    if user_input == "exit":
        break

    messages.append({"role": "user", "parts": [{"text": user_input}]})
    ai_response = get_ai_response(messages)
    messages.append({"role": "model", "parts": [{"text": ai_response}]})
    print("AI: " + ai_response)