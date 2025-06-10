from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app.products import models
from app.users.schema import UserSignup, UserOut
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.users.models import User
from app.utils import oauth2, util
from app.utils.util import hash_password
from typing import List
from app.users.models import PasswordResetToken
from app.users.schema import ForgotPassword, ResetPassword
from app.utils.util import hash_password, generate_reset_token
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



@router.post("/login")
def login(user_credentials:  OAuth2PasswordRequestForm=Depends(), db:  Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if not util.verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password"
        )
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}






@router.get("/getAllUsers", response_model=List[UserOut])
def get_all_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found!")
    return users


@router.post("/forgot-password")
def secure_forgot_password(request: ForgotPassword, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    token, expires_at = generate_reset_token()
    reset_token = PasswordResetToken(token=token, user_id=user.id, expires_at=expires_at)
    db.add(reset_token)
    db.commit()
    
    return {"message": "Reset token created", "token": token}


@router.post("/reset-password")
def secure_reset_password(request: ResetPassword, db: Session = Depends(get_db)):
    token_entry = db.query(PasswordResetToken).filter(PasswordResetToken.token == request.token).first()

    if not token_entry or token_entry.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired token.")

    user = db.query(User).filter(User.id == token_entry.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    user.password = hash_password(request.new_password)

    # Invalidate token after use
    db.delete(token_entry)
    db.commit()

    return {"message": "Password successfully reset"}

