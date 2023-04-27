from src.Model import product
from src.View import productView
from src.Controller import productToJSON,playOnAttributesProduct


def main():
    print("Welcome to PTJ in Python, this program convert input program to JSON and print it in txt file")
    p = product.Product(1, "sedia", 56)
    my_product = productView.product_input()

    print(p.__str__())
    print(my_product.__str__())

#   product => JSON
    my_json_product=productToJSON.convert_product_to_json(my_product)

    print(my_json_product)

    productToJSON.write_json_on_file(my_json_product)

    playOnAttributesProduct.sum_price(my_product.price,p.price)
    playOnAttributesProduct.link_names(my_product.name,p.name)

if __name__ == "__main__":
    main()