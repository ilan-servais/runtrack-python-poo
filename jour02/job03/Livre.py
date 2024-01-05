class Livre:

    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages
        self._disponible = True

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, titre):
        self._titre = titre

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, auteur):
        self._auteur = auteur

    @property
    def nombre_pages(self):
        return self._nombre_pages

    @nombre_pages.setter
    def nombre_pages(self, nombre_pages):
        if not isinstance(nombre_pages, int) or nombre_pages < 1:
            print("Le nombre de pages doit être un nombre entier positif")
        else:
            self._nombre_pages = nombre_pages

    def verification(self):
        return self._disponible

    def emprunter(self):
        if self._disponible is True:
            self._disponible = False
        else:
            print("Le livre est déjà emprunté")

    def rendre(self):
        if self._disponible is False:
            self._disponible = True
        else:
            print("Le livre n'est pas emprunté")


livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1000)

print("Le livre est-il disponible ? :", livre.verification())

# Emprunt du livre
livre.emprunter()

print("Le livre est-il disponible ? :", livre.verification())

# Renvoie du livre
livre.rendre()

print("Le livre est-il disponible ? :", livre.verification())
