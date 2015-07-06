#!/usr/bin/env python3
'''
Research yield
http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
'''

import time
import logging


NUMBER = 10000

'''
Log handle
'''
# Add logger
logger = logging.getLogger('fab')
logger.setLevel(logging.DEBUG)

# Add file log
fh = logging.FileHandler('fab.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# Add console debug
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)

'''
Level 1
'''
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

start = time.time()
fab(NUMBER)
stop = time.time()
logger.info("Level {0}: {1}".format(1, stop - start))

'''
Level 2
'''
def fab(max):
    n, a, b = 0, 0, 1
    fab_list = []
    while n < max:
        fab_list.append(b)
        a, b = b, a + b
        n = n + 1
    return fab_list


start = time.time()
for i in fab(NUMBER):
    print(i)
stop = time.time()
logger.info("Level {0}: {1}".format(2, stop - start))

'''
Level 3
'''
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return result
        raise StopIteration()

start = time.time()
for i in Fab(NUMBER):
    print(i)
stop = time.time()
logger.info("Level {0}: {1}".format(3, stop - start))


'''
Level 4
'''
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

start = time.time()
for i in fab(NUMBER):
    print(i)
stop = time.time()
logger.info("Level {0}: {1}".format(4, stop - start))

