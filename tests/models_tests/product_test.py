import pytest
from unittest.mock import MagicMock
from app.models.products.products import Products

@pytest.fixture
def mock_db_session():
    mock_session = MagicMock()
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()
    return mock_session

def test_product(mock_db_session):
    new_product = Products(
        name="test_product",
        description="test_description",
        price=1.0,
        stock=100
    )

    mock_db_session.add(new_product)
    mock_db_session.commit()

    mock_db_session.add.assert_called_once_with(new_product)
    mock_db_session.commit.assert_called_once()

    assert new_product.name == "test_product"
    assert new_product.description == "test_description"
    assert new_product.price == 1.0
    assert new_product.stock == 100
