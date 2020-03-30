# xSheets/functionlib/textfunction.py

def text_cat(*seq):
    '''Text function
str
cat(*seq)
concatenate the given string.'''
    string = ''
    for x in seq[:-1]:
        if x :
            string += str(x) + ' '
    else:
        string += str(seq[-1])
        return string
    

def text_format(s, *formatlist):
    '''Text function
str; list
format(s, formatlist)
return s % formatlist.'''
    return s % tuple(formatlist)

def text_find(s, start=None, end=None):
    '''Text function
str; int; int
find(s,start=None, end=None)
return the lowest index in s where substring sub is found,
such that sub is contained within s[start:end].
    
return -1 on failure.'''
    return s.find(start, end)

def text_lower(s):
    '''Text function
str
upper(s)
return lowercase of s.'''
    return s.lower()

def text_repeat(s, n):
    '''Text function
str; int
repeat(s, n)
repeat s for n times.'''
    return str(s) * n

def text_replace(s, old, new, count=-1):
    '''Text function
str; str; str; int
replace(s, old, new, count=-1)
replace the old part of s as new count times.'''
    return s.replace(old, new, count)

def text_slice(s, start=None, end=None, step=None):
    '''Text function
str; int; int
slice(s, start=None, end=None, step=None)
return s[start:end:step].'''
    return s[start:end:step]

def text_upper(s):
    '''Text function
str
upper(s)
return uppercase of s.'''
    return s.upper()

functions = {
    'cat':          text_cat,
    'format':       text_format,
    'find':         text_find,
    'lower':        text_lower,
    'repeat':       text_repeat,
    'replace':      text_replace,
    'slice':        text_slice,
    'upper':        text_upper
    }
