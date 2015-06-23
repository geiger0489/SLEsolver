# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import QtGui, QtCore, uic

import core

APP_NAME = 'SLE solver'
VERSION = '1.0'

icon = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABmElEQVQ4T6WTPWvCUBiFjx9xciqIIF0Esbh06y9wclAQRVxFouLk0LVD/4DgT2h3g0OKXxE6iGJ0Sqe2QxCqdjFU1IIotdzXxmildEjgwrk3933ec25yLTD5WABszTAIcC9I6D+9EOtZGeDi8uoPJuvFSgDu6xPF22uabW+KdxAf+wTQ3l5xdu7/F/DxrkKVH3aASqWC6XQKm80GWZaRSqVgt9uPBsdxR3NJkpBMJg2Apmm0odfrIZ1OnwB0oA5qNptIJBI7QLlcxmKxIAeHANalUChgOByeABkgHo8bDubzOW3qdrvgeZ50IBCAqqqkf0eo1+uIxWIGYLlckgMGyGQyVOD37w5zPB7D4/GQFgQBoVAItVoN0WjUiLBerwnQ6XSQzWapq8/nw2g0Iu12u9FqtRAMBrFardBoNBAOhw0HbFF3kMvlqMjr9WIymZB2uVx0Tk6nE5vNBtVq9RjAFhmg3W4jn8+fZD78rCyeKIoGoFQqYTabUUZFURCJRGC1WmkwqK7Ze4fDsf/J9hHM3gUz9T83wwTiG3cQsgR+G17SAAAAAElFTkSuQmCC'

class MainWindow(QtGui.QWidget):
    def __init__(self, parent = None):
     super(MainWindow, self).__init__(parent)
     
     uic.loadUi('gui.ui', self)
     
if __name__ == "__main__":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID((APP_NAME + VERSION).replace(" ", ""))
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon())
    translator = QtCore.QTranslator()
    locale = QtCore.QLocale.system().name()
    translator.load('qt_%s' % locale,
              QtCore.QLibraryInfo.location(
               QtCore.QLibraryInfo.TranslationsPath)
              )
    app.installTranslator(translator)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
