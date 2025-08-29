import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from app.database.database import Base
from sqlalchemy.orm import  declarative_base
from sqlalchemy.orm import relationship

class UserRole(str, enum.Enum):
    admin = "admin"
    user = "user"

#create table named User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.user)

    
    cart_items = relationship("Cart", back_populates="user", cascade="all, delete-orphan")
    products = relationship("Product", back_populates="creator", cascade="all, delete")
    

# Create a table for password reset tokens
class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    expires_at = Column(DateTime, nullable=False)

    user = relationship("User")