import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = 6379
POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://postgres:Meghna/1234@localhost:5432/ai_assistant")

