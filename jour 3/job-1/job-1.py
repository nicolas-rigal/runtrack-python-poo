class Ville:
    def __init__(self,nom,habitants):
        self.__nom = nom
        self.__NBhabitants = habitants
        
    def afficheInfos(self):
        print("Population de la Ville de % s: % s habitants" % (self.__nom,self.__NBhabitants))
        
class Personne:
    def __init__(self,nom,age,ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        
    def ajouterPopulation(self):
        self.__ville._Ville__NBhabitants += 1
        
paris = Ville("Paris",1000000)
paris.afficheInfos()
marseille = Ville("Marseille",861635)
marseille.afficheInfos()

john = Personne("John", 45, paris)
john.ajouterPopulation()
paris.afficheInfos()

myrthille = Personne("Myrthille", 4, paris)
myrthille.ajouterPopulation()
paris.afficheInfos()

chloe = Personne("chloe",18 , marseille)
chloe.ajouterPopulation()
marseille.afficheInfos()