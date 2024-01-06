class Voiture:

    # Attributs privés
    __marque = None
    __modele = None
    __annee = None
    __kilometrage = None
    __en_marche = False
    __reservoir = 50

    # Mutateurs

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    # Accesseurs

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    # Méthodes

    def demarrer(self):
        # Vérifier que le réservoir est plein
        if self.verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Le réservoir est vide, la voiture ne peut pas démarrer.")

    def arreter(self):
        self.__en_marche = False

    def verifier_plein(self):
        return self.__reservoir

# Créer une voiture
voiture = Voiture()

# Définir les attributs de la voiture
voiture.set_marque("Peugeot")
voiture.set_modele("208")
voiture.set_annee(2023)
voiture.set_kilometrage(10000)

# Vérifier si la voiture peut démarrer
if voiture.verifier_plein() > 5:
    print("La voiture peut démarrer.")
else:
    print("La voiture ne peut pas démarrer.")

# Démarrer la voiture
voiture.demarrer()

# Vérifier l'état de la voiture
print("La voiture est-elle en marche ?", voiture.get_en_marche())

# Arrêter la voiture
voiture.arreter()

# Vérifier l'état de la voiture
print("La voiture est-elle en marche ?", voiture.get_en_marche())
