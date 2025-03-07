from pydantic import BaseModel
from typing import  List, Literal
from openai.types.chat import ChatCompletionMessageParam

# TODO: update types to use opeai sdk types

class Chat(BaseModel):
    role: Literal['user', 'assistant']
    content: str


class UserPrompt(BaseModel):
    prompt: str
    chatHistory: List[ChatCompletionMessageParam]
