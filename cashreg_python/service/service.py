from repository.repository import *
import math


class ProductService():
    
    GREENTEA_CODE = "GR1"
    STRAWBERRIES_CODE = "SR1"
    COFFEE_CODE = "CF1"
    
    
    def addProduct(self,data):
        response = ProductRepository.addProduct(data['product_code'], data['product_name'], data['product_price'])
        return response

    def getProducts(self):
        return ProductRepository.getProducts()

    def getProduct(self,product_code):
        return ProductRepository.getProduct(product_code)
    
    def buyProducts(self,product_codes):
        total_price = 0
        valid_products = dict()
        for product_code in product_codes.split(','):
            if product_code not in valid_products:
                valid_products[product_code] = 0
            valid_products[product_code] += 1
        
        for product_code, count in valid_products.items():
            response,status = ProductRepository.getProduct(product_code)
            if product_code == ProductService.GREENTEA_CODE:
                valid_products[product_code] = math.ceil(count/2)
            
            if product_code == ProductService.STRAWBERRIES_CODE and count >= 3:
                response['product']['product_price'] = "4.50"
                
            if product_code == ProductService.COFFEE_CODE and count >= 3:
                response['product']['product_price'] = str(float(response['product']['product_price']) * (2/3))
                
            total_price += float(response['product']['product_price']) * valid_products[product_code]

         
        return str(total_price)

	
