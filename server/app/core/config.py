import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "HackPrix"
    MONGO_URI = "mongodb+srv://codebreakers260:passtoken@cluster0.tonpigo.mongodb.net/Hackprix?retryWrites=true&w=majority&appName=Cluster0"
    JWT_SECRET = os.getenv("JWT_SECRET", "supersecret")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRE_MINUTES = 60
    SECRET_KEY = "TOPsecret"

settings = Settings()
