import pytest
from pydantic import ValidationError
from app.schemas.order import OrderCreate, OrderResponse


def test_order_create_success():
    valid_data = {
        "customer_name": "John Doe",
        "item": "Laptop",
        "quantity": 1,
        "total_price": 1500.00,
        "status": "processing"
    }
    order = OrderCreate(**valid_data)

    assert order.customer_name == "John Doe"
    assert order.item == "Laptop"
    assert order.quantity == 1
    assert order.total_price == 1500.00
    assert order.status == "processing"


def test_order_create_invalid_quantity():
    invalid_data = {
        "customer_name": "John Doe",
        "item": "Laptop",
        "quantity": -1,
        "total_price": 1500.00,
        "status": "processing"
    }

    with pytest.raises(ValidationError):
        OrderCreate(**invalid_data)


def test_order_create_invalid_total_price():
    invalid_data = {
        "customer_name": "John Doe",
        "item": "Laptop",
        "quantity": 1,
        "total_price": "invalid_price",
        "status": "processing"
    }

    with pytest.raises(ValidationError):
        OrderCreate(**invalid_data)


def test_order_response_success():
    valid_data = {
        "id": 1,
        "customer_name": "Jane Doe",
        "item": "Smartphone",
        "quantity": 2,
        "total_price": 2000.00,
        "status": "completed"
    }
    order_response = OrderResponse(**valid_data)

    assert order_response.id == 1
    assert order_response.customer_name == "Jane Doe"
    assert order_response.item == "Smartphone"
    assert order_response.quantity == 2
    assert order_response.total_price == 2000.00
    assert order_response.status == "completed"


def test_order_response_invalid_id():
    invalid_data = {
        "id": "invalid_id",
        "customer_name": "Jane Doe",
        "item": "Smartphone",
        "quantity": 2,
        "total_price": 2000.00,
        "status": "completed"
    }

    try:
        order_response = OrderResponse(**invalid_data)
        print(f"Order created: {order_response}")
    except ValidationError as e:
        print(f"Validation Error: {e}")
        raise


def test_order_response_missing_field():
    invalid_data = {
        "id": 1,
        "customer_name": "Jane Doe",
        "item": "Smartphone",
        "quantity": 2,
        # Поле "total_price" отсутствует
        "status": "completed"
    }

    try:
        OrderResponse(**invalid_data)
    except ValidationError as e:
        print(f"Validation Error: {e}")
        raise


def test_order_response_invalid_quantity():
    invalid_data = {
        "id": 1,
        "customer_name": "Jane Doe",
        "item": "Smartphone",
        "quantity": "invalid_quantity",
        "status": "completed"
    }

    try:
        OrderResponse(**invalid_data)
    except ValidationError as e:
        print(f"Validation Error: {e}")
        raise
