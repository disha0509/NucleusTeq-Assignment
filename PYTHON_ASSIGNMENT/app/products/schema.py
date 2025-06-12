from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float = Field(..., gt=0)
    stock: int
    category: str
    image_url: str

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True