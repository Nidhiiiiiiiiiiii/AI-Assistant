from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True


class ConversationCreate(BaseModel):
    user_id: int

class ConversationOut(BaseModel):
    id: int
    user_id: int
    started_at: datetime
    class Config:
        orm_mode = True


class MessageCreate(BaseModel):
    content: str
    sender: str

class MessageOut(BaseModel):
    id: int
    conversation_id: int
    content: str
    sender: str
    timestamp: datetime
    class Config:
        orm_mode = True
