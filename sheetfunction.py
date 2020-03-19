#sheet/sheetfuncion.py

import cmath
import math
import statistics as static

__all__ = [
    'f_abs',
    'f_all',
    'f_any',
    'f_average',
    'f_bin',
    'f_choose',
    'f_chooses',
    'f_cos',
    'f_hex',
    'f_oct',
    'f_sin',
    'f_sum',
    'f_tan',
    'v_e',
    'v_pi',
    'v_tau'
]

v_e = math.e
v_pi = math.pi
v_tau = math.tau

def f_abs(x):
    """math function
abs(x: (int, float, complex)) => abs(x)
return the absolute value of x.
"""
    if instance(x, (int, float, complex)):
        return abs(x)
    else:
        raise TypeError

def f_all(seq):
    """logical function
all(seq: list) => bool
return True if all value in seq is not None.
"""
    for i in seq:
        if not i:
            return False
    else:
        return True

def f_any(seq):
    """logical function
any(seq: list) => bool
return True if one value in seq is not None.
"""
    for i in seq:
        if i:
            return True
    else:
        return False

def f_average(seq):
    """statistics function
average(seq: list) => float
return average number of seq.
"""
    l = []
    for x in seq:
        if x is not None:
            l.append(x)
    else:
        return static.fmean(l)

def f_bin(n):
    """logical function
bin(n: int) => '0b...'
return the binary representation of n.
"""
    return bin(n)

def f_choose(con, a, b):
    """logical function
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

def f_chooses(n, l):
    """logical function
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

def f_cos(x):
    """math function
cos(x: (int, float, complex)) => (float, complex)
return the cos of x.
"""
    if isinstance(x, complex):
        return cmath.cos(x)
    elif isinstance(x, (int, float)):
        return math.cos(x)
    else:
        raise TypeError

def f_hex(n):
    """logical function
hex(n: int) => '0x...'
return the hexadecimal representation of n.
"""
    return hex(n)

def f_oct(n):
    """logical function
oct(n: int) => '0o...'
return the octal representation of n.
    """
    return oct(n)

def f_sin(x):
    """math function
sin(x: (int, float, complex)) => (float, complex)
return the sin of x
"""
    if isinstance(x, complex):
        return cmath.sin(x)
    elif isinstance(x, (int, float)):
        return math.sin(x)
    else:
        raise TypeError

def f_sum(seq):
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

def f_tan(x):
    """"math function
tan(x: (int, float, complex)) => (float, complex)
return the tan of x
"""
    if isinstance(x, complex):
        return cmath.tan(x)
    elif isinstance(x, (int, foat)):
        return math.tan(x)
    else:
        raise TypeError

functions = {
    'abs':      f_abs,
    'all':      f_all,
    'any':      f_any,
    'average':  f_average,
    'bin':      f_bin,
    'choose':   f_choose,
    'chooses':  f_chooses,
    'cos':      f_cos,
    'hex':      f_hex,
    'oct':      f_oct,
    'sin':      f_sin,
    'sum':      f_sum,
    'tan':      f_tan,
    ####################
    'E':        v_e,
    'PI':       v_pi,
    'TAU':      v_tau
}
