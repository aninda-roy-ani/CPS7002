from week5.animal import Animal
from week5.plant import Plant


class Human(Plant, Animal):
    MAX_ENERGY = 100
    ENERGY_FOR_REPRODUCTION = 20
    ENERGY_FOR_MOVEMENT = 10

    def __init__(self, name, energy):
        super().__init__(name, energy)

    def __repr__(self):
        return f'human(name={self._name}, age={self._age}, energy={self._energy})'

    def __str__(self):
        return f'{self._name} is {self._age} years old with {self._energy} units of energy'








