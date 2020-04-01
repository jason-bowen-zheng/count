# xSheets/xscript/ui.py

from tkinter import messagebox

def askyesno(message='', title='xscript'):
    return messagebox.askyesno(message=message, title=title)

def showinfo(message='', title='xscript'):
    return messagebox.showinfo(message=message, title=title)
