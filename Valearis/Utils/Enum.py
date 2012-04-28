class Enum():
    def __init__(self, *keys):
        self.__dict__.update(zip(keys, range(len(keys))))