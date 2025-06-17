from sqlalchemy import Column, String, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import POSTGRES_URL

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True)
    preferences = Column(Text)  # Store as JSON string

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Already defined UserProfile...

class DeclarativeMemory(Base):
    __tablename__ = 'declarative_memory'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("user_profiles.user_id"))
    fact = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class ProceduralMemory(Base):
    __tablename__ = 'procedural_memory'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("user_profiles.user_id"))
    task_name = Column(String)
    steps = Column(Text)  # JSON or text description
    usage_count = Column(Integer, default=0)

class EpisodicMemory(Base):
    __tablename__ = 'episodic_memory'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("user_profiles.user_id"))
    event_description = Column(Text)
    emotion_marker = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class SemanticMemory(Base):
    __tablename__ = 'semantic_memory'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("user_profiles.user_id"))
    concept = Column(String)
    related_concept = Column(String)
    relationship_type = Column(String)



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)

    conversations = relationship("Conversation", back_populates="user")


class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    started_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    content = Column(Text)
    sender = Column(String)  # "user" or "assistant"
    timestamp = Column(DateTime, default=datetime.utcnow)

    conversation = relationship("Conversation", back_populates="messages")

