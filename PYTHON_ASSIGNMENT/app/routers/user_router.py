from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from app.schemas.userSchema import UserSignup, UserOut
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.users import User
from app.utils.util import hash_password
from typing import List
#from app.models.users import PasswordResetToken
#from app.schemas.usersS import ForgotPassword, ResetPassword
#from app.utils.util import hash_password, generate_reset_token
from datetime import datetime

router = APIRouter()
@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def signup(user: UserSignup,db: Session = Depends(get_db)):
    user_data = user.dict()
    user_data["password"] = hash_password(user_data["password"])
    print(user_data)
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


