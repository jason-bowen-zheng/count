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
    'f_max',
    'f_min',
    'f_oct',
    'f_round',
    'f_sin',
    'f_sum',
    'f_tan',
]

v_e = math.e
v_pi = math.pi
v_tau = math.tau

def f_abs(x):
    '''Math function
abs(x:ifc) => abs(x)
return the absolute value of x.
'''
    if instance(x, (int, float, complex)):
        return abs(x)
    else:
        raise TypeError

def f_all(seq):
    '''Logical function
all(seq:l) => b
return True if all value in seq is not None.
'''
    for i in seq:
        if not i:
            return False
    else:
        return True

def f_any(seq):
    '''Logical function
any(seq:l) => b
return True if one value in seq is not None.
'''
    for i in seq:
        if i:
            return True
    else:
        return False

def f_average(seq):
    '''Statistics function
average(seq:l) => f
return average number of seq.
'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return static.fmean(l)

def f_bin(n):
    '''Logical function
bin(n:i) => '0b...'
return the binary representation of n.
'''
    return bin(n)

def f_choose(con, a, b):
    '''Logical function
choose(con:b, a, b) => a or b
if con is True:
 return a
else:
 return b
'''
    if con:
        return a
    else:
        return b

def f_chooses(n, l):
    '''Logical function
chooses(n:i, l:l) => l[int(n)]
if n < 0 or n > length of l:
 return l[0] or l[-1]
else:
 return l[int(n)]
'''
    if  not instance(l, list):
        raise TypeError
    elif int(n) < 0:
        return l[0]
    elif int(n) > len(l):
        return l[-1]
    else:
        return l[int(n)]

def f_cos(x):
    '''Math function
cos(x:ifc) => fc
return the cos of x.
'''
    if isinstance(x, complex):
        return cmath.cos(x)
    elif isinstance(x, (int, float)):
        return math.cos(x)
    else:
        raise TypeError

def f_hex(n):
    '''Logical function
hex(n:i) => '0x...'
return the hexadecimal representation of n.
'''
    return hex(n)

def f_max(seq):
    '''Math function
max(seq:l) => if
return the maximum number in seq
'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return max(l)

def f_min(seq):
    '''Math function
min(seq:l) => if
return the minimum number in seq
'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return min(l)

def f_oct(n):
    '''Logical function
oct(n:i) => '0o...'
return the octal representation of n.
'''
    return oct(n)

def f_round(x, n=None):
    '''Math function
round(x:i, n:i=None) => (int, float)

'''
    return round(x, n)

def f_sin(x):
    '''Math function
sin(x:ifc) => fc
return the sin of x
'''
    if isinstance(x, complex):
        return cmath.sin(x)
    elif isinstance(x, (int, float)):
        return math.sin(x)
    else:
        raise TypeError

def f_sum(seq):
    '''Statistics function
sum(seq:l) => f
return sum of seq
'''
    total = 0
    for x in seq:
        if x:
            total += x
    else:
        return total

def f_tan(x):
    '''Math function
tan(x: ifc) => fc
return the tan of x
'''
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
    'max':      f_max,
    'min':      f_min,
    'oct':      f_oct,
    'round':    f_round,
    'sin':      f_sin,
    'sum':      f_sum,
    'tan':      f_tan,
}
