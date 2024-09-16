from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app
from app.models.orders import Base
from ..routers.order import get_db

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://owner:password@localhost:5432/jip_project"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_order():
    response = client.post("/orders/", json={"customer_name": "John Doe", "item": "Book", "quantity": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "John Doe"
    assert data["item"] == "Book"
    assert data["quantity"] == 1
    assert data["status"] == "new"
