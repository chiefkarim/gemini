from pydantic import BaseModel
from typing import List


class Chat(BaseModel):
    role: str
    content: str


class UserPrompt(BaseModel):
    prompt: str
    chatHistory: List[Chat]
