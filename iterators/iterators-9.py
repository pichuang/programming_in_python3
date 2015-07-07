__author__ = 'roan'

'''
Iterating Over All Possible Combinations or Permutations
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p09_iterate_over_combination_or_permutation.html
'''

print("Permutations")
items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)
print("=" * 100)

for p in permutations(items, 2):
    print(p)
print("=" * 100)


print("Combination")
from itertools import combinations
for p in combinations(items, 3):
    print(p)
print("=" * 100)

for p in combinations(items, 2):
    print(p)
print("=" * 100)

for p in combinations(items, 1):
    print(p)
print("=" * 100)


print("Combination with replacement")
from itertools import combinations_with_replacement
for p in combinations_with_replacement(items, 3):
    print(p)
print("=" * 100)
