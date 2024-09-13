import pytest
from unittest.mock import MagicMock
from app.models.sellers.sellers import Sellers


@pytest.fixture
def mock_db_session():
    mock_session = MagicMock()
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()

    yield mock_session


def test_create_seller(mock_db_session):
    new_seller = Sellers(
        name = "test_name",
        description = "test_description"
    )

    mock_db_session.add(new_seller)
    mock_db_session.commit()

    mock_db_session.add.assert_called_once_with(new_seller)
    mock_db_session.commit.assert_called_once()

    assert new_seller.name == "test_name"
    assert new_seller.description == "test_description"
