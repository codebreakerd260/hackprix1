from pydantic import BaseModel, EmailStr
from typing import Literal
from app.core.constants import ALLOWED_ROLES

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Literal["user", "admin"] = "user"  # default to "user"

class UserLogin(BaseModel):
    email: EmailStr
    password: str
