from pydantic import BaseModel, Field
from typing import List
from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionUserMessageParam,
)


class UserPrompt(BaseModel):
    prompt: str = Field(examples=["what is typescript"])
    chatHistory: List[
        ChatCompletionUserMessageParam | ChatCompletionAssistantMessageParam
    ] = Field(
        examples=[
            [
                {"content": "my name is karim", "role": "user", "name": "string"},
                {
                    "content": "Hello karim, how can i help you today?",
                    "role": "assistant",
                    "name": "string",
                },
            ]
        ]
    )
