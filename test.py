from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton,QMessageBox,QDateEdit,QComboBox
from PyQt5 import uic,QtWidgets
import sys
from os import environ
from ISIMM import ISIMM
from Etudiant import etudiant
import re   
from PyQt5.QtCore import QDate

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    
if __name__ == "__main__":
    suppress_qt_warnings()

class Ajoute(QMainWindow):
    
    def __init__(self,ISIMM) :
        self.isimm=ISIMM
        super(Ajoute,self).__init__()
        uic.loadUi("mainAjoute.ui",self)
        
        self.k=1
        #QLineEdite
        self.lineEdit_num=self.findChild(QLineEdit,"lineEdit")
        self.lineEdit_nom=self.findChild(QLineEdit,"lineEdit_2")
        self.lineEdit_prenom=self.findChild(QLineEdit,"lineEdit_3")
        self.lineEdit_ad=self.findChild(QLineEdit,"lineEdit_5")
        self.lineEdit_admail=self.findChild(QLineEdit,"lineEdit_6")
        self.lineEdit_tel=self.findChild(QLineEdit,"lineEdit_8")
        
        #QPushButton
        self.ok=self.findChild(QPushButton,"pushButton")
        self.cancel=self.findChild(QPushButton,"pushButton_2")
        
        #date
        self.Date=self.findChild(QDateEdit,"dateEdit")
        
        #ComboBox
        self.combo1=self.findChild(QComboBox,"comboBox")
        self.combo2=self.findChild(QComboBox,"comboBox_2")
        self.combo1.addItem("Choisir..",["Choisir.."])
        self.combo1.addItem("Licence en électronique électrotechnique et automatique (L-EAA)",["1","2","3"])
        self.combo1.addItem("Licence en sciences de l’informatique (L-INF) ",["1","2","3"])
        self.combo1.addItem("Licence en mathématiques appliquée (L-M) ",["1","2","3"])
        self.combo1.addItem("Licence en systèmes embarqués (L-SE) ",["1","2","3"])
        self.combo1.addItem("Diplôme national d'ingénieur en électronique (ING) ",["1","2","3"])
        self.combo1.addItem("Cycle préparatoire intégré (CPI) ",["1","2"])
        self.combo1.addItem("Mastère de recherche en génie logiciel (MR-GL) ",["1","2"])
        self.combo1.addItem("Mastère professionnel en génie logiciel (MP-GL) ",["1"])
        self.combo1.activated.connect(self.choisi)

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
        if not(len(self.lineEdit_num.text())==8) or not(self.lineEdit_num.text().isdigit()) :
                 self.k=0
                 self.showDialog("Numéro d'inscription invalide! Il doit contient uniquement 8 chiffre")
        else :
                self.num=self.lineEdit_num.text()

        if len(self.lineEdit_nom.text())==0 or not(self.lineEdit_nom.text().isalpha()) :
                 self.k=0
                 self.showDialog("Nom invalide!")
        else :
                self.nom=self.lineEdit_nom.text()

        if len(self.lineEdit_prenom.text())==0 or not(self.lineEdit_prenom.text().isalpha()) :
                self.k=0
                self.showDialog("Prenom invalide!")
        else :
                self.prenom=self.lineEdit_prenom.text()
        date = QtWidgets.QDateEdit(self)      
        self.date1=date.date().toPyDate()
        self.adresse=self.lineEdit_ad.text()
        
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        
        
        self.mail=self.lineEdit_admail.text()
        if not(re.search(regex,self.mail)):
            self.k=0
            self.showDialog("Email invalide!")
            self.mail=""
        
        t=self.lineEdit_tel.text()        
        if len(t)==0 or(t[0]!="9" and t[0]!="2" and t[0]!="4" and t[0]!="5" and len(t)!=8 and not(t.isdigit())):
            self.k=0
            self.showDialog("Numéo de téléphone invalide!")
        else :
            self.tel=t
  
        if self.combo1.currentText()=="Choisir.." :
            self.k=0
            self.showDialog("Veuillez choisir une section!")
        else :
            self.section=self.combo1.currentText()
            
        if self.combo2.currentText()=="Choisir.." :
            self.k=0
            self.showDialog("Veuillez choisir un niveau!")
        else :
            self.niveau=self.combo2.currentText()
        if self.k==1 :
            e=etudiant(self.num,self.nom,self.prenom,self.date1,self.adresse,self.mail,self.tel,self.section,self.niveau)
            self.isimm.ajoute_etudiant(e)
            self.showSuccess("Ajoute a effectué avec succéss!")
    def choisi (self,index):
            self.combo2.clear()
            self.combo2.addItems(self.combo1.itemData(index))
           
    def CANCEL(self) :
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_8.setText("")
    
    

