#!/usr/bin/env python3
'''
Research counter
'''

'''
Use dict()
'''
data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_freq = dict()
for item in data:
    if item in count_freq:
        count_freq[item] += 1
    else:
        count_freq[item] = 1

print(count_freq)

'''
Use defaultdict
'''
from collections import defaultdict
data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_freq = defaultdict(int)
for item in data:
    count_freq[item] += 1
print(count_freq)

'''
Use set and list
'''
data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_set = set(data)
count_list = []
for item in count_set:
    count_list.append((item, data.count(item)))
print(count_list)

'''
Use Collections Counter
'''
from collections import Counter
data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
print(Counter(data))
