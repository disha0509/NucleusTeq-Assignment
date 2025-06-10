from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.order.models import Order
from app.order.schema import OrderOut
from app.utils.oauth2 import get_current_user

router = APIRouter(tags=["orders"])

@router.get("/", response_model=List[OrderOut])
def order_history(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    orders = db.query(Order).filter(Order.user_id == current_user.id).all()
    return orders

@router.get("/{order_id}", response_model=OrderOut)
def order_detail(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == current_user.id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order