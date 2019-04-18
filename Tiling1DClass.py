# francois oder le 18 avril 2019


class Tiling1D:
    """
    Everything for 1D Tilings
    """

    def __init__(self, name, substitution):
        self.name = name
        self.substitution = substitution
        self.nb_tiles = len(substitution.keys())
        self.tiling = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def substitution(self):
        return self.__substitution

    @substitution.setter
    def substitution(self, substitution):
        self.__substitution = substitution

    @property
    def nb_tiles(self):
        return self.__nb_tiles

    @nb_tiles.setter
    def nb_tiles(self, nb_tiles):
        self.__nb_tiles = nb_tiles

    @property
    def tiling(self):
        return self.__tiling

    @tiling.setter
    def tiling(self, tiling):
        self.__tiling = tiling
