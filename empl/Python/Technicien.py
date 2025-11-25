from Employe import Employe


class Technicien(Employe):
    def __init__(self, nom, age, salaire, numero_securite_sociale, grade):
        super().__init__(nom, age, salaire, numero_securite_sociale)
        self.grade = grade

    def prime(self):
        if self.grade == "A":
            return 300
        elif self.grade == "B":
            return 200
        elif self.grade == "C":
            return 100
        else:
            return 0

    def calculer_salaire(self):
        return super().calculer_salaire() + self.prime()

    def __repr__(self):
        return (
            super().__repr__()
            + f", Grade: {self.grade}, Prime: {self.prime()}, Salaire avec prime: {self.calculer_salaire()}"
        )
