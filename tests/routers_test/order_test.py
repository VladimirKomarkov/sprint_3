import pytest
from unittest.mock import patch, MagicMock

from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.main import app
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import create_order

client = TestClient(app)

order_data = {
    "customer_name": "John Doe",
    "item": "laptop",
    "quantity": 1,
    "total_price": 2000.0,
    "status": "pending"
}

@pytest.fixture
def mock_db():
    mock_session = MagicMock(spec=Session)
    mock_session.execute = MagicMock()
    mock_session.execute.return_value.fetchone.return_value = (1,)  #
    mock_session.execute.return_value.fetchall.return_value = [
        (1, "John Doe", "laptop", 1, 2000.0, "pending")
    ]
    yield mock_session

@patch("app.services.rabbitmq_service.pika.BlockingConnection")
@patch("app.services.order_service.create_order")
@patch("app.services.rabbitmq_service.send_to_queue")
def test_create_new_order_success(mock_send_to_queue, mock_create_order, mock_db):
    mock_create_order.return_value = OrderResponse(
        id=1,
        customer_name="John Doe",
        item="laptop",
        quantity=1,
        total_price=2000.0,
        status="pending"
    )

    mock_send_to_queue.return_value = None

    with patch('app.db.base.SessionLocal', return_value=mock_db):
        response = client.post("/orders/", json=order_data)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == 1
    assert response_json["customer_name"] == "John Doe"
    assert response_json["item"] == "laptop"
    assert response_json["quantity"] == 1
    assert response_json["total_price"] == 2000.0
    assert response_json["status"] == "pending"

    mock_create_order.assert_called_once_with(
        customer_name="John Doe",
        item="laptop",
        quantity=1,
        total_price=2000.0,
        status="pending",
        created_at=None,
        updated_at=None,
        user_id=1
    )
    mock_send_to_queue.assert_called_once()
