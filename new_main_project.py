import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets , QtGui , QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from ISIMM import ISIMM
from os import environ,path
from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(path.join(path.dirname('__file__'),"Main.ui"))

import sqlite3

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    
if __name__ == "__main__":
    suppress_qt_warnings()

class Main(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.inst = ISIMM()
        QMainWindow.__init__(parent)
        self.ui.setupUi(self.fen)
        self.Handel_Buttons()
        
        def Handel_Buttons(self):
            pass



def main():
    app = QApplication(sys.argv)
    window=main()
    window.show()
    app.exec_()
if __name__=='__main__' :
    main()