__author__ = 'root'

"""
P249
"""
class FuzzyBool:

    def __init__(self, value=0.0):
        self.__value = value if 0.0 <= vlaue <= 1.0 else 0.0

    def __invert__(self):
        # Revert number
        return FuzzyBool(1.0 - self.__value)

    def __and__(self, other):
        # And number
        return FuzzyBool(min(self.__value, other.__value))

    def __iand__(self, other):
        # In-place Override value
        self.__value = min(self.__value, other.__value)
        return self

