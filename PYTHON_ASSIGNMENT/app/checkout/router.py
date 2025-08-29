from typing import Dict
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.cart.models import Cart
from app.products.models import Product
from app.order.models import Order, OrderItem
from app.utils.oauth2 import get_current_user
from app.logging_config import logger

router = APIRouter(tags=["checkout"])

# Process the checkout for the current user
@router.post("/", status_code=201)
def checkout(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
)-> Dict[str, object]:
    """
    Process the checkout for the current user.

    """
    logger.info(f"User {current_user.id} initiated checkout")
    cart_items = db.query(Cart).filter(Cart.user_id == current_user.id).all()
    # Check if the cart is empty
    if not cart_items:
        logger.warning(f"Checkout failed: Cart is empty for user {current_user.id}")
        raise HTTPException(status_code=400, detail="Cart is empty")
    total = 0
    order_items = []
    # Validate products and calculate total
    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        # Check if the product exists and is not deleted
        if not product or product.is_deleted:
            logger.warning(f"Product {item.product_id} is deleted or not found during checkout for user {current_user.id}")
            raise HTTPException(
                status_code=400,
                detail=f"Product with id {item.product_id} is not available for checkout."
            )
        # Check if the requested quantity is available in stock
        if item.quantity > product.stock:
            logger.warning(f"Insufficient stock for product {product.id} (requested: {item.quantity}, available: {product.stock})")
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for product '{product.name}'. Available: {product.stock}, Requested: {item.quantity}"
            )
        subtotal = product.price * item.quantity
        total += subtotal
        order_items.append(OrderItem(
            product_id=product.id,
            quantity=item.quantity,
            price_at_purchase=product.price
        ))
    # Create the order and update product stock
        for item in cart_items:
            product = db.query(Product).filter(Product.id == item.product_id).first()
            product.stock -= item.quantity
    order = Order(user_id=current_user.id, total_amount=total, status="paid", items=order_items)
    db.add(order)
    db.query(Cart).filter(Cart.user_id == current_user.id).delete()
    db.commit()
    db.refresh(order)
    logger.info(f"Order {order.id} created for user {current_user.id} with total {total}")
    return {"order_id": order.id, "total": total, "status": "paid"}