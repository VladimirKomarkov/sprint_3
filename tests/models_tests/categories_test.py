import pytest
from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Date
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from app.db.base import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

metadata = MetaData()


@pytest.fixture(scope='function', autouse=True)
def setup_and_teardown():
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)


def create_category_test(table_name):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    test_table = Table(
        table_name, metadata,
        Column('name', String, primary_key=True),
        Column('description', String, unique=True),
        Column('created_at', Date)
    )
    metadata.create_all(engine)
    return test_table


def table_exists(table_name):
    query = text("""
    SELECT EXISTS (
        SELECT FROM information_schema.tables
        WHERE table_name = :table_name
        );
    """)
    with engine.connect() as conn:
        result = conn.execute(query, {"table_name": table_name})
        return result.scalar()


def drop_test_table(table_name):
    try:
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(text(f"DROP TABLE IF EXISTS {table_name};"))
    except SQLAlchemyError as e:
        print(f"Error dropping table {table_name}: {e}")



@pytest.mark.parametrize("table_name", ["test_table_1", "test_table_2"])
def test_create_table(table_name):
    drop_test_table(table_name)

    assert not table_exists(table_name)

    create_category_test(table_name)

    assert table_exists(table_name)

    drop_test_table(table_name)

    assert not table_exists(table_name)
