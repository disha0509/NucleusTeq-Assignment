from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.cart.models import Cart
from app.cart.schema import CartAdd, CartOut
from app.utils.oauth2 import get_current_user
from app.products.models import Product
from app.logging_config import logger

router = APIRouter(tags=["cart"])

@router.post("/", response_model=CartOut)
def add_to_cart(
    cart_item: CartAdd,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
) -> CartOut:
    """
    Add a product to the user's cart or update quantity if it already exists.
    """
    product = db.query(Product).filter(Product.id == cart_item.product_id).first()
    if not product or product.is_deleted:
        logger.warning(f"Attempt to add deleted or non-existent product {cart_item.product_id} to cart by user {current_user.id}")
        raise HTTPException(status_code=400, detail="Product is not available.")
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
)-> List[CartOut]:
    """
    Retrieve all items in the current user's cart.

    Args:
        db (Session): Database session.
        current_user: The currently authenticated user.

    Returns:
        List[CartOut]: List of cart items for the user.
    """
    logger.info(f"User {current_user.id} viewing cart")
    return db.query(Cart).filter(Cart.user_id == current_user.id).all()

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_from_cart(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    
    Remove a product from the user's cart.

    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product or product.is_deleted:
        logger.warning(f"Attempt to delete deleted or non-existent product {product_id} from cart by user {current_user.id}")
        raise HTTPException(status_code=400, detail="Product is not available.")
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
    return {"message": "cart deleted sucessfully"}

@router.put("/{product_id}", response_model=CartOut)
def update_quantity(
    product_id: int,
    cart_item: CartAdd,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
) -> CartOut:
    """
    Update the quantity of a product in the user's cart.
    """

    product = db.query(Product).filter(Product.id == product_id).first()
    if not product or product.is_deleted:
        logger.warning(f"Attempt to update deleted or non-existent product {product_id} in cart by user {current_user.id}")
        raise HTTPException(status_code=400, detail="Product is not available.")

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