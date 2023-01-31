from Etudiant import etudiant
from matiere import matiere
from notes import note

class ISIMM:
    def __init__(self):
        self.liste_etudiant=[]
        self.liste_matiere=[]
        self.liste_notes=[]
    def ajoute_etudiant(self,e):
        self.liste_etudiant.append(e)
    def ajoute_matiéres(self,e):
        self.liste_matiere.append(e)
    def ajoute_notes(self,e):
        self.liste_notes.append(e)
        
#*********************************---RECHERCHER ETUDIANT--********************************#
    def recherche_tel(self,e):
        self.k=1
        self.r=0
        for i in range (len(self.liste_etudiant)):
            if self.liste_etudiant[i].telephone==e :
                 self.k=0
                 self.r=i
        if(self.k==0):
            return self.r
        else :
            return -1
        
    def recherche_mail(self,e):
        self.k=1
        self.r=0
        for i in range (len(self.liste_etudiant)):
            if self.liste_etudiant[i].mail==e :
                 self.k=0
                 self.r=i
        if(self.k==0):
            return self.r
        else :
            return -1
        
    def recherche_adresse(self,e):
        self.k=1
        self.r=0
        for i in range (len(self.liste_etudiant)):
            if self.liste_etudiant[i].adresse==e :
                 self.k=0
                 self.r=i
        if(self.k==0):
            return self.r
        else :
            return -1 
    
    def recherche_ins(self,e):
        self.k=1
        self.r=0
        for i in range (len(self.liste_etudiant)):
            if self.liste_etudiant[i].nInscription==e :
                 self.k=0
                 self.r=i
        if(self.k==0):
            return self.r
        else :
            return -1
    def recherche_section(self,e):
       new=[]
       for i in range (len(self.liste_etudiant)):
           if self.liste_etudiant[i].section==e :
               new.append(self.liste_etudiant[i])
       if(len(new)!=0):
            return new
       else :
            return -1
    def recherche_sec_niv(self,e,n):
       new=[]
       for i in self.liste_etudiant:
           if self.liste_etudiant[i].section==e and self.liste_etudiant[i].niveauEtude==n:
               new.append(self.liste_etudiant[i])
       if(len(new)!=0):
            return new
       else :
            return -1
    def recherche_niveau(self,e):
       new=[]
       for i in self.liste_etudiant:
           if self.liste_etudiant[i].niveauEtude==e :
               new.append(self.liste_etudiant[i])
       if(len(new)!=0):
            return new
       else :
            return -1
#*********************************---MODIFIER---************************************#
    def modifier_tel(self,e):
        if self.recherche_tel(e)!=-1:
            k=self.recherche_tel(e)
            self.liste_etudiant[k].telephone=e
            
    def modifier_mail(self,e):
        if self.recherche_mail(e)!=-1:
            k=self.recherche_mail(e)
            self.liste_etudiant[k].mail=e
            
    def modifier_adresse(self,e):
        if self.recherche_adresse(e)!=-1:
            k=self.recherche_adresse(e)
            self.liste_etudiant[k].adresse=e
            
#*********************************---SUPPRIMER---******************************************#
    def suppIns(self,sec):
        new=[]
        new1=[]
        for i in self.liste_etudiant:
            if i.nInscription!=sec:
                new.append(i)
        self.liste_etudiant=new
        for i in self.liste_notes:
            if i.nInscription!=sec:
                new1.append(i)
        self.liste_notes=new1
    def suppSec(self,sec):
        new=[]
        for i in self.liste_etudiant:
            if i.section!=sec:
                new.append(i)
        self.liste_etudiant=new
    def suppSec_Niv(self,sec,niv):
        new=[]
        for i in self.liste_etudiant:
            if i.section!=sec or i.niveauEtude!=niv:
                    new.append(i)
        self.liste_etudiant=new
    def suppNiv(self,sec):
        new=[]
        for i in self.liste_etudiant:
            if i.niveauEtude!=sec:
                new.append(i)
        self.liste_etudiant=new
#*********************************---RECHERCHER MATIERE--********************************#
    def recherche_code(self,e):
        self.k=1
        self.r=0
        for i in range (len(self.liste_matiere)):
            if self.liste_matiere[i].code==e :
                 self.k=0
                 self.r=i
        if(self.k==0):
            return self.r
        else :
            return -1
    def recherche_des(self,e):
        new=[]
        for i in range (len(self.liste_matiere)):
            if self.liste_matiere[i].designation==e :
                 new.append(self.liste_matiere[i])
        if(len(new)!=0):
            return new
        else :
            return -1
    def recherche_sem(self,e):
        new=[]
        for i in range (len(self.liste_matiere)):
            if self.liste_matiere[i].semestre==e :
                 new.append(self.liste_matiere[i])
        if(len(new)!=0):
            return new
        else :
            return -1
    def recherche_list_code(self,e):
        new=[]
        for i in range (len(self.liste_matiere)):
           if self.liste_matiere[i].code==e :
            new.append(self.liste_matiere[i])
        if(len(new)!=0):
            return new
        else :
            return -1
#*********************************---SUPPRIMER MATIERE--********************************#
    def suppNom(self,sec):
        new=[]
        for i in self.liste_matiere:
            if i.designation!=sec:
                new.append(i)
        self.liste_matiere=new
    def suppSem(self,sec):
        new=[]
        for i in self.liste_matiere:
            if i.semestre!=sec:
                new.append(i)
        self.liste_matiere=new
#*********************************---RECHERCHER MATIERE--********************************#
    def recherche_code_n(self,e):
        self.k=1
        self.r=0
        for i in range (len(self.liste_notes)):
            if self.liste_notes[i].code_matiére==e :
                self.k=0
                self.r=i
            if(self.k==0):
                return self.r
            else :
                return -1
        
    def recherche_ins_n(self,e):
        self.k=1
        self.r=0
        for i in range (len(self.liste_notes)):
            if self.liste_notes[i].nInscription==e :
                self.k=0
                self.r=i
            if(self.k==0):
                return self.r
            else :
                return -1
    def recherche_list_ins(self,e):
        new=[]
        for i in range (len(self.liste_notes)):
           if self.liste_notes[i].nInscription==e :
                new.append(self.liste_notes[i])
        if(len(new)!=0):
            return new
        else :
            return -1
#*********************************- Gestion Etudiant -*************************************#
    def moyenne(self,e):
        self.c=0
        self.m=0.0
        self.f=0.00
        for i in range(len(self.liste_notes)):
            if self.liste_notes[i].nInscription==e :
                c=self.recherche_code(self.liste_notes[i].code_matiére)
                self.m=self.m+(((float(self.liste_notes[i].ds)*0.3)+(float(self.liste_notes[i].ex)*0.7))*float(self.liste_matiere[c].coeff))
                self.f=self.f+float(self.liste_matiere[c].coeff)
        if(self.f!=0):
            moyen=self.m/self.f
            return moyen
        else : return 0