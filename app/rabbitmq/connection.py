import pika
import logging

logging.basicConfig(level=logging.INFO)

try:
    connection_params = pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/',
        credentials=pika.PlainCredentials(
            username='guest',
            password='guest'
        )
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue='my_queue')
    logging.info("Очередь создана и подключение установлено.")

except pika.exceptions.AMQPConnectionError as e:
    logging.error(f"Ошибка подключения к RabbitMQ: {e}")

finally:
    if 'connection' in locals() and connection.is_open:
        connection.close()
        logging.info("Подключение закрыто.")
