from tkinter import *
from random import randint
from formes import *

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)

		# configuration de la fenêtre
        self.title('Jeu du pendu')
        self.geometry('500x600+400+100')
        
        #liste des opérations
        self.__operation=[]
		# Touches du haut
        self.__bBox = Frame(self,bg='#eeeeee')
        self.__bBox.pack(side=TOP, padx=10, pady=10)

        self.__bNewGame = Button(self.__bBox, text=' Nouvelle partie ', bg='#884400', fg='white')
        self.__bNewGame.pack(side=LEFT, padx=5, pady=0)

        self.__bQuit = Button(self.__bBox, text=' Quitter ', bg='#884400', fg='white')
        self.__bQuit.pack(side=LEFT, padx=5, pady=0)

		# mise en place du comportement des touches ded contrôle
        self.__bQuit.config(command=self.destroy)
        self.__bNewGame.config(command=self.nouvellePartie)

		# Zone de dessin
        self.__pendu = ZoneAffichage(self, width=480, height=380, bg='#aaaaaa')
        self.__pendu.pack(side=TOP, padx=10, pady=0)

		# Mot à trouver
        self.__displayText = StringVar()
        self.__displayText.set('Sélectionner "Nouvelle Partie"')
        self.__display = Label(self,  textvariable=self.__displayText)
        self.__display.config(font=("Consolas",12))
        self.__display.pack(side=TOP, padx=5, pady=5)
    

        # Bouton undo
        self.__bBoxMid=Frame(self,bg='white')
        self.__bBoxMid.pack(side=TOP,padx=10,pady=10)
        
        self.__buttonUndo=Button(self.__bBoxMid,text='Undo')
        self.__buttonUndo.pack()
        #self.__buttonUndo.config(command=self.undo)
        
		# Clavier
        self.__kbd = Frame(self,bg='#eeeeee')
        self.__kbd.pack(side=TOP, padx=10, pady=(0,10))

        self.__touches = []
        for i in range(26):
            t = MonBoutonLettre(self.__kbd, text=chr(ord('A')+i) , width=7, bg='#cccccc')
            t.grid(column=i%7 + (1 if i>20 else 0), row=i//7, padx=2, pady=2)
            t.config(state=DISABLED, command=self.traitement)
            self.__touches.append(t)

		# Lecture du fichier de mots
        f = open('mots.txt', 'r')
        s = f.read()
        self.__mots = s.split('\n')
        f.close()
######EXERCICE 7
        ###on définit la barre d'outils qui est une Frame
        self.__barreOutils=Frame(self,bg="white")
        self.__barreOutils.pack(side=TOP,padx=10,pady=10)
        
        # #on définit les boutons de la barre d'outils
        # self.__buttonNouvellePartie = Button(self.__barreOutils, text='Nouvelle partie')
        # self.__buttonNouvellePartie.pack(side=LEFT, padx=5, pady=5)

        # self.__buttonQuit = Button(self.__barreOutils, text='Quitter')
        # self.__buttonQuit.pack(side=LEFT, padx=5, pady=5)
        
        # ###on rajoute un bouton pour faire apparaitre un menu déroulant dans le but de pouvoir personnaliser les couleurs de l'interface
        # self.__buttonMenu = Button(self.__barreOutils,text='Personnaliser')
        # self.__buttonMenu.pack(side=LEFT, padx=10,pady=10)
        # self.__buttonMenu.config(bg='grey')
        # self.__buttonMenu.config(command=self.proposerMenu)

        # #on crée une frame dans laquelle on va ranger les boutons de personnalisation        

        # self.__menu=Frame(FenPrincipale,bg='black')
        
        # #on implémente les différents boutons pour changer les couleurs
        
        # self.__buttonColorFP = Button(self.__menu, text='CouleurFenPrin')
        # self.__buttonColorFP.pack(side=LEFT, padx=5, pady=5)
        # self.__buttonColorFP.config(command=self.selectColor)
        
        # self.__buttonColorZA = Button(self.__menu, text='CouleurZoneAff')
        # self.__buttonColorZA.pack(side=LEFT, padx=5, pady=5)
        # self.__buttonColorZA.config(command=self.selectColor)
        
        # self.__buttonColorCL = Button(self.__menu, text='CouleurClavier')
        # self.__buttonColorCL.pack(side=LEFT, padx=5, pady=5)
        # self.__buttonColorCL.config(command=self.selectColor)
        
    def selectColor(self):
    	color = colorchooser.askcolor(color=None)
    	self.__zoneAffichage.setColor(color[1])
    	print(color[1])
        
    def nouvellePartie(self):
		# nouveau mot à trouver
        self.__motMystere = self.__mots[randint(0,len(self.__mots))]
        self.__motCache = '*'*len(self.__motMystere)
        self.afficheMot()

		# réactivation des touches du clavier
        for t in self.__touches:
            t.config(state=NORMAL)

		# effacement du pendu
        self.__erreurs = 0
        self.__pendu.tracer(0)

    def afficheMot(self):
        self.__displayText.set('Mot à trouver : ' + self.__motCache)


    def traitement(self,lettre):

		# mise à jour du mot caché (contenant les *)
        nouveauMotCache = ''
        for i,c in enumerate(self.__motMystere):
            if c == lettre:
                nouveauMotCache += lettre
            else:
                nouveauMotCache += self.__motCache[i]

		# nombre d'erreurs et mise à jour du pendu
            if self.__motCache == nouveauMotCache:
                self.__erreurs += 1
                self.__pendu.tracer(self.__erreurs)

		# affichage du mot caché mis à jour
        self.__motCache = nouveauMotCache
        self.afficheMot()

		# a-t-on gagné ?
        if not '*' in self.__motCache:
            self.partieGagnee()

		# a-t-on perdu ?
        if self.__erreurs > 9:
            self.partiePerdue()

    def partieGagnee(self):
        self.__displayText.set('Gagné ! Le mot était: '+self.__motCache)
        self.griserClavier()

    def partiePerdue(self):
        self.__displayText.set('Perdu ! Le mot était: '+self.__motMystere)
        self.griserClavier()

    def griserClavier(self):
        for t in self.__touches:
            t.config(state=DISABLED)
            
    def undo(self):
        m
        

class ZoneAffichage(Canvas):

	def __init__(self,*args,**kwargs):
		# on appelle le constructeur de la classe mère avec la même liste
		# d'arguments (args) et les mêmes arguments nommés (kwargs) que
		# ceux qu'on a nous-même reçus...
		Canvas.__init__(self, *args, **kwargs)

		self.__items = []

		# Base, Poteau, Traverse, Corde
		self.__items.append(Rectangle(self, 50,  270, 200,  26, "saddlebrown"))
		self.__items.append(Rectangle(self, 87,   83,  26, 200, "saddlebrown"))
		self.__items.append(Rectangle(self, 87,   70, 150,  26, "saddlebrown"))
		self.__items.append(Rectangle(self, 188,  67,  5,  60, "orange"))

		# Tete, Tronc
		self.__items.append(Ellipse(self, 198, 125,  15,  15, "red"))
		self.__items.append(Rectangle(self, 175, 143,  26,  60, "black"))

		# Bras gauche et droit
		self.__items.append(Rectangle(self, 133, 150,  40, 10, "pink"))
		self.__items.append(Rectangle(self, 203, 150,  40,  10, "pink"))

		# Jambes gauche et droite
		self.__items.append(Rectangle(self, 175, 205,  10,  40, "navy"))
		self.__items.append(Rectangle(self, 191, 205,  10,  40, "navy"))

		# on recentre le pendu
		for i in self.__items:
			i.deplacement(80,0)

	def tracer(self,n):
		for i in range(10):
			s = 'normal' if i < n else 'hidden'
			self.__items[i].set_state(s)

class MonBoutonLettre(Button):
    def __init__(self,*args,**kwargs):
        Button.__init__(self, *args, **kwargs)
        self.config(**kwargs)

    def config(self,**kwargs):
        Button.config(self, **kwargs)
        if 'text' in kwargs:
            self.__lettre = kwargs['text']
        if 'command' in kwargs:
            self.__command = kwargs['command']
            Button.config(self, command=self.cliquer)


    def cliquer(self):
        self.config(state=DISABLED)
        self.__command(self.__lettre)
        self.__opearions.append(self.__lettre)


    def selectColor(self):
    	color = colorchooser.askcolor(color=None)
    	self.__zoneAffichage.setColor(color[1])
    	print(color[1])



if __name__ == '__main__':
	fen = FenPrincipale()
	fen.mainloop()
