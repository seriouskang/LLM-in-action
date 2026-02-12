from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(
    api_key=os.getenv("API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="너는 유치원생이야. 유치원생처럼 답변해줘",
        temperature=0.9
    ),
    contents="오리"
)

print(response.text)