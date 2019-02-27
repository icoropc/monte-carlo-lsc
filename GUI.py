# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:46:59 2013

@author: Igor
"""

import sys
from PyQt4 import QtCore, QtGui
from form import Ui_MainWindow
import main

simulationResults=main.mainf()

class wind_inst(Ui_MainWindow):
    def updateform(self):
        self.lineEdit.setText(str(round(simulationResults[0])))
        self.lineEdit_2.setText(str(round(simulationResults[1])))
        self.lineEdit_3.setText(str(round(simulationResults[2])))
        self.lineEdit_4.setText(str(round(simulationResults[3])))
        print(simulationResults)

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = wind_inst()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
