__author__ = 'Michali'

class Narrative:

    def __init__(self, area):
        self.__intro = area.shortDescription
        self.__items = {item.description for item in area.items}
        self.__presentationOfItems = 'Here there are:' if self.__items.__len__() > 0 else None

    @property
    def intro(self):
        return self.__intro

    @property
    def presentationOfItems(self):
        return self.__presentationOfItems

    @property
    def items(self):
        return self.__items