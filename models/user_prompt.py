from pydantic import BaseModel
from typing import List


class UserPrompt(BaseModel):
    prompt: str
    chatHistory: List[str]
