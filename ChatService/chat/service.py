from typing import List
from datetime import datetime
from chat.schemas.RoomResponse import RoomResponse

# 예시 데이터
rooms = [
    {"room_id": "1", "participants": ["user1", "user2"]},
    {"room_id": "2", "participants": ["user2", "user3"]}
]

rooms2 = []

messages = [
    {"room_id": "1", "sender_id": "user1", "message": "Hello, user2!", "timestamp": datetime.now()},
    {"room_id": "1", "sender_id": "user2", "message": "Hi, user1!", "timestamp": datetime.now()},
    {"room_id": "2", "sender_id": "user2", "message": "Hello, user3!", "timestamp": datetime.now()}
]

# 채팅방 목록 조회
def get_rooms(user_id: str) -> List[RoomResponse]:
    # user_id가 user_1이면 rooms, user_2이면 rooms2 반환
    if user_id == "user1":
        return rooms
    elif user_id == "user2":
        return rooms2
    else:
        return [] 
    