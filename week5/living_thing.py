class LivingThing:
    INITIAL_AGE = 0
    MAX_ENERGY = 100
    ENERGY_FOR_MOVEMENT = 10
    ENERGY_TO_REPRODUCE = 20

    def __init__(self, name, energy):
        self._age = 0
        self._energy = energy
        self._name = name

    def __repr__(self):
        return f'LivingThing(name={self._name},age={self._age},energy={self._energy}'

    def __str__(self):
        return f'The living thing named {self._name} of age {self._age} has {self._energy} unit(s) of energy'

    def grow(self):
        self._age += 1

    def reproduce(self):
        if self._energy >= self.ENERGY_TO_REPRODUCE:
            self._energy -= self.ENERGY_TO_REPRODUCE
            return True
        return False










