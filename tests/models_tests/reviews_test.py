import pytest
from unittest.mock import MagicMock
from app.models.reviews import Reviews


@pytest.fixture
def mock_db_session():
    mock_session = MagicMock()
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()

    yield mock_session


def test_create_review(mock_db_session):
    new_review = Reviews(
        rating = 1,
        comment = "test_comment"
    )

    mock_db_session.add(new_review)
    mock_db_session.commit()

    mock_db_session.add.assert_called_once_with(new_review)
    mock_db_session.commit.assert_called_once()

    assert new_review.rating == 1
    assert new_review.comment == "test_comment"
