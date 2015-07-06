__author__ = 'roan'

'''
Delegating Iteration
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p02_delegating_iteration.html
'''

class Node(object):
    def __init__(self, value):
        self._value = value
        self._chidren = []

    def add_child(self, node):
        self._chidren.append(node)

    def __iter__(self):
        # delegates iteration to the internally held container, like '_children'
        return iter(self._chidren)

    def __repr__(self):
        return 'Node( {!r} )'.format(self._value)

    def __str__(self):
        return repr(self)

if __name__ == '__main__':
    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_2)

    for ch in root:
        print(str(ch))
