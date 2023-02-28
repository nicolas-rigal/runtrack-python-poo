class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

#standart position        
    def afficherLesPoints(self):
        positionDeMesPoint = "X est situer horizontalement à : " + self.x + " et Y est situer verticalement à : " + self.y
        print(positionDeMesPoint)

    def afficherX(self):
        positionDeX = "X est situer horizontalement à : " + self.x
        print(positionDeX)
        
    def afficherY(self):
        positionDeY = "Y est situer horizontalement à : " + self.y
        print(positionDeY)
#new localisation 
    def changerX(self):
        newLocalisationX = "X est situer maintenant horizontalement à : " + self.x
        print(newLocalisationX)
        
    def changerY(self):
        newLocalisationY = "Y est maintenant situer horizontalement à : " + self.y
        print(newLocalisationY)

#----------------------- old -------------------------------
# print de la position initile 
x = input("Veillier renseigner un coodoner pour X :")
y = input("Veillier renseigner un coodoner pour Y :")
localisation = Point(x,y)
localisation.afficherLesPoints()

#----------------------- new -------------------------------
# print de la nouvelle position      
newX = input("Veillier renseigner une nouvelle coodoner pour X :")
newY = input("Veillier renseigner une nouvelle coodoner pour Y :")

x = newX
y = newY

Newlocalisation = Point(x,y)
Newlocalisation.changerX()
Newlocalisation.changerY()
