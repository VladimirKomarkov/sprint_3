from unittest.mock import patch, MagicMock
import json

from app.consumers.notification_consumer import start_notification_consumer


def test_start_notification_consumer():
    with patch('pika.BlockingConnection') as mock_connection:
        mock_channel = MagicMock()
        mock_connection.return_value.channel.return_value = mock_channel

        mock_channel.basic_consume = MagicMock()

        test_message = {
            "order_id": 1,
            "status": "confirmed"
        }
        body = json.dumps(test_message)

        mock_method = MagicMock()
        mock_properties = MagicMock()

        def mock_start_consuming():
            callback = mock_channel.basic_consume.call_args[1]['on_message_callback']
            callback(mock_channel, mock_method, mock_properties, body)

            start_notification_consumer()

            mock_channel.basic_ack.assert_called_once_with(delivery_tag=mock_method.delivery_tag)

            mock_channel.start_consuming.assert_called_once()
