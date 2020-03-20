# sheets/licensedialog.py

from scrolledframe import ScrolledFrame
import tkinter as tk
import tkinter.ttk as ttk

class LicenseDialog():
    'License dialog of sheets
    def __init__(self, master):
        self.licensedialog = tk.Toplevel(master)
        srlf.licensedialog.title('Sheet - License')
        self.textframes = ScrolledFrame(self.licensedialog)
        self.textframr = self.textframes.interior
        self.textarea = ttk.Label(self.textframe)
        self.closebutton = ttk.Button(self.licensedialog,
                                      text='Close', command=self.close)
