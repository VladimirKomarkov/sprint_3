import pytest
from unittest.mock import MagicMock, patch

from sqlalchemy.orm import Session

from app.models.orders import Order
from app.schemas.order import OrderCreate
from app.services.order_service import create_order, process_order


@pytest.fixture
def mock_db_session():
    return MagicMock(spec=Session)


@pytest.fixture
def valid_order_data():
    return OrderCreate(
        customer_name="John Doe",
        item="Laptop",
        quantity=1,
        total_price=1000.00,
        status="pending"
    )


@patch("app.services.order_service.validate_order_data", return_value=True)
@patch("app.services.order_service.send_to_queue")
def test_create_order(mock_send_to_queue, mock_validate_order_data, mock_db_session, valid_order_data):
    new_order = MagicMock(spec=Order)
    new_order.to_dict.return_value = {
        'id': None,
        'customer_name': 'John Doe',
        'item': 'Laptop',
        'quantity': 1,
        'total_price': 1000.00,
        'status': 'pending',
        'created_at': None,
        'updated_at': None,
        'user_id': None
    }

    mock_db_session.add.return_value = None
    mock_db_session.commit.return_value = None
    mock_db_session.refresh.return_value = new_order

    order = create_order(mock_db_session, valid_order_data)

    mock_validate_order_data.assert_called_once_with(valid_order_data)

    mock_db_session.add.assert_called_once()

    mock_send_to_queue.assert_called_once_with("order_processing", new_order.to_dict())


@patch("app.services.order_service.send_to_queue")
def test_process_order(mock_send_to_queue, mock_db_session):
    mock_order = MagicMock(spec=Order)
    mock_order.id = 1
    mock_order.status = "pending"

    process_order(mock_order, mock_db_session)

    assert mock_order.status == "processed"

    mock_db_session.commit.assert_called_once()

    mock_send_to_queue.assert_called_once_with("notification", {"order_id": mock_order.id, "status": "processed"})
