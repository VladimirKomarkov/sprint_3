from app.models.base import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
import logging


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    description = Column(String, unique=True)
    price = Column(Float)
    stock = Column(Boolean)
    created_at = Column(Date)
    updated_at = Column(Date)
    seller_id = Column(Integer, ForeignKey('sellers.id'))

    logging.info(f"Таблица {__tablename__} успешно создана")