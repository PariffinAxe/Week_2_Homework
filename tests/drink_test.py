import unittest

from src.drink import *

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Beer", 120, 5)

    def test_name(self):
        self.assertEquals("Beer", self.drink.name)

    def test_alcoholic_content(self):
        self.assertEquals(120, self.drink.alcohol_level)

    def test_price(self):
        self.assertEquals(5, self.drink.price)
