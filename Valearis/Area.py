class Area:

    def __init__(self, name, short_description = None, long_description = None):
        if (name == None):
            raise ValueError("name should be given")

        self.__name = name
        self.__short_description = short_description
        self.__long_description = long_description
        self.__adjacents = set()
        self.__items = set()

    @property
    def name(self):
        return self.__name

    @property
    def shortDescription(self):
        return self.__short_description

    @property
    def longDescription(self):
        return self.__long_description

    @property
    def items(self):
        return self.__items

    def addAdjacent(self, adjacent_area):
        self.__adjacents.add(adjacent_area)
        adjacent_area.__adjacents.add(self)

    @property
    def adjacents(self):
        return self.__adjacents