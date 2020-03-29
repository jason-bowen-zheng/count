# xSheets/functionlib/logicalfunction
# logical function

import random

def logical_all(seq):
    '''Logical function
list
all(seq)
return True if all value in seq is not None.'''
    for i in seq:
        if not i:
            return False
    else:
        return True

def logical_any(seq):
    '''Logical function
list
any(seq)
return True if one value in seq is not None.'''
    for i in seq:
        if i:
            return True
    else:
        return False

def logical_bin(n):
    '''Logical function
int
bin(n)
return the binary representation of n.'''
    return bin(n)

def logical_choose(con, a, b):
    '''Logical function
boolean; boolean; boolean
choose(con, a, b)
if con is True:
 return a
else:
 return b'''
    if con:
        return a
    else:
        return b

def logical_chooses(n, l):
    '''Logical function
int; list
chooses(n, l)
if n < 0 or n > length of l:
 return l[0] or l[-1]
else:
 return l[int(n)]'''
    if  not instance(l, list):
        raise TypeError
    elif int(n) < 0:
        return l[0]
    elif int(n) > len(l):
        return l[-1]
    else:
        return l[int(n)]

def logical_count(seq):
    '''Logical function
list
count(seq)
return the number of not null cells.'''
    count = 0
    for x in seq:
        if isinstance(x, (int, float, complex)):
            count += 1
    else:
        return count

def logical_false():
    '''Logical function
None
false()
return boolean False.'''
    return False

def logical_hex(n):
    '''Logical function
int
hex(n)
return the hexadecimal representation of n.'''
    return hex(n)

def logical_not(n):
    '''Logical function
boolean
not(n)
return true when n = false,
return false when n = true.'''
    return not n

def logical_oct(n):
    '''Logical function
int
oct(n)
return the octal representation of n.'''
    return oct(n)

def logical_rand():
    '''Logical function
None
rand()
return a random number.'''
    return random.random()

def logical_randint(a, b):
    '''Logical function
int; int
randint(a, b)
return a random number between a and b.'''
    return random.randint(a, b)

def logical_roman2int(roman):
    '''Logical function
str
roman2int(roman)
covered roman number to integer.
'''
    roman = roman.upper()
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    place = 0
    while place < len(roman):
        if (place + 1 < len(roman)) and (vals[roman[place]] < vals[roman[place + 1]]):
            total += vals[roman[place + 1]] - vals[roman[place]]
            place += 2
        else:
            total += vals[roman[place]]
            place += 1
    else:
        return total

def logical_true():
    '''Logical function
None
true()
return boolean True.'''
    return True

functions = {
    'all':          logical_all,
    'any':          logical_any,
    'bin':          logical_bin,
    'choose':       logical_choose,
    'chooses':      logical_chooses,
    'count':        logical_count,
    'false':        logical_false,
    'hex':          logical_hex,
    'not':          logical_not,
    'oct':          logical_oct,
    'rand':         logical_rand,
    'randint':      logical_randint,
    'roman2int':    logical_roman2int,
    'true':         logical_true
    }
