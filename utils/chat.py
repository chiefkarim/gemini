from google import genai
from dotenv import load_dotenv
import os
from models.user_prompt import UserPrompt

load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError('Please add API_KEY to .env file!')

# TODO: make the streaming faster
# first stream is taking some time which makes the user experince bad


def chat(prompt: UserPrompt):
    client = genai.Client(api_key=API_KEY)
    chat = client.chats.create(
        model="gemini-2.0-flash",
    )
    response = chat.send_message_stream(prompt.prompt)

    for chunck in response:
        yield f'{chunck.text}'
