
from tkinter import *
from tkinter import colorchooser
from random import randint
from formes import *

###DEF DE LA CLASSE FenPrincipale

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="pink") 
        self.title('Jeu du pendu') 
        
###on définit la barre d'outils qui est une Frame
        self.__barreOutils=Frame(self,bg="white")
        self.__barreOutils.pack(side=TOP,padx=10,pady=10)
        
        #on définit les boutons de la barre d'outils
        self.__buttonNouvellePartie = Button(self.__barreOutils, text='Nouvelle partie')
        self.__buttonNouvellePartie.pack(side=LEFT, padx=5, pady=5)

        self.__buttonQuit = Button(self.__barreOutils, text='Quitter')
        self.__buttonQuit.pack(side=LEFT, padx=5, pady=5)
        
        self.__buttonUndo = Button(self.__barreOutils, text='Undo')
        self.__buttonUndo.pack(side=LEFT, padx=5, pady=5)
        
        # création de la liste des opérations
        self.__operation=[]
        
        #on implémente le comportement des boutons
        self.__buttonQuit.config(command=self.destroy)
        self.__buttonNouvellePartie.config(command=self.nouvellePartie)
        self.__buttonUndo.config(command=self.undo)
        
###on définit la grande zone d'affichage du pendu
        self.__zoneAffichage=ZoneAffichage(self,width=400,height=300,bg='#aaaaaa')
        self.__zoneAffichage.pack(side=TOP,padx=10,pady=0)
        self.__zoneAffichage.configure(bg="white")
        
###on définit le mot à découvrir      
        self.chargeMots()
        self.__displayText = StringVar()
        self.__displayText.set("Personnaliser au moins un élément de l'interface puis sélectionner 'Nouvelle Partie'")
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

#<<<<<<< Updated upstream
###on rajoute un bouton pour faire apparaître un menu déroulant dans le but de pouvoir personnaliser les couleurs de l'interface
        self.__buttonMenu = Menubutton(self.__barreOutils,text='Personnaliser')
        self.__buttonMenu.pack(side=LEFT, padx=10,pady=10)
        self.__buttonMenu.config(bg='black',fg='white')

        #création du menu déroulant    
        #on rajoute la commande lambda dans la commande pour éviter que la fonction soit appelée au lancement du jeu
        self.__menuDeroulant=Menu(self.__buttonMenu)
        self.__menuDeroulant.add_command(label='Couleur Fenêtre Principale', command = lambda : self.modifierColorInterface(0))
        self.__menuDeroulant.add_command(label='Couleur Zone Affichage', command = lambda : self.modifierColorInterface(1))
        self.__menuDeroulant.add_command(label='Couleur Clavier', command = lambda : self.modifierColorInterface(2))
        self.__menuDeroulant.add_command(label='Couleur Nouvelle Partie', command = lambda : self.modifierColorInterface(3))
        self.__menuDeroulant.add_command(label='Couleur Quitter', command = lambda : self.modifierColorInterface(4))
        self.__menuDeroulant.add_command(label='Couleur Undo', command = lambda : self.modifierColorInterface(5))
        self.__menuDeroulant.add_command(label='Couleur Bonhomme', command = self.modifierColorCanvas)
        self.__buttonMenu.configure(menu=self.__menuDeroulant)
        
        
    def modifierColorCanvas(self):   
        color = colorchooser.askcolor(color=None)
        #on vérifie que la couleur a été choisie
        if color[1] : 
            #on ne récupère que les formes du corps
            for i in range(4,10): 
                self.__zoneAffichage.itemconfig(self.__zoneAffichage.__listeFormes[i],fill=color[1])
        
        
        
    def modifierColorInterface(self,i):
        #on crée une liste de tous les éléments dont la couleur est modifiable
        list=[self,self.__zoneAffichage,self.__clavier,self.__buttonNouvellePartie,self.__buttonQuit,self.__buttonUndo]
        color = colorchooser.askcolor(color=None)
        if color[1]:
            list[i].config(bg=color[1])
            
###FIN DE L'EXERCICE 7        

