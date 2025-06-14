from fastapi import APIRouter, HTTPException
from app.models.user_model import UserCreate, UserLogin
from app.services import auth_service

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    success = await auth_service.register_user(user)
    if not success:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"msg": "User registered"}

@router.post("/login")
async def login(user: UserLogin):
    token = await auth_service.login_user(user)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token}
