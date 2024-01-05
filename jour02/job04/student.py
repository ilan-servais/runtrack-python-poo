# Classe Student
class Student:

    # Constructeur
    def __init__(self, nom, prenom, numero_etudiant, nombre_credits=0):
        # Initialisation des attributs
        self.nom = nom
        self.prenom = prenom
        self.numero_etudiant = numero_etudiant
        self.credits = nombre_credits

    # Méthode pour ajouter des crédits
    def add_credits(self, nombre_credits):
        # Vérification que le nombre de crédits est positif
        if nombre_credits <= 0:
            raise ValueError("Le nombre de crédits doit être supérieur à 0")

        # Ajout des crédits
        self.credits += nombre_credits

    # Méthode pour évaluer le niveau de l'étudiant
    @staticmethod
    def student_eval(nombre_credits):
        # Niveau excellent
        if nombre_credits >= 90:
            return "Excellent"

        # Niveau très bien
        elif nombre_credits >= 80:
            return "Très bien"

        # Niveau bien
        elif nombre_credits >= 70:
            return "Bien"

        # Niveau passable
        elif nombre_credits >= 60:
            return "Passable"

        # Niveau insuffisant
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def student_info(self):
        # Affichage du nom
        print("Nom:", self.nom)

        # Affichage du prénom
        print("Prénom:", self.prenom)

        # Affichage du numéro d'étudiant
        print("id:", self.numero_etudiant)

        # Affichage du niveau
        print("Niveau:", Student.student_eval(self.credits))

        # Créer un objet Student
        john_doe = Student("John", "Doe", 145)

        # Ajouter 10 crédits à John Doe
        john_doe.add_credits(10)

        # Afficher les informations de John Doe
        john_doe.student_info()
