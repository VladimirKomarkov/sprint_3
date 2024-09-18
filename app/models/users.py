from app.models.base import Base
from sqlalchemy import Column, Integer, String, Date
import logging


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    status = Column(String)
    created_at = Column(Date)
    preferences = Column(String)
    password_hash = Column(String, unique=True)
    first_name = Column(String, unique=True)
    last_name = Column(String, unique=True)
    address = Column(String, unique=True)

    logging.info(f"Таблица {__tablename__} успешно создана")
