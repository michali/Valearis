from Area import Area
from unittest.case import TestCase
from Directions import direction
from Item import Takeable

class Area_props(TestCase):

    def test_can_name(self):
        area = Area('an area')
        self.assertEqual(area.name, 'an area')

    def test_can_short_description(self):
        area = Area('', 'short desc', '')
        self.assertEqual(area.short_description, 'short desc')

    def test_can_long_description(self):
        area = Area('', '', 'long desc')
        self.assertEqual(area.long_description, 'long desc')

class Area_set_get_adjacent(TestCase):

    def test_north_is_set(self):
        main_area = Area('Main')
        north_area = Area('North Area')

        main_area.set_adjacent(north_area, direction.North)

        self.assertEqual(north_area.get_adjacent(direction.South), main_area)

    def test_south_is_set(self):
        main_area = Area('Main')
        south_area = Area('South Area')

        main_area.set_adjacent(south_area, direction.South)

        self.assertEqual(south_area.get_adjacent(direction.North), main_area)

    def test_east_is_set(self):
        main_area = Area('Main')
        east_area = Area('East Area')

        main_area.set_adjacent(east_area, direction.East)

        self.assertEqual(east_area.get_adjacent(direction.West), main_area)

    def test_west_is_set(self):
        main_area = Area('Main')
        west_area = Area('West Area')

        main_area.set_adjacent(west_area, direction.West)

        self.assertEqual(west_area.get_adjacent(direction.East), main_area)

class Area_add_item(TestCase):

    def test_adds_item(self):
        area = Area('area')
        item = Takeable('object')

        area.items.append(item)

        self.assertTrue(area.items.__len__() == 1)
        self.assertEqual(area.items[0], item)