# Importation des bibliothèques
import math

# Définition de la classe Rectangle
class Rectangle:

    # Initialisation des attributs privés
    def __init__(self, longueur, largeur):
        # Longueur
        self._longueur = longueur
        # Largeur
        self._largeur = largeur

    # Getter pour la longueur
    @property
    def longueur(self):
        return self._longueur

    # Setter pour la longueur
    @longueur.setter
    def longueur(self, longueur):
        # Vérification de la valeur
        if not isinstance(longueur, int) or longueur < 0:
            raise ValueError("La longueur doit être un entier positif")
        self._longueur = longueur

    # Getter pour la largeur
    @property
    def largeur(self):
        return self._largeur

    # Setter pour la largeur
    @largeur.setter
    def largeur(self, largeur):
        # Vérification de la valeur
        if not isinstance(largeur, int) or largeur < 0:
            raise ValueError("La largeur doit être un entier positif")
        self._largeur = largeur


# Création d'un objet rectangle
rectangle = Rectangle(10, 5)

# Affichage des valeurs par défaut
print("Longueur :", rectangle.longueur)
print("Largeur :", rectangle.largeur)

# Modification des valeurs des attributs
# Saisie de la nouvelle longueur
longueur_nouvelle = input("Saisissez la nouvelle longueur (0 pour quitter) :")
if longueur_nouvelle == "0":
    print("Aucune modification apportée")
else:
    # Conversion de la chaîne de caractères en entier
    longueur_nouvelle = int(longueur_nouvelle)
    # Affectation de la nouvelle valeur
    rectangle.longueur = longueur_nouvelle

# Saisie de la nouvelle largeur
largeur_nouvelle = input("Saisissez la nouvelle largeur (0 pour quitter) :")
if largeur_nouvelle == "0":
    print("Aucune modification apportée")
else:
    # Conversion de la chaîne de caractères en entier
    largeur_nouvelle = int(largeur_nouvelle)
    # Affectation de la nouvelle valeur
    rectangle.largeur = largeur_nouvelle

# Affichage des nouvelles valeurs
print("Longueur :", rectangle.longueur)
print("Largeur :", rectangle.largeur)
