# Importation des bibliothèques Tkinter, messagebox et simpledialog
from tkinter import *
from tkinter import messagebox, simpledialog


# Définition de la classe Morpion qui hérite de la classe Frame
class Morpion(Frame):
  def __init__(self, master=None):
      super().__init__(master)
      self.master = master
      self.master.title("Jeu du Morpion")
# Initialisation des variables pour le jeu
      self.plateau = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
      self.joueurs = {"X": "", "O": ""}
      self.tour = 'X'
      self.jeu_en_cours = True
# Création de l'interface graphique
      self.creer_interface()




  def creer_interface(self):
# Création des boutons pour le plateau de jeu
      self.cases = []
      for i in range(9):
          case = Button(self.master, text="", font=("Helvetica", 36), width=3, height=1, command=lambda i=i: self.jouer_coup(i))
          case.grid(row=i//3, column=i%3)
          self.cases.append(case)
# Création d'un bouton pour commencer une nouvelle partie
      self.bouton_nouvelle_partie = Button(self.master, text="Nouvelle partie", font=("Helvetica", 18), width=15, command=self.nouvelle_partie)
      self.bouton_nouvelle_partie.grid(row=3, column=0, columnspan=3)
# Création d'un label pour afficher le nom du joueur actuel
      self.label_joueur = Label(self.master, text="", font=("Helvetica", 18))
      self.label_joueur.grid(row=4, column=0, columnspan=3)
# Définition des noms des joueurs
      self.definir_joueurs()
# Affichage du nom du joueur actuel
      self.afficher_joueur()


  def definir_joueurs(self):
# Demande des noms des joueurs à l'utilisateur
      joueur_x = simpledialog.askstring("Nom du joueur X", "Entrez le nom du joueur X")
      joueur_o = simpledialog.askstring("Nom du joueur O", "Entrez le nom du joueur O")
# Assignation des noms des joueurs
      if joueur_x:
          self.joueurs["X"] = joueur_x
      if joueur_o:
          self.joueurs["O"] = joueur_o


  def afficher_joueur(self):
# Affichage du nom du joueur actuel ou de la fin du jeu
      if self.jeu_en_cours:
          nom_joueur = self.joueurs[self.tour]
          self.master.title("Jeu du Morpion - Tour de " + nom_joueur)
          self.label_joueur.config(text="C'est au tour de " + nom_joueur)
      else:
          self.master.title("Jeu du Morpion - Fin de la partie")


  def jouer_coup(self, coup):
# Vérification si le jeu est en cours et si la case est vide
      if self.jeu_en_cours and self.plateau[coup] == " ":
# Jouer le coup en remplissant la case correspondante
          self.plateau[coup] = self.tour
          self.cases[coup].config(text=self.tour)
# Vérifiez si le joueur actuel a gagné la partie
          if self.gagne(self.plateau, self.tour):
              self.jeu_en_cours = False
              self.afficher_joueur()
              nom_joueur = self.joueurs[self.tour]
# Afficher une boîte de message annonçant le gagnant
              messagebox.showinfo("Fin de la partie", "Félicitations ! " + nom_joueur + " a gagné !")
# Si le plateau est plein et qu'aucun joueur n'a gagné, déclarer un match nul
          elif " " not in self.plateau:
              self.jeu_en_cours = False
              self.afficher_joueur()
# Afficher une boîte de message annonçant le tirage
              messagebox.showinfo("Fin de la partie", "Match nul !")
# Passer au tour du joueur suivant
          else:
              self.tour = 'O' if self.tour == 'X' else 'X'
              self.afficher_joueur()


# Réinitialisez le plateau de jeu et démarrez une nouvelle partie
  def nouvelle_partie(self):
                  self.plateau = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                  self.tour = 'X'
                  self.jeu_en_cours = True
# Effacer l'affichage du tableau
                  for i in range(9):
                      self.cases[i].config(text="")
# Afficher le tour du joueur actuel
                  self.afficher_joueur()


  def gagne(self, plateau, symbole):
# Check if the given symbol has won the game by checking all possible winning combinations
      return (plateau[0] == plateau[1] == plateau[2] == symbole or
              plateau[3] == plateau[4] == plateau[5] == symbole or
              plateau[6] == plateau[7] == plateau[8] == symbole or
              plateau[0] == plateau[3] == plateau[6] == symbole or
              plateau[1] == plateau[4] == plateau[7] == symbole or
              plateau[2] == plateau[5] == plateau[8] == symbole or
              plateau[0] == plateau[4] == plateau[8] == symbole or
              plateau[2] == plateau[4] == plateau[6] == symbole)




root = Tk()
# Create the Morpion game app and start the main loopm
app = Morpion(master=root)
app.mainloop()
