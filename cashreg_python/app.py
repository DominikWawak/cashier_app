from flask import (Flask, request, jsonify)
from config import Config
import awsgi


app = Flask(__name__)
app.config.from_object(Config)



from database.database_model import *

db.init_app(app)


from service.service import ProductService
ProductService = ProductService()

@app.route('/product', methods=['GET'])
def index():
    return ProductService.getProducts()


@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    return ProductService.addProduct(data)

@app.route('/product/<product_code>', methods=['Get'])
def get_product(product_code):
    return ProductService.getProduct(product_code)

@app.route('/products/buy', methods=['GET'])
def buy_products():
    product_codes = request.args.get('product_codes')
    return ProductService.buyProducts(product_codes)





def handler(event, context):
    return awsgi.response(app, event, context)

if __name__ == '__main__':
    app.run()