from product import Product
from product_manager import ProductManager

product_manager = ProductManager()
product_manager.add_product(Product("Laptop", 3500, 5))
product_manager.add_product(Product("Telefon", 2000, 10))
product_manager.add_product(Product("Căști", 150, 20))

product_manager.display_products()
