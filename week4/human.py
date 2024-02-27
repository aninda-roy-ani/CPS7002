
class Human:
    MAX_ENERGY = 100
    ENERGY_FOR_REPRODUCTION = 20
    ENERGY_FOR_MOVEMENT = 10

    def __init__(self, name, age=0, energy=100):
        self.__name = name
        self.__age = age
        self.__energy = energy

    def __repr__(self):
        return f'human(name={self.__name}, age={self.__age}, energy={self.__energy})'

    def __str__(self):
        return f'{self.__name} is {self.__age} years old with {self.__energy} units of energy'

    def grow(self):
        self.__age += 1

    def eat(self, amount):
        #excess = min(self.MAX_ENERGY - self.energy, amount)
        excess = self.MAX_ENERGY - self.__energy
        self.__energy += amount
        excess = self.__energy-self.MAX_ENERGY
        if self.__energy>=self.MAX_ENERGY:
            self.__energy = self.MAX_ENERGY
        return excess

    def reproduce(self):
        if self.__energy >= self.ENERGY_FOR_REPRODUCTION:
            self.__energy -= self.ENERGY_FOR_REPRODUCTION
            return True
        return False

    def move(self, distance):
        if self.__energy >= self.ENERGY_FOR_MOVEMENT:
            self.__energy -= self.ENERGY_FOR_MOVEMENT
            return True
        return False



