from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()


class Config:
    OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')
