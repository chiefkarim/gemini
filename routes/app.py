from fastapi import FastAPI, status
from fastapi.responses import StreamingResponse
from repositories.db import connect_db
from repositories.get_chat_history import getChatHistory
from services.chat import chat
from models.user_prompt import UserPrompt
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from os import getenv

load_dotenv()
CORS = getenv("CORS")


app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://gemini-frontend-git-chat-v1-chiefkarims-projects.vercel.app",
    CORS
]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)


@app.post(
    "/",
    description="sends a stream of data for chating with gemeni llm",
    status_code=status.HTTP_201_CREATED,
)
async def post_chat(prompt: UserPrompt):
    return StreamingResponse(chat(prompt), media_type="text/plain")

@app.get('/chat-history',description="returns chat history",status_code=status.HTTP_200_OK)
async def get_chat_history():
    db =await  connect_db()
    chat_history =await getChatHistory(db)
    return chat_history 
