class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, quantity):
        self.products.append({"product": product, "quantity": quantity})

    def sell_product(self, product_name, quantity):
        for product_entry in self.products:
            if product_entry["product"].name == product_name:
                if product_entry["quantity"] >= quantity:
                    self.income += product_entry["product"].price * quantity
                    product_entry["quantity"] -= quantity
                    return
                else:
                    raise ValueError("Not enough products in stock")

    def get_product_info(self, product_name):
        for product_entry in self.products:
            if product_entry["product"].name == product_name:
                return product_name, product_entry["quantity"]

    def get_income(self):
        return self.income

store = ProductStore()
ramen = Product("Food", "Ramen", 10)
shirt = Product("Clothing", "Shirt", 20)

store.add(ramen, 100)
store.add(shirt, 50)

print(store.get_product_info("Ramen"))
print(store.get_product_info("Shirt"))

store.sell_product("Ramen", 5)
store.sell_product("Shirt", 10)

print(f"Income: ${store.get_income()}")
print(store.get_product_info("Ramen"))
print(store.get_product_info("Shirt"))
