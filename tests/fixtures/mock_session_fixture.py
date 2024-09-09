import pytest
from unittest.mock import patch


@pytest.fixture
def mock_session():
    with patch('app.db.base.SessionLocal') as mock_session_cls:
        yield mock_session_cls.return_value

