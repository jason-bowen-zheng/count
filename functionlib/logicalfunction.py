# sheet/functionlib/logicalfunction

def logical_all(seq):
    '''Logical function
list
all(seq) => boolean
return True if all value in seq is not None.'''
    for i in seq:
        if not i:
            return False
    else:
        return True

def logical_any(seq):
    '''Logical function
list
any(seq) => boolean
return True if one value in seq is not None.'''
    for i in seq:
        if i:
            return True
    else:
        return False

def logical_bin(n):
    '''Logical function
int
bin(n) => '0b...'
return the binary representation of n.'''
    return bin(n)

def logical_choose(con, a, b):
    '''Logical function
boolean; boolean; boolean
choose(con, a, b) => a or b
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
chooses(n, l) => l[int(n)]
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

def logical_hex(n):
    '''Logical function
int
hex(n) => '0x...'
return the hexadecimal representation of n.'''
    return hex(n)

def logical_oct(n):
    '''Logical function
int
oct(n) => '0o...'
return the octal representation of n.'''
    return oct(n)

functions = {
    'all':      logical_all,
    'any':      logical_any,
    'bin':      logical_bin,
    'choose':   logical_choose,
    'chooses':  logical_chooses,
    'hex':      logical_hex,
    'oct':      logical_oct
    }
