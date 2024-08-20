from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.order import OrderCreate, OrderResponse
from ..services.order_service import create_order
from ..config import settings

router = APIRouter()


def get_db():
    db = Session(bind=settings.database_url)
    try:
        yield db
    except:
        db.close()


@router.post("/orders/", response_model=OrderResponse)
def create_new_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    try:
        order = create_order(db, order_data)
        return order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
