from app.models.base import Base
from sqlalchemy import Column, Integer, ForeignKey
import logging


class ShopsSellers(Base):
    __tablename__ = 'shops_sellers'

    shop_id = Column(Integer, ForeignKey('shops.id'), primary_key=True)

    logging.info(f"Таблица {__tablename__} успешно создана")