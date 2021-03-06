__author__ = 'roan'

'''
Skipping the First Part of an Iterable
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p08_skip_first_part_of_iterable.html
'''

'''
Print all content
'''
with open("/etc/hosts") as file:
    try:
        while True:
            line = next(file)
            if line is None:
                break
            print(line, end='')
    except StopIteration:
        pass


'''
Use itertools, skip all '#' words
'''
print("=" * 100)
from itertools import dropwhile
with open("/etc/hosts") as file:
    for line in dropwhile(lambda line: line.startswith('#'), file):
        print(line, end='')

'''
Messy code
'''
print("=" * 100)
with open("/etc/hosts") as file:
    while True:
        line = next(file)
        if not line.startswith('#'):
            break
    while line:
        print(line, end='')
        line = next(file, None)

