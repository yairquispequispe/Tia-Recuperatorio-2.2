class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount

product1 = Product("Gaming Laptop", 1200.00)
product2 = Product("Bluetooth Headphones", 150.00)

product1.apply_discount(15) 
product2.apply_discount(10)  

print(f"The final price of the {product1.name} after the discount is: ${product1.price}")
print(f"The final price of the {product2.name} after the discount is: ${product2.price}")