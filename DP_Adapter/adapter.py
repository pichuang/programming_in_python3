class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Adpater(object):
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


def main():
    objects = []
    dog = Dog()
    objects.append(Adpater(dog, make_noise=dog.bark))
    print(objects[0].__dict__)
    print(objects[0].original_dict())


if __name__ == "__main__":
    main()
