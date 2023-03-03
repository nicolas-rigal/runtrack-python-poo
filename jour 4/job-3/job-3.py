class Rectangle():
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
    
    def perimetre(self):
        return  self.__largeur * 2 + self.__longeur * 2 

    def surface(self):
        return self.__largeur * self.__longeur
              
    def set_largeur(self,largeur):
        self.__largeur = largeur
        
    def set_longuer(self,longeur):  
        self.__longuer = longeur 
                   
    def get_longeur(self):
        self.__longeur
        
    def get_largeur(self):
        self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self,hauter,longueur,largeur):
        self.hauteur = hauter
        Rectangle.__init__(self, longueur, largeur)
        
    def volume(self):
        return self.hauteur * self.surface()

rectangle1 = Rectangle(5,2)
print(rectangle1.perimetre())
print(rectangle1.surface())

parallelepipede1 = Parallelepipede(5,5,5)
print(parallelepipede1.volume())
