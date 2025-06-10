from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.cart.models import Cart
from app.products.models import Product
from app.order.models import Order, OrderItem
from app.utils.oauth2 import get_current_user

router = APIRouter(tags=["checkout"])

@router.post("/", status_code=201)
def checkout(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    cart_items = db.query(Cart).filter(Cart.user_id == current_user.id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")
    total = 0
    order_items = []
    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            continue
        subtotal = product.price * item.quantity
        total += subtotal
        order_items.append(OrderItem(
            product_id=product.id,
            quantity=item.quantity,
            price_at_purchase=product.price
        ))
    order = Order(user_id=current_user.id, total_amount=total, status="paid", items=order_items)
    db.add(order)
    db.query(Cart).filter(Cart.user_id == current_user.id).delete()
    db.commit()
    db.refresh(order)
    return {"order_id": order.id, "total": total, "status": "paid"}