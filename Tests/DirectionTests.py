from unittest.case import TestCase
from Directions import get_opposite_direction, direction

class DirectionTests(TestCase):

    def test_opposite_of_north(self):
        north = direction.North

        expected_opposite_direction = get_opposite_direction(north)

        self.assertEqual(expected_opposite_direction, direction.South)
        
    def test_opposite_of_south(self):
        south = direction.South

        expected_opposite_direction = get_opposite_direction(south)

        self.assertEqual(expected_opposite_direction, direction.North)
    
    def test_opposite_of_east(self):
        east = direction.East

        expected_opposite_direction = get_opposite_direction(east)

        self.assertEqual(expected_opposite_direction, direction.West)

    def test_opposite_of_west(self):
        west = direction.West

        expected_opposite_direction = get_opposite_direction(west)

        self.assertEqual(expected_opposite_direction, direction.East)

