#!/usr/bin/env python3

"""
Writing functions that only accept keyword argument
"""


def recv(maxsize, *, block):
    #  Recv a mesg
    pass

recv(1024, True)  # TypeError
recv(1024, block=True)  # Correct


def mininum(*values, clip=None):
    m = min(values)
    # Handle clip argument
    if clip is not None:
        m = clip if clip > m else m
    return m

mininum(1, 5, 2, -5, 10)  # Return -5
mininum(1, 5, 2, -5, 10, clip=0)  # Return 0




