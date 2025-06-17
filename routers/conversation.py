from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Conversation, User, Message
from schemas import ConversationCreate, ConversationOut, MessageCreate, MessageOut
from datetime import datetime

router = APIRouter(prefix="/conversations", tags=["Conversations"])

@router.post("/", response_model=ConversationOut)
def start_conversation(conv: ConversationCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == conv.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_conv = Conversation(user_id=conv.user_id, started_at=datetime.utcnow())
    db.add(new_conv)
    db.commit()
    db.refresh(new_conv)
    return new_conv

@router.post("/{conversation_id}/messages", response_model=MessageOut)
def add_message(conversation_id: int, msg: MessageCreate, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    new_msg = Message(
        conversation_id=conversation_id,
        content=msg.content,
        sender=msg.sender,
        timestamp=datetime.utcnow()
    )
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg

@router.get("/{conversation_id}/messages", response_model=list[MessageOut])
def get_messages(conversation_id: int, db: Session = Depends(get_db)):
    messages = db.query(Message).filter(Message.conversation_id == conversation_id).all()
    return messages
