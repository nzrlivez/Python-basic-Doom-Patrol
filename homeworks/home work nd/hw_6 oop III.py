# HW 6

import random
import uuid
from abc import abstractmethod, ABC
from random import random, randint, choice


class Animal(ABC):
    types = ("Predator", "Herbivores")

    def __init__(self, power, speed, max_power):
        self.max_power = max_power
        self.id = str(uuid.uuid4())
        self.power = power
        self.current_power = power
        self.speed = speed
        self.is_out_of_power = False

    def eat(self, power):
        self.current_power += power \
            if self.current_power + power <= self.max_power else self.max_power

    def waist_power(self, power):
        self.current_power -= power
        if self.current_power <= 0:
            self.is_out_of_power = True

    @abstractmethod
    def get_name(self):
        pass

    def get_animal_info(self):
        return self.get_name() + "\t" + str(self.id)


class Predator(Animal, ABC):
    def get_name(self):
        return self.types[0]


class Herbivores(Animal):

    def eat(self, forest):
        print(f"now {self, name}'s power: {self.current_power} points")
        if self.current_power > 0.5 * self.power:
            self.current_power = self, max_power
        else:
            self.current_power += 0.5 * self.power
        print(f'{self, name} eats...')
        print(f"now {self, name}'s power: {self.current_power} points")
        print('\n')


class Forest:

    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal):
        del self.animals[animal.id]

    def get_animals_count(self):
        return len(self.animals)

    @property
    def is_hunting_possible(self):
        if self.get_animals_count() <= 1:
            return False
        return True

    def get_animal(self, hunter_id=None):

        if not isinstance(hunter_id, type(None)):
            key_list = list(key for key in self.animals.keys()
                            if key != hunter_id)
        else:
            key_list = list(self.animals.keys())

        animal_key = random.choice(key_list)
        return self.animals[animal_key]

    @staticmethod
    def print_animal_list():

        for animal in my_forest.animals.keys():
            print(my_forest.animals[animal].get_animal_info())

    def any_predator_left(self):

        for key in self.animals.keys():
            if isinstance(self.animals[key], Predator):
                return True
        print("no more predators in the forest.")
        return False

    def start_hunting(self):
        hunter = Forest.get_animal(self)

        if isinstance(hunter, Herbivorous):
            hunter.eat(50)

        # hunter is Predator, try to catch some victim
        victim = Forest.get_animal(self, hunter.id)

        if hunter.speed > victim.speed and \
                hunter.current_power > victim.current_power:
            hunter.eat(50)
            # hunter's power +50%, victim - dead
            victim.is_out_of_power = True
        else:
            hunter.waist_power(30)
            victim.waist_power(30)

        # checking who's out of power and get rid of such animal
        if hunter.is_out_of_power:
            self.remove_animal(hunter)

        if victim.is_out_of_power:
            self.remove_animal(victim)


def animal_generator(value):
    wolf = Predator('wolf', randint(25, 100), randint(25, 100))
    bear = Predator('bear', randint(25, 100), randint(25, 100))
    fox = Predator('fox', randint(25, 100), randint(25, 100))
    lynx = Predator('fox', randint(25, 100), randint(25, 100))
    snake = Predator('snake', randint(25, 100), randint(25, 100))
    bunny = Herbivores('bunny', randint(25, 100), randint(25, 100))
    squirrel = Herbivores('squirrel', randint(25, 100), randint(25, 100))
    mouse = Herbivores('mouse', randint(25, 100), randint(25, 100))
    dear = Herbivores('moose', randint(25, 100), randint(25, 100))
    boar = Herbivores('beaver', randint(25, 100), randint(25, 100))
    while value >= 0:
        value -= 1
        yield choice([wolf, bear, fox, lynx, bunny, squirrel, snake, mouse, dear, boar])


if __name__ == "__main__":
    nature = animal_generator(30)

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while forest.any_predator_left():
        for animal in forest:
            animal.eat(forest=forest)
            forest.number = 1
