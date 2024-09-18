from app.models.base import Base
from sqlalchemy import Column, Integer, String, Date
import logging


class Sellers(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String, unique=True)
    created_at = Column(Date)

    logging.info(f"Таблица {__tablename__} успешно создана")