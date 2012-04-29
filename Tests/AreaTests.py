from Area import Area
from unittest.case import TestCase
from Directions import direction, get_opposite_direction
from Item import Takeable

class Area_props(TestCase):

    def test_can_name(self):
        area = Area('an area')
        self.assertEqual(area.name, 'an area')

    def test_can_short_description(self):
        area = Area('', 'short desc')
        self.assertEqual(area.short_description, 'short desc')

    def test_can_long_description(self):
        area = Area('', '', 'long desc')
        self.assertEqual(area.long_description, 'long desc')

class Area_set_get_adjacent(TestCase):

    def setUp(self):
        self.main_area = Area('Main')

    def set_adjacent(self, adjacent_area, direction_of_main_area):
        self.main_area.set_adjacent(adjacent_area, direction_of_main_area)

    def test_north_is_set(self):
        self.north_area = Area('North Area')
        self.set_adjacent(self.north_area, direction.North)

        self.assertEqual(self.north_area.get_adjacent(direction.South), self.main_area)

    def test_south_is_set(self):
        self.south_area = Area('South Area')
        self.main_area.set_adjacent(self.south_area, direction.South)

        self.assertEqual(self.south_area.get_adjacent(direction.North), self.main_area)

    def test_east_is_set(self):
        self.east_area = Area('East Area')
        self.main_area.set_adjacent(self.east_area, direction.East)

        self.assertEqual(self.east_area.get_adjacent(direction.West), self.main_area)

    def test_west_is_set(self):
        self.west_area = Area('West Area')
        self.main_area.set_adjacent(self.west_area, direction.West)

        self.assertEqual(self.west_area.get_adjacent(direction.East), self.main_area)

class Area_add_item(TestCase):

    def test_adds_item(self):
        self.area = Area('area')
        self.item = Takeable('object')

        self.area.items.append(self.item)

        self.assertTrue(self.area.items.__len__() == 1)
        self.assertEqual(self.area.items[0], self.item)