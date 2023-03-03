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
    
    def bonjour(self):
        print("Hello la team")
        
    def allerEnCours(self):
        print("je vais en cours")
        
        
        
class Professeur(Persone):
    def __init__(self,matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée
        Persone.__init__(self)        
        
    def enseigner(self):
        print("Le cours va commencer !!!!!!!!!!!")


persone1 = Persone()
persone1.afficherAge()
    
eleve1 = Eleve()
eleve1.modifierAge(15)
eleve1.affichageAge()
eleve1.bonjour()
eleve1.allerEnCours()

prof1 = Professeur("EPS")
prof1.bonjour()
prof1.modifierAge(40)
prof1.enseigner()


        
