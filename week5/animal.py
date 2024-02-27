from week5.living_thing import LivingThing


class Animal(LivingThing):

    def __init__(self, name, energy):
        super(Animal, self).__init__(name, energy)

    def __repr__(self):
        return f'Animal(name={self._name},age={self._age},energy={self._energy}'

    def __str__(self):
        return f'Animal {self._name} of age {self._age} has {self._energy} unit(s) of energy'

    def absorb(self, amount):
        self._energy += amount
        excess = self._energy - self.MAX_ENERGY
        if self._energy >= self.MAX_ENERGY:
            self._energy = self.MAX_ENERGY
        return excess

    def move(self, distance):
        if self._energy >= self.ENERGY_FOR_MOVEMENT:
            self._energy -= self.ENERGY_FOR_MOVEMENT
            return True
        return False

