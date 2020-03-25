# sheet/functiondialog.py

import tkinter as tk
import tkinter.ttk as ttk
from scrolledframe import ScrolledText
import sheetfunction as function


class FunctionDialog():

    def __init__(self, master, type_=None):
        self.functiontype = type_ or 'All'
        self.functiondialog = tk.Toplevel(master)
        self.functiondialog.title('Sheet - function')
        self.labeltype = ttk.Label(self.functiondialog, text='Type:')
        self.typebox = ttk.Combobox(self.functiondialog)
        self.typebox['state'] ='readonly'
        self.typebox['values'] = ('All',
                                  'Economy',
                                  'Logical',
                                  'Math',
                                  'Statistics',
                                  'Text')
        self.typebox.bind('<<ComboboxSelected>>', self.typeboxsel)
        self.typebox.set('All')
        self.frame = ttk.Frame(self.functiondialog, width=300)
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.listbox = tk.Listbox(self.frame, height=8,
                                  yscrollcommand=self.scrollbar.set)
        self.listbox.bind('<Double-1>', self.listboxsel)
        for k, v in function.functions.items():
                self.listbox.insert('end', k)
        self.scrollbar.config(command=self.listbox.yview)
        self.labeldetail = ttk.Label(self.functiondialog, text='Detail:')
        self.detail = ScrolledText(self.functiondialog, height=5)
        self.detail['state'] == 'disabled'
        self.detail.pack(side='bottom', fill='x', pady=3)
        self.labeldetail.pack(side='bottom', pady=1)
        self.frame.pack(side='bottom', fill='both')
        self.scrollbar.pack(side='right', fill='y', expand=0)
        self.listbox.pack(side='bottom', fill='both')
        self.labeltype.pack(side='left')
        self.typebox.pack(side='left', fill='x', expand=1, padx=3, pady=2)     

    def typeboxsel(self, event):
        self.listbox.delete(0, 'end')
        types = self.typebox.get()
        if types == 'All':
            for k, v in function.functions.items():
                self.listbox.insert('end', k)
        else:
            for k, v in function.functions.items():
                if v.__doc__.split('\n')[0] == types + ' function':
                    self.listbox.insert('end', k)

    def listboxsel(self, event):
        if self.listbox.curselection() == ():
            f = self.listbox.get(0)
        else:
            f = self.listbox.get(self.listbox.curselection()[0])
        for k, v in function.functions.items():
            if k == f:
                self.detail['state'] = 'normal'
                if hasattr(v, '__doc__'):
                    detail = v.__doc__.split('\n',2)[-1]
                    self.detail.delete('1.0', 'end')
                    self.detail.insert('end', detail)
                self.detail['state'] = 'disable'
    
    def show(self):
        self.typebox.set('All')
        for f in function.functions.keys():
            self.listbox.insert('end', f)
        self.functiondialog.geometry('300x270')
        self.functiondialog.resizable(False, False)
        self.functiondialog.mainloop()

