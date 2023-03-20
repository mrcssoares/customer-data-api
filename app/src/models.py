from sqlalchemy import Column, Integer, String
from .config import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    image = Column(String)
    price = Column(Integer)
    review_score = Column(Integer)


class Favorite(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
