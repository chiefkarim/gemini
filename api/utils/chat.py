from google import genai
from dotenv import load_dotenv
import os
import PIL.Image

load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError('Please add API_KEY to .env file!')

# TODO: make the streaming faster
# first stream is taking some time which makes the user experince bad


def chat():
    client = genai.Client(api_key=API_KEY)

    chat = client.chats.create(
        model="gemini-2.0-flash",
    )
    image = PIL.Image.open('./api/utils/avatar-1.jpg')
    response = chat.send_message_stream(['describe what do you see, and write 20 lines response analysing potenial personality of the person in the image', image])

    for chunck in response:
        yield f'{chunck.text}'
