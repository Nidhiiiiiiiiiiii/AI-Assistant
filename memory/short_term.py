import redis
from config import REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

def save_to_memory(user_id: str, message: str):
    r.lpush(f"context:{user_id}", message)
    r.ltrim(f"context:{user_id}", 0, 14)  # keep last 15 messages

def get_context(user_id: str):
    return r.lrange(f"context:{user_id}", 0, 14)
