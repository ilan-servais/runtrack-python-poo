class Joueur:
    def __init__(self, nom, numero, position, buts=0, passes=0, jaunes=0, rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.jaunes = jaunes
        self.rouges = rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.jaunes += 1

    def recevoirUnCartonRouge(self):
        self.rouges += 1

    def afficherStatistiques(self):
        print(f"Joueur : {self.nom} ({self.numero})")
        print(f"Position : {self.position}")
        print(f"Buts : {self.buts}")
        print(f"Passes décisives : {self.passes}")
        print(f"Cartons jaunes : {self.jaunes}")
        print(f"Cartons rouges : {self.rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
        self.buts = 0

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, buts=0, passes=0, jaunes=0, rouges=0):
        joueur.buts += buts
        joueur.passes += passes
        joueur.jaunes += jaunes
        joueur.rouges += rouges


# Exemple d'utilisation

joueur_paris_1 = Joueur("Kylian Mbappé", 7, "Attaquant")
joueur_paris_2 = Joueur("Neymar", 10, "Attaquant")
joueur_paris_3 = Joueur("Lionel Messi", 30, "Attaquant")
joueur_marseille_1 = Joueur("Dimitri Payet", 10, "Milieu offensif")
joueur_marseille_2 = Joueur("Arkadiusz Milik", 9, "Attaquant")
joueur_marseille_3 = Joueur("Boubacar Kamara", 6, "Milieu défensif")

equipe_paris = Equipe("Paris Saint-Germain")
equipe_marseille = Equipe("Olympique de Marseille")

equipe_paris.ajouterJoueur(joueur_paris_1)
equipe_paris.ajouterJoueur(joueur_paris_2)
equipe_paris.ajouterJoueur(joueur_paris_3)
equipe_marseille.ajouterJoueur(joueur_marseille_1)
equipe_marseille.ajouterJoueur(joueur_marseille_2)
equipe_marseille.ajouterJoueur(joueur_marseille_3)

print("** Joueurs de l'équipe Paris Saint-Germain **")
equipe_paris.afficherStatistiquesJoueurs()
print("** Joueurs de l'équipe Olympique de Marseille **")
equipe_marseille.afficherStatistiquesJoueurs()

# Simulation du match
# But de Kylian Mbappé pour Paris
equipe_paris.mettreAJourStatistiquesJoueur(joueur_paris_1, buts=1)
# Carton rouge pour Dimitri Payet pour Marseille
equipe_marseille.mettreAJourStatistiquesJoueur(joueur_marseille_1, rouges=1)
# Passé décisive de Neymar pour Messi, qui marque
equipe_paris.mettreAJourStatistiquesJoueur(joueur_paris_2, passes=1)
equipe_paris.mettreAJourStatistiquesJoueur(joueur_paris_3, buts=1)

print("** Joueurs de l'équipe Paris Saint-Germain après le match **")
equipe_paris.afficherStatistiquesJoueurs()
print("** Joueurs de l'équipe Olympique de Marseille après le match **")
equipe_marseille.afficherStatistiquesJoueurs()

# Affichage des résultats du match
print("** Résultat du match **")
print(f"Paris Saint-Germain : {equipe_paris.buts} - {equipe_marseille.buts} Olympique de Marseille")
