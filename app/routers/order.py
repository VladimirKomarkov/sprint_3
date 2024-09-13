from fastapi import APIRouter, Depends, HTTPException
from app.db.base import SessionLocal
from sqlalchemy.orm import Session
from ..schemas.order import OrderCreate, OrderResponse
from ..services.order_service import create_order

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/orders/", response_model=OrderResponse)
def create_new_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    try:
        order = create_order(db, order_data)
        return order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
