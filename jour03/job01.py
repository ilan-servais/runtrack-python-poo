class Ville:
    def __init__(self, nom, nb_habitants):
        self.nom = nom
        self.nb_habitants = nb_habitants

    def get_nom(self):
        return self.nom

    def get_nb_habitants(self):
        return self.nb_habitants

    def ajouter_habitant(self):
        self.nb_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def get_nom(self):
        return self.nom

    def get_age(self):
        return self.age

    def get_ville(self):
        return self.ville

    def ajouter_habitant(self):
        self.ville.ajouter_habitant()


# Création des villes
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage des populations initiales
print("Population de la ville de Paris:", paris.get_nb_habitants())
print("Population de la ville de Marseille:", marseille.get_nb_habitants())

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout des personnes à la population
john.ajouter_habitant()
myrtille.ajouter_habitant()
chloe.ajouter_habitant()

# Affichage des populations après l'arrivée des nouvelles personnes
print("Mise à jour de la population de la ville de Paris:", paris.get_nb_habitants())
print("Mise à jour de la population de la ville de Marseille:", marseille.get_nb_habitants())
