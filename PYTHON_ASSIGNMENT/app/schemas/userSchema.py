from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum = RoleEnum.user

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: RoleEnum

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]=None

class ForgotPassword(BaseModel):
    email: EmailStr

class ResetPassword(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8, max_length=128)
