from fastapi import APIRouter, Depends
from app.core.deps import require_user, require_admin

router = APIRouter()

@router.get("/")
def report_placeholder():
    return {"message": "Report system placeholder active."}

@router.get("/user/reports")
def get_user_reports(user=Depends(require_user)):
    # logic here
    return {"msg": "Only users can see this"}

@router.get("/admin/dashboard")
def get_admin_dashboard(admin=Depends(require_admin)):
    # logic here
    return {"msg": "Only admins can see this"}
