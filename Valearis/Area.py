import Directions

class Area:

    def __init__(self, name, short_description = None, long_description = None):
        self.__name = name
        self.__short_description = short_description
        self.__long_description = long_description
        self.__adjacents = {}
        self.__items = []

    @property
    def name(self):
        return self.__name

    @property
    def short_description(self):
        return self.__short_description

    @property
    def long_description(self):
        return self.__long_description

    def set_adjacent(self, area, dir):
        self.__adjacents[dir] = area
        area.__adjacents[Directions.get_opposite_direction(dir)] = self

    def get_adjacent(self, direction):
        return self.__adjacents[direction]

    @property
    def items(self):
        return self.__items