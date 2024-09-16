import pika

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
    print("Очередь создана и подключение установлено.")


finally:
    connection.close()
    print("Подключение закрыто.")
