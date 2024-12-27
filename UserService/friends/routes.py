from fastapi import APIRouter
from friends.service import find_friend, add_friend, list_friends

router = APIRouter()

@router.get("/find")
def find(user_id: int):
    return find_friend(user_id)

@router.post("/add")
def add(user_id: int, friend_id: int):
    return add_friend(user_id, friend_id)

@router.get("/list")
def list_all(user_id: int):
    return list_friends(user_id)
