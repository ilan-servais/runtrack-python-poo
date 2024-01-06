class CompteBancaire:

    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.numero_compte = numero_compte
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        self.decouvert = decouvert

    def afficher(self):
        print("Numéro de compte:", self.numero_compte)
        print("Nom:", self.nom)
        print("Prénom:", self.prenom)
        print("Solde:", self.solde)

    def afficherSolde(self):
        print("Solde:", self.solde)

    def versement(self, montant):
        self.solde += montant
        print("Le nouveau solde est de:", self.solde)

    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print("Le nouveau solde est de:", self.solde)
        else:
            print("Erreur : le solde est insuffisant.")

    def agios(self):
        if self.solde < 0:
            agios = 0.05 * self.solde
            self.solde += agios
            print("Agios appliqués :", agios)

    def virement(self, reference, compte_destinataire, montant):
        if self.solde >= montant:
            self.solde -= montant
            compte_destinataire.solde += montant
            print("Virement effectué avec succès.")
            print("Le nouveau solde du compte 1 est de:", self.solde)
            print("Le nouveau solde du compte 2 est de:", compte_destinataire.solde)
        else:
            print("Erreur : le solde est insuffisant.")


# Création d'un compte bancaire
compte_1 = CompteBancaire(
    "123456789", "Dupont", "Jean", 1000, decouvert=True
)

# Affichage des informations du compte
compte_1.afficher()

# Versement d'un montant
compte_1.versement(500)

# Retrait d'un montant
compte_1.retrait(250)

# Calcul des agios
compte_1.agios()

# Création d'un deuxième compte bancaire
compte_2 = CompteBancaire(
    "987654321", "Martin", "Marie", -500, decouvert=False
)

# Affichage des informations du deuxième compte
compte_2.afficher()

# Virement du compte 1 vers le compte 2
compte_1.virement("123456789", compte_2, 500)
