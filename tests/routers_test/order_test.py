import pytest
from unittest.mock import patch, MagicMock

from app.routers.order import get_db
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

from app.main import app
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import create_order

client = TestClient(app)

order_data = {
    "customer_name": "John Doe",
    "item": "laptop",
    "quantity": 1,
    "total_price": 2000,
    "status": "pending",
    "created_at": "2024-09-12T00:00:00",
    "updated_at": "2024-09-12T00:00:00",
    "user_id": 1
}



@pytest.fixture
def mock_db():
    mock_session = MagicMock(spec=Session)
    yield mock_session


def test_get_db(mock_db):
    with patch('app.db.base.SessionLocal', return_value=mock_db):
        db_gen = get_db()
        db = next(db_gen)
        assert db is not None
        db_gen.close()


@patch("app.services.order_service")
def test_create_new_order_success(mock_create_order, mock_db):
    mock_create_order.return_value = OrderResponse(
        id=1,
        customer_name = "John Doe",
        item = "laptop",
        quantity = 1,
        total_price = 2000,
        status = "pending"
    )

    response = client.post("/orders/", json=order_data)

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "customer_name": "John Doe",
        "item": "laptop",
        "quantity": 1,
        "total_price": 2000,
        "status": "pending"
    }
    mock_create_order.assert_called_once_with()


