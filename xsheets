#!/usr/bin/python3

# xSheets v1.0
# A simple GUI sheet program.
# Copyright (c) jason-bowen-zheng 2018-2029
# All Right Reserved.
# You can find source code on website:
# http://jason-bowen-zheng.github.io/xSheets
# The license is GPLv3.

import sys
import ui

if __name__ == '__main__':
    if sys.argv[1:]:
        filename = sys.argv[1]
    else:
        filename = ''
    if sys.platform == 'darwin':
        pass
    else:
        win = ui.xSheetsGUI(filename)
        win.root.mainloop()
