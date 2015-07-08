__author__ = 'root'

'''
Iterating in Sorted Order Over Merged Sorted Iterable
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p15_iterate_in_sorted_order_over_merged_sorted_iterables.html
'''

import heapq

a = [1, 3, 5, 7, 9, 12]
b = [2, 4, 6, 8, 10, 11]

for i in heapq.merge(a, b):
    print(i)


'''
Merge two files
'''

with open('/etc/hosts', 'rt') as file1, open('/etc/passwd', 'rt') as file2, open('/tmp/mergefile', 'wt') as output:
    for line in heapq.merge(file1, file2):
        output.write(line)
