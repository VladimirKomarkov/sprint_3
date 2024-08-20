from app.db.base import Base
from sqlalchemy import Column, Integer, String, Date


class Sellers(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String, unique=True)
    created_at = Column(Date)