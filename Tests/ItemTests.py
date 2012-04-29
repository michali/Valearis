from unittest import TestCase
from Item import Item

class Item_Name(TestCase):

    def test_name(self):
        item = Item("An object")

        self.assertEqual(item.name, "An object")

    def test_description(self):
        item = Item(None, "Desc")

        self.assertEqual(item.description, "Desc")