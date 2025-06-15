from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from app.database.database import Base
from sqlalchemy.orm import relationship
from app.order.models import OrderItem

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String)
    image_url = Column(String)
    is_deleted = Column(Boolean,default=False,nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    creator = relationship("User", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    cart_items = relationship("Cart", back_populates="product")