from fastapi import APIRouter, Body
from .service import login_user, signup_user

router = APIRouter()

@router.post("/login", summary='로그인')
def login(data: dict = Body(...)):
    return login_user(data)

@router.post("/signup", summary='회원가입', description='-')
def signup(data: dict = Body(...)):
    return signup_user(data)
