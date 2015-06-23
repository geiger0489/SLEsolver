# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import QtGui, QtCore, uic

import core

APP_NAME = 'SLE solver'
VERSION = '1.0'

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
