class Vehicule():
    def __init__(self,marque,model,annee,prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

        
    def informationVehicule(self): 
        return "Voiture nom:% s model:% s année:%  s coûte % s €" % (self.marque,self.model, self.annee, self.prix)

    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Vehicule):
    def __init__(self,marque,model,annee,prix):
        self.porte = 4
        Vehicule.__init__(self,marque,model,annee,prix)
        
    def informationVehicule(self): 
        return "Marque : % s model : % s année : % s prix : % s nombre de porte : % s " % (self.marque,self.model, self.annee, self.prix, self.porte)

    def demarrer(self):
        print("Attention, je roule en voiture .")


class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix):
        self.roue = 2
        Vehicule.__init__(self,marque, model, annee, prix)
        
    def informationVehicule(self): 
        return "Marque : % s model : % s année : % s prix : % s nombre de roue : % s " % (self.marque,self.model, self.annee, self.prix, self.roue)

    def demarrer(self):
        print("Attention, je chevauche une moto vrmmm vrmmm .")



vehicule1 = Vehicule("clio","3","2005","1")
print(vehicule1.informationVehicule())

voiture1 = Voiture("clio","3","2005","1")
print(voiture1.informationVehicule())

moto1 = Moto("clio","3","2005","1")
print(moto1.informationVehicule())

vehicule1.demarrer()
voiture1.demarrer()
moto1.demarrer()