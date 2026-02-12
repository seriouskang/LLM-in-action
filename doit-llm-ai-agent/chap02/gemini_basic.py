from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(
    api_key=os.environ.get("API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful assistant.",
        temperature=0.1
    ),
    contents="2022년 월드컵 우승 팀은 어디야?"
)

print(response)
print('----')
print(response.text)