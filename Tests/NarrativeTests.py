from unittest.case import TestCase
from Area import Area
from Item import Item
from Narrative import Narrative


class NarrativeTests(TestCase):

    def test_getScene_getsAreaShortDescription(self):
        area = Area("area", "You are in area.")
        narrative = Narrative(area)

        self.assertEqual(narrative.intro, "You are in area.")
        self.assertEqual(narrative.presentationOfItems, None)
        self.assertEqual(narrative.items.__len__(), 0)

    def test_getScene_getsAreaNameAreaShortDescriptionAreaItems(self):
        area = Area("area", "you are in another area")
        item1 = Item("", "an item.")
        item2 = Item("", "another item.")
        area.items.add(item1)
        area.items.add(item2)
        narrative = Narrative(area)

        self.assertEqual(narrative.intro, "you are in another area")
        self.assertEqual(narrative.presentationOfItems, "Here there are:")
        self.assertEqual(narrative.items.__len__(), 2)
        self.assertTrue(narrative.items.__contains__("an item."))
        self.assertTrue(narrative.items.__contains__("another item."))