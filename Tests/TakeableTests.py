from unittest.case import TestCase
from Item import Takeable

class Takeable_Name(TestCase):

    def test_name(self):
        t = Takeable("An object")

        self.assertEqual(t.name, "An object")

    def test_description(self):
        t = Takeable(None, "Desc")

        self.assertEqual(t.description, "Desc")

