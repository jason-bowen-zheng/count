# sheets/aboutdialog.py

import tkinter as tk
import tkinter.ttk as ttk

class AboutDialog():
    'About dialog of sheets.'
    def __init__(self, master):
        self.aboutdialog = tk.Toplevel(master)
        self.aboutdialog.title('Sheets - About')
        self.notebook = ttk.Notebook(self.aboutdialog)
        self.aboutnotebook = ttk.Frame(self.notebook)
        self.licensenotebook = ttk.Frame(self.notebook)
        self.notebook.add(self.aboutnotebook, text='About')
        self.notebook.add(self.licensenotebook, text='License')
        self.notebook.pack(fill='both', expand=1)
        self._createabout()
        self._createlicense()
        self.aboutdialog.mainloop()

    def _createabout(self):
        abouttext = '''\
Sheet version 1.0.0

A simple GUI sheet program

Copyright (c) 2018-2020 jason-bowen-zheng.
All Right Reserved
'''
        self.aboutlabel = ttk.Label(self.aboutnotebook, text=abouttext)
        self.aboutlabel.pack(fill='both', expand=1)

    def _createlicense(self):
        pass
