from app.db.base import Base
from sqlalchemy import Column, Integer, ForeignKey


class SellersUsers(Base):
    __tablename__ = 'sellers_users'

    seller_id = Column(Integer, ForeignKey('sellers.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
