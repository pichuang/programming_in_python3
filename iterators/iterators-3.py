__author__ = 'roan'

'''
Creating New Iteration Patterns with Generators
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p03_create_new_iteration_with_generators.html
'''

def frange(start, stop, interval):
    x = start
    while x < stop:
        yield x  # Generator
        x += interval



for i in frange(1, 3, 1):
    print(i)
