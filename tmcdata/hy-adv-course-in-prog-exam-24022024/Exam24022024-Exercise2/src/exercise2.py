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
    
    
class ShoppingList:
    def __init__(self):
        self.products = []

    def add_product(self, product_info):
        name, price, unit, quantity = product_info
        if quantity <= 0:
            return
        for i, (product_name, product_price, product_unit, product_quantity) in enumerate(self.products):
            if product_name == name:
                self.products[i] = (name, price, unit, self.products[i][3] + quantity)
                break
        else:
            self.products.append((name, price, unit, quantity))

    def return_product(self, name):
        for product in self.products:
            if product[0] == name:
                return f"name: {product[0]}, unit price: {product[1]:.2f}€/{product[2]}, quantity: {product[3]}{product[2]}, total price: {(product[3] * product[1]):.2f}€"
        raise ValueError("Product not found on the shopping list.")
            
    def remove_product(self, name, amount=None):
            for i, (product_name, product_price, product_unit, product_quantity) in enumerate(self.products):
                if product_name == name:
                    if amount is None or amount >= product_quantity:
                        del self.products[i]
                    else:
                        self.products[i] = (product_name, self.products[i][1], self.products[i][2], product_quantity - amount)
                    break
            else:
                raise ValueError("Product not found on the shopping list.")

    def change_product_unit_price(self, name, new_price):
            for i, (product_name, product_price, product_unit, product_quantity) in enumerate(self.products):
                if product_name == name:
                    self.products[i] = (product_name, new_price, product_unit, product_quantity)
                    break

    def return_all_products(self):
        all_products = []
        for product_name, price, unit, quantity in self.products:
            all_products.append(f"name: {product_name}, unit price: {price:.2f}€/{unit}, quantity: {quantity}{unit}, total price: {(quantity * price):.2f}€")
        return all_products

    def return_total_price_of_shopping_list(self):
        total_price = sum(product_quantity * product_price for product_name, product_price, product_unit, product_quantity in self.products)
        return total_price


if __name__ == "__main__":
    apple = ("apple", 1.60, "kg", 2.2)  # 2.2 kg of apples
    potato = ("potato", 1.30, "kg", 5.0)  # 5 kg of potatoes
    banana = ("banana", 0.95, "kg", 1.2)  # 1.2 kg of bananas
    milk = ("milk", 1.25, "l", 2.0)  # 2 liters of milk
    bread = ("sourdough bread", 2.50, "piece", 3.0)  # 3 pieces of bread

    shopping_list = ShoppingList()

    shopping_list.add_product(apple)
    shopping_list.add_product(potato)
    shopping_list.add_product(banana)
    shopping_list.add_product(milk)
    shopping_list.add_product(bread)

    print("Product information at the beginning:")
    all_products = shopping_list.return_all_products()
    for product in all_products:
        print(product)

    shopping_list.change_product_unit_price("sourdough bread", 4.00)

    shopping_list.change_product_unit_price("apple", 1)

    print()
    print("After the changes:")
    all_products = shopping_list.return_all_products()
    for product in all_products:
        print(product)

    print()
    print("Removing 2 loaves of bread, all bananas, and more milk than available:")
    shopping_list.remove_product("sourdough bread", 2)
    shopping_list.remove_product("banana")
    shopping_list.remove_product("milk", 3)
    all_products = shopping_list.return_all_products()
    for product in all_products:
        print(product)

    print("Total price of the shopping list:", shopping_list.return_total_price_of_shopping_list())