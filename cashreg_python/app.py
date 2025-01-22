from flask import (Flask, request, jsonify)
from config import Config

# import awsgi


app = Flask(__name__)
app.config.from_object(Config)



from database.database_model import *

db.init_app(app)


from service.service import ProductService
ProductService = ProductService()

@app.route('/', methods=['GET'])
def index():
    return jsonify(status=200, message='Hello World!')


@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    print("recieved",data)
    return ProductService.addProduct(data)




# TODO Future
# def lambda_handler(event, context):
#     return awsgi.response(app, event, context, base64_content_types={"image/png"})



if __name__ == '__main__':
    app.run()