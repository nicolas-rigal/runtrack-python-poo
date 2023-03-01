class Student:
    def __init__(self,nom,prenom):
        self.__nom = nom
        self.__prenom = prenom
        self.__numStudent = int
        self.__credit = 0
        #self.level =
        #credit “Excellent” à 90, 
        # “Très bien.” si le nombre est supérieur ou égal à 80, 
        # “Bien” si le nombre est supérieur ou égale à 70, 
        # “Passable” si égale ou supérieure à 60 
        # et “insuffisant” si inférieur à 60.
##>nom<###########################
    def set_nom(self,nom):
        self.__nom = nom 
        return nom
    
    def get_nom(self):
        return self.__nom
##>prenom<###########################
    def set_prenom(self,prenom):
        self.__prenom = prenom 
        return prenom
    
    def get_prenom(self):
        return self.__prenom
##>numStudiant<###########################
    def set_numStudiant(self,numStudiant):
        self.__numStudent = numStudiant 
        return numStudiant
    
    def get_numStudiant(self):
        return self.__numStudent


Etudiant1 = Student()
print(Etudiant1.set_nom("john"))
#print(Etudiant1.set_prenom())
#print(Etudiant1.set_numStudiant())


