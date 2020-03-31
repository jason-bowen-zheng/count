# xSheets/xscript.py

import os
import shlex
import string
import time

class XscriptInterpreter():
    'xscript interpreter.'
    def __init__(self, string='', var={}, debug=False):
        self.restart(string, var, debug)

    def exitrun(self, code=0):
        print('\nProgram raise exit code: %s' % code)
    
    def restart(self, string='', var={}, debug=False):
        self.string = string.replace(os.sep, '\n')
        self.program = self.string.split('\n')
        if debug:
            print(self.program)
        else:
            pass
        self.var = {}
        self.debug = debug

    def run(self):
        self.now = 1
        starttime = time.time()
        while True:
            if self.now + 1 <= len(self.program):
                line = self.program[self.now - 1]
            else:
                self.exitrun()
                break
            lines = shlex.split(line)
            ret = None
            if self.debug:
                print('command:', lines)
            else:
                pass
            if lines == []:
                pass
            elif lines[0][0] == '#':
                pass
            elif lines[0] == 'exit':
                self.exitrun(*lines[1:])
                break
            elif lines[0] == 'puts':
                ret = self.puts(*lines[1:])
            elif lines[0] == 'set':
                ret = self.set(*lines[1:])
            elif lines[0] == 'unset':
                ret = self.unset(*lines[1:])
            else:
                print('Unknow command')
                self.exitrun(1)
                break
            self.now += 1
            if self.debug:
                print('return:', ret)
            else:
                pass
            if ret == None:
                pass
            elif ret[:6] == 'error ':
                print('Error:', ret[6:])
                break
        print('\nRunning in %ss' % (time.time() - starttime))

    def puts(self, *args):
        for item in args:
            print(item)

    def set(self, name, value):
        pass

    def unset(self, *names):
        for name in names:
            try:
                del self.var[name]
            except KeyError:
                return 'error Unknow name: %s' % name

code = '''puts Hello
set a b
'''
ipr = XscriptInterpreter(code, debug=0)
ipr.run()
