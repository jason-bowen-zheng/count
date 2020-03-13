#!/usr/bin/python3
# count v3.0
# Now it's 2020/3/12 14:05
# Copyright (c) 2019-2020 jason-bowen-zheng
#  All Right Reserved
# All sources code can find on the website
#  http://github.com/jason-bowen-zheng/data/count
# License is GPLv3
####################

try:
    import colorama as color
except ModuleNotFoundError:
    print("ERROR: No 'colorama' packages!")
    print("Use 'pip install colorama' to install.")
    exit(1)
import os
import statistics as static
from sys import argv, platform, version_info

description = 'a little database'
name = 'data'
ver = (3, 0, 0)

####################

if version_info[:2] >= (3, 8):
    if not platform.startswith('win'):
        import readline
    else:
        pass
else:
    print('ERROR: %s needs python v3.8!'%name)
    exit(1)

####################

def init(*arg):
    # init function
    if len(arg) == 1:
        # just a argument: argv[0]
        pass
    elif len(arg) >= 2:
        # larger than one argument
        if (len(arg) == 2) and (arg[1] == 'version'):
            # count version
            print('%s version%d.%d.%d'%(name, ver))
            exit(0)
        elif (len(arg) == 3) and (arg[1] == 'load') and (os.path.isfile(arg[2])):
            # count load [file]
            loader(arg[2])
        elif (len(arg) == 3) and (arg[1] == 'load') and (not os.path.isfile(arg[2])):
            # count load [a non-existent file or a directory]
            print("ERROR: No such file or directory: '%s'!"%arg[2])
        else:
            print('ERROR: Unknow arguments!')
    else:
        print('ERROR: Unknow arguments!')
    print(name + ' %d.%d.%d'%ver + ': ' + description +'.')
    print("Type 'quit' to quit, 'help' for help.")
    main()

def main():
    #main function
    while True:
        cmd = input('$ ')
        if cmd == '':
            pass
        elif cmd == 'quit':
            exit(0)
        else:
            print("ERROR: %s: command not found!"%cmd)

####################

if __name__ == '__main__':
    try:
        init(*argv)
    except (KeyboardInterrupt, EOFError):
        print()
    else:
        pass
