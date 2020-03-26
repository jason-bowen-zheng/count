# sheet/functiondialog.py

import tkinter as tk
import tkinter.ttk as ttk
from scrolledframe import ScrolledText
import sheetfunction as function


class FunctionDialog():

    def __init__(self, master, entry, type_=None):
        self.master = master
        self.entry = entry
        self.functiontype = type_ or 'All'
        self.functiondialog = tk.Toplevel(master)
        self.functiondialog.title('Insert function')
        self.labeltype = ttk.Label(self.functiondialog, text='Type:')
        self.typebox = ttk.Combobox(self.functiondialog)
        self.typebox['state'] ='readonly'
        self.typebox['values'] = ('All',
                                  'Economy',
                                  'Logical',
                                  'Math',
                                  'Statistics',
                                  'Text')
        self.typebox.bind('<<ComboboxSelected>>', self._typeboxsel)
        self.typebox.set('All')
        self.frame = ttk.Frame(self.functiondialog, width=300)
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.listbox = tk.Listbox(self.frame, height=8,
                                  yscrollcommand=self.scrollbar.set)
        self.listbox.bind('<Double-1>', self._listboxsel)
        self.scrollbar.config(command=self.listbox.yview)
        self.labeldetail = ttk.Label(self.functiondialog, text='Detail:')
        self.detail = ScrolledText(self.functiondialog, height=5)
        self.insertbutton = ttk.Button(self.functiondialog, text='Insert',
                                       underline=0, command=self._insert)
        self.detail.pack(side='bottom', fill='x', pady=3)
        self.labeldetail.pack(side='bottom', pady=1)
        self.frame.pack(side='bottom', fill='both')
        self.scrollbar.pack(side='right', fill='y', expand=0)
        self.listbox.pack(side='bottom', fill='both')
        self.labeltype.pack(side='left')
        self.insertbutton.pack(side='right', padx=3, pady=2)
        self.typebox.pack(side='left', fill='x', expand=1, padx=3, pady=2)     

    def _typeboxsel(self, event):
        self.listbox.delete(0, 'end')
        types = self.typebox.get()
        if types == 'All':
            for k, v in function.functions.items():
                self.listbox.insert('end', k)
        else:
            for k, v in function.functions.items():
                if v.__doc__.split('\n')[0] == types + ' function':
                    self.listbox.insert('end', k)

    def _listboxsel(self, event):
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

    def _insert(self, event=None):
        try:
            s = self.listbox.get(self.listbox.curselection()[0])
        except:
            pass
        else:
            self.entry.delete(0, 'end')
            self.entry.insert(0, '=' + s + '()')
            self.functiondialog.destroy()
    
    def show(self):
        self.detail['state'] = 'disabled'
        self.typebox.set('All')
        for f in function.functions.keys():
            self.listbox.insert('end', f)
        self.functiondialog.resizable(False, False)
        self.functiondialog.mainloop()

