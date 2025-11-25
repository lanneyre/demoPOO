from typing import Optional


class Categorie:
    def __init__(self):
        self.id: Optional[int] = None
        self.nom: str = ""
        self.description: str = ""
        self.image: str = ""

    def __repr__(self):
        return f"Categorie(nom='{self.nom}', desc='{self.description}')"
