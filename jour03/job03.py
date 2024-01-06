class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __repr__(self):
        return f"Tâche {self.titre} ({self.statut})"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for i, tache in enumerate(self.taches):
            if tache.titre == titre:
                del self.taches[i]
                return

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminer"

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        filtered_taches = []
        for tache in self.taches:
            if tache.statut == statut:
                filtered_taches.append(tache)
        return filtered_taches


if __name__ == "__main__":
    # Créer des instances de Tache
    tache1 = Tache("Faire les courses", "Acheter du pain, du lait et des œufs", "à faire")
    tache2 = Tache("Nettoyer la maison", "Passer l'aspirateur, laver la vaisselle, faire le lit", "à faire")
    tache3 = Tache("Aller au cinéma", "Voir le nouveau film de Marvel", "à faire")

    # Ajouter les tâches à la liste
    liste_taches = ListeDeTaches()
    liste_taches.ajouterTache(tache1)
    liste_taches.ajouterTache(tache2)
    liste_taches.ajouterTache(tache3)

    # Afficher la liste des tâches
    print("Liste des tâches :")
    liste_taches.afficherListe()

    # Supprimer une tâche
    liste_taches.supprimerTache("Nettoyer la maison")

    # Afficher la liste des tâches après suppression
    print("Liste des tâches après suppression :")
    liste_taches.afficherListe()

    # Changer le statut d’une tâche
    liste_taches.marquerCommeFinie("Faire les courses")

    # Afficher la liste des tâches après changement de statut
    print("Liste des tâches après changement de statut :")
    liste_taches.afficherListe()

    # Afficher les tâches à faire
    print("Liste des tâches à faire :")
    for tache in liste_taches.filterListe("à faire"):
        print(tache)
