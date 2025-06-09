from fastapi import FastAPI
from app.database.database import engine, get_db
from sqlalchemy.orm import Session
from app.models.users import Base, User
from app.routers import user_router, auth

Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/users", tags=["Authentication"])

@app.get("/")
def root():
    return {"message" : "Welcome to the e-commerce Project Using FastAPI!"}