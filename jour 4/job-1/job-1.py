class Persone():
    def __init__(self):
        self.age = 14
        
    def afficherAge(self):
        print(self.age)
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self,age):
        self.age = age
        
        
class Eleve(Persone):
    def __init__(self):
        Persone.__init__(self)
             
    def allerEnCours(self):
        print("Je vais en cours")
        
    def affichageAge(self):
        print("J'ai",self.age,"ans")  
        
        
        
class Professeur(Persone):
    def __init__(self,matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée
        Persone.__init__(self)        
        
    def enseigner(self):
        print("Le cours va commencer !!!!!!!!!!!")

persone1 = Persone()
persone1.afficherAge()
#variable d'instence 
eleve1 = Eleve()
eleve1.modifierAge(26)
eleve1.affichageAge()


        
