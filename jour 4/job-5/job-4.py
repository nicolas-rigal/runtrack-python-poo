class Forme():
    def __init__(self):
        pass
    
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self,largeur,longeur):
        self.largeur = largeur
        self.longeur = longeur
        Forme.__init__(self)
        
    def aire(self):
        return self.largeur * self.longeur
    
class Cercle(Forme):
    def __init__(self,radius):
        self.radius = radius
        Forme.__init__(self)
        
    def aire(self):
        return (self.radius **2) * 3.14

    
rectangle1 = Rectangle(5,5)
print(rectangle1.aire())

cercle1 = Cercle(5)
print(cercle1.aire())
