from itertools import product

from cart import Cart
from product import Product
from product_manager import ProductManager

product_manager = ProductManager()
product_manager.add_product(Product("Laptop", 3500, 5))
product_manager.add_product(Product("Telefon", 2000, 10))
product_manager.add_product(Product("Căști", 150, 20))

product_manager.display_products()

print(f"Valoarea totala a inventarului: {product_manager.total_inventory_value()} RON")

# Instantiate Cart
cart = Cart()

# Add products in cart
cart.add_to_cart(product_manager.products[0])
cart.add_to_cart(product_manager.products[1])
cart.add_to_cart(product_manager.products[2])

# Show cart items
cart.display_cart()
print(f"Total de plata: {cart.cart_total()} RON")