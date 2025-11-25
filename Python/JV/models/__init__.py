from .Genre import Genre
from .Plateforme import Plateforme
from .Jeu import Jeu

""""Pour ceux qui ne veulent pas écrire des lignes d'importation """

# import os
# import importlib

# # Récupère le chemin du dossier où se trouve ce fichier __init__.py
# dossier_actuel = os.path.dirname(__file__)

# # On liste tous les fichiers du dossier
# for fichier in os.listdir(dossier_actuel):
#     # On ne traite que les fichiers .py et on ignore __init__.py
#     if fichier.endswith(".py") and fichier != "__init__.py":

#         # On retire l'extension .py pour avoir le nom du module (ex: "produit")
#         nom_module = fichier[:-3]

#         # Import dynamique (équivalent de "from .produit import ...")
#         module = importlib.import_module(f".{nom_module}", package=__name__)

#         # --- MAGIE ---
#         # On cherche une classe qui a le même nom que le fichier mais avec une majuscule
#         # ex: fichier "produit.py" -> on cherche la classe "Produit"
#         nom_classe = nom_module.capitalize()

#         if hasattr(module, nom_classe):
#             # On rend la classe disponible directement dans le package
#             globals()[nom_classe] = getattr(module, nom_classe)
