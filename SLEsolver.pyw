# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import QtGui, QtCore, uic

import parse, matrix

APP_NAME = 'SLEsolver'
VERSION = '1.0'

class MainWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi('gui.ui', self)
        
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        self.solveButton.clicked.connect(self.solve)
        self.clearButton.clicked.connect(self.textEdit.clear)
        self.closeButton.clicked.connect(sys.exit)
        
    def solve(self):
        m = matrix.Matrix(
                parse.Parser( self.textEdit.toPlainText() ).parse()
            )
        
        self.textEdit.append( str(m) )
        
    def validate(self):
        pass
     
if __name__ == "__main__":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_NAME + VERSION)
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
