from db.models import DeclarativeMemory, ProceduralMemory, EpisodicMemory, SemanticMemory, SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

# Declarative memory
def add_fact(user_id: str, fact: str):
    db: Session = SessionLocal()
    mem = DeclarativeMemory(user_id=user_id, fact=fact)
    db.add(mem)
    db.commit()
    db.close()

def get_facts(user_id: str):
    db: Session = SessionLocal()
    facts = db.query(DeclarativeMemory).filter_by(user_id=user_id).all()
    db.close()
    return [f.fact for f in facts]

# Procedural memory
def store_task_pattern(user_id: str, task_name: str, steps: str):
    db = SessionLocal()
    task = ProceduralMemory(user_id=user_id, task_name=task_name, steps=steps)
    db.add(task)
    db.commit()
    db.close()

# Episodic memory
def log_event(user_id: str, description: str, emotion: str):
    db = SessionLocal()
    ep = EpisodicMemory(user_id=user_id, event_description=description, emotion_marker=emotion)
    db.add(ep)
    db.commit()
    db.close()

# Semantic memory
def add_relation(user_id: str, concept: str, related: str, relation_type: str):
    db = SessionLocal()
    rel = SemanticMemory(user_id=user_id, concept=concept, related_concept=related, relationship_type=relation_type)
    db.add(rel)
    db.commit()
    db.close()
