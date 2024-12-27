from pydantic import BaseModel

class MessageResponse(BaseModel):
    sender_id: str
    room_id: str
    message: str
    timestamp: str
