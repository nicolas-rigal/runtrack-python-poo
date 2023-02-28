class Cercle():
    def __init__(self,rayon):
        self.rayon = rayon
        
    def changerRayon(self,newRayon):
        self.rayon = newRayon
        
    def afficherInfos(self):
        information = "Le rayon est de :" + str(self.rayon)
        print(information)
        
    def circonference(self):
        cirf = 2 * 3.14 * self.rayon
        return cirf
        
    def aire(self):
        space = 3.14 * (self.rayon **2)
        return space
    
    def diametre(self):
        diams = 2 * self.rayon
        return diams
    
cercle1 = Cercle(4)
cercle1.afficherInfos()
print("La circonférence est de :", cercle1.circonference())
print("L'aire est de :", cercle1.aire())
print("Le diamètre est de :", cercle1.diametre())

cercle1 = Cercle(7)
cercle1.afficherInfos()
print("La circonférence est de :", cercle1.circonference())
print("L'aire est de :", cercle1.aire())
print("Le diamètre est de :", cercle1.diametre())