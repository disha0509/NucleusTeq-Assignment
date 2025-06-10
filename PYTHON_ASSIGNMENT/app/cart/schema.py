from pydantic import BaseModel

class CartAdd(BaseModel):
    product_id: int
    quantity: int

class CartOut(CartAdd):
    id: int
    user_id: int

    class Config:
        from_attribute = True