__author__ = 'roan'

'''
Defining Generator Functions with Extra State
http://python3-cookbook.readthedocs.org/zh_CN/latest/c04/p06_define_generator_func_with_extra_state.html
'''

from collections import deque

# Double-Ended Queue: Deque

class linehistory(object):
    def __init__(self, lines, histlen=3):
        self._lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self._lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('/etc/hosts') as file:
    lines = linehistory(file)
    for line in lines:
        if ' ' in line:
            for lineno, hline in lines.history:
                print("{0} {1}".format(lineno, hline), end='')
