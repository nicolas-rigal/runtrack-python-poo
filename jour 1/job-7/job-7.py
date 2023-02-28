class Personnage:
# x horizontal / y vertical
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y -= 1

    def haut(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)
    
player1 = Personnage(0,0)
#position de base 
print(player1.position())

#deplacement a droite donc x +=1
player1.droite()
print(player1.position())
#deplacement vers le bas donc y -=1
player1.bas()
print(player1.position())
#deplacement a gauche donc x -=1
player1.gauche()
print(player1.position())
#deplacement vers le haut donc y +=1
player1.haut()
print(player1.position())

