# config.py

import os


class Config:
    # 기본 환경 변수
    OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')
