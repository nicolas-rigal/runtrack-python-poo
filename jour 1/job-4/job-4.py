#instatiatin de l'object 
class Personne:
    #construction atribut 
    def __init__(self, nom, prenom):
        self.nom = nom 
        self.prenom = prenom
        
    def SePresenter(self):
        salutation = "je suis " + self.nom +" "+ self.prenom
        print(salutation)
        
  
#input  
nom =(input("entre un nom :"))
prenom =(input("entre un prénom :"))

#la variable initialiser par l'objet et ces parametre 
presentation = Personne(nom, prenom)

#inpression de la fonction de mon object 
presentation.SePresenter()