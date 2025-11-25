class Employe:
    def __init__(self, nom, age, salaire, numero_securite_sociale):
        self.nom = nom
        self.age = age
        self.salaire = salaire
        self.numero_securite_sociale = numero_securite_sociale

    def afficher(self):
        return f"Nom: {self.nom}, Age: {self.age}, Salaire: {self.salaire}, N° Sécurité Sociale: {self.numero_securite_sociale}"

    def augmentation(self, pourcentage):
        return self.salaire * (pourcentage / 100)

    def calculer_salaire(self):
        return self.salaire * 0.765  # après déduction des charges sociales

    def __repr__(self):
        return f"Nom: {self.nom}, Age: {self.age}, Salaire: {self.salaire}, N° Sécurité Sociale: {self.numero_securite_sociale}"
