# funclib.py
# function library

import math
import random

# Math function #

def math_abs(x):
    # abs(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.fabs(x)}
    else:
        return {'ERR': 'value error'}

def math_ceil(x):
    # ceil(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.ceil(x)}
    else:
        return {'ERR': 'value error'}

def math_cos(x):
    # cos(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.cos(x)}
    else:
        return {'ERR': 'value error'}

def math_exp(x):
    # exp(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.exp(x)}
    else:
        return {'ERR': 'value error'}

def math_floor(x):
    # floor(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.floor(x)}
    else:
        return {'ERR': 'value error'}

def math_round(x, n=None):
    # round(x, n)
    if isinstance(x, (int, float)) and (isinstance(n, int) or n == None):
        return {'NUM': round(x, n)}
    else:
        return {'ERR': 'value error'}

def sin(x):
    # sin(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.sin(x)}
    else:
        return {'ERR': 'value error'}

def sqrt(x):
    # sqrt(x)
    if isinstance(x, (int, float)) and x >= 0:
        return {'NUM': math.sqrt(x)}
    else:
        return {'ERR': 'value error'}

def tan(x):
    if isinstance(x, (int, float)):
        return {'NUM': math.tan(x)}
    else:
        return {'ERROR': 'value error'}
