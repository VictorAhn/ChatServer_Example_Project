from fastapi import APIRouter, HTTPException
from chat.service import get_rooms
from chat.schemas.RoomResponse import RoomResponse
from typing import List

router = APIRouter()

# 채팅방 목록 조회
@router.get("/rooms", summary='채팅방 목록 조회', response_model=List[RoomResponse], response_description="사용자가 참여한 채팅방의 목록")
def get_rooms_list(user_id: str):
    rooms = get_rooms(user_id)
    if not rooms:
        raise HTTPException(status_code=404, detail="No rooms found")
    return rooms