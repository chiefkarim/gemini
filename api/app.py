from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from .utils.chat import chat

app = FastAPI()
# TODO: change response type in the docs


@app.get('/')
def get_chat():
    return StreamingResponse(chat(), media_type='text/plain')
