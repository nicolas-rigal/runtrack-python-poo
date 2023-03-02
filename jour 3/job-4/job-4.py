class Joueur:
    def __init__(self,nom,numéro,poste):
        self.nom = nom
        self.numéro = numéro
        self.poste = poste
        self.nbbut = 0
        self.passe = 0
        self.jaune = 0
        self.rouge = 0
        
    def marquerUnBut(self):
        self.nbbut += 1
        
    def effectuerUnePasseDecisive (self):
        self.passe += 1
        
    def recevoirUnCartonJaune(self):
        if self.jaune < 2:
            self.jaune += 1
            if self.jaune == 2 :
                self.recevoirUnCartonRouge()
   
    def recevoirUnCartonRouge (self):
        self.rouge += 1
        
    def afficherStatistiques (self):
        print("stat de ",self.nom)
        print("porte le numéro",self.numéro)
        print("joue au poste",self.poste)
        print("a marqué",self.nbbut,"but")
        print("a effectuer",self.passe,"passe decisive")
        print("a reçu",self.jaune,"carton jaune")
        print("a reçu",self.rouge,"carton rouge")
        print("################################")


class Equipe:
    def __init__(self,nom):
        self.nom = nom
        self.joueurs = []
        
    def ajouterJoueur(self,joueur):
        self.joueurs.append(joueur)
        
    def AfficherStatistiquesJoueurs(self):
        print("Statistiques des joueurs de l'équipe", self.nom)
        for joueur in self.joueurs:
            joueur.afficherStatistiques()   
    # pas besoin car il se fonf deja dans la classe jouer ?;
    def mettreAJourStatistiquesJoueur(self, numero_joueur, action):
        for joueur in self.joueurs:
            if joueur.numero == numero_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()


########################################################################################

joueur1 = Joueur("Sophie", 10, "Gardien de but")
joueur2 = Joueur("Nicolas", 9, "Defenseurs")
joueur3 = Joueur("Pierre", 11, "Attaquant")

joueur4 = Joueur("Jérome", 666, "Gardien de but")
joueur5 = Joueur("Tara", 45 , "Attaquant")
joueur6 = Joueur("Céline", 34, "Defenseurs")

equipe1 = Equipe("FC Poufsouffle")
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)

equipe2 = Equipe("😡Griffin-dor")
equipe2.ajouterJoueur(joueur4)
equipe2.ajouterJoueur(joueur6)
equipe2.ajouterJoueur(joueur5)

joueur5.recevoirUnCartonJaune()
joueur5.recevoirUnCartonJaune()

joueur1.marquerUnBut()
joueur1.marquerUnBut()
joueur1.marquerUnBut()
joueur1.marquerUnBut()
joueur1.marquerUnBut()
joueur1.marquerUnBut()
joueur2.marquerUnBut()



equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()