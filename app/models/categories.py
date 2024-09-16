from app.models.base import Base
from sqlalchemy import Column, String, Date, Integer


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, unique=True)
    created_at = Column(Date)
