import math

class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon

    def afficherInfos(self):
        print(f"Rayon : {self.rayon}")
        print(f"Diamètre : {2 * self.rayon}")
        print(f"Circonférence : {2 * math.pi * self.rayon}")
        print(f"Aire : {math.pi * self.rayon ** 2}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon


cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
cercle2.afficherInfos()
