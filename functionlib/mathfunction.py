# sheet/functionlib/mathfunction.py

import cmath
import math

def math_abs(x):
    '''Math function
int, float, complex
abs(x) => abs(x)
return the absolute value of x.'''
    if instance(x, (int, float, complex)):
        return abs(x)
    else:
        raise TypeError

def math_cos(x):
    '''Math function
int, float, complex
cos(x) => cos(x)
return the cos of x.'''
    if isinstance(x, complex):
        return cmath.cos(x)
    elif isinstance(x, (int, float)):
        return math.cos(x)
    else:
        raise TypeError

def math_max(seq):
    '''Math function
list
max(seq) => int,float
return the maximum number in seq.'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return max(l)

def math_min(seq):
    '''Math function
list
min(seq) => int, float
return the minimum number in seq.'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return min(l)

def math_pi():
    '''Math function
None
pi() => 3.14...
return PI.'''
    return math.pi

def math_round(x, n=None):
    '''Math function
int, float; int
round(x, n=None) => int, float
round a number to a given precision in decimal digits.
'''
    return round(x, n)

def math_sin(x):
    '''Math function
int, float, complex
sin(x) => sin(x)
return the sin of x.'''
    if isinstance(x, complex):
        return cmath.sin(x)
    elif isinstance(x, (int, float)):
        return math.sin(x)
    else:
        raise TypeError

def math_tan(x):
    '''Math function
int, float, complex
tan(x) => tan(x)
return the tan of x'''
    if isinstance(x, complex):
        return cmath.tan(x)
    elif isinstance(x, (int, foat)):
        return math.tan(x)
    else:
        raise TypeError

def math_tau():
    '''Math function
None
tau() => 6.28...
return TAU.'''
    return math.tau

functions = {
    'cos':      math_cos,
    'max':      math_max,
    'min':      math_min,
    'pi':       math_pi,
    'round':    math_round,
    'sin':      math_sin,
    'tan':      math_tan,
    'tau':      math_tau
}
