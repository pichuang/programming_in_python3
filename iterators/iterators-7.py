__author__ = 'roan'

'''
Taking a Slice of an Iterator
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p07_taking_slice_of_iterator.html
'''

def count(n):
    while True:
        yield n
        n += 1

c = count(0)

import itertools
# Slicing generator
for x in itertools.islice(c, 10, 30):
    print(x)