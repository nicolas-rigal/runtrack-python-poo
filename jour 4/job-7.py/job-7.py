import random
import time

valeurs = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

jeu_de_cartes = []
for couleur in couleurs:
    for valeur in valeurs:
        carte = Carte(valeur, couleur)
        jeu_de_cartes.append(carte)

cartes_affichees = []
while True:
    carte = random.choice(jeu_de_cartes)
    if carte not in cartes_affichees:
        cartes_affichees.append(carte)
        print(carte)
    if len(cartes_affichees) == len(jeu_de_cartes):
        print("Toutes les cartes ont été affichées.")
        break
    time.sleep(1)
