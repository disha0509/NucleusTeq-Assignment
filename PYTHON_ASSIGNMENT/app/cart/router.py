from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.cart.models import Cart
from app.cart.schema import CartAdd, CartOut
from app.utils.oauth2 import get_current_user
from app.logging_config import logger

router = APIRouter(tags=["cart"])

@router.post("/", response_model=CartOut)
def add_to_cart(
    cart_item: CartAdd,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    logger.info(f"User {current_user.id} adding product {cart_item.product_id} (qty {cart_item.quantity}) to cart")
    cart = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == cart_item.product_id
    ).first()
    if cart:
        cart.quantity += cart_item.quantity
        logger.info(f"Updated quantity for product {cart_item.product_id} in user {current_user.id}'s cart")
    else:
        cart = Cart(user_id=current_user.id, **cart_item.dict())
        db.add(cart)
        logger.info(f"Added new product {cart_item.product_id} to user {current_user.id}'s cart")
    db.commit()
    db.refresh(cart)
    return cart

@router.get("/", response_model=list[CartOut])
def view_cart(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    logger.info(f"User {current_user.id} viewing cart")
    return db.query(Cart).filter(Cart.user_id == current_user.id).all()

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_from_cart(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    logger.info(f"User {current_user.id} removing product {product_id} from cart")
    cart = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == product_id
    ).first()
    if not cart:
        logger.warning(f"Product {product_id} not found in user {current_user.id}'s cart")
        raise HTTPException(status_code=404, detail="Item not found in cart")
    db.delete(cart)
    db.commit()
    logger.info(f"Product {product_id} removed from user {current_user.id}'s cart")
    return

@router.put("/{product_id}", response_model=CartOut)
def update_quantity(
    product_id: int,
    cart_item: CartAdd,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    logger.info(f"User {current_user.id} updating quantity for product {product_id} to {cart_item.quantity}")
    cart = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == product_id
    ).first()
    if not cart:
        logger.warning(f"Product {product_id} not found in user {current_user.id}'s cart for update")
        raise HTTPException(status_code=404, detail="Item not found in cart")
    cart.quantity = cart_item.quantity
    db.commit()
    db.refresh(cart)
    return cart