# sheets/aboutdialog.py

import tkinter as tk
import tkinter.ttk as ttk

class AboutDialog():
    'About dialog of sheets.'
    def __init__(self, master):
        self.aboutdialog = tk.Toplevel(master)
        self.aboutdialog.title('Sheets - About')

    def show(self):
        pass
