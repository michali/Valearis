from Area import Area
from unittest.case import TestCase
from Item import Item

class Area_init(TestCase):
    def test_noNameRaisesError(self):
        self.assertRaises(ValueError, Area, None, 'desc')

    def test_noShortDescriptionRaisesError(self):
        self.assertRaises(ValueError, Area, 'name', None)

class Area_props(TestCase):

    def test_sets_name(self):
        area = Area('an area', '')
        self.assertEqual(area.name, 'an area')

    def test_sets_shortDescription(self):
        area = Area('', 'short desc')
        self.assertEqual(area.shortDescription, 'short desc')

    def test_sets_longDescription(self):
        area = Area('', '', 'long desc')
        self.assertEqual(area.longDescription, 'long desc')

class Area_set_get_adjacent(TestCase):

    def test_adjacent_is_set(self):
        main_area = Area('main', '')
        adjacent_area = Area('North Area', '')
        main_area.addAdjacent(adjacent_area)

        self.assertEqual(main_area.adjacents.__len__(), 1)
        self.assertEqual(main_area.adjacents.pop(), adjacent_area)
        self.assertEqual(adjacent_area.adjacents.__len__(), 1)
        self.assertEqual(adjacent_area.adjacents.pop(), main_area)

class Area_add_item(TestCase):

    def test_adds_item(self):
        area = Area('area', '')
        item = Item('object')

        area.items.add(item)

        self.assertTrue(area.items.__len__() == 1)
        self.assertEqual(area.items.pop(), item)