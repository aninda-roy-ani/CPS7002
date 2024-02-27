from planet import Planet
from non_planet import NonPlanet
import random

class Universe:

    def __init__(self):
        self.__planets = []
        self.__non_planets = []

    def generate(self, planet):
        if random.choice([True, False]):  # Randomly choose between generating a planet or non-planet
            self.__planets.append(Planet())
        else:
            self.__non_planets.append(NonPlanet())

    def display(self):
        print("Planets:")
        for planet in self.__planets:
            print(planet)


