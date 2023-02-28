class Produit():
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA 
        #prix ht X tva (% 100)
    def CalculerPrixTTC(self):
        calc = self.prixHT * self.TVA
        rajoutTTC = calc /100.00
        prixTTC = rajoutTTC + self.prixHT
        return prixTTC
    
    def afficher(self,):
        return "votre % s coûte hors taxe est de % s € et il a une TVA de % s € et coute % s € TTC"  % (self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC())

    def newProduit(self, nouveau_nom):
        self.nom = nouveau_nom
        return self.nom
    
    def newPrixHT(self,nouveau_prix):
        self.prixHT = nouveau_prix
        return self.prixHT
        
Produit1 = Produit("baguette",0.85,5.5)
print(Produit1.CalculerPrixTTC())
print(Produit1.afficher())

Produit2 = Produit("bouteille de vin",5,20)
print(Produit2.CalculerPrixTTC())
print(Produit2.afficher())

produit3 = Produit("Ordinateur HP", 950, 20.6)
print(produit3.CalculerPrixTTC())
print(produit3.afficher())
print(produit3.newProduit("Ordinateur Asus"))
print(produit3.newPrixHT(473.77))