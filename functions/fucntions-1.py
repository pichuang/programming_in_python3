#!/usr/bin/env python3

'''
Sample
'''
def anyone(*args, **kwargs):
    print(args)  # Tuple
    print(kwargs)  # Dict

def avg(first, *rest):
    return (first + sum(rest) / (1 + len(rest)))

avg(1, 2)
avg(1, 2, 3, 4)
