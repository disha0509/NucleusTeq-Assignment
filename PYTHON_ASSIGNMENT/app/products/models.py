from sqlalchemy import Column, ForeignKey, Integer, String, Float
from app.database.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String)
    image_url = Column(String)
    #created_by = Column(Integer, ForeignKey("users.id"), nullable=False)