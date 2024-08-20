from app.db.base import Base
from sqlalchemy import Column, String, Date


class Categories(Base):
    __tablename__ = 'categories'

    name = Column(String, PrimaryKey=True)
    description = Column(String, unique=True)
    created_at = Column(Date)