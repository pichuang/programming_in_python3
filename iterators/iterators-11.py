__author__ = 'roan'



'''
Iterating Over Multiple Sequences Simultaneously
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p11_iterate_over_multiple_sequences_simultaneously.html
'''


'''
By default, the length of the iterators is same as the length of the shortest list
'''
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99, 100]
for x, y in zip(xpts, ypts):
    print(x, y)
    # Miss '100' in ypts

'''
Choose longest
'''
print("=" * 100)
from itertools import zip_longest
for x, y in zip_longest(xpts, ypts):
    print(x, y)

'''
Change to dictionary
'''
print("=" * 100)
zip_dictionary = dict(zip_longest(xpts, ypts))
print(zip_dictionary.items())

'''
Change to list
'''
zip_list = list(zip_longest(xpts, ypts))
print(zip_list)