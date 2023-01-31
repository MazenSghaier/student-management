from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton,QMessageBox,QDateEdit,QComboBox
from PyQt5 import uic,QtWidgets
import sys
from os import environ
from ISIMM import ISIMM
from notes import note
import re   
  

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    
if __name__ == "__main__":
    suppress_qt_warnings()

class ajoute(QtWidgets.QDialog):
    
    def __init__(self,ISIMM) :
        self.isimm=ISIMM
        super(ajoute,self).__init__()
        uic.loadUi("test3.ui",self)
        
        self.k=1
        #QLineEdite
        self.code_line=self.findChild(QLineEdit,"lineEdit")
        self.num_line=self.findChild(QLineEdit,"lineEdit_2")
        self.ds_line=self.findChild(QLineEdit,"lineEdit_7")
        self.ex_line=self.findChild(QLineEdit,"lineEdit_6")
        
        #QPushButton
        self.ok=self.findChild(QPushButton,"pushButton")
        self.cancel=self.findChild(QPushButton,"pushButton_2")

        #Click
        self.ok.clicked.connect(self.OK)
        self.cancel.clicked.connect(self.CANCEL)
        
        self.show()
    def showDialog(self,str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        msgBox.setWindowTitle("Message Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
    
    def showSuccess(self,str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Jawek behi")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
    def OK(self):
        x=0.25
        if not(len(self.code_line.text())==4) or not(self.code_line.text().isdigit()) or self.isimm.recherche_code(self.code_line.text())==-1:
            self.k=0
            self.showDialog("Code invalide! Il doit contient uniquement 4 chiffre\n Ou bien code matiére n'existe pas")
        else :
            self.code=self.code_line.text()
        if not(len(self.num_line.text())==8) or not(self.num_line.text().isdigit()) or self.isimm.recherche_ins(self.num_line.text())==-1 :
            self.k=0
            self.showDialog("Numéro d'inscription invalide! Il doit contient uniquement 8 chiffre\n Ou bien numéro inscription n'existe pas")
        else :
            self.num=self.num_line.text()
            
        if len(self.ds_line.text())==0 or not(self.ds_line.text().isdigit()):
            self.k=0
            self.showDialog("Note invalide!")
        else:
            self.ds=self.ds_line.text()
        if len(self.ex_line.text())==0 or not(self.ex_line.text().isdigit()):
            self.k=0
            self.showDialog("Note invalide!")
        else:
            self.ex=self.ex_line.text()
        if self.k==1 :
            e=note(self.code,self.num,self.ds,self.ex)
            self.isimm.ajoute_notes(e)
            self.showSuccess("Ajoute a effectué avec succéss!")
        
    def CANCEL(self) :
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_6.setText("")
 