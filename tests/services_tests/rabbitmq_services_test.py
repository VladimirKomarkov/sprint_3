import json

import pika
import pytest
from unittest.mock import patch, MagicMock
from app.services.rabbitmq_service import send_to_queue
from app.config import settings


@pytest.fixture
def mock_blocking_connection():
    with patch('pika.BlockingConnection') as mock:
        yield mock


def test_send_to_queue(mock_blocking_connection):
    mock_connection = MagicMock()
    mock_channel = MagicMock()

    mock_blocking_connection.return_value = mock_connection
    mock_connection.channel.return_value = mock_channel

    queue_name = 'test_queue'
    message = {'key': 'value'}

    send_to_queue(queue_name, message)

    mock_blocking_connection.assert_called_once_with(pika.URLParameters(settings.rabbitmq_url))
    mock_connection.channel.assert_called_once()
    mock_channel.queue_declare.assert_called_once_with(queue=queue_name, durable=True)
    mock_channel.basic_publish.assert_called_once_with(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    mock_connection.close.assert_called_once()
