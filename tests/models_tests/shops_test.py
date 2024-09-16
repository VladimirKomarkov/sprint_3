import pytest
from unittest.mock import MagicMock
from app.models.shops import Shops


@pytest.fixture
def mock_db_session():
    mock_session = MagicMock()
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()

    yield mock_session


def test_create_shop(mock_db_session):
    new_shop = Shops(
        name = "test_name",
        description = "test_description",
        address = "test_address"
    )

    mock_db_session.add(new_shop)
    mock_db_session.commit()

    mock_db_session.add.assert_called_once_with(new_shop)
    mock_db_session.commit.assert_called_once()

    assert new_shop.name == "test_name"
    assert new_shop.description == "test_description"
    assert new_shop.address == "test_address"
