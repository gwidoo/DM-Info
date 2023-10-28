from tkinter import *
from tkinter import colorchooser
from zoneaffichage import *
from random import randint
from monboutonlettre import *

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="black")
        
    #configuration de la fenêtre
        self.geometry('500x500+400+400')
        self.title('Jeu du pendu')
        
    #Frame    
        self.__bBoxTop = Frame(self, bg="white")
        self.__bBoxTop.pack(side=TOP,padx=10,pady=10)
        
    #Boutons
        self.__buttonQuit=Button(self.__bBoxTop,text='Quitter')
        self.__buttonQuit.pack(side=RIGHT, padx=5, pady=5)
        self.__buttonQuit.config(command=self.destroy)
        

        
        self.__buttonNew=Button(self.__bBoxTop,text='Nouvelle Partie')
        self.__buttonNew.pack(side=LEFT,padx=5,pady=5)
        self.__buttonNew.config(command=self.nouvelle_partie)
        
        self.__bBoxBot = Frame(self, bg="white")
        self.__bBoxBot.pack(side=BOTTOM,padx=10,pady=10)
        
        self.__bBoxMid=Frame(self,bg='white')
        self.__bBoxMid.pack(side=BOTTOM,padx=10,pady=10)
        
        self.__buttonUndo=Button(self.__bBoxMid,text='Undo')
        self.__buttonUndo.pack()
        #self.__buttonUndo.config(command=self.undo)

        self.__motaffiche = StringVar()
        labelResultat = Label(self, textvariable=self.__motaffiche)
        labelResultat.pack(side=BOTTOM, padx=5, pady=5)

        self.__operations=[]
    #Zone Affichages   
        self.__zoneAffiche = ZoneAffichage(self,400,300)
        self.__zoneAffiche.pack(side=TOP, padx=10, pady=10)
        
        # self.__zonemot=ZoneAffichage(self,80,20)
        # self.__zonemot.pack(side=TOP,padx=10,pady=10)
        # self.__zonemot.configure(bg='white')
        self.__boutons=[]
        self.chargeMots()
        
    #config clavier
        for i in range(26):
            t=chr(ord('A')+i)
            self.__buttonLetter=Button(self.__bBoxBot,text='{}'.format(t))
            self.__boutons.append(self.__buttonLetter)
            self.__buttonLetter.config(state=DISABLED)
            self.__boutons[i].grid(row=i//7,column=i%7 +(1 if i>20 else 0),padx=2,pady=2)
            #self.__buttonLetter.config(command=MonBoutonLettre.cliquer(self.__lettre))
            
            #lecture du dico
    def chargeMots(self):
        f=open('mots.txt', 'r')
        s=f.read()
        self.__mots = s.split('\n')
        f.close()

    def nouvelle_partie(self):
        i=randint(0,len(self.__mots))
        self.__mot = self.__mots[i]
        for a in self.__boutons:
            a.config(state=NORMAL)
        self.__motCache='*'*len(self.__mot)
        self.affiche_mot()
        self.efface_pendu()
        self.__compteur=0
    def affiche_mot(self):
        self.__motaffiche.set('Mot:'+self.__motCache)
    
    def efface_pendu(self):
        pass
         
    # def traitement(self,lettre):
    #     l=[]
    #     for a in self.__mot:
    #         if lettre==a:
    #             l.append(self.__mot.index(a))
    #     if l==[]:
    #         self.__compteur+=1
    #     else:
    #         for i in l:
    #             self.__motaffiche[i]=a
    #     if self.__compteur==10:
    #         for b in self.__boutons:
    #             b.config(state=DISABLED)
    #         self.__motaffiche.set('Perdu, le mot était: '+self.__mot)
    #     if self.__motaffiche==self.__mot:
    #         for b in self.__boutons:
    #             b.config(state=DISABLED)
    #         self.__motaffiche.set('Gagné! Le mot était bien: '+self.__mot)
                
    #def undo(self):
        
            

    
if __name__ == '__main__':
	fen = FenPrincipale()
	fen.mainloop()