#charge la liste des mots possibles, enregistrés dans un fichier txt
#=======
        self.__menu=Frame(FenPrincipale,bg='black')
        
        #on implémente les différents boutons pour changer les couleurs
        
        self.__buttonColorFP = Button(self.__menu, text='CouleurFenPrin')
        self.__buttonColorFP.pack(side=LEFT, padx=5, pady=5)
        self.__buttonColorFP.config(command=self.selectColor)
        
        self.__buttonColorZA = Button(self.__menu, text='CouleurZoneAff')
        self.__buttonColorZA.pack(side=LEFT, padx=5, pady=5)
        self.__buttonColorZA.config(command=self.selectColor)
        
        self.__buttonColorCL = Button(self.__menu, text='CouleurClavier')
        self.__buttonColorCL.pack(side=LEFT, padx=5, pady=5)
        self.__buttonColorCL.config(command=self.selectColor)
        
    def selectColor(self):
    	color = colorchooser.askcolor(color=None)
    	self.__zoneAffichage.setColor(color[1])
    	print(color[1])
        
        
    def cliquer(self):
        self.config(state=DISABLED)
        self.__command(self.__lettre)
        self.__operation.append(self.__lettre)
        
        
        #on définit les fonctions relatives aux fonctionnement du jeu
        
        
    def chargeMots(self): #charge la liste des mots possibles
#>>>>>>> Stashed changes
        f=open('mots.txt', 'r')
        s= f.read()
        self.__mots = s.split('\n')
        f.close()
               
    def nouvellePartie(self):
        #on charge self.__mots et on tire un mot aux hasard dans self.__mots
        #on récupère le mot choisi aléatoirement parmi la liste self.__mots
        self.__motMystere=self.__mots[randint(0,len(self.__mots))] 
        self.__motCache=len(self.__motMystere)*'*' 
        self.afficheMot() 
        
        #on dégrise les boutons lettres du clavier et le bouton undo
        for i in self.__boutons:
            i.config(state=NORMAL)
        self.__buttonUndo.config(state=NORMAL)
                
        #on efface le dessin du pendu précédent
        self.__erreurs= 0
        self.__zoneAffichage.tracer(0)
      
    def afficheMot(self):
        self.__displayText.set('Mot : ' + self.__motCache)
                
            
    def traitement(self,lettre):
		# mise à jour du mot caché (contenant les *)
        nouveauMotCache = ''
        self.__operation.append(lettre)
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
        if not '*' in self.__motCache:
            self.partieGagnee()
		
		# a-t-on perdu ?
        if self.__erreurs > 9:
            self.partiePerdue()
			
    def partieGagnee(self):
        self.__displayText.set('Bravo, tu as gagné ! Le mot était: '+self.__motMystere) 
        self.griserClavier()
        self.__buttonUndo.config(state=DISABLED)
	
    def partiePerdue(self):
        self.__displayText.set('Perdu, essaie encore ! Le mot était: '+self.__motMystere)
        self.griserClavier()
        self.__buttonUndo.config(state=DISABLED)
	
    def griserClavier(self):
        for t in self.__boutons:
            t.config(state=DISABLED)
            
    def undo(self):
        if self.__operation==[]:
            self.__displayText.set('Il faudrait jouer avant de revenir en arrière! Mot:'+self.__motCache)
        else:
            l=self.__operation.pop()
            i=ord(l)-65
            self.__boutons[i].config(state=NORMAL)
            if l in self.__motMystere:
                for j in range(len(self.__motCache)):
                    if l==self.__motCache[j]:
                        self.__motCache=self.__motCache[0:j]+'*'+self.__motCache[j+1:len(self.__motCache)]
                        self.afficheMot()
            else:
                self.__erreurs-=1
                self.__zoneAffichage.cacheFormes()
                self.__zoneAffichage.tracer(self.__erreurs)
                self.afficheMot()
                
 ###DEF DE LA CLASSE ZoneAffichage
 
        
class ZoneAffichage(Canvas):
    def __init__(self,*args,**kwargs):
	# on appelle le constructeur de la classe mère avec la même liste
	# d'arguments (args) et les mêmes arguments nommés (kwargs) que
	# ceux qu'on a nous-même reçus...
        Canvas.__init__(self, *args, **kwargs)
        self.__listeFormes=[] 

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
        self.__listeFormes.append(Ellipse(self, 168, 170,  5,  25, "black"))
        self.__listeFormes.append(Ellipse(self, 208, 170,  5,  25, "black"))
        
        # Jambes gauche et droite
        self.__listeFormes.append(Rectangle(self, 175, 205,  10,  40, "black"))
        self.__listeFormes.append(Rectangle(self, 191, 205,  10,  40, "black"))
    
        #on cache toutes les formes au début 
        self.cacheFormes()
        
    def cacheFormes(self):
        for i in self.__listeFormes:
            i.set_state('hidden')
    
    def cachederniereforme(self):
        l=self.__listeFormes.pop()
        l.set_state('hidden')
            
    def setColor(self,color):
        self.__couleur = color
        
    #on trace le pendu au fur et à mesure    
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
        #quand on clique sur le bouton pour choisir une lettre, celui-ci se grise ensuite
        self.config(state=DISABLED) 
        self.__command(self.__lettre)

if __name__ == "__main__":
	fen = FenPrincipale()
	fen.mainloop()        
        