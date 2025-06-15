from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.order.models import Order
from app.order.schema import OrderOut
from app.utils.oauth2 import get_current_user
from app.logging_config import logger

router = APIRouter(tags=["orders"])

@router.get("/", response_model=List[OrderOut])
def order_history(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
)-> List[OrderOut]:
    """
    Retrieve the order history for the current user.

    """
    logger.info(f"User {current_user.id} requested order history")
    orders = db.query(Order).filter(Order.user_id == current_user.id).all()
    logger.info(f"Found {len(orders)} orders for user {current_user.id}")
    return orders

@router.get("/{order_id}", response_model=OrderOut)
def order_detail(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
)-> OrderOut:
    """
    Retrieve the details of a specific order for the current user.

    """
    logger.info(f"User {current_user.id} requested details for order {order_id}")
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == current_user.id).first()
    if not order:
        logger.warning(f"Order {order_id} not found for user {current_user.id}")
        raise HTTPException(status_code=404, detail="Order not found")
    logger.info(f"Order {order_id} details returned for user {current_user.id}")
    return order