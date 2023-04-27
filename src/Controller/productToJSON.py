import json
import os.path


def convert_product_to_json(my_product):
    json_product = json.dumps(my_product.__dict__)
    return json_product


def write_json_on_file(my_json_product):
    directory = "/home/edo/Documents/Repository/PYTJ_PythonToJason/src/Files/"
    filename = "my_product.json"
    filepath = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    file = open(filepath, "w")
    file.write(my_json_product)
    file.close()
