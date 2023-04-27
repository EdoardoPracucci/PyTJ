from unittest import TestCase
from ..Controller import playOnAttributesProduct


class Test(TestCase):
    def test_sum_price(self):
        self.assertEqual(playOnAttributesProduct.sum_price(5, 6), 11)


class Test(TestCase):
    def test_link_names(self):
        self.assertEqual(playOnAttributesProduct.link_names("ciao", "hello"), "ciaohello")
