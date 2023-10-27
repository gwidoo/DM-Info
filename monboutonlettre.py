from tkinter import *

class MonBoutonLettre(Button):
    def __init__(self,parent,fenetre,a):
        Button.__init__(self,parent,text=t,state=DISABLED)
        self.__fenetre=fenetre
        self.__lettre=a #notre bouton est associé à une unique lettre de l'alphabet
        
        
    def cliquer(self):
        self.config(state=DISABLED)
        self.__fenetre.traitement(self.__lettre) #lorsqu'on clique sur le bouton, on appelle traitement, définit dans FenPrincipale
        
    
        