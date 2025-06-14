import jwt
from app.core.database import db
from app.core.security import hash_password, verify_password, create_token
from app.core.config import Settings

async def register_user(data):
    exists = await db.users.find_one({"email": data.email})
    if exists:
        return None
    user_dict = data.dict()
    user_dict["password"] = hash_password(user_dict["password"])
    await db.users.insert_one(user_dict)
    return True

async def login_user(data):
    user = await db.users.find_one({"email": data.email})
    if not user or not verify_password(data.password, user["password"]):
        return None
    token = create_token({"user_id": str(user["_id"]), "role": user["role"]})
    return token

def create_access_token(user: dict):
    payload = {
        "sub": str(user["_id"]),
        "email": user["email"],
        "role": user["role"]
    }
    token = jwt.encode(payload, Settings.SECRET_KEY, algorithm="HS256")
    return token
