
from tkinter import *
from tkinter import colorchooser
from random import randint
from formes import *

###DEF DE LA CLASSE FenPrincipale

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="pink") #on colore la fenêtre prinicipale en rose
        self.title('Jeu du pendu') #on nomme la fenêtre principale
        
###on définit la barre d'outils qui est une Frame
        self.__barreOutils=Frame(self,bg="white")
        self.__barreOutils.pack(side=TOP,padx=10,pady=10)
        
        #on définit les boutons de la barre d'outils
        self.__buttonNouvellePartie = Button(self.__barreOutils, text='Nouvelle partie')
        self.__buttonNouvellePartie.pack(side=LEFT, padx=5, pady=5)

        self.__buttonQuit = Button(self.__barreOutils, text='Quitter')
        self.__buttonQuit.pack(side=LEFT, padx=5, pady=5)
        
        #on implémente le comportement des boutons
        
        self.__buttonQuit.config(command=self.destroy)
        self.__buttonNouvellePartie.config(command=self.nouvellePartie)
        
###on définit la grande zone d'affichage du pendu
        self.__zoneAffichage=ZoneAffichage(self,width=400,height=300,bg='#aaaaaa')
        self.__zoneAffichage.pack(side=TOP,padx=10,pady=0)
        self.__zoneAffichage.configure(bg="white")
        
###on définit le mot à découvrir      
        self.__displayText = StringVar()
        self.__displayText.set('Sélectionner "Nouvelle Partie"')
        self.__display = Label(self,  textvariable=self.__displayText)
        self.__display.pack(side=TOP, padx=5, pady=5)
               
###on définit le clavier qui est une frame 
        self.__clavier=Frame(self,bg='white')
        self.__clavier.pack(side=BOTTOM,padx=10,pady=10)
     
        #création des 26 boutons du clavier
        self.__boutons = []
        for i in range(26):
            t= MonBoutonLettre(self.__clavier, text=chr(ord('A')+i) , width=7, bg='#cccccc')
            t.grid(column=i%7 + (1 if i>20 else 0), row=i//7, padx=2, pady=2)
            t.config(state=DISABLED, command=self.traitement)
            self.__boutons.append(t)

###EXERCICE 7   

###on rajoute un bouton pour faire apparaître un menu déroulant dans le but de pouvoir personnaliser les couleurs de l'interface
        self.__buttonMenu = Menubutton(self.__barreOutils,text='Personnaliser')
        self.__buttonMenu.pack(side=LEFT, padx=10,pady=10)
        self.__buttonMenu.config(bg='grey')

        #création du menu déroulant         
        self.__menuDeroulant1=Menu(self.__buttonMenu)
        # self.__menuDeroulant1.add_command(label='CouleurFenPrin', command = self.selectColor)
        # self.__menuDeroulant1.add_command(label='CouleurZoneAff', command = self.selectColor)
        # self.__menuDeroulant1.add_command(label='CouleurClavier', command = self.selectColor)
        # self.__menuDeroulant1.add_command(label='CouleurNouvellePartie', command = self.selectColor)
        # self.__menuDeroulant1.add_command(label='CouleurQuitter', command = self.selectColor)
        # self.__menuDeroulant1.add_command(label='CouleurUndo', command = self.selectColor)
        self.__menuDeroulant1.add_command(label='CouleurBonhomme', command = self.modifierColorCanvas)
        self.__buttonMenu.configure(menu=self.__menuDeroulant1)
        
        
     
 #    def proposerMenu(self):
 # #on crée une frame dans laquelle on va ranger les boutons de personnalisation        
 #        self.__menu=Frame(self.__barreOutils,bg='black')
        
 #        #on implémente les différents boutons pour changer les couleurs
 #        #Fenêtre Principale
 #        self.__buttonColorFP = Button(self.__menu, text='CouleurFenPrin')
 #        self.__buttonColorFP.pack(side=LEFT, padx=5, pady=5)
 #        self.__buttonColorFP.config(command=self.selectColor)
        
 #        #Zone d'affichage
 #        self.__buttonColorZA = Button(self.__menu, text='CouleurZoneAff')
 #        self.__buttonColorZA.pack(side=LEFT, padx=5, pady=5)
 #        self.__buttonColorZA.config(command=self.selectColor)
        
 #        # #Clavier
 #        self.__buttonColorCL = Button(self.__menu, text='CouleurClavier')
 #        self.__buttonColorCL.pack(side=LEFT, padx=5, pady=5)
 #        self.__buttonColorCL.config(command=self.selectColor)
        
 #        # #Nouvelle Partie
 #        self.__buttonColorNouvellePartie = Button(self.__menu, text='CouleurNouvellePartie')
 #        self.__buttonColorNouvellePartie.pack(side=LEFT, padx=5, pady=5)
 #        self.__buttonColorNouvellePartie.config(command=self.selectColor)
        
 #        # #Quitter
 #        self.__buttonColorQuit = Button(self.__menu, text='CouleurQuitter')
 #        self.__buttonColorQuit.pack(side=LEFT, padx=5, pady=5)
 #        self.__buttonColorQuit.config(command=self.selectColor)
        
        
 #        #on teste déjà si cette façon de faire marche pr un bouton
 #        #Undo
 #        self.__buttonColorUndo= Button(self.__menu, text='CouleurUndo')
 #        self.__buttonColorUndo.pack(side=LEFT, padx=5, pady=5)
 #        self.__buttonColorUndo.config(command=self.selectColor(self.__buttonColorUndo))
        
 #        #Bonhomme
 #        self.__buttonColorBonhomme= Button(self.__menu, text='CouleurBonhomme')
 #        self.__buttonColorBonhomme.pack(side=LEFT, padx=5, pady=5)
 #        self.__buttonColorBonhomme.config(command=self.modifierColorCanvas)
        
        
    # def modifierColorCanvas(self):
    #     color = colorchooser.askcolor(color=None)
    #     self.__zoneAffichage.setColor(color[1])
    #     print(color[1])
        
    def modifierColorCanvas(self):    
        color = colorchooser.askcolor(color=None)
        for i in self.__listeFormes:
            i.setColor(color[1])
            print(color[1])
        
   
    # def selectColor(self,label):
    #     color = colorchooser.askcolor(color=None)
    #     self.__zoneAffichage.setColor(color[1])
    #     label.config(bg='color[1]')
        
###FIN DE L'EXERCICE 7        

#charge la liste des mots possibles, enregistrés dans un fichier txt
        f=open('mots.txt', 'r')
        s= f.read()
        self.__mots = s.split('\n')
        f.close()
               
    def nouvellePartie(self):
        #on charge self.__mots et on tire un mot aux hasard dans self.__mots
        self.__motMystere=self.__mots[randint(0,len(self.__mots))] #on récupère le mot choisi aléatoirement parmi la liste self.__mots
        self.__motCache=len(self.__motMystere)*'_' #on réinitialise le mot à découvrir
        self.afficheMot() #on modifie le texte à afficher en dessous de la zone d'affichage du pendu
            
        #on dégrise les boutons lettres du clavier
        for i in self.__boutons:
            i.config(state=NORMAL)
                
        #on efface le dessin du pendu précédent
        self.__erreurs= 0
        self.__zoneAffichage.tracer(0)
      
    def afficheMot(self):
        self.__displayText.set('Mot : ' + self.__motCache)
                
            
    def traitement(self,lettre):
		# mise à jour du mot caché (contenant les *)
        nouveauMotCache = ''
        for i,c in enumerate(self.__motMystere):
            if c== lettre:
                nouveauMotCache += lettre
            else:
                nouveauMotCache += self.__motCache[i]		
	
		# nombre d'erreurs et mise à jour du pendu
        if self.__motCache == nouveauMotCache:
            self.__erreurs += 1
            self.__zoneAffichage.tracer(self.__erreurs)

		# affichage du mot caché mis à jour
        self.__motCache = nouveauMotCache
        self.afficheMot()
			
		# a-t-on gagné ?
        if not '_' in self.__motCache:
            self.partieGagnee()
		
		# a-t-on perdu ?
        if self.__erreurs > 9:
            self.partiePerdue()
			
    def partieGagnee(self):
        self.__displayText.set('Victoire ! Le mot était: '+self.__motCache) #le motCache est a se stade le même que le mot mystère puisque toutes les lettres ont été trouvées
        self.griserClavier() #on grise le clavier car on revient la parti est finie, on ne peut plus 
	
    def partiePerdue(self):
        self.__displayText.set('Défaite ! Le mot était: '+self.__motMystere)
        self.griserClavier()
	
    def griserClavier(self):
        for t in self.__boutons:
            t.config(state=DISABLED)
         
 ###DEF DE LA CLASSE ZoneAffichage
 
        
class ZoneAffichage(Canvas):
    def __init__(self,*args,**kwargs):
	# on appelle le constructeur de la classe mère avec la même liste
	# d'arguments (args) et les mêmes arguments nommés (kwargs) que
	# ceux qu'on a nous-même reçus...
        Canvas.__init__(self, *args, **kwargs)
        self.__listeFormes=[] #on va stocker nos formes du pendu dans cette liste


###on ajoute les formes qui constituent le pendu à la liste des formes
        
        # Base, Poteau, Traverse, Corde
        self.__listeFormes.append(Rectangle(self, 50,  270, 200,  26, "beige"))
        self.__listeFormes.append(Rectangle(self, 87,   83,  26, 200, "beige"))
        self.__listeFormes.append(Rectangle(self, 87,   70, 150,  26, "beige"))
        self.__listeFormes.append(Rectangle(self, 183,  67,  10,  40, "beige"))
        
        # Tete, Tronc
        self.__listeFormes.append(Ellipse(self, 188, 125,  17,  17, "black"))
        self.__listeFormes.append(Rectangle(self, 175, 143,  26,  60, "black"))
        
        # Bras gauche et droit
        self.__listeFormes.append(Rectangle(self, 163, 150,  10,  40, "black"))
        self.__listeFormes.append(Rectangle(self, 203, 150,  10,  40, "black"))
        
        # Jambes gauche et droite
        self.__listeFormes.append(Rectangle(self, 175, 205,  10,  40, "black"))
        self.__listeFormes.append(Rectangle(self, 191, 205,  10,  40, "black"))
    
        #on cache toutes les formes au début 
        self.cacheFormes()
        
    def cacheFormes(self):
        for i in self.__listeFormes:
            i.set_state('hidden')
            
            
    def setColor(self,color):
        self.__couleur = color
        
        
    def tracer(self,n):
        for i in range(10):
            s = 'normal' if i < n else 'hidden'
            self.__listeFormes[i].set_state(s)     
   
    
###CREATION DE LA CLASSE MonBoutonLettre

class MonBoutonLettre(Button):
    def __init__(self,*args,**kwargs):
        Button.__init__(self, *args, **kwargs)
        self.config(**kwargs)
		
    def config(self,**kwargs):
        Button.config(self, **kwargs)
        if'text' in kwargs:
            self.__lettre = kwargs['text']
        if'command' in kwargs:
            self.__command = kwargs['command']
            Button.config(self, command=self.cliquer)
				
    def cliquer(self):
        self.config(state=DISABLED) #quand on clique sur le bouton pour choisir une lettre, celui-ci se grise ensuite
        self.__command(self.__lettre)
        
if __name__ == "__main__":
	fen = FenPrincipale()
	fen.mainloop()        
        