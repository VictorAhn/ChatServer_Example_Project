import pytest
from fastapi.testclient import TestClient
from mock import patch
from chat.route import router  # 라우터 임포트
# FastAPI 앱을 테스트할 때 사용되는 기본 앱 객체
from fastapi import FastAPI

# 테스트용 애플리케이션 생성
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router, prefix="/chat")  # 실제 라우터 포함
    return app

# TestClient를 사용하여 테스트
client = TestClient(create_app())

# 채팅방 목록 조회 성공 테스트
def test_get_rooms_list_success():
    # mock_rooms 데이터를 정의
    mock_rooms = [ {"room_id": "1", "participants": ["user1", "user2"]}, {"room_id": "2", "participants": ["user2", "user3"]}]
    
    # patch를 사용하여 get_rooms 함수가 mock_rooms를 반환하도록 처리
    with patch('chat.service.get_rooms', return_value=mock_rooms):
        response = client.get("/chat/rooms?user_id=user1")  # 요청을 보낼 URL
        # 상태 코드가 200이어야 하고
        assert response.status_code == 200   
        # 응답 JSON이 mock_rooms와 일치해야 함
        assert response.json() == mock_rooms

# 채팅방 목록 조회 실패 테스트 (빈 목록 반환)
def test_get_rooms_list_no_rooms():
    # 빈 목록을 반환하도록 mock 처리
    with patch('chat.service.get_rooms', return_value=[]):  # 빈 목록 반환
        response = client.get("/chat/rooms?user_id=user2")  # 요청을 보낼 URL
        
        # 상태 코드가 404이어야 하고
        assert response.status_code == 404
        
        # 응답 메시지가 "No rooms found"이어야 함
        assert response.json() == {"detail": "No rooms found"}
