#!/usr/bin/env python
import types


class Strategy(object):
    def __init__(self, func=None):
        self.name = 'Level 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)

def execute_replacement_execute_1(self):
    print("{} from execute 1".format(self.name))

def execute_replacement_execute_2(self):
    print("{} from execute 2".format(self.name))