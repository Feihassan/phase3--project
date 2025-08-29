# models/models.py
#You’ll use these to define table columns and types.
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime

from sqlalchemy.orm import relationship #Declares ORM relationships i.e links between tables.
from database import Base # this is declarative base
from datetime import datetime # this is For timestamps used as default order date.


#customer model
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True) #Primary key column
    name = Column(String, nullable=False) #
    email = Column(String, nullable=False, unique=True)
    phone = Column(String)

    orders = relationship("Order", back_populates="customer") #Declares a one-to-many link: one customer → many orders

#menuItem model(maps to menu items table)

class MenuItem(Base):
    __tablename__ = "menu_items"
#Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String)

    orders = relationship("Order", back_populates="menu_item")#One-to-many: one menu item → many orders that include it.

#order model(maps to orders table)
class Order(Base):
    __tablename__ = "orders"
#Columns
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    quantity = Column(Integer, nullable=False)
    status = Column(String, default="Pending")
    order_date = Column(DateTime, default=datetime.utcnow)  

#The inverse sides of the relationships defined on Customer and MenuItem.
    customer = relationship("Customer", back_populates="orders")
    menu_item = relationship("MenuItem", back_populates="orders")
