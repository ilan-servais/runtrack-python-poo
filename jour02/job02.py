import math


# Définition de la classe Livre
class Livre:

    # Initialisation des attributs privés
    def __init__(self, titre, auteur, nombre_pages):
        # Titre
        self._titre = titre
        # Auteur
        self._auteur = auteur
        # Nombre de pages
        self._nombre_pages = nombre_pages

    # Getter pour le titre
    @property
    def titre(self):
        """
        Retourne le titre du livre.

        :return: Titre du livre
        """
        return self._titre

    # Setter pour le titre
    @titre.setter
    def titre(self, titre):
        """
        Modifie le titre du livre.

        :param titre: Nouveau titre du livre
        :type titre: str
        """
        self._titre = titre

    # Getter pour l'auteur
    @property
    def auteur(self):
        """
        Retourne l'auteur du livre.

        :return: Auteur du livre
        """
        return self._auteur

    # Setter pour l'auteur
    @auteur.setter
    def auteur(self, auteur):
        """
        Modifie l'auteur du livre.

        :param auteur: Nouveau auteur du livre
        :type auteur: str
        """
        self._auteur = auteur

    # Getter pour le nombre de pages
    @property
    def nombre_pages(self):
        """
        Retourne le nombre de pages du livre.

        :return: Nombre de pages du livre
        """
        return self._nombre_pages

    # Setter pour le nombre de pages
    @nombre_pages.setter
    def nombre_pages(self, nombre_pages):
        """
        Modifie le nombre de pages du livre.

        :param nombre_pages: Nouveau nombre de pages du livre
        :type nombre_pages: int
        """
        # Vérifie que la valeur est un nombre entier positif
        if not isinstance(nombre_pages, int) or nombre_pages < 1:
            print("Le nombre de pages doit être un nombre entier positif")
        else:
            # Modifie la valeur
            self._nombre_pages = nombre_pages


# Création d'un objet livre
livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1000)

# Affichage des valeurs par défaut
print("Titre :", livre.titre)
print("Auteur :", livre.auteur)
print("Nombre de pages :", livre.nombre_pages)

# Changement du nombre de pages
livre.nombre_pages = -10

# Affichage des nouvelles valeurs
print("Titre :", livre.titre)
print("Auteur :", livre.auteur)
print("Nombre de pages :", livre.nombre_pages)
