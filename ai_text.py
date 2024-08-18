from openai import OpenAI

from config import Config

print(Config.OPEN_AI_API_KEY)

client = OpenAI(
    api_key=Config.OPEN_AI_API_KEY
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "너에 대해서 설명해줘",
        }
    ],
    model="gpt-4o-mini",
)

print(chat_completion.choices[0].message.content)
