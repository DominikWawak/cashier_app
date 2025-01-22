from repository.repository import *

class ProductService():
	
	def addProduct(self,data):
		print("service",data)
		response = ProductRepository.addProduct(data['product_code'], data['product_name'], data['product_price'])
		# response = json_message("You have added a new product")
		return response

	
