__author__ = 'root'
"""
http://wklken.me/posts/2012/10/27/python-base-decorator.html#python
"""

class Property():
    def __init__(self):
        self.__prop = 1

    @property
    def prop(self):
        result = self.__prop
        print("call get {0}".format(result))
        return result

    @prop.setter
    def prop(self, value):
        result = self.__prop = value
        print("call set {0}".format(result))

    @prop.deleter
    def prop(self):
        del self.__prop
        print("call del")


bbb = Property()
bbb.prop()
bbb.prop(2)
del bbb.prop
