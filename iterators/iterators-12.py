__author__ = 'roan'


'''
Iterating on Items in Separate Containers
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p12_iterate_on_items_in_separate_containers.html
'''

from itertools import chain
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']

# more elegant
for char in chain(a, b):
    print(char)


# Inefficent
for char in a + b:
    print(char)
