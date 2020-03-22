# sheets/aboutdialog.py

import os
from scrolledframe import ScrolledText
import sys
import tkinter as tk
import tkinter.ttk as ttk

class AboutDialog():
    'About dialog of sheets.'
    def __init__(self, master):
        self.aboutdialog = tk.Toplevel(master)
        self.aboutdialog.geometry('550x450')
        self.aboutdialog.resizable(False, False)
        self.aboutdialog.title('Sheets - About')
        self.notebook = ttk.Notebook(self.aboutdialog)
        self.aboutnotebook = ttk.Frame(self.notebook)
        self.licensenotebook = ttk.Frame(self.notebook)
        self.readmenotebook = ttk.Frame(self.notebook)
        self.closebutton = ttk.Button(self.aboutdialog, text='Close',
                                      command=self._destory)
        self.notebook.add(self.aboutnotebook, text='About')
        self.notebook.add(self.licensenotebook, text='License')
        self.notebook.add(self.readmenotebook, text='README')
        self.closebutton.pack(side='bottom' ,padx=10, pady=10)
        self.notebook.pack(fill='both', expand=1)
        self._createabout()
        self._createlicense()
        self._createreadme()

    def _destory(self, event=None):
        self.aboutdialog.destroy()
    
    def _createabout(self):
        abouttext = '''\
Sheet version 1.0.0

A simple GUI sheet program.

You can find source code on:
http://github.com/jason-bowen-zheng/sheets

Copyright (c) 2020 jason-bowen-zheng.
All Right Reserved


The license is GPLv3.
'''
        self.aboutlabel = ttk.Label(self.aboutnotebook, anchor='e',
                                    text=abouttext,font=('helvetica', 12))
        self.aboutlabel.pack(fill='both', expand=1)

    def _createlicense(self):
        try:
            licensetext = open(sys.path[0] + os.sep + 'LICENSE', 'r').read()
        except:
            licensetext = 'No LICENSE found!'
        self.textarea = ScrolledText(self.licensenotebook)
        self.textarea.pack(fill='both', expand=1)
        self.textarea.insert('end', licensetext)
        self.textarea['state'] = 'disabled'

    def _createreadme(self):
        try:
            readmetext = open(sys.path[0] + os.sep + 'README.md', 'r').read()
        except:
            readmetext = 'No README found!'
        self.textarea = ScrolledText(self.readmenotebook)
        self.textarea.pack(fill='both', expand=1)
        self.textarea.insert('end', readmetext)
        self.textarea['state'] = 'disabled'

    def show(self):
        self.aboutdialog.mainloop()
