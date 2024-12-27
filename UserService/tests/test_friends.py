import pytest
from fastapi.testclient import TestClient
from mock import patch
from friends.routes import router  # 라우터 임포트
# FastAPI 앱을 테스트할 때 사용되는 기본 앱 객체
from fastapi import FastAPI

# 테스트용 애플리케이션 생성
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router, prefix="/friends")  # 실제 라우터 포함
    return app

# TestClient를 사용하여 테스트
client = TestClient(create_app())

def test_login_user():
    user_id = 1

    # patch를 사용하여 login_user 함수가 예측된 결과를 반환하도록 처리
    with patch('friends.service.find_friend', return_value={"user_id": user_id, "friends": ["John", "Jane"]}):
        # 로그인 API 호출
        response = client.get(f"/friends/find?user_id={user_id}")

        # 응답 상태 코드 확인
        assert response.status_code == 200

        # 응답 JSON 데이터 확인
        response_data = response.json()
        assert response_data["user_id"] == user_id  # user_id가 일치하는지 확인
        assert "friends" in response_data  # friends 키가 존재하는지 확인
        assert response_data["friends"] == ["John", "Jane"]  # 예상된 친구 목록과 일치하는지 확인