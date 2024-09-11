import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.db.base import Base, DATABASE_URL

@pytest.fixture(scope='module')
def engine():
    return create_engine(DATABASE_URL, echo=True)

@pytest.fixture(scope='module')
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(engine, tables):
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    yield session
    session.close()

def test_example(db_session):
    result = db_session.execute(text('SELECT 1'))
    assert result.scalar() == 1
