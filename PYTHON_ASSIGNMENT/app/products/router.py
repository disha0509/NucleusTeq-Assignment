from typing import List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.products.models import Product
from app.products.schema import ProductCreate, ProductOut
from app.utils.admin import admin_required

router = APIRouter()

@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=List[ProductOut])
def read_products(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max number of items to return"),
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@router.get("/{product_id}", response_model=ProductOut)
@router.get("/{id}", response_model=ProductOut)
def read_product_detail(
    id: int,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Product not found")
    return product

from fastapi import HTTPException

@router.put("/{id}", response_model=ProductOut)
def update_product(
    id: int,
    product_update: ProductCreate,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product_update.dict().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    id: int,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return

public_router = APIRouter()


@public_router.get("/public", response_model=List[ProductOut], tags=["Public"])
def public_product_listing(
    category: str = Query(None),
    min_price: float = Query(None, ge=0),
    max_price: float = Query(None, ge=0),
    sort_by: str = Query("id", description="Sort by field: id, price, name"),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if sort_by in ["id", "price", "name"]:
        query = query.order_by(getattr(Product, sort_by))
    products = query.offset((page - 1) * page_size).limit(page_size).all()
    return products

@public_router.get("/public/search", response_model=List[ProductOut], tags=["Public"])
def public_product_search(
    keyword: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    products = db.query(Product).filter(
        (Product.name.ilike(f"%{keyword}%")) | (Product.description.ilike(f"%{keyword}%"))
    ).all()
    return products

@public_router.get("/public/{id}", response_model=ProductOut, tags=["Public"])
def public_product_detail(
    id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Product not found")
    return product
