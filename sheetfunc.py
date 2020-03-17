#sheet/sheetfunc.py

import cmath
import math

def average(seq):
    total = 0
    l = 0
    for x in seq:
        if x is not None:
            total += x
            l += 1
    return total / l

def choose(con, a, b):
    if con:
        return a
    return b

def cos(x):
    if isinstance(x, complex):
        return cmath.cos(x)
    math.cos(x)

def chooses(n, l):
    assert isinstance(l, list)
    if int(n) < 0:
        return l[0]
    elif int(n) > len(l):
        return l[-1]
    return l[int(n)]

def sin(x):
    if isinstance(x, complex):
        return cmath.sin(x)
    return math.sin(x)

def sum_(seq):
    total = 0
    for x in seq:
        if x is not None:
            total += x
    return total

