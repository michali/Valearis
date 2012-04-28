from Utils.Enum import Enum

direction = Enum('North', 'South', 'East', 'West')

opposite_directions = {direction.North : direction.South,
                       direction.South : direction.North,
                       direction.East : direction.West,
                       direction.West : direction.East }

def get_opposite_direction(dir):
    return opposite_directions[dir]
