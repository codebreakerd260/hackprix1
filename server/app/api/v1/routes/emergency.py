from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def emergency_mock_status():
    return {"message": "Emergency system placeholder active."}
