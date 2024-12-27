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
