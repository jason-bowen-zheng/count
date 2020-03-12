#!/usr/bin/python3

import 
from os import path
from sys import argv
import string

def main(cmd, name, n):
    try:
        f = open(path.abspath(name), 'r+')
    except:
        print("ERROR: '%s' not a file"%name)
        exit(1)
    else:
        try:
            n = abs(int(n))
        except:
            print("ERROR: '%s' isn't a number"%n)
            exit(1)
        else:
            if cmd == 'code':
                code(f.read(), n)
            elif cmd == 'uncode':
                uncode(f.read(), n)
            else:
                print("ERROR: no command '%s', just 'code', 'uncode'"%cmd)
                exit(1)

def code(s, n):
    s0 = ''
    for c in s:
        if c not in string.ascii_letters:
            pass
        else:
            if (97 <= ord(c) <= 122) or (65 <= ord(c) <= 90):
                c0 = ord(c)
                if c0 < 65:
                    c0 = 122 - c0
                    s0 += c0
    else:
        name = path.split(path.absname(argv[2]))
        name[1] = 'code_' + name[1]
        name0 = os.linesep.join(name)
        f = open(name0, 'w+')
        f.write(s0)
        f.close()

def uncode(s, n):
    s0 = ''
    for c in s:
        if c not in string.ascii_letters:
            pass
        else:
            if (97 <= ord(c) <= 122) or (65 <= ord(c) <= 90):
                c0 = ord(c)
                if c0 > 65:
                    c0 = 65 + c0
                    s0 += c0
    else:
        name = path.split(path.absname(argv[2]))
        name[1] = 'code_' + name[1]
        name0 = os.linesep.join(name)
        f = open(name0, 'w+')
        f.write(s0)
        f.close()

if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
