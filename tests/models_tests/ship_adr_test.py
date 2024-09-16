import pytest
from unittest.mock import MagicMock
from app.models.shipping_addresses import ShippingAddresses


@pytest.fixture
def mock_db_session():
    mock_session = MagicMock()
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()

    yield mock_session


def test_create_address(mock_db_session):
    new_address = ShippingAddresses(
        address_line = "test_address",
        country = "test_country",
        city = "test_city",
        postal_code = 12345
    )

    mock_db_session.add(new_address)
    mock_db_session.commit()

    mock_db_session.add.assert_called_once_with(new_address)
    mock_db_session.commit.assert_called_once()

    assert new_address.address_line == "test_address"
    assert new_address.country == "test_country"
    assert new_address.city == "test_city"
    assert new_address.postal_code == 12345
