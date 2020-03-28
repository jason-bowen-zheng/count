# xSheets/functionlib/textfunction.py

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

def text_upper(s):
    '''Text function
str
upper(s)
return uppercase of s.'''
    return s.upper()

functions = {
    'find':     text_find,
    'lower':    text_lower,
    'upper':    text_upper
    }
