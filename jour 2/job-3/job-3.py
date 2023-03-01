class Operation:
	def __init__(self,nombre1,nombre2):
		self.nombre1 = nombre1
		self.nombre2 = nombre2

	def adition(self):
		result = self.nombre1 + self.nombre2
		print(result)
		
  
resultat = Operation(5,5)
resultat.adition()