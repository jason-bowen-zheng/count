# funclib.py
# function library

import math
import random

# Math function #

def math_abs(x):
    # abs(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.fabs(x)]
    else:
        return ['ERR', 'value error']

def math_acos(x):
    # acos(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.acos(x)]
    else:
        return ['ERR', 'value error']

def math_asin(x):
    # asin(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.asin(x)]
    else:
        return ['ERR', 'value error']

def math_atan(x):
    # atan(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.atan(x)]
    else:
        return ['ERR', 'value error']

def math_atan2(y, x):
    # atan2(y, x)
    if isinstance(x, (int, float)) and isinstance(x, (int, float)):
        return ['NUM', math.atan2(y,x)]
    else:
        return ['ERR', 'value error']

def math_ceil(x):
    # ceil(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.ceil(x)]
    else:
        return ['ERR', 'value error']

def math_cos(x):
    # cos(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.cos(x)]
    else:
        return ['ERR', 'value error']

def math_degrees(x):
    # degrees(x)
    if isinstance(x, (int, float)):
        return ['NUM',  math.degrees(x)]
    else:
        return ['ERR',  'value error']

def math_exp(x):
    # exp(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.exp(x)]
    else:
        return ['ERR', 'value error']

def math_E():
    # E()
    return ['NUM', math.e]

def math_floor(x):
    # floor(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.floor(x)]
    else:
        return ['ERR', 'value error']

def math_mod(x, y):
    # mod(x, y)
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return ['NUM', math.fmod(x, y)]
    else:
        return ['ERR', 'value error']

def math_pow(x, y):
    # pow(x, y)
    if isinstance(x, (int, float)) and isinstance(x, (int, float)):
        return ['NUM', math.pow(x, y)]
    else:
        return ['ERR', 'value error']

def math_PI():
    # PI()
    return ['NUM', math.pi]

def math_radians(x):
    # radians(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.radians(x)]
    else:
        return ['ERR', 'value error']

def math_rand():
    # rand()
    return ['NUM', random.random()]

def math_round(x, n=None):
    # round(x, n)
    if isinstance(x, (int, float)) and (isinstance(n, int) or (n == None)):
        return ['NUM', round(x, n)]
    else:
        return ['ERR', 'value error']

def math_sin(x):
    # sin(x)
    if isinstance(x, (int, float)):
        return ['NUM', math.sin(x)]
    else:
        return ['ERR', 'value error']

def math_sqrt(x):
    # sqrt(x)
    if isinstance(x, (int, float)) and (x >= 0):
        return ['NUM', math.sqrt(x)]
    else:
        return ['ERR', 'value error']

def math_tan(x):
    if isinstance(x, (int, float)):
        return ['NUM', math.tan(x)]
    else:
        return ['ERROR', 'value error']

def math_TAU():
    # TAU()
    # PI is wrong, use TAU!
    return ['NUM', math.tau]

# Str function #

def str_formatText(text, *value):
    # text%value
    try:
        return ['STR': text%value]
    except:
        return ['ERR': 'argument error']
    else:
        pass

def str_slice(s, start=None, end=None):
    # s[start:end]
    try:
        return ['STR', s[start:end]]
    except:
        return ['ERR', 'index error']
    else:
        pass

# Run function #

def run_function(fname, *args):
    # fname(*args)
    try:
        # Math function #
        if fname == 'abs':
            return math_abs(*args)
        elif fname == 'acos':
            return math_acos(*args)
        elif fname == 'asin':
            return math_asin(*args)
        elif fname == 'atan':
            return math_atan(*args)
        elif fname == 'atan2':
            return math_atan2(*args)
        elif fname == 'ceil':
            return math_ceil(*args)
        elif fname == 'cos':
            return math_cos(*args)
        elif fname == 'exp':
            return math_exp(*args)
        elif fname == 'E':
            return math_E(*args)
        elif fname == 'degrees':
            return math_degrees(*arg)
        elif fname == 'floor':
            return math_floor(*args)
        elif fname == 'mod':
            return math_mod(*args)
        elif fname == 'pow':
            return math_pow(*args)
        elif fname == 'PI':
            return math_PI(*args)
        elif fname == 'radians':
            return math_radians(*args)
        elif fname == 'rand':
            return math_rand(*args)
        elif fname == 'round':
            return math_round(*args)
        elif fname == 'sin':
            return math_sin(*args)
        elif fname == 'sqrt':
            return math_sqrt(*args)
        elif fname == 'tan':
            return math_tan(*args)
        elif fname == 'TAU':
            return math_TAU(*args)
        # Str function #
        elif fname == 'formatText':
            return str_formatText(*args)
        elif fname == 'slice':
            return str_slice(*args)
        else:
            return ['ERR', 'function not found']
    except:
        return ['ERR', 'argument error']
