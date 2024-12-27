from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    sender_id: str
    room_id: str
    message: str
    timestamp: datetime