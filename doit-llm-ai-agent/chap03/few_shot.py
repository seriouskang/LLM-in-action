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
    contents=[
        {"role": "user", "parts": [{"text": "참새"}]},
        {"role": "model", "parts": [{"text": "짹짹"}]},
        {"role": "user", "parts": [{"text": "말"}]},
        {"role": "model", "parts": [{"text": "히이잉"}]},
        {"role": "user", "parts": [{"text": "개구리"}]},
        {"role": "model", "parts": [{"text": "개굴개굴"}]},
        {"role": "user", "parts": [{"text": "오리"}]}
    ]
)

print(response.text)