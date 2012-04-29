from Area import Area
from unittest.case import TestCase
from Directions import direction, get_opposite_direction
from Item import Takeable

class Area_init(TestCase):
    def test_noNameRaisesError(self):
        self.assertRaises(ValueError, Area, None)

class Area_props(TestCase):

    def test_sets_name(self):
        area = Area('an area')
        self.assertEqual(area.name, 'an area')

    def test_sets_shortDescription(self):
        area = Area('', 'short desc')
        self.assertEqual(area.shortDescription, 'short desc')

    def test_sets_longDescription(self):
        area = Area('', '', 'long desc')
        self.assertEqual(area.longDescription, 'long desc')

class Area_set_get_adjacent(TestCase):

    def setUp(self):
        self.main_area = Area('Main')

    def set_adjacent(self, adjacent_area, direction_of_main_area):
        self.main_area.setAdjacent(adjacent_area, direction_of_main_area)

    def test_north_is_set(self):
        self.north_area = Area('North Area')
        self.main_area.setAdjacent(self.north_area, direction.North)

        self.assertEqual(self.north_area.getAdjacent(direction.South), self.main_area)

    def test_south_is_set(self):
        self.south_area = Area('South Area')
        self.main_area.setAdjacent(self.south_area, direction.South)

        self.assertEqual(self.south_area.getAdjacent(direction.North), self.main_area)

    def test_east_is_set(self):
        self.east_area = Area('East Area')
        self.main_area.setAdjacent(self.east_area, direction.East)

        self.assertEqual(self.east_area.getAdjacent(direction.West), self.main_area)

    def test_west_is_set(self):
        self.west_area = Area('West Area')
        self.main_area.setAdjacent(self.west_area, direction.West)

        self.assertEqual(self.west_area.getAdjacent(direction.East), self.main_area)

class Area_add_item(TestCase):

    def test_adds_item(self):
        self.area = Area('area')
        self.item = Takeable('object')

        self.area.items.append(self.item)

        self.assertTrue(self.area.items.__len__() == 1)
        self.assertEqual(self.area.items[0], self.item)