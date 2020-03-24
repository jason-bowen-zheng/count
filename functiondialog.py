# sheet/functiondialog.py

import tkinter as tk
import tkinter.ttk as ttk
import sheetfunction as function

class FunctionDialog():

    def __init__(self, master, type_):
        self.functiontype = type_
        self.helpdialog = tk.Toplevel(master)
        self.helpdialog.title('Sheet - function')
        self.label = ttk.Label(self.helpdialog, text='Type:')
        self.typebox = ttk.Combobox(self.helpdialog)
        self.typebox['state'] ='readonly'
        self.typebox['values'] = ('All',
                                  'Economy',
                                  'logic',
                                  'Math',
                                  'Statistics',
                                  'Text')
        self.typebox.bind('<<ComboboxSelected>>', self.typeboxsel)
        self.listbox = ttk.Listbox(master, height=8)
    
    def show(self):
        self.functiondialog.mainloop()

