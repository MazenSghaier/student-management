from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton,QMessageBox,QDateEdit,QComboBox
from PyQt5 import uic,QtWidgets
import sys
from os import environ
from ISIMM import ISIMM
from matiere import matiere
import re   
  

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    
if __name__ == "__main__":
    suppress_qt_warnings()

class Ajoute(QtWidgets.QDialog):
    
    def __init__(self,ISIMM) :
        self.isimm=ISIMM
        super(Ajoute,self).__init__()
        uic.loadUi("test2.ui",self)
        
        self.k=1
        #QLineEdite
        self.code_line=self.findChild(QLineEdit,"lineEdit")
        self.désignation_line=self.findChild(QLineEdit,"lineEdit_2")
        self.coeff_line=self.findChild(QLineEdit,"lineEdit_3")
        
        #QPushButton
        self.ok=self.findChild(QPushButton,"pushButton")
        self.cancel=self.findChild(QPushButton,"pushButton_2")
        
        #ComboBox
        self.combo1=self.findChild(QComboBox,"comboBox")
        self.combo2=self.findChild(QComboBox,"comboBox_2")

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
        if not(len(self.code_line.text())==4) or not(self.code_line.text().isdigit()) :
                 self.k=0
                 self.showDialog("Code invalide! Il doit contient uniquement 4 chiffre")
        else :
                self.code=self.code_line.text()
                
        if len(self.désignation_line.text())==0 or not(self.désignation_line.text().isalpha()) :
                 self.k=0
                 self.showDialog("Désignation invalide!")
        else :
                self.designation=self.désignation_line.text()
                
        if len(self.coeff_line.text())==0 or not(self.coeff_line.text().isdigit()):
                self.k=0
                self.showDialog("Coefficient invalide!")
        else :
            self.coeff=self.coeff_line.text()
            
        if self.combo1.currentText()=="Choisir.." :
            self.k=0
            self.showDialog("Veuillez choisir une section!")
        else :
            self.section=self.combo1.currentText()
            
        if self.combo2.currentText()=="Choisir.." :
            self.k=0
            self.showDialog("Veuillez choisir la semestre!")
        else :
            self.sem=self.combo2.currentText()
        
        if self.k==1 :
            e=matiere(self.code,self.designation,self.section,self.coeff,self.sem)
            self.isimm.ajoute_matiéres(e)
            self.showSuccess("Ajoute a effectué avec succéss!")
            
    def CANCEL(self) :
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
      
    