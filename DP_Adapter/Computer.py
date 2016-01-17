class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer.'.format(self.name)

    def execute(self):
        return 'execute a program.'