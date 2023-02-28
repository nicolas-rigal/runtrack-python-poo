class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
        print("L'age de votre animal est de :",self.age, "ans")

    def veillir(self):
        self.age += 1

        

    def nommer(self, nom):
        self.prenom = "Votre animal se nomme "+nom
            

pet = Animal()
pet.veillir()
pet.nommer("polo")
print(pet.prenom)
print("l'année prochaine il aura :", pet.age, "ans")
