class NonPlanet:
    def __init__(self, name=""):
        self.__name = name

    def __repr__(self):
        return f'NonPlanet(name={self.__name})'

    def __str__(self):
        return f'Non-Planet: {self.__name}'