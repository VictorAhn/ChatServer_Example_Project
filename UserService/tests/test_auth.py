import pytest
from fastapi.testclient import TestClient
from mock import patch
from auth.routes import router  # 라우터 임포트
# FastAPI 앱을 테스트할 때 사용되는 기본 앱 객체
from fastapi import FastAPI

# 테스트용 애플리케이션 생성
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router, prefix="/auth")  # 실제 라우터 포함
    return app

# TestClient를 사용하여 테스트
client = TestClient(create_app())

def test_login_user():
    # 테스트용 데이터 (예: 로그인하려는 사용자 정보)
    login_data = {"username": "user1", "password": "password123"}

    # patch를 사용하여 login_user 함수가 예측된 결과를 반환하도록 처리
    with patch('auth.service.login_user', return_value={"token": "user-token"}):
        # 로그인 API 호출
        response = client.post("auth/login", json=login_data)

        # 응답 상태 코드 확인
        assert response.status_code == 200

        # 응답 JSON 데이터 확인
        response_data = response.json()
        assert "token" in response_data  # 토큰 키가 존재하는지 확인
        assert response_data["token"] == "user-token"  # 예상된 토큰 값과 일치하는지 확인