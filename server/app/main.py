from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import admin
from app.api.v1.routes import auth, emergency, report, feedback, admin


print("STARTING APP")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "✅ Backend is up and running"}

@app.get("/ping")
def ping():
    return "pong"

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(emergency.router, prefix="/api/v1/emergency")
app.include_router(report.router, prefix="/api/v1/report")
app.include_router(feedback.router, prefix="/api/v1/feedback")
app.include_router(admin.router, prefix="/api/v1/admin")
