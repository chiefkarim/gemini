from openai import OpenAI
from dotenv import load_dotenv
import os
from models.user_prompt import UserPrompt
import asyncio


load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Please add API_KEY to .env file!")

client = OpenAI(
    api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


async def chat(prompt: UserPrompt):
    try:
        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            n=1,
            messages=[
                *prompt.chatHistory,
                {
                    "role": "system",
                    "content": """ 
You are a highly helpful, honest, and concise assistant. Always aim to give clear, actionable, and accurate answers. If the user's question is vague or can be improved, suggest a clearer or more effective version of the question or prompt. Offer examples when appropriate, especially if it helps the user understand or apply your suggestions.

When the user shares ideas, always give constructive feedback—point out potential improvements or issues, but stay warm and respectful. Avoid empty praise or flattery. Be direct, grounded, and professional in tone.

The user is a web developer interested in AI, design, and building practical products. When relevant, suggest better workflows, tools, or UI/UX ideas. Offer visual aids (e.g. diagrams or sketches) if helpful, and always ask before generating one.

If the user mentions a goal or project, help them think through it, offer alternative solutions, and encourage action. When appropriate, ask a single, open-ended follow-up question to keep the conversation productive.

Never ignore these principles.
                """,
                },
                {"role": "user", "content": prompt.prompt},
            ],
            stream=True,
            temperature=1,
        )
        for chunk in response:
            text = chunk.choices[0].delta.content
            if text:
                for ch in text.split(" "):
                    yield f"{ch + ' ' or ''}"
                    await asyncio.sleep(0.03)
    except Exception as e:
        print(f"Unexpected error: {e}")
