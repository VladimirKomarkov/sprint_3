from sqlalchemy.orm import Session
from app.models.orders import Order
from ..schemas.order import OrderCreate
from ..utils.validation import validate_order_data
from ..services.rabbitmq_service import send_to_queue
import logging


def create_order(db: Session, order_data: OrderCreate):
    if not validate_order_data(order_data):
        raise ValueError("Invalid order data")

    new_order = Order(
        customer_name=order_data.customer_name,
        item=order_data.item,
        quantity=order_data.quantity,
        total_price=order_data.total_price,
        status=order_data.status
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    logging.info(f"Создан новый заказ: {new_order.id}")

    send_to_queue("order_processing", new_order.to_dict())
    logging.info(f"Отправлено сообщение о новом заказе в очередь: {new_order.id}")

    return new_order


def process_order(order: Order, db: Session):
    order.status = "processed"
    db.commit()
    db.refresh(order)

    send_to_queue("notification", {"order_id": order.id, "status": order.status})
