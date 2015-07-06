__author__ = 'roan'

"""
Manually Consuming an Iterator
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p01_manually_consuming_iterator.html
"""

def manual_iter():
    with open("/etc/hosts") as file:
        try:
            while True:
                line = next(file)
                print(line, end='')
        except StopIteration:
            pass

def manual_iter1():
    with open("/etc/hosts") as file:
        try:
            while True:
                line = next(file)
                if line is None:
                    break
                print(line, end='')
        except StopIteration:
            pass