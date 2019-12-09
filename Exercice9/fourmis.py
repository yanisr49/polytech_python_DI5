from tkinter import *

class fourmis():

    def __init__(self):
        self.type_deplacement = "d" #d ou o
        self.couleurr = 10          #couleur rouge de la fourmis
        self.couleurg = 10          #couleur verte de la fourmis
        self.couleurb = 10          #couleur bleu de la fourmis
        self.suivir = 10            #couleur rouge suivie de la fourmis
        self.suivig = 10            #couleur verte suivie de la fourmis
        self.suivib = 10            #couleur bleu suivie de la fourmis
        self.probag = 0.4           #probabilité d'aller à gauche
        self.probad = 0.3           #probabilité d'aller à droite
        self.probat = 0.3           #probabilité d'aller tout droit
        self.probacoul = 0.5        #probabilité de suivre la couleur suivie
        self.seuil_luminescence = 40

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()


w.create_rectangle(50, 50, 400, 400, width=0, fill="red")


mainloop()