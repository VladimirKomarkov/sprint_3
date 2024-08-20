from app.db.base import Base
from sqlalchemy import Column, Integer, ForeignKey


class ShopsSellers(Base):
    __tablename__ = 'shops_sellers'

    shop_id = Column(Integer, ForeignKey('shops.id'), primary_key=True)