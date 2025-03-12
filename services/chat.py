from typing import Iterable
from openai import OpenAI
from dotenv import load_dotenv
import os
from openai.types.chat import ChatCompletionToolParam
from models.user_prompt import UserPrompt
import asyncio

load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError('Please add API_KEY to .env file!')

client = OpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
# TODO: make the streaming faster
# first stream is taking some time which makes the user experince bad


# TODO: type the function returned data


# TODO: figure out a way to presist messages

tools:Iterable[ChatCompletionToolParam]= [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City e.g. Tokyo or blida"
                }
                ,"country":{
                    "type":"string",
                    "description":"Country e.g. Algeria or France"
                }
            },
            "required": [
                "city","country"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]

async def  chat(prompt: UserPrompt):
        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            n=1,
            messages=[
                *prompt.chatHistory,
                {"role": "system", "content": """You are a helpful assistant and a funny weather woman.
                You ALWAYS call the get_weather function when asked for weather information.
                Even if the location seems strange, you must ask for clarification if the country or city seems off.                """},
                {
                    "role": "user",
                    "content": prompt.prompt}

            ],
            stream=True
        ,tools=tools
        ,temperature=1,
        )

        for chunk in response:
            yield f"{chunk.choices[0].delta.content or ''}"
            print(chunk.choices[0].delta.tool_calls)
            await asyncio.sleep(1)

    # TODO: uninstall genai package


# TODO:  make the function async
