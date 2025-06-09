from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import database
from app import models, schemas
from app.database.database import get_db
from app.utils import oauth2
from app.utils import util


router = APIRouter(tags=["Authentication"])
@router.post("/login")
def login(user_credentials:  OAuth2PasswordRequestForm=Depends(), db:  Session = Depends(get_db)):
    user= db.query(models.users.User).filter(models.users.User.email == user_credentials.username).first()
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