def find_friend(user_id: int):
    # 친구 찾기 로직
    return {"user_id": user_id, "friends": ["John", "Jane"]}

def add_friend(user_id: int, friend_id: int):
    # 친구 추가 로직
    return {"user_id": user_id, "added_friend_id": friend_id}

def list_friends(user_id: int):
    # 친구 목록 조회 로직
    return {"user_id": user_id, "friends": ["John", "Jane", "Doe"]}
