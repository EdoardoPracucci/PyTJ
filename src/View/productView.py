from ..Model import product

def product_input():
    print('Insert Product: id, name, price')
    my_id = int(input("Insert Product ID: "))
    name = input("Insert Product Name: ")
    price = float(input("Insert Product Price: "))
    my_product = product.Product(my_id, name, price)
    return my_product