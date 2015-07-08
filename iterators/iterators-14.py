__author__ = 'root'

'''
Flattening a Nested Sequence
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p14_flattening_nested_sequence.html
'''

from collections import Iterable

def flatten(items, ignore_types=(bytes, str)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            # print("iterable")
            yield from flatten(x)
        else:
            # print("Not iterable")
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]  # Produces 1 2 3 4 5 6 7 8

for items in flatten(items):
    print(items)