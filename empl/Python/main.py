from Employe import Employe
from Technicien import Technicien

if __name__ == "__main__":
    emp = Employe("Dupont", 30, 3000, "123-45-6789")
    tech = Technicien("Martin", 28, 3200, "987-65-4321", "A")

    print("Employé:")
    print(emp)
    print(f"Salaire après déduction des charges sociales: {emp.calculer_salaire()}")
    print(f"Augmentation de 10%: {emp.augmentation(10)}")

    print("\nTechnicien:")
    print(tech)
    print(
        f"Salaire après déduction des charges sociales et prime: {tech.calculer_salaire()}"
    )
    print(f"Augmentation de 10%: {tech.augmentation(10)}")
