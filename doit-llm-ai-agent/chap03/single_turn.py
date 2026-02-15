from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(
    api_key=os.getenv("API_KEY")
)

while True:
    user_input = input("사용자: ")
    
    if user_input == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            temperature=0.9,
            system_instruction="너는 사용자를 도와주는 상담사야."
        ),
        contents=user_input
    )
    print("AI: " + response.text)