from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = "products"

    product_code = db.Column('product_code', db.String(3), primary_key=True)
    product_name = db.Column('product_name', db.Unicode(255), unique=True) 
    product_price = db.Column('product_price', db.Unicode(255))
    
    def to_dict(self):
        return {
            'product_code': str(self.product_code),  
            'product_name': self.product_name,
            'product_price': self.product_price
        }

class Transaction(db.Model):
    __tablename__ = "transactions"

    transaction_id = db.Column('transaction_id', db.String(255), primary_key=True)
    transaction_total = db.Column('transaction_total', db.Unicode(255))  
    
    def to_dict(self):
	    return {
			'transaction_id': str(self.transaction_id),  
			'transaction_total': self.transaction_total
		}