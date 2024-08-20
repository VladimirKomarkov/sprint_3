import pika
import json
from ..config import settings


def start_notification_consumer():
    connection = pika.BlockingConnection(pika.URLParameters(settings.rabbitmq_url))
    channel = connection.channel()

    channel.queue_declare(queue="notification", durable=True)

    def callback(ch, method, properties, body):
        try:
            notification_data = json.loads(body)
            print(f"Sending notification for order ID: {notification_data['order_id']}"
                  f" with status: {notification_data}['status")
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Error processing notification: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)

        channel.basic_consume(queue="notification", on_message_callback=callback)
        print("Notification consumer started")
        channel.start_consuming()
