from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItemOut(BaseModel):
    product_id: int
    quantity: int
    price_at_purchase: float
    is_deleted : bool

    class Config:
        from_attributes = True

class OrderOut(BaseModel):
    id: int
    total_amount: float
    status: str
    created_at: datetime
    items: List[OrderItemOut]

    class Config:
        from_attributes = True