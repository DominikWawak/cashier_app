from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = "products"

    product_code = db.Column('product_code', db.String(3), primary_key=True)
    product_name = db.Column('product_name', db.Unicode(255), unique=True) 
    product_price = db.Column('product_price', db.Unicode(255)) 

class Transaction(db.Model):
    __tablename__ = "transactions"

    transaction_id = db.Column('transaction_id', db.String(255), primary_key=True)
    transaction_total = db.Column('transaction_total', db.Unicode(255))  