class Commande:

    # Attributs privés
    __numero_commande = None
    __liste_plats = None
    __statut_commande = None

    # Constructeur
    def __init__(self, numero_commande, liste_plats, statut_commande):
        # Initialisation des attributs
        self.__numero_commande = numero_commande
        self.__liste_plats = liste_plats
        self.__statut_commande = statut_commande

    # Méthodes

    def ajouter_plat(self, nom_plat, prix):
        # Vérification que la commande n'est pas annulée
        if self.__statut_commande != "annulée":
            # Ajout du plat à la liste des plats commandés
            self.__liste_plats[nom_plat] = {"prix": prix, "statut": "en cours"}

    def annuler_commande(self):
        # Modification du statut de la commande
        self.__statut_commande = "annulée"

    def calculer_total(self):
        # Calcul du total de la commande
        total = 0
        for plat, infos_plat in self.__liste_plats.items():
            total += infos_plat["prix"]
        return total

    def afficher_commande(self):
        # Affichage de la commande
        print("Numéro de commande :", self.__numero_commande)
        print("Liste des plats commandés :")
        for plat, infos_plat in self.__liste_plats.items():
            print("*", plat, "(", infos_plat["prix"], "€)")
        print("Statut de la commande :", self.__statut_commande)
        print("Total à payer :", self.calculer_total())

    def calculer_tva(self):
        # Calcul de la TVA
        tva = self.calculer_total() * 20 / 100
        return tva

# Créer une commande
commande = Commande(1, {"pizza": {"prix": 15, "statut": "en cours"}}, "en cours")

# Ajouter un plat à la commande
commande.ajouter_plat("salade", 10)

# Afficher la commande
commande.afficher_commande()
