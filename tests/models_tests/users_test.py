import pytest
from unittest.mock import MagicMock
from app.models.users.users import Users


@pytest.fixture
def mock_db_session():
    mock_session = MagicMock()
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()

    yield mock_session


def test_create_user(mock_db_session):
    new_user = Users(
        username = "test_name",
        phone_number = "123",
        email = "test",
        status = "active",
        preferences = "test_preferences",
        password_hash = "test_hash",
        first_name = "John",
        last_name = "Doe",
        address = "test_address"
    )

    mock_db_session.add(new_user)
    mock_db_session.commit()

    mock_db_session.add.assert_called_once_with(new_user)
    mock_db_session.commit.assert_called_once()

    assert new_user.username == "test_name"
    assert new_user.phone_number == "123"
    assert new_user.email == "test"
    assert new_user.status == "active"
    assert new_user.preferences == "test_preferences"
    assert new_user.password_hash == "test_hash"
    assert new_user.first_name == "John"
    assert new_user.last_name == "Doe"
    assert new_user.address == "test_address"
