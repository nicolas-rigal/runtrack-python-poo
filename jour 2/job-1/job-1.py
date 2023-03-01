class Rectangle:
    
# Les méthodes set et get sont des méthodes d'accès aux attributs en Python. 
# Elles sont souvent utilisées pour contrôler l'accès aux attributs privés. 
# Les attributs privés sont des attributs dont le nom commence par un double tiret bas (__).
	def __init__(self,larger,longeur):
		self.__larger = larger
		self.__longueur = longeur
#larger
	def get_Lager(self):
		return self.__larger

	def set_Lager(self,larger):
		self.__larger = larger
		return self.__larger
#longeur 



	def get_Longeur(self):
		return self.__longueur

	def set_Longeur(self,longeur):
		self.__longueur = longeur
		return self.__longueur



Rectangle1 = Rectangle(10,20)
print("la largeur est de ",Rectangle1.get_Lager())
print("la longeur est de",Rectangle1.get_Longeur())
Rectangle1.set_Lager(20)
Rectangle1.set_Longeur(40)
print("la nouvelle valeur de la larger",Rectangle1.get_Lager())
print("la nouvelle valeur de la longeur",Rectangle1.get_Longeur())





