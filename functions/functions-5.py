#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'root'


def spam(a, b=42):
    print(a, b)

spam(1, 2)  # a=1 b=2
spam(1)  # a=1 b=42

# Using a list as a default value
def default_spam(a, b=None):
    if b is None:
        b = []


# Send object to function
# Recommand use
_no_value = object()

def no_value(a, b=_no_value):
    if b is _no_value:
        print("No b value supplied")

spam(1)  # No b value supplied
spam(1, 2)  # b=2
spam(1, None)  # b=None

# def no_use(a, b=[]):  # DONT DO THAT

