from week5.living_thing import LivingThing


class Plant(LivingThing):

    def __init__(self, name, energy):
        super().__init__(name, energy)

    def __repr__(self):
        return f'Plant(name={self._name},age={self._age},energy={self._energy}'

    def __str__(self):
        return f'Plant: name:{self._name}, age:{self._age}, energy:{self._energy}'

    def absorb(self, amount):
        self._energy += amount
        return amount

