from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from services.chat import chat
from models.user_prompt import UserPrompt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://gemini-frontend-git-chat-v1-chiefkarims-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)



@app.post("/", description="sends a stream of data for chating with gemeni llm")
async def post_chat(prompt: UserPrompt):
    return StreamingResponse(chat(prompt), media_type="text/plain")


# TODO: clean up unused packages
