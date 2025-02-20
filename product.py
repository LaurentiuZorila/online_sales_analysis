class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"{self.name}: {self.quantity} bucăți - {self.price} RON fiecare"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity