class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

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


livre1 = Livre("One piece","oda", 10)
print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_nb_pages())

livre2 = Livre("Full Metal Alchemist","Hirumu Arakawa", 30)
print(livre2.get_titre())
print(livre2.get_auteur())
print(livre2.get_nb_pages())
livre2.set_nb_pages(-20)
print(livre2.get_nb_pages())


#livre2 = Livre()
#print(livre1.set_titre("FMA"))
#print(livre1.set_auteur("hiromu harakawa"))
#print(livre1.set_nb_pages(-1))