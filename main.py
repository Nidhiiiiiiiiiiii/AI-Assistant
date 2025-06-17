from fastapi import FastAPI, Request
from memory.short_term import save_to_memory, get_context
from uuid import uuid4
from fastapi import FastAPI
from routers import user, conversation

app = FastAPI()
app.include_router(user.router)
app.include_router(conversation.router)


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_id = data.get("user_id", str(uuid4()))
    user_message = data["message"]

    save_to_memory(user_id, f"User: {user_message}")

    # [Placeholder] AI model response generation
    ai_response = "Sure! I have noted that."

    save_to_memory(user_id, f"AI: {ai_response}")

    context = get_context(user_id)
    return {"response": ai_response, "context": context}
from memory.long_term import add_fact, get_facts, store_task_pattern, log_event, add_relation

@app.post("/store_fact")
async def store_fact(request: Request):
    data = await request.json()
    add_fact(data["user_id"], data["fact"])
    return {"status": "fact stored"}

@app.get("/facts/{user_id}")
def get_user_facts(user_id: str):
    facts = get_facts(user_id)
    return {"facts": facts}

@app.post("/store_task")
async def store_task(request: Request):
    data = await request.json()
    store_task_pattern(data["user_id"], data["task_name"], data["steps"])
    return {"status": "task stored"}

@app.post("/log_event")
async def log_event_route(request: Request):
    data = await request.json()
    log_event(data["user_id"], data["description"], data["emotion"])
    return {"status": "event logged"}

@app.post("/add_relation")
async def relation(request: Request):
    data = await request.json()
    add_relation(data["user_id"], data["concept"], data["related"], data["type"])
    return {"status": "relation added"}
