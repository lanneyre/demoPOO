# Fichier: demo_db.py

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Jeu, Plateforme  # Importez vos modèles
from datetime import datetime

# Configuration de la connexion (similaire à app.py)
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

print("--- Traduction de demoPDO.php ---")

try:
    # Requete simple (SELECT * FROM jeux)
    # $sql = "SELECT * FROM jeux";
    # $query = $pdo->query($sql);
    print("\n[Requête simple ORM]")
    jeux = session.query(Jeu).all()
    for jeu in jeux:
        print(
            f"- {jeu.Jeux_Titre} ({jeu.Jeux_Prix} €) : {jeu.Jeux_DateSortie.strftime('%d/%m/%Y')}"
        )

    # Requetes préparées (paramétrées)
    # $sql = "SELECT * FROM jeux WHERE jeux_titre LIKE :search AND jeux_prix >= :prix";
    print("\n[Requête paramétrée (préparée) ORM]")
    search = "ba"
    prix = 30

    # L'ORM gère la paramétrisation pour vous, prévenant les injections SQL
    jeux_filtres = (
        session.query(Jeu)
        .filter(Jeu.Jeux_Titre.like(f"%{search}%"), Jeu.Jeux_Prix >= prix)
        .all()
    )

    for jeu in jeux_filtres:
        print(f"- {jeu.Jeux_Titre} ({jeu.Jeux_Prix} €)")

except Exception as e:
    print(f"Erreur: {e}")


print("\n--- Traduction de platPDO.php (Démonstration SQL Injection) ---")

# Le code PHP avait : $jeuxId = "1; DROP DATABASE test;";
# C'est une injection SQL qui supprime une base de données.

jeux_id_vulnerable = "1; DROP DATABASE test;"  # L'attaque
jeux_id_legitime = 1

# --- 1. La MAUVAISE façon (vulnérable, équivalent de votre $pdo->query($sql)) ---
# Utiliser du texte brut avec f-string est DANGEREUX
sql_vulnerable = f"SELECT p.* FROM plateforme AS p JOIN jeuxplateforme AS jp USING(Plateforme_Id) WHERE jp.Jeux_Id = {jeux_id_vulnerable}"

print(f"\n[Requête VULNÉRABLE (NE PAS FAIRE !)]")
print(f"SQL généré: {sql_vulnerable}")
try:
    # L'exécution de ceci pourrait être catastrophique
    # result = session.execute(text(sql_vulnerable))
    # print(result.fetchall())
    print("-> Exécution bloquée pour la sécurité, mais le SQL est mauvais.")
except Exception as e:
    print(f"Une erreur se produirait (ou pire): {e}")


# --- 2. La BONNE façon (sécurisée, équivalent de votre $pdo->prepare($sql)) ---
# On utilise la paramétrisation (binding)
sql_securise = "SELECT p.* FROM plateforme AS p JOIN jeuxplateforme AS jp USING(Plateforme_Id) WHERE jp.Jeux_Id = :id"

print(f"\n[Requête SÉCURISÉE (paramétrée)]")
try:
    # On passe l'ID légitime
    params = {"id": jeux_id_legitime}
    result = session.execute(text(sql_securise), params)
    print("Plateformes pour l'ID 1 (légitime):")
    for row in result:
        print(f"- {row.Plateforme_Nom}")

    # On passe la tentative d'attaque.
    # Le SGBD traitera "1; DROP DATABASE test;" comme une simple chaîne
    # et ne trouvera aucun ID correspondant. L'attaque échoue.
    params = {"id": jeux_id_vulnerable}
    result = session.execute(text(sql_securise), params)
    print("\nPlateformes pour l'ID '1; DROP DATABASE test;' (l'attaque):")
    rows = result.fetchall()
    if not rows:
        print("-> Aucune plateforme trouvée. L'injection SQL a ÉCHOUÉ (c'est bien !)")

except Exception as e:
    print(f"Erreur lors de la requête sécurisée: {e}")


session.close()
