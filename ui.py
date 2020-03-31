# xSheets/ui.py

from functiondialog import FunctionDialog
from helpdialog import (AboutDialog, HelpDialog)
from xsheetsdialog import (FindDialog, ReplaceDialog, GotoDialog)
from xsheetsframe import ScrolledFrame, StatueBar
from xsheetstools import *
import os
import sys
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk


class xSheetsGUI():

    def __init__(self, filename='', rows=10, columns=10):
        # Create and load the sheet.
        self.filename = filename
        self.sheet = Sheet()
        if os.path.isfile(filename):
            self.sheet.load(filename)
        # Calculate the needed grid size.
        maxx, maxy = self.sheet.getsize()
        rows = max(rows, maxy)
        columns = max(columns, maxx)
        # Create the widgets.
        self.root = tk.Tk()
        self.root.geometry('640x480')
        self.root.minsize(640, 480)
        if self.filename:
            self.root.title('xSheets - %s' % self.filename)
        else:
            self.root.title('xSheets')
        self.makemenu()
        self.beacon = ttk.Label(self.root, text='A1',
                               font=('helvetica', 16, 'bold'))
        self.entry = ttk.Entry(self.root)
        self.cellgrids = ScrolledFrame(self.root)
        self.cellgrid = self.cellgrids.interior
        self.separator = ttk.Separator(self.root)
        self.statuebar = StatueBar(self.root)
        self.statuebaritem = []
        # Configure the widget lay-out.
        self.statuebar.pack(side='bottom', fill='both')
        self.separator.pack(side='bottom', fill='both')
        self.cellgrids.pack(side='bottom', expand=1, fill='both')
        self.beacon.pack(side='left')
        self.entry.pack(side='left', expand=1, fill='x', padx=3, pady=2)
        # Bind some events.
        self.entry.bind('<Return>', self.return_event)
        self.entry.bind('<Shift-Return>', self.shift_return_event)
        self.entry.bind('<Tab>', self.tab_event)
        self.entry.bind('<Shift-Tab>', self.shift_tab_event)
        self.entry.bind('<Delete>', self.delete_event)
        self.entry.bind('<Escape>', self.escape_event)
        # Now create the cell grid
        self.makegrid(rows, columns)
        # Select the top-left cell
        self.currentxy = None
        self.cornerxy = None
        self.setcurrent(1, 1)
        # Copy the sheet cells to the GUI cells.
        self.sync()

    def aboutdialog(self, event=None):
        AboutDialog(self.root).show()

    def functiondialog(self, event=None):
        FunctionDialog(self.root, self.entry).show()

    def helpdialog(self, event=None):
        HelpDialog(self.root).show()

    def delete_event(self, event):
        if self.cornerxy != self.currentxy and self.cornerxy is not None:
            self.sheet.clearcells(*(self.currentxy + self.cornerxy))
        else:
            self.sheet.clearcell(*self.currentxy)
        self.sync()
        self.entry.delete(0, 'end')
        return 'break'

    def escape_event(self, event):
        x, y = self.currentxy
        self.load_entry(x, y)

    def load_entry(self, x, y):
        cell = self.sheet.getcell(x, y)
        if cell is None:
            text = ''
        elif isinstance(cell, FormulaCell):
            text = '=' + cell.formula
        else:
            text, alignment = cell.format()
        self.entry.delete(0, 'end')
        self.entry.insert(0, text)
        self.entry.selection_range(0, 'end')

    def makegrid(self, rows, columns):
        '''Helper to create the grid of GUI cells.

        The edge (x==0 or y==0) is filled with labels; the rest is real cells.
        '''
        self.rows = rows
        self.columns = columns
        self.gridcells = {}
        # Create the top left corner cell (which selects all).
        cell = tk.Label(self.cellgrid, border=1, relief='solid',
                        fg='black')
        cell.grid_configure(column=0, row=0, sticky='NSWE')
        cell.bind('<ButtonPress-1>', self.selectall)
        self.gridcells[0, 0] = cell
        # Create the top row of labels, and configure the grid columns.
        for x in range(1, columns+1):
            self.cellgrid.grid_columnconfigure(x, minsize=64)
            cell = tk.Label(self.cellgrid, text=colnum2name(x), border=1, relief='solid',
                            fg='black')
            cell.grid_configure(column=x, row=0, sticky='WE')
            self.gridcells[x, 0] = cell
            cell.__x = x
            cell.__y = 0
            cell.bind('<ButtonPress-1>', self.selectcolumn)
            cell.bind('<B1-Motion>', self.extendcolumn)
            cell.bind('<ButtonRelease-1>', self.extendcolumn)
            cell.bind('<Shift-Button-1>', self.extendcolumn)
        # Create the leftmost column of labels.
        for y in range(1, rows+1):
            cell = tk.Label(self.cellgrid, text=str(y), border=1, relief='solid',
                            fg='black')
            cell.grid_configure(column=0, row=y, sticky='WE')
            self.gridcells[0, y] = cell
            cell.__x = 0
            cell.__y = y
            cell.bind('<ButtonPress-1>', self.selectrow)
            cell.bind('<B1-Motion>', self.extendrow)
            cell.bind('<ButtonRelease-1>', self.extendrow)
            cell.bind('<Shift-Button-1>', self.extendrow)
        # Create the real cells.
        for x in range(1, columns+1):
            for y in range(1, rows+1):
                cell = tk.Label(self.cellgrid, border=1, relief='solid',
                                bg='white', fg='black')
                cell.grid_configure(column=x, row=y, sticky='NSWE')
                self.gridcells[x, y] = cell
                cell.__x = x
                cell.__y = y
                # Bind mouse events.
                cell.bind('<ButtonPress-1>', self.press)
                cell.bind('<B1-Motion>', self.motion)
                cell.bind('<ButtonRelease-1>', self.release)
                cell.bind('<Shift-Button-1>', self.release)
    
    def makemenu(self):
        self.root.option_add('*tearOff', 0)
        # Create menu bar.
        self.menubar = tk.Menu(self.root)
        self.root['menu'] = self.menubar
        self.menu_file = tk.Menu(self.menubar)
        self.menu_edit = tk.Menu(self.menubar)
        self.menu_data = tk.Menu(self.menubar)
        self.menu_formula = tk.Menu(self.menubar)
        self.menu_view = tk.Menu(self.menubar)
        self.menu_help = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='File',
                                 underline=0)
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit',
                                 underline=0)
        self.menubar.add_cascade(menu=self.menu_data, label='Data',
                                 underline=0)
        self.menubar.add_cascade(menu=self.menu_formula, label='Formula',
                                 underline=1)
        self.menubar.add_cascade(menu=self.menu_view, label='View',
                                 underline=0)
        self.menubar.add_cascade(menu=self.menu_help, label='Help',
                                 underline=0)
        # Create File menu.
        self.menu_file.add_command(label='New', accelerator='Ctrl+N',
                                   underline=0)
        self.menu_file.add_command(label='Open...', accelerator='Ctrl+O',
                                   underline=0, command=self.openfile)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Save', accelerator='Ctrl+S',
                                   underline=0, command=self.save)
        self.menu_file.add_command(label='Save As...', accelerator='Ctrl+Shift+S',
                                   underline=5, command=self.saveas)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Exit', accelerator='Ctrl+Q',
                                   underline=0)
        # Create Edit menu.
        self.menu_edit.add_command(label='Cut', accelerator='Ctrl+X',
                                   underline=0)
        self.menu_edit.add_command(label='Copy', accelerator='Ctrl+C',
                                   underline=1)
        self.menu_edit.add_command(label='Paste', accelerator='Ctrl+V',
                                   underline=0)
        self.menu_edit.add_command(label='Select All', accelerator='Ctrl+A',
                                   underline=0,command=self.selectall)
        self.menu_edit.add_separator()
        self.menu_edit.add_command(label='Find...', accelerator='Ctrl+F',
                                   underline=0)
        self.menu_edit.add_command(label='Find Next', accelerator='F3',
                                   underline=5)
        self.menu_edit.add_command(label='Replace...', accelerator='Ctrl+R',
                                   underline=1)
        self.menu_edit.add_command(label='Goto...', accelerator='Ctrl+G',
                                   underline=0)
        # Create Data menu.
        self.menu_data.add_command(label='Data validity...', underline=5)
        # Create Function menu.
        self.menu_formula.add_command(label='Insert function...', underline=0,
                                       command=self.functiondialog)
        self.menu_formula.add_separator()
        self.menu_formula.add_command(label='Recalc',accelerator='F5',
                                      underline=0,command=self.sync)
        # Create View menu.
        self.gridlinestatue = tk.BooleanVar(self.root, True)
        self.menu_view.add_checkbutton(label='Show cell gridline',
                                       underline=5, variable=self.gridlinestatue,
                                       onvalue=True, offvalue=False, command=self.setcellgridline)
        self.titlelinestatue = tk.BooleanVar(self.root, True)
        self.menu_view.add_checkbutton(label='Show title gridline',
                                       underline=5, variable=self.titlelinestatue,
                                       onvalue=True, offvalue=False, command=self.settitlegridline)
        # Create Help menu.
        self.menu_help.add_command(label='Help', accelerator='F1',
                                   underline=0, command=self.helpdialog)
        self.menu_help.add_separator()
        self.menu_help.add_command(label='About',
                                   underline=0, command=self.aboutdialog)

    def selectall(self, event=None):
        self.setcurrent(1, 1)
        self.setcorner(sys.maxsize, sys.maxsize)

    def selectcolumn(self, event):
        x, y = self.whichxy(event)
        self.setcurrent(x, 1)
        self.setcorner(x, sys.maxsize)

    def extendcolumn(self, event):
        x, y = self.whichxy(event)
        if x > 0:
            self.setcurrent(self.currentxy[0], 1)
            self.setcorner(x, sys.maxsize)

    def selectrow(self, event):
        x, y = self.whichxy(event)
        self.setcurrent(1, y)
        self.setcorner(sys.maxsize, y)

    def extendrow(self, event):
        x, y = self.whichxy(event)
        if y > 0:
            self.setcurrent(1, self.currentxy[1])
            self.setcorner(sys.maxsize, y)

    def press(self, event):
        x, y = self.whichxy(event)
        if x > 0 and y > 0:
            self.setcurrent(x, y)

    def motion(self, event):
        x, y = self.whichxy(event)
        if x > 0 and y > 0:
            self.setcorner(x, y)

    release = motion

    def whichxy(self, event):
        w = self.cellgrid.winfo_containing(event.x_root, event.y_root)
        if w is not None and isinstance(w, tk.Label):
            try:
                return w.__x, w.__y
            except AttributeError:
                pass
        return 0, 0

    filetypes = [
        ('xml files', '*.xml', 'TEXT'),
        ('csv files', '*.csv', 'TEXT'),
        ('all files', '*')
        ]

    def save(self, filename=None):
        if self.filename:
            self.sheet.save(self.filename)
        else:
            name = filedialog.SaveAs(filetypes=self.filetypes,
                                 defaultextension='*.xml',
                                 initialdir=os.getcwd(),
                                 initialfile='untitled.xml').show()
            if name:
                self.filename = name
                self.sheet.save(self.filename)
            else:
                pass

    def saveas(self):
        name = filedialog.SaveAs(filetypes=self.filetypes,
                                 defaultextension='*.xml',
                                 initialdir=os.getcwd(),
                                 initialfile='untitled.xml').show()
        if name:
            self.sheet.save(name)
        else:
            pass

    def openfile(self, event=None):
        pass
    
    def setcurrent(self, x, y):
        'Make (x, y) the current cell.'
        if self.currentxy is not None:
            self.change_cell()
        self.clearfocus()
        self.beacon['text'] = cellname(x, y)
        self.load_entry(x, y)
        self.entry.focus_set()
        self.currentxy = x, y
        self.cornerxy = None
        gridcell = self.gridcells.get(self.currentxy)
        if gridcell is not None:
            gridcell['bg'] = 'lightblue'

    def setcorner(self, x, y):
        if self.currentxy is None or self.currentxy == (x, y):
            self.setcurrent(x, y)
            return
        self.clearfocus()
        self.cornerxy = x, y
        x1, y1 = self.currentxy
        x2, y2 = self.cornerxy or self.currentxy
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for (x, y), cell in self.gridcells.items():
            if x1 <= x <= x2 and y1 <= y <= y2:
                cell['bg'] = 'lightblue'
        gridcell = self.gridcells.get(self.currentxy)
        if gridcell is not None:
            gridcell['bg'] = 'white'
        self.setbeacon(x1, y1, x2, y2)

    def setbeacon(self, x1, y1, x2, y2):
        if x1 == y1 == 1 and x2 == y2 == sys.maxsize:
            name = ':'
        elif (x1, x2) == (1, sys.maxsize):
            if y1 == y2:
                name = '%d' % y1
            else:
                name = '%d:%d' % (y1, y2)
        elif (y1, y2) == (1, sys.maxsize):
            if x1 == x2:
                name = '%s' % colnum2name(x1)
            else:
                name = '%s:%s' % (colnum2name(x1), colnum2name(x2))
        else:
            name1 = cellname(*self.currentxy)
            name2 = cellname(*self.cornerxy)
            name = '%s:%s' % (name1, name2)
        self.beacon['text'] = name

    def setcellgridline(self, event=None):
        for k, v in self.gridcells.items():
            if k[0] != 0 and k[1] != 0:
                if v['border'] == 1:
                    v['border'] = 0
                else:
                    v['border'] =1

    def settitlegridline(self, event=None):
        for k, v in self.gridcells.items():
            if k[0] == 0 or k[1] == 0:
                if v['border'] == 1:
                    v['border'] = 0
                else:
                    v['border'] = 1
    
    def setstatuebar(self, obj=[]):
        self.statuebar.del_item()
        for item in obj[::-1]:
            if item == ':sep:':
                self.statuebar.add_separator()
            else:
                self.statuebar.add_text(item)

    def clearfocus(self):
        if self.currentxy is not None:
            x1, y1 = self.currentxy
            x2, y2 = self.cornerxy or self.currentxy
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            for (x, y), cell in self.gridcells.items():
                if x1 <= x <= x2 and y1 <= y <= y2:
                    cell['bg'] = 'white'

    def return_event(self, event):
        'Callback for the Return key.'
        self.change_cell()
        x, y = self.currentxy
        self.setcurrent(x, y+1)
        return 'break'

    def shift_return_event(self, event):
        'Callback for the Return key with Shift modifier.'
        self.change_cell()
        x, y = self.currentxy
        self.setcurrent(x, max(1, y-1))
        return 'break'

    def tab_event(self, event):
        'Callback for the Tab key.'
        self.change_cell()
        x, y = self.currentxy
        self.setcurrent(x+1, y)
        return 'break'

    def shift_tab_event(self, event):
        'Callback for the Tab key with Shift modifier.'
        self.change_cell()
        x, y = self.currentxy
        self.setcurrent(max(1, x-1), y)
        return 'break'

    def change_cell(self):
        'Set the current cell from the entry widget.'
        x, y = self.currentxy
        text = self.entry.get()
        cell = None
        if text.startswith('='):
            cell = FormulaCell(text[1:])
        else:
            for cls in int, float, complex:
                try:
                    value = cls(text)
                except (TypeError, ValueError):
                    continue
                else:
                    cell = NumericCell(value)
                    break
        if cell is None and text:
            cell = StringCell(text)
        if cell is None:
            self.sheet.clearcell(x, y)
        else:
            self.sheet.setcell(x, y, cell)
        self.sync()

    def sync(self):
        # Fill the GUI cells from the sheet cells.
        self.sheet.recalc()
        for (x, y), gridcell in self.gridcells.items():
            if x == 0 or y == 0:
                continue
            cell = self.sheet.getcell(x, y)
            if cell is None:
                gridcell['text'] = ''
            else:
                if hasattr(cell, 'format'):
                    text, alignment = cell.format()
                else:
                    text, alignment = str(cell), LEFT
                gridcell['text'] = text
                gridcell['anchor'] = align2anchor[alignment]
