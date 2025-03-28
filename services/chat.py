from openai import OpenAI
from dotenv import load_dotenv
import os
from models.user_prompt import UserPrompt
import asyncio


load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Please add API_KEY to .env file!")

client = OpenAI(
    api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


async def chat(prompt: UserPrompt):
    try:
        response = client.chat.completions.create(
        model="gemini-2.0-flash",
        n=1,
        messages=[
            *prompt.chatHistory,
            {
                "role": "system",
                "content": """You are a helpful assistant and a funny assistant.
                         """,
            },
            {"role": "user", "content": prompt.prompt},
        ],
        stream=True,
        temperature=1,
        )
        for chunk in response:
            text = chunk.choices[0].delta.content
            if text:
                for ch in text.split(" "):
                    yield f"{ch + ' ' or ''}"
                    await asyncio.sleep(0.03)
    except Exception as e:
        print(f"Unexpected error: {e}")

    
