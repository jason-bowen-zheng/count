# sheet.py

import os
import re
import sheetfunction as func
import sys
from xml.parsers import expat
from xml.sax.saxutils import escape

LEFT, CENTER, RIGHT = "LEFT", "CENTER", "RIGHT"

def ljust(x, n):
    return x.ljust(n)

def center(x, n):
    return x.center(n)

def rjust(x, n):
    return x.rjust(n)

align2action = {LEFT: ljust, CENTER: center, RIGHT: rjust}

align2xml = {LEFT: "left", CENTER: "center", RIGHT: "right"}
xml2align = {"left": LEFT, "center": CENTER, "right": RIGHT}

align2anchor = {LEFT: "w", CENTER: "center", RIGHT: "e"}


class Sheet:

    def __init__(self):
        self.cells = {} # {(x, y): cell, ...}
        self.ns = {
            'cell': self.cellvalue,
            'cells': self.multicellvalue,
        }.update(func.functions)

    def cellvalue(self, x, y):
        cell = self.getcell(x, y)
        if hasattr(cell, 'recalc'):
            return cell.recalc(self.ns)
        else:
            return cell

    def multicellvalue(self, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        seq = []
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                seq.append(self.cellvalue(x, y))
        return seq

    def getcell(self, x, y):
        return self.cells.get((x, y))

    def setcell(self, x, y, cell):
        assert x > 0 and y > 0
        assert isinstance(cell, BaseCell)
        self.cells[x, y] = cell

    def clearcell(self, x, y):
        try:
            del self.cells[x, y]
        except KeyError:
            pass

    def clearcells(self, x1, y1, x2, y2):
        for xy in self.selectcells(x1, y1, x2, y2):
            del self.cells[xy]

    def clearrows(self, y1, y2):
        self.clearcells(0, y1, sys.maxsize, y2)

    def clearcolumns(self, x1, x2):
        self.clearcells(x1, 0, x2, sys.maxsize)

    def selectcells(self, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        return [(x, y) for x, y in self.cells
                if x1 <= x <= x2 and y1 <= y <= y2]

    def movecells(self, x1, y1, x2, y2, dx, dy):
        if dx == 0 and dy == 0:
            return
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        assert x1+dx > 0 and y1+dy > 0
        new = {}
        for x, y in self.cells:
            cell = self.cells[x, y]
            if hasattr(cell, 'renumber'):
                cell = cell.renumber(x1, y1, x2, y2, dx, dy)
            if x1 <= x <= x2 and y1 <= y <= y2:
                x += dx
                y += dy
            new[x, y] = cell
        self.cells = new

    def insertrows(self, y, n):
        assert n > 0
        self.movecells(0, y, sys.maxsize, sys.maxsize, 0, n)

    def deleterows(self, y1, y2):
        if y1 > y2:
            y1, y2 = y2, y1
        self.clearrows(y1, y2)
        self.movecells(0, y2+1, sys.maxsize, sys.maxsize, 0, y1-y2-1)

    def insertcolumns(self, x, n):
        assert n > 0
        self.movecells(x, 0, sys.maxsize, sys.maxsize, n, 0)

    def deletecolumns(self, x1, x2):
        if x1 > x2:
            x1, x2 = x2, x1
        self.clearcells(x1, x2)
        self.movecells(x2+1, 0, sys.maxsize, sys.maxsize, x1-x2-1, 0)

    def getsize(self):
        maxx = maxy = 0
        for x, y in self.cells:
            maxx = max(maxx, x)
            maxy = max(maxy, y)
        return maxx, maxy

    def reset(self):
        for cell in self.cells.values():
            if hasattr(cell, 'reset'):
                cell.reset()

    def recalc(self):
        self.reset()
        for cell in self.cells.values():
            if hasattr(cell, 'recalc'):
                cell.recalc(self.ns)

    def display(self):
        maxx, maxy = self.getsize()
        width, height = maxx+1, maxy+1
        colwidth = [1] * width
        full = {}
        # Add column heading labels in row 0
        for x in range(1, width):
            full[x, 0] = text, alignment = colnum2name(x), RIGHT
            colwidth[x] = max(colwidth[x], len(text))
        # Add row labels in column 0
        for y in range(1, height):
            full[0, y] = text, alignment = str(y), RIGHT
            colwidth[0] = max(colwidth[0], len(text))
        # Add sheet cells in columns with x>0 and y>0
        for (x, y), cell in self.cells.items():
            if x <= 0 or y <= 0:
                continue
            if hasattr(cell, 'recalc'):
                cell.recalc(self.ns)
            if hasattr(cell, 'format'):
                text, alignment = cell.format()
                assert isinstance(text, str)
                assert alignment in (LEFT, CENTER, RIGHT)
            else:
                text = str(cell)
                if isinstance(cell, str):
                    alignment = LEFT
                else:
                    alignment = RIGHT
            full[x, y] = (text, alignment)
            colwidth[x] = max(colwidth[x], len(text))
        # Calculate the horizontal separator line (dashes and dots)
        sep = ""
        for x in range(width):
            if sep:
                sep += "+"
            sep += "-"*colwidth[x]
        # Now print The full grid
        for y in range(height):
            line = ""
            for x in range(width):
                text, alignment = full.get((x, y)) or ("", LEFT)
                text = align2action[alignment](text, colwidth[x])
                if line:
                    line += '|'
                line += text
            print(line)
            if y == 0:
                print(sep)

    def xml(self):
        out = ['<sheet>']
        for (x, y), cell in self.cells.items():
            if hasattr(cell, 'xml'):
                cellxml = cell.xml()
            else:
                cellxml = '<value>%s</value>' % escape(cell)
            out.append('<cell row="%s" col="%s">\n  %s\n</cell>' %
                       (y, x, cellxml))
        out.append('</sheet>')
        return '\n'.join(out)

    def save(self, filename):
        text = self.xml()
        with open(filename, "w", encoding='utf-8') as f:
            f.write(text)
            if text and not text.endswith('\n'):
                f.write('\n')

    def load(self, filename):
        with open(filename, 'rb') as f:
            SheetParser(self).parsefile(f)


class SheetParser:

    def __init__(self, sheet):
        self.sheet = sheet

    def parsefile(self, f):
        parser = expat.ParserCreate()
        parser.StartElementHandler = self.startelement
        parser.EndElementHandler = self.endelement
        parser.CharacterDataHandler = self.data
        parser.ParseFile(f)

    def startelement(self, tag, attrs):
        method = getattr(self, 'start_'+tag, None)
        if method:
            method(attrs)
        self.texts = []

    def data(self, text):
        self.texts.append(text)

    def endelement(self, tag):
        method = getattr(self, 'end_'+tag, None)
        if method:
            method("".join(self.texts))

    def start_cell(self, attrs):
        self.y = int(attrs.get("row"))
        self.x = int(attrs.get("col"))

    def start_value(self, attrs):
        self.fmt = attrs.get('format')
        self.alignment = xml2align.get(attrs.get('align'))

    start_formula = start_value

    def end_int(self, text):
        try:
            self.value = int(text)
        except (TypeError, ValueError):
            self.value = None

    end_long = end_int

    def end_double(self, text):
        try:
            self.value = float(text)
        except (TypeError, ValueError):
            self.value = None

    def end_complex(self, text):
        try:
            self.value = complex(text)
        except (TypeError, ValueError):
            self.value = None

    def end_string(self, text):
        self.value = text

    def end_value(self, text):
        if isinstance(self.value, BaseCell):
            self.cell = self.value
        elif isinstance(self.value, str):
            self.cell = StringCell(self.value,
                                   self.fmt or "%s",
                                   self.alignment or LEFT)
        else:
            self.cell = NumericCell(self.value,
                                    self.fmt or "%s",
                                    self.alignment or RIGHT)

    def end_formula(self, text):
        self.cell = FormulaCell(text,
                                self.fmt or "%s",
                                self.alignment or RIGHT)

    def end_cell(self, text):
        self.sheet.setcell(self.x, self.y, self.cell)


class BaseCell:
    __init__ = None # Must provide
    """Abstract base class for sheet cells.
    Subclasses may but needn't provide the following APIs:
    cell.reset() -- prepare for recalculation
    cell.recalc(ns) -> value -- recalculate formula
    cell.format() -> (value, alignment) -- return formatted value
    cell.xml() -> string -- return XML
    """

class NumericCell(BaseCell):

    def __init__(self, value, fmt="%s", alignment=RIGHT):
        assert isinstance(value, (int, float, complex))
        assert alignment in (LEFT, CENTER, RIGHT)
        self.value = value
        self.fmt = fmt
        self.alignment = alignment

    def recalc(self, ns):
        return self.value

    def format(self):
        try:
            text = self.fmt % self.value
        except:
            text = str(self.value)
        return text, self.alignment

    def xml(self):
        method = getattr(self, '_xml_' + type(self.value).__name__)
        return '<value align="%s" format="%s">%s</value>' % (
                align2xml[self.alignment],
                self.fmt,
                method())

    def _xml_int(self):
        if -2**31 <= self.value < 2**31:
            return '<int>%s</int>' % self.value
        else:
            return '<long>%s</long>' % self.value

    def _xml_float(self):
        return '<double>%r</double>' % self.value

    def _xml_complex(self):
        return '<complex>%r</complex>' % self.value

class StringCell(BaseCell):

    def __init__(self, text, fmt="%s", alignment=LEFT):
        assert isinstance(text, str)
        assert alignment in (LEFT, CENTER, RIGHT)
        self.text = text
        self.fmt = fmt
        self.alignment = alignment

    def recalc(self, ns):
        return self.text

    def format(self):
        return self.text, self.alignment

    def xml(self):
        s = '<value align="%s" format="%s"><string>%s</string></value>'
        return s % (
            align2xml[self.alignment],
            self.fmt,
            escape(self.text))

class FormulaCell(BaseCell):

    def __init__(self, formula, fmt="%s", alignment=RIGHT):
        assert alignment in (LEFT, CENTER, RIGHT)
        self.formula = formula
        self.translated = translate(self.formula)
        self.fmt = fmt
        self.alignment = alignment
        self.reset()

    def reset(self):
        self.value = None

    def recalc(self, ns):
        if self.value is None:
            try:
                self.value = eval(self.translated, None, ns)
            except:
                exc = sys.exc_info()[0]
                if hasattr(exc, "__name__"):
                    self.value = exc.__name__
                else:
                    self.value = str(exc)
        return self.value

    def format(self):
        try:
            text = self.fmt % self.value
        except:
            text = str(self.value)
        return text, self.alignment

    def xml(self):
        return '<formula align="%s" format="%s">%s</formula>' % (
            align2xml[self.alignment],
            self.fmt,
            escape(self.formula))

    def renumber(self, x1, y1, x2, y2, dx, dy):
        out = []
        for part in re.split(r'(\w+)', self.formula):
            m = re.match('^([A-Z]+)([1-9][0-9]*)$', part)
            if m is not None:
                sx, sy = m.groups()
                x = colname2num(sx)
                y = int(sy)
                if x1 <= x <= x2 and y1 <= y <= y2:
                    part = cellname(x+dx, y+dy)
            out.append(part)
        return FormulaCell("".join(out), self.fmt, self.alignment)

def translate(formula):
    """Translate a formula containing fancy cell names to valid Python code.

    Examples:
        B4 -> cell(2, 4)
        B4:Z100 -> cells(2, 4, 26, 100)
    """
    out = []
    for part in re.split(r"(\w+(?::\w+)?)", formula):
        m = re.match(r"^([A-Z]+)([1-9][0-9]*)(?::([A-Z]+)([1-9][0-9]*))?$", part)
        if m is None:
            out.append(part)
        else:
            x1, y1, x2, y2 = m.groups()
            x1 = colname2num(x1)
            if x2 is None:
                s = "cell(%s, %s)" % (x1, y1)
            else:
                x2 = colname2num(x2)
                s = "cells(%s, %s, %s, %s)" % (x1, y1, x2, y2)
            out.append(s)
    return "".join(out)

def cellname(x, y):
    "Translate a cell coordinate to a fancy cell name (e.g. (1, 1)->'A1')."
    assert x > 0 # Column 0 has an empty name, so can't use that
    return colnum2name(x) + str(y)

def colname2num(s):
    "Translate a column name to number (e.g. 'A'->1, 'Z'->26, 'AA'->27)."
    s = s.upper()
    n = 0
    for c in s:
        assert 'A' <= c <= 'Z'
        n = n*26 + ord(c) - ord('A') + 1
    return n

def colnum2name(n):
    "Translate a column number to name (e.g. 1->'A', etc.)."
    assert n > 0
    s = ""
    while n:
        n, m = divmod(n-1, 26)
        s = chr(m+ord('A')) + s
    return s
