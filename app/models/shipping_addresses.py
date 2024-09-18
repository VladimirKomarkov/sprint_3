from app.models.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
import logging


class ShippingAddresses(Base):
    __tablename__ = 'shipping_addresses'

    id = Column(Integer, primary_key=True)
    address_line = Column(String, unique=True)
    country = Column(String)
    city = Column(String)
    postal_code = Column(Integer)
    created_at = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)

    logging.info(f"Таблица {__tablename__} успешно создана")