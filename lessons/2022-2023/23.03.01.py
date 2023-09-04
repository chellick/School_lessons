class Shop:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.product_list = []

    def get_products(self):
        return list(self.product_list)
    
    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)
        else:
            print('There is no such product')

        
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address

    
class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"name: {self.name}, description: {self.description},\
                 price: {self.price}, quantity: {self.quantity}"



cola = Product('Cola', 'can', 10, 20)
cheese = Product('Cheese', 'can', 20, 10)


walmart = Shop('Walmart', '30 saint. street')

walmart.add_product(cola)
walmart.add_product(cheese)



