from openai import OpenAI
from dotenv import load_dotenv
import os
from models.user_prompt import UserPrompt

load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError('Please add API_KEY to .env file!')

client = OpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
# TODO: make the streaming faster
# first stream is taking some time which makes the user experince bad


# TODO: type the function returned data


# TODO: figure out a way to presist messages


def chat(prompt: UserPrompt):
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        n=1,
        messages=[
            prompt.chatHistory,
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt.prompt}
        ],
        stream=True
    )

    for chunk in response:
        yield f"{chunk.choices[0].delta.content or ''}"


# TODO: uninstall genai package


# TODO:  make the function async
