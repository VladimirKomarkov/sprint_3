from app.models.base import Base
from sqlalchemy import Column, Integer, String, Date
import logging


class Shops(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String, unique=True)
    address = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)

    logging.info(f"Таблица {__tablename__} успешно создана")
