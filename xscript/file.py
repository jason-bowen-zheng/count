# xSheets/xscript/file.py

def fileclose(fileobj):
    fileobj.close()

def fileflush(fileobj):
    fileobj.flush()

def fileopen(name, mode='r'):
    return open(name, mode)
