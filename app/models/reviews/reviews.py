from app.db.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String, unique=True)
    updated_at = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
