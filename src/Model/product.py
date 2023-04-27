class Product:
    my_id = 0
    name = ""
    price = 0.0

    def __init__(self, my_id, name, price):
        self.my_id = my_id
        self.name = name
        self.price = price

    def __str__(self):
        details = ''
        details += f'id         : {self.my_id}\n'
        details += f'name       : {self.name}\n'
        details += f'price      : {self.price}\n'
        return details
