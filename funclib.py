# funclib.py
# function library

import math

# Math function #

def abs(x):
    # abs(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.fabs(x)}
    else:
        return {'ERR': 'value error'}

def ceil(x):
    # ceil(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.ceil(x)}
    else:
        return {'ERR': 'value error'}

def exp(x):
    # exp(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.exp(x)}
    else:
        return {'ERR': 'value error'}

def floor(x):
    # floor(x)
    if isinstance(x, (int, float)):
        return {'NUM': math.floor(x)}
    else:
        return {'ERR': 'value error'}

def sqrt(x):
    # sqrt(x)
    if isinstance(x, (int, float)) and x >= 0:
        return {'NUM': math.sqrt(x)}
    else:
        return {'ERR': 'value error'}
