from app.models.base import Base
from sqlalchemy import Column, String, Date, Integer
import logging


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, unique=True)
    created_at = Column(Date)

    logging.info(f"Таблица {__tablename__} успешно создана")
