from unittest.mock import patch, MagicMock

from app.config import settings


def test_order_consumer():
    with patch('pika.BlockingConnection') as mock_connection:
        mock_channel = MagicMock()
        mock_connection.return_value.channel.return_value = mock_channel

        mock_channel.basic_consume = MagicMock()

        def start_consuming_messages(mock_session):
            mock_session.assert_called_with(bind=settings.database_url)
