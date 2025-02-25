from pydantic import BaseModel
from typing import Optional


class UserPrompt(BaseModel):
    prompt: Optional[str] = None
