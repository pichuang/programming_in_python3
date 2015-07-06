__author__ = 'roan'

'''
Iterating in Reverse
http://chimera.labs.oreilly.com/books/1230000000393/ch04.html#_discussion_61
'''

class Countdown(object):
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        num = self._start
        while num > 0:
            yield num
            num -= 1

    # Customize reversed function
    def __reversed__(self):
        num = 1
        while num < self._start:
            yield num
            num += 1


for gg in Countdown(10):
    print(gg)

for reversed_gg in reversed(Countdown(10)):
    print(reversed_gg)
