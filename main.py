import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_project import Ui_MainWindow
from ISIMM import ISIMM
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    
if __name__ == "__main__":
    suppress_qt_warnings()

class main:
    def __init__(self):
        self.inst = ISIMM()
        self.fen = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.inst)
        self.ui.setupUi(self.fen)
        self.fen.show()

app = QtWidgets.QApplication(sys.argv)
window=main()
app.exec()