from classes.categorie import Categorie
from classes.produit import Produit

c1 = Categorie()
c1.nom = "Catégorie 1"
c1.description = "J'ai pas envie de me prendre la tête"

c2 = Categorie()
c2.nom = "Catégorie 2"
c2.description = "J'ai pas envie de me prendre la tête une deuxième fois"

p = Produit(id=1, nom="test", description="description du test", prix=42.1)

p.add_image("http://localhost/monimage.png")
p.add_image("http://localhost/monimage2.png")

p.add_categorie(c1)
p.add_categorie(c2)

# print("--- Dump de p.categories ---")
# for cat in p.categories:
#     print(cat)

print(p.display())
