import pytest
from unittest.mock import MagicMock
from app.models.orders import Order


@pytest.fixture
def mock_db_session():
    mock_session = MagicMock()
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()

    yield mock_session


def test_create_order(mock_db_session):
    new_order = Order(
        customer_name="test_customer",
        item="test_item",
        quantity=1,
        total_price=1.0,
        status="in stock"
    )

    mock_db_session.add(new_order)
    mock_db_session.commit()

    mock_db_session.add.assert_called_once_with(new_order)
    mock_db_session.commit.assert_called_once()

    assert new_order.customer_name == "test_customer"
    assert new_order.item == "test_item"
    assert new_order.quantity == 1
    assert new_order.total_price == 1.0
    assert new_order.status == "in stock"
