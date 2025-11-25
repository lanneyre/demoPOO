from typing import List, Optional
from classes.categorie import Categorie


class Produit:
    def __init__(
        self,
        nom: str,
        description: str,
        prix: float,
        id: Optional[int] = None,
        stock: int = 0,
    ):
        self.nom = nom
        self.id = id
        self.description = description
        self.prix = prix
        self.stock = stock
        self.images: List[str] = []
        self.categories: List[Categorie] = []

    def get_nom(self) -> str:
        if self.id is not None:
            return self.nom
        else:
            return "erreur"

    def add_image(self, url: str):
        self.images.append(url)

    def add_categorie(self, c: Categorie):
        self.categories.append(c)

    def display(self):
        return f"Nom : [ nom : {self.nom}, description : {self.description} , prix : {self.prix}]"
