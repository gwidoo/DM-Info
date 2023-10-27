# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 07:29:26 2023

@author: celin
"""

from tkinter import *
from tkinter import colorchooser
from random import randint
from formes import *

#je n'arrive pas à dégriser les lettres en cliquant sur nouvelle partie ni à choisir un mot au hasard
#je n'arrive pas non plus à créer correctement la classe MonBoutonLettre
#problème lors  de la création des pièces du dessin du pendu et aussi du set.state

###DEF DE LA CLASSE FenPrincipale


class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="pink") #on colore la fenêtre prinicipale en rose
        
###on définit la barre d'outils qui est une Frame
        self.__barreOutils=Frame(self,bg="white")
        self.__barreOutils.pack(side=TOP,padx=10,pady=10)
        
        #on définit les boutons de la barre d'outils
        self.__buttonNouvellePartie = Button(self.__barreOutils, text='Nouvelle partie')
        self.__buttonNouvellePartie.pack(side=LEFT, padx=5, pady=5)

        self.__buttonQuit = Button(self.__barreOutils, text='Quitter')
        self.__buttonQuit.pack(side=LEFT, padx=5, pady=5)
        
###on définit la grande zone d'affichage
        self.__zoneAffichage=ZoneAffichage(self,400,300)
        self.__zoneAffichage.pack(side=TOP,padx=10,pady=10)
        self.__zoneAffichage.configure(bg="white")
        
###on définit la zone du mot à découvrir
        self.__zoneMot=ZoneAffichage(self,80,20)
        self.__zoneMot.pack(side=TOP,padx=30,pady=5)
        self.__zoneMot.configure(bg="white")
        
        
        #mot à écrire qui est une étiquette
        self.__mot=Label(self.__zoneMot,text='Mot :')
        self.__mot.pack(side=LEFT, padx=5,pady=5)
        
###on définit le clavier (est ce une frame ou une zone d'affichage?)
        self.__clavier=ZoneAffichage(self,400,100)
        self.__clavier.pack(side=BOTTOM,padx=10,pady=10)
     
        #création des 26 boutons du clavier
        self.__buttonList=[]
        for i in range(0,26):
            #chaque bouton est un élément de la classe MonBoutonLettre
            self.__buttoni=Button(self.__clavier,text = chr(ord('A')+i)) #la commande t = chr(ord('A')+i) transforme un entier en une chaîne de caractère
            self.__buttonList.append(self.__buttoni)
            self.__buttoni.config(state=DISABLED) #à l'ouverture de la page, tous les boutons sont grisés
            #on les met mtn en forme de clavier classique grâce à la commande grid
            if i<21 :#il y a 7 lettres par ligne et 3 lignes complètes donc 21 lettres à placer en haut
                self.__buttoni.grid(row=i//7,column=i%7) 
            else:
                self.__buttoni.grid(row=4,column=i%7+1) #on met à part les lettres qu'on a tout en bas du clavier, qui sont séparés d'un trou de la frame
        
        
###on implémente le comportement des boutons
        
        #bouton quitter
        self.__buttonQuit.config(command=self.destroy)
        
        #bouton Nouvelle Partie
        self.__buttonNouvellePartie.config(state=NORMAL) #on dégrise toutes les lettres 
        self.__buttonNouvellePartie.config(command=self.__zoneMot.tirageMot) #on choisi un mot aléatoirement pour le pendu
        
        
        #les boutons du clavier lors du jeu doivent se griser si sélectionnés
        
        
        

        
 
    
    
        
 ###DEF DE LA CLASSE ZoneAffichage
 
        
class ZoneAffichage(Canvas):
    def __init__(self, parent, largeur, hauteur):
        Canvas.__init__(self, parent, width=largeur, height=hauteur)
        self.__formes=[] #on va stocker nos formes du pendu dans cette liste


###on s'occupe de la partie du dessin du pendu

        #on crée les formes qui constituent le pendu
        
        # Base, Poteau, Traverse, Corde
        Rectangle(self, 50,  270, 200,  26, "beige")
        Rectangle(self, 87,   83,  26, 200, "brown")
        Rectangle(self, 87,   70, 150,  26, "brown")
        Rectangle(self, 183,  67,  10,  40, "brown")
        
        # Tete, Tronc
        Rectangle(self, 188, 120,  20,  20, "black")
        Rectangle(self, 175, 143,  26,  60, "black")
        
        # Bras gauche et droit
        Rectangle(self, 133, 150,  40,  10, "black")
        Rectangle(self, 203, 150,  40,  10, "black")
        
        # Jambes gauche et droite
        Rectangle(self, 175, 205,  10,  40, "black")
        Rectangle(self, 191, 205,  10,  40, "black")
        
    def chargeMots(self): #charge la liste des mots possibles
        open('mots.txt', 'r')
        s= f.read()
        self.__mots = s.split('\n')
        f.close()
        return self.__mots
        
    def tirageMot(self): #réussir à tirer un mot au hasard parmi la liste de chargeMots
        i=randint(1,100)
        l=self.__mots
        return l[i] #on retourne au hasard le ième élément de la liste des mots de la fonction chargeMots
    
 
    
    

    
    

    
    
    
###CREATION DE LA CLASSE MonBoutonLettre

class MonBoutonLettre(Button):
    def __init__(self,text):
        Button.__init__(self,text)
        
    
    



        
if __name__ == "__main__":
	fen = FenPrincipale()
	fen.mainloop()        
        