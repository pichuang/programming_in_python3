__author__ = 'root'

"""
http://www.wklken.me/posts/2013/12/22/difference-between-staticmethod-and-classmethod-in-python.html
http://wklken.me/posts/2012/10/27/python-base-decorator.html
"""

class zoo():
    zoo = "zoo"

    @classmethod
    def foo(cls, name):
        print("hi! {0}. it's classmethod.\n zoo={1}".format(name, cls.zoo))

    @staticmethod
    def bar(name):
        print("hi! {0}. it's staticmethod.\n zoo={1}".format(name, zoo.zoo))

    def normal_method(self):
        print("hi! it's normal method.\n zoo={0}".format(self.zoo))


zoo.foo("mission")
zoo.bar("mission")
zoo.normal_method(zoo)


class Fruit(object):
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print("calling class_method({0}, {1})".format(cls, value))

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

print("\nCreate apple 1")
apple_1 = Apple()

print("\nSet apple 1")
apple_1.set(200)

print("\nCreate apple 2")
apple_2 = Apple()

print("\nCreate orange 1")
orange_1 = Orange()

print("\nSet orange 1")
orange_1.set(300)

print("\nCreate orange 2")
orange_2 = Orange()

print("\nprint apple 1")
apple_1.print_total()

print("\nprint orange 1")
orange_1.print_total()

