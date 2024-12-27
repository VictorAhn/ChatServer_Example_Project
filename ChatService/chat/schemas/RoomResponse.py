from pydantic import BaseModel, Field
from typing import List

class RoomResponse(BaseModel):
    room_id: str = Field(description="채팅방의 고유 ID")
    participants: List[str]
