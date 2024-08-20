import pika
import json
from sqlalchemy.orm import Session
from ..models.orders.orders import Order
from ..services.order_service import process_order
from ..config import settings


def start_order_consumer():
    connection = pika.BlockingConnection(pika.URLParameters(settings.rabbitmq_url))
    channel = connection.channel()

    channel.queue_declare(queue="order_processing", durable=True)

    def callback(ch, method, properties, body):
        session = Session(bind=settings.database_url)
        try:
            order_data = json.loads(body)
            order = session.query(Order).get(order_data["id"])
            if order:
                process_order(order, session)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Error processing order {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue="order_processing", on_message_callback=callback)
    print("Order consumer started")
    channel.start_consuming()
