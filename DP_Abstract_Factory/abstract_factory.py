#!/usr/bin/env python
"""
https://github.com/faif/python-patterns

Implementation of the abstract factory pattern

"""

import random


# pylint: disable=R0201
class Cat(object):
    def speak(self):
        return "Meow"

    def __str__(self):
        return "Cat"


class CatFactory(object):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


class Dog(object):
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


def get_factory():
    return random.choice([DogFactory(), CatFactory()])
    # return DogFactory()


class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))


if __name__ == "__main__":
    for _ in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("#" * 100)
