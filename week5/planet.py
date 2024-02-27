from week5.living_thing import LivingThing


class Planet:
    def __init__(self, name=""):
        self.__name = name
        self.__living_things= []

    def __repr__(self):
        return f'Planet(name={self.__name}, population={self.population()})'

    def __str__(self):
        return f'Planet: {self.__name}, Population: {self.population()}'

    def add(self, living_thing):
        if isinstance(living_thing, LivingThing):
            self.__living_things.append(living_thing)
            return True
        return False

    def remove(self, living_thing):
        if living_thing in self.__living_things:
            self.__living_things.remove(living_thing)
            return True
        return False

    def has(self, living_thing):
        return living_thing in self.__living_things

    def population(self):
        return len(self.__living_things)