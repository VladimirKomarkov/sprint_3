from sqlalchemy.orm import Session
from ..models.orders.orders import Order
from ..schemas.order import OrderCreate
from ..utils.validation import validate_order_data
from ..services.rabbitmq_service import send_to_queue


def create_order(db: Session, order_data: OrderCreate):
    if not validate_order_data(order_data):
        raise ValueError("Invalid order data")

    new_order = Order(
        customer_name=order_data.customer_name,
        item=order_data.item,
        quantity=order_data.quantity,
        total_price=order_data.total_price,
        status=order_data.status,
        created_at=order_data.created_at,
        updated_at=order_data.updated_at,
        user_id=order_data.user_id
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    send_to_queue("order_processing", new_order.to_dict())

    return new_order


def process_order(order: Order, db: Session):
    order.status = "processed"
    db.commit()
    db.refresh(order)

    send_to_queue("notification", {"order_id": order.id, "status": order.status})
