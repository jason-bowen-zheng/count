#sheet/sheetfuncion.py

import cmath
import math

def abs_(x):
    """math function
    abs(x: (int, float, complex)) => abs(x)
    return the absolute value of x.
    """
    if instance(x, (int, float, complex)):
        return abs(x)
    else:
        raise TypeError

def all_(seq):
    """logic function
    all(seq: list) => bool
    return True if all value in seq is not None.
    """
    for i in seq:
        if not i:
            return False
    else:
        return True

def any_(seq):
    """logic function
    any(seq: list) => bool
    return True if one value in seq is not None.
    """
    for i in seq:
        if i:
            return True
    else:
        return False

def average(seq):
    """statistics function
    average(seq: list) => float
    return average number of seq.
    """
    total, l = 0, 0
    for x in seq:
        if x is not None:
            total += x
            l += 1
    else:
        return total / l

def choose(con, a, b):
    """logic function
    choose(con: bool, a, b) => a or b
    if con is True:
     return a
    else:
     return b
    """
    if con:
        return a
    else:
        return b

def chooses(n, l):
    """logic function
    chooses(n: int, l: list) => l[int(n)]
    if n < 0 or n > length of l:
     return l[0] or l[-1]
    else:
     return l[int(n)]
    """
    if  not instance(l, list):
        raise TypeError
    elif int(n) < 0:
        return l[0]
    elif int(n) > len(l):
        return l[-1]
    else:
        return l[int(n)]

def cos(x):
    """math function
    cos(x: (int, float, complex)) => (float, complex)
    """
    if isinstance(x, complex):
        return cmath.cos(x)
    elif isinstance(x, (int, float)):
        return math.cos(x)
    else:
        raise TypeError

def sin(x):
    """math function
    sin(x: (int, float, complex)) => (float, complex)
    """
    if isinstance(x, complex):
        return cmath.sin(x)
    elif isinstance(x, (int, float)):
        return math.sin(x)
    else:
        raise TypeError

def sum_(seq):
    """statistics function
    sum(seq: list) => float
    return sum of seq
    """
    total = 0
    for x in seq:
        if x is not None:
            total += x
    else:
        return total

def tan(x):
    """"math function
    tan(x: (int, float, complex)) => (float, complex)
    """
    if isinstance(x, complex):
        return cmath.tan(x)
    elif isinstance(x, (int, foat)):
        return math.tan(x)
    else:
        raise TypeError

functions = {
    'abs': abs_,
    'all': all_,
    'any': any_,
    'average': average,
    'choose': choose,
    'chooses': chooses,
    'cos': cos,
    'sin': sin,
    'sum': sum_,
    'tan': tan
}
