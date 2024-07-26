class Product:
    def __init__(self, name: str, price: float, unit: str, quantity: float = 0):
        self.name = name
        self.price = price
        self.unit = unit
        self.quantity = quantity

        if len(self.name) < 3:
            raise ValueError("The name must be at least 3 characters long")

        if self.price <= 0:
            raise ValueError("The unit price cannot be negative or zero.")
        
        if self.unit == "":
            raise ValueError("The unit cannot be empty and must be a string")

        if self.quantity =="":
            self.quantity = 0

    def total_price(self):
        total_price = self.price * self.quantity
        return total_price
    
    
    def __str__(self):
        return f"name: {self.name}, unit price: {self.price:.2f}€/{self.unit}, quantity: {self.quantity}{self.unit}, total price: {self.total_price():.2f}€"
    
    
    def __add__(self, other):
        total_quantity = self.quantity + other.quantity
        total_price = self.price * self.quantity + other.price * other.quantity
        total_unit = self.unit if self.unit == other.unit else "various units"
        return Product("Mixed Products", total_price / total_quantity, total_unit, total_quantity)


if __name__ == "__main__":
    apple = Product("apple", 1.60, "kg", 2)
    potato = Product("potato", 1.30, "kg", 2)
    banana = Product("banana", 0.90, "kg", 3)
    bread = Product("sourdough bread", 2.70, "piece", 1)

    print("Apple price", apple.total_price())
    print("Total price:", (apple + potato + banana + bread).total_price())
