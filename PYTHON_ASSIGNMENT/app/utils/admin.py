from fastapi import HTTPException, Depends
from app.utils.oauth2 import get_current_user

def admin_required(current_user=Depends(get_current_user)) -> object:
    """
    Dependency to ensure the current user is an admin.

    Args:
        current_user: The currently authenticated user, injected by Depends(get_current_user).

    Returns:
        object: The current user object if they are an admin.

    Raises:
        HTTPException: If the current user is not an admin.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user