from openai import OpenAI

from config import Config

client = OpenAI(
    api_key=Config.OPEN_AI_API_KEY
)

response = client.images.generate(
  model="dall-e-3",
  prompt="대나무 숲의 판다",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)