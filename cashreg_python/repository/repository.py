from database.database_model import *
import json
from flask import Response
from sqlalchemy.exc import SQLAlchemyError



## Repository layer will handle database transactions.

def json_message(value):
	json_a = {"message": value}
	json_response = json.dumps(json_a)

	return json_response

class ProductRepository:
    def addProduct(product_code, product_name, product_price):
        try:
            product = Product(
                product_code=product_code,
                product_name=product_name,
                product_price=product_price
            )
            print("Attempting to add product:", product.product_code)

            db.session.add(product)
            db.session.commit()

            print("Product added successfully!")
            return {"status": "success", "message": "Product added successfully"}, 201

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error adding product: {e}")
            return {"status": "error", "message": "Failed to add product, please try again"}, 500

        finally:
            db.session.close()
	