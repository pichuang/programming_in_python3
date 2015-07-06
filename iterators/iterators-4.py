__author__ = 'roan'

'''
Implementing the Iterator Protocol
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p04_implement_iterator_protocol.html
'''

'''
DFS
'''

class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def __str__(self):
        return repr(self)

    def add_child(self, node):
        self._children.append(node)

    def depth_first(self):
        '''
        return DepthFirstIterator(self)
        '''
        yield self
        for c in self:
            yield from c.depth_first()


class DepthFirstIterator(object):
    '''
    Depth-First traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_tier = None
        self._child_tier = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_tier is None:
            self._children_tier = iter(self._node)
            return self._node
        elif self._child_tier:
            try:
                nextchild = next(self._child_tier)
                return nextchild
            except StopIteration:
                self._child_tier = None
                return next(self)
        else:
            self._child_tier = next(self._children_tier).depth_first()
            return next(self)

if __name__ ==  "__main__":
    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)

    root.add_child(child_1)
    root.add_child(child_2)

    child_1.add_child(Node(3))
    child_2.add_child(Node(4))

    for ch in root.depth_first():
        print(ch)
