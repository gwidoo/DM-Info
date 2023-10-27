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
#problème lors  de la création des pièces du dessin du pendu et aussi du set.state

###DEF DE LA CLASSE FenPrincipale


class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="purple") #on colore la fenêtre prinicipale en rose
        self.title('Jeu du pendu') #on nomme la fenêtre principale
        
        #on charge le fichier de mots chargeMots
        self.__mots=self.chargeMots() #on récupère la liste de la fonction
        
        
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
        
###on définit la zone du mot à découvrir qui est une zone d'affichage
        self.__zoneMot=ZoneAffichage(self,80,20)
        self.__zoneMot.pack(side=TOP,padx=30,pady=5)
        self.__zoneMot.configure(bg="white")
        
        
        #mot à écrire qui est une étiquette
        self.__MotComplete=Label(self.__zoneMot,text='Mot :')
        self.__MotComplete.pack(side=LEFT, padx=5,pady=5)
        
###on définit le clavier qui est une frame 
        self.__clavier=Frame(self,bg='white')
        self.__clavier.pack(side=BOTTOM,padx=10,pady=10)
     
        #création des 26 boutons du clavier
        self.__boutons=[]
        for i in range(0,26):
            #chaque bouton est un élément de la classe MonBoutonLettre
            self.__buttoni=MonBoutonLettre(parent, fenetre, a)Button(self.__clavier,text = chr(ord('A')+i)) #la commande t = chr(ord('A')+i) transforme un entier en une chaîne de caractère
            self.__boutons.append(self.__buttoni)
            self.__buttoni.config(state=DISABLED) #à l'ouverture de la page, tous les boutons sont grisés
            self.__buttoni.config(command=self.select)
            
            #on les met mtn en forme de clavier classique grâce à la commande grid
            if i<21 :#il y a 7 lettres par ligne et 3 lignes complètes donc 21 lettres à placer en haut
                self.__buttoni.grid(row=i//7,column=i%7)  #grid est une nouvelle méthode de ranger, plus pratique ici que pack
            else:
                self.__buttoni.grid(row=4,column=i%7+1) #on met à part les lettres qu'on a tout en bas du clavier, qui sont séparés d'un trou de la frame
    
    
    
    def select(self,lettre):
        print('Sélection de la lettre'+lettre)
        
        
        
###on implémente le comportement des boutons
        
        #bouton quitter
        self.__buttonQuit.config(command=self.destroy)
        
        #bouton Nouvelle Partie
        self.__buttonNouvellePartie.config(command=self.nouvellePartie)
        
        
        #on définit les fonctions relatives aux fonctionnement du jeu
        
        
    def chargeMots(self): #charge la liste des mots possibles
        f=open('mots.txt', 'r')
        s= f.read()
        self.__mots = s.split('\n')
        f.close()
            
        
    def nouvellePartie(self):
        #on charge self.__mots et on tire un mot aux hasard dans self.__mots
        n=randint(0,len(self.__mots)-1) #on choisit au hasard un entier entre 0 et le nombre de mots possibles
        self.__motMystere=self.__mots[n] #on récupère le mot choisi aléatoirement parmi la liste self.__mots
            
        #on réinitialise le mot à découvrir
        self.__motCache=len(self.__motMystere)*'_'
        self.__MotComplete.config(text='Mot : ' + self.__motCache) #on modifie le texte à afficher en dessous de la zone d'affichage du pendu
            
        #on dégrise les boutons lettres du clavier
        for i in range(26):
            self.__boutons[i].config(state=NORMAL)
                
        #on efface le dessin du pendu précédent
        self.cacheFormes()
      
        
    def traitement(self,lettre):
        print('Sélection de la lettre' + lettre)
        nouveauMotCache=''
        for i,c in enumerate(self.__motMystere):
            if c==lettre:
                nouveauMotCache+=lettre
            else: 
                nouveauMotCache+= self.__motCache[i]
        self.__motCache=nouveauMotCache
        self.afficheMot()

        #on regarde si on a gagné 
        if not'_' in self.__motCache :
            self.partieGagnee()
            
    def afficheMot(self):
        self.__MotComplete.set(text='Mot : ' + self.__motCache)
            
    def partieGagnee(self):
        self.__motCache= 'Victoire ! Le mot était : '+self.__motMystere
        self.afficheMot()
        
 ###DEF DE LA CLASSE ZoneAffichage
 
        
class ZoneAffichage(Canvas):
    def __init__(self, parent, largeur, hauteur):
        Canvas.__init__(self, parent, width=largeur, height=hauteur)
        self.__listeFormes=[] #on va stocker nos formes du pendu dans cette liste


##on s'occupe de la partie du dessin du pendu

###on ajoute les formes qui constituent le pendu à la liste des formes
        
        # Base, Poteau, Traverse, Corde
        self.__listeFormes.append(Rectangle(self, 50,  270, 200,  26, "beige"))
        self.__listeFormes.append(Rectangle(self, 87,   83,  26, 200, "beige"))
        self.__listeFormes.append(Rectangle(self, 87,   70, 150,  26, "beige"))
        self.__listeFormes.append(Rectangle(self, 183,  67,  10,  40, "beige"))
        
        # Tete, Tronc
        self.__listeFormes.append(Rectangle(self, 178, 120,  20,  20, "black"))
        self.__listeFormes.append(Rectangle(self, 175, 143,  26,  60, "black"))
        
        # Bras gauche et droit
        self.__listeFormes.append(Rectangle(self, 163, 150,  10,  40, "black"))
        self.__listeFormes.append(Rectangle(self, 203, 150,  10,  40, "black"))
        
        # Jambes gauche et droite
        self.__listeFormes.append(Rectangle(self, 175, 205,  10,  40, "black"))
        self.__listeFormes.append(Rectangle(self, 191, 205,  10,  40, "black"))
        
        #au lancement de la partie, toutes les formes du pendu sont cachées
        self.cacheFormes()
    
###on crée les fonctions qui permettent de cacher (au début) ou de faire apparaître les formes du pendu 
    def cacheFormes(self):
        for i in range(len(self.__listeFormes)) :
            self.__listeFormes[i].set_state('hidden')
            
    def dessinePendu(self,i):
        if i <=len(self.__listeFormes): #i correspond au numéro de la forme attribué en fonction de son ordre d'apparition
            self.__listeFormes[i].set_state('normal') #on décache seulement la ième forme de la liste des formes 
                
        
   
    
###CREATION DE LA CLASSE MonBoutonLettre

class MonBoutonLettre(Button):
    def __init__(self,parent,fenetre,a):
        Button.__init__(self,parent,text=t,state=DISABLED)
        self.__fenetre=fenetre
        self.__lettre=a #notre bouton est associé à une unique lettre de l'alphabet
        
        
        
        #on initialise une nouvelle partie
        self.nouvellePartie() 
        
    def cliquer(self):
        self.config(state=DISABLED)
        self.__fenetre.traitement(self.__text) #lorsqu'on clique sur le bouton, on appelle traitement, définit dans FenPrincipale
        
        
     
    



        
if __name__ == "__main__":
	fen = FenPrincipale()
	fen.mainloop()        
        