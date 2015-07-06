
__author__ = 'root'

"""
lambda

lamba parameters: expression
"""


elements = [(2, 4, "yy"), (4, 1, "xx"), (3, 3, "aa"), (1, 5, "gg")]

"""
Original
"""
elements.sort()
print("Original: {0}".format(elements))


"""
def sort_key(e):
    return e[1]. e[2]

same as

lambda e: (e[1], e[2])
"""


elements.sort(key=lambda e: (e[1], e[2]))
print("Use lambda: {0}".format(elements))

"""
Misc
"""
import collections
minus_one_dict = collections.defaultdict(lambda: -1)
point_zero_dict = collections.defaultdict(lambda: (0, 0))
message_dict = collections.defaultdict(lambda: "No message available")