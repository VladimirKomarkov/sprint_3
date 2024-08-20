from app.db.base import Base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    item = Column(String)
    quantity = Column(Integer)
    total_price = Column(Float)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "item": self.item,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user_id": self.user_id
        }
