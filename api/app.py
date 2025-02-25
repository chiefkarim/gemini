from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from utils.chat import chat
from models.user_prompt import UserPrompt
app = FastAPI()


@app.post('/')
async def post_chat(prompt: UserPrompt):
    return StreamingResponse(chat(prompt), media_type='text/plain')
