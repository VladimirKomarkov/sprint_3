from app.models.base import Base
from sqlalchemy import Column, Integer, ForeignKey


class ProductsSellers(Base):
    __tablename__ = 'products_sellers'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)