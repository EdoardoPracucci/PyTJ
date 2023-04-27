from unittest import TestCase
from ..Controller import productToJSON
from ..Model import product
import json


class Test(TestCase):
    def test_convert_product_to_json(self):
        p=product.Product(1,"c",1.0)
        pj=json.dumps(p.__dict__)
        self.assertEqual(productToJSON.convert_product_to_json(p),pj)


# class Test(TestCase):
#     def test_write_json_on_file(self):
#         self.fail()
