from fastapi import FastAPI
from app.database.database import engine, get_db
from sqlalchemy.orm import Session
from app.users.models import Base, User
from app.users import router as user_router
from app.products import router as product_router
from app.products.router import public_router
from app.cart import router as cart_router
from app.order import router as order_router
from app.checkout import router as checkout_router


Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(product_router.router, prefix="/admin/products", tags=["products"])
app.include_router(public_router, prefix="/products", tags=["public-products"])
app.include_router(cart_router.router, prefix="/cart", tags=["cart"])
app.include_router(checkout_router.router, prefix="/checkout", tags=["checkout"])
app.include_router(order_router.router, prefix="/orders", tags=["orders"])

@app.get("/")
def root():
    return {"message" : "Welcome to the e-commerce Project Using FastAPI!"}