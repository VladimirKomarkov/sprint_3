import pika
import unittest


class TestRabbitMQConnection(unittest.TestCase):
    def setUp(self):
        self.connection_params = pika.ConnectionParameters(
            host='localhost',
            port=5672,
            virtual_host='/',
            credentials=pika.PlainCredentials(
                username='guest',
                password='guest'
            )
        )

    def test_connection(self):
        connection = pika.BlockingConnection(self.connection_params)
        channel = connection.channel()
        self.assertIsNotNone(channel)
        connection.close()


if __name__ == '__main__':
    unittest.main()
