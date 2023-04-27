from unittest import TestCase
from ..Controller import productToJSON
from ..Model import product
import os.path
import json


class Test(TestCase):
    def test_convert_product_to_json(self):
        p=product.Product(1,"c",1.0)
        pj=json.dumps(p.__dict__)
        self.assertEqual(productToJSON.convert_product_to_json(p),pj)


class Test(TestCase):
    def test_write_json_on_file(self):
        path = "/home/edo/Documents/Repository/PYTJ_PythonToJason/src/Files/my_product.json"
        os.path.isfile(path)
        self.assertEqual(os.path.isfile(path),True)
