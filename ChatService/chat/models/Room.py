from pydantic import BaseModel
from typing import List

class Room(BaseModel):
    room_id: str
    participants: List[str]