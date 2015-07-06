__author__ = 'root'

"""
http://www.wklken.me/posts/2013/12/22/difference-between-staticmethod-and-classmethod-in-python.html
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

