from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError('Please add API_KEY to .env file!')

client = genai.Client(api_key=API_KEY)

chat = client.chats.create(
    model="gemini-2.0-flash",
)
response = chat.send_message_stream('what is typescript breifly')

for chunck in response:
    print(chunck.text, end="")
