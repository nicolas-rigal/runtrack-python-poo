class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def get_titre(self):
        return self.__titre

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def get_auteur(self):
        return self.__auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if type(nouveau_nb_pages) == int and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : le nombre de pages doit être un nombre entier positif.")
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def verification(self):
        return self.__disponible
    
    def enprunter(self):
        if not self.__disponible:
            print("Le livre n'est pas disponible pour l'emprunt.")
        else:
            self.__disponible = False
            print("Le livre a été emprunté.")
            
    def rendre(self):
        if self.__disponible:
            print("Le livre n'a pas été emprunté.")
        else:
            self.__disponible = True
            print("Le livre a été rendu.")


livre1 = Livre("Full Metal Alchemist","Hirumu Arakawa", 30)
print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_nb_pages())
print(livre1.verification())
livre1.set_nb_pages(-20)
print(livre1.get_nb_pages())
livre1.enprunter()
print(livre1.verification())
livre1.rendre()
print(livre1.verification())
