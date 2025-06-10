from fastapi import HTTPException, Depends
from app.utils.oauth2 import get_current_user

def admin_required(current_user=Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user