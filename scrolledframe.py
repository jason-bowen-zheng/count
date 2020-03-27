# xSheets/scrolledframe.py

import tkinter as tk
import tkinter.ttk as ttk


class ScrolledFrame(ttk.Frame):
    'Another version of idlelib.configdialog.VerticalScrolledFrame'
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)
        # Create a canvas object and two scrollbars for scrolling it.
        hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill='y', side='right', expand=0)
        hscrollbar.pack(fill='x', side='bottom', expand=0)
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                           xscrollcommand=hscrollbar.set,
                           yscrollcommand=vscrollbar.set, width=240)
        canvas.pack(fill='both', expand=1)
        hscrollbar.config(command=canvas.xview)
        vscrollbar.config(command=canvas.yview)
        # Reset the view.
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor='nw')
        
        def _configure_interior(event):
            # Track changes to the canvas and frame width and sync them,
            # also updating the scrollbar.
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion='0 0 %s %s' % size)
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            # It's wise not to do anything.
            pass
        canvas.bind('<Configure>', _configure_canvas)
        

class ScrolledText(tk.Text):
    def __init__(self, master=None, **kw):
        self.frame = ttk.Frame(master)
        self.vbar = ttk.Scrollbar(self.frame)
        self.vbar.pack(side='right', fill='y')

        kw.update({'yscrollcommand': self.vbar.set})
        tk.Text.__init__(self, self.frame, **kw)
        self.pack(side='left', fill='both', expand=1)
        self.vbar['command'] = self.yview
        # Copy geometry methods of self.frame without overriding Text
        text_meths = vars(tk.Text).keys()
        methods = vars(tk.Pack).keys() | vars(tk.Grid).keys() | vars(tk.Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)


class VerticalScrolledFrame(ttk.Frame):
    'idlelib.configdialog.VerticalScrolledFrame'
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill='y', side='right', expand=0)
        canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set, width=240)
        canvas.pack(side='left', fill='both', expand=1)
        vscrollbar.config(command=canvas.yview)
        # Reset the view.
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor='nw')

        def _configure_interior(event):
            # Track changes to the canvas and frame width and sync them,
            # also updating the scrollbar.
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
