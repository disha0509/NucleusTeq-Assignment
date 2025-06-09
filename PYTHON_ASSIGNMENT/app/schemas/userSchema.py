from enum import Enum
from pydantic import BaseModel, EmailStr


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
