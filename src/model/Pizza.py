from sqlalchemy import Column, Integer, String, Float, func, TIMESTAMP
from src.db.db import engine, session, Base


class Pizza(Base):
    __tablename__ = 'pizza'

    pizza_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    price = Column(Float(), nullable=False)
    quantity = Column(Integer(), nullable=False)
    created_by = Column(TIMESTAMP, server_default=func.now())
    updated_by = Column(TIMESTAMP, server_default=func.now())

    def __init__(self, name, type, price, quantity, created_by, updated_by):
        self.name = name
        self.type = type
        self.price = price
        self.quantity = quantity
        self.created_by = created_by
        self.updated_by = updated_by


Base.metadata.create_all(bind=engine)
session.commit()
