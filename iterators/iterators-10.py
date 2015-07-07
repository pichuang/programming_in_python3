__author__ = 'roan'


'''
Iterating Over the Index-Value Pairs of a Sequence
http://chimera.labs.oreilly.com/books/1230000000393/ch04.html#_solution_65
'''

my_list = ['a', 'b', 'c']

for index, value in enumerate(my_list):
    print("{0}:{1}".format(index, value))


print("=" * 100)
'''
typically start number
'''
for index, value in enumerate(my_list, 1):
    print("{0}:{1}".format(index, value))


print("=" * 100)
data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for index, (x, y) in enumerate(data, 1):  # Wrong: for index, x, y in enumerate(data)
    print("{0}: ({1}, {2})".format(index, x, y))


print("=" * 100)
from collections import defaultdict
word_summary = defaultdict(list)
with open("/etc/hosts", "r") as file:
    lines = file.readline()

for index, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[index].append(word)

print(word_summary.items())
