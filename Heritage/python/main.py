import sys
import os

# Astuce : On ajoute le dossier courant au path pour éviter les erreurs d'import
sys.path.append(os.getcwd())

# IMPORTATION DES CLASSES
# On va chercher dans le dossier 'model', les fichiers 'user' et 'admin'
from model.user import User
from model.admin import Admin


def main():
    print("========================================")
    print("      TEST DES CLASSES PYTHON           ")
    print("========================================\n")

    # ---------------------------------------------------------
    # PARTIE 1 : TEST DE LA CLASSE USER (Mère)
    # ---------------------------------------------------------
    print("--- 1. Création d'un User manuel (Instance) ---")
    # Ici, on utilise le constructeur __init__
    u1 = User(pseudo="Etudiant_Test", email="test@ecole.com", mdp="secret123")
    print(f"✅ Objet créé : {u1.pseudo} (Email: {u1.email})")
    print(f"🔒 Mot de passe hashé : {u1.mdp}")
    # Note : u1.mdp sera affiché en bytes (b'$2b$...') car bcrypt retourne des bytes

    print("\n--- 2. Test de la Factory User (Static) ---")
    # Ici, on appelle la classe, pas l'objet u1 !
    try:
        # On essaie de récupérer l'ID 1 (Assure-toi d'avoir ta BDD lancée)
        u_bdd = User.get_user_by_id(1)

        if u_bdd.id:
            print(f"✅ User récupéré depuis BDD : ID {u_bdd.id} -> {u_bdd.pseudo}")
        else:
            print("⚠️ L'utilisateur ID 1 n'existe pas en BDD (Test normal si BDD vide)")

    except Exception as e:
        print(f"❌ Erreur de connexion BDD (Normal si WAMP/XAMPP éteint) : {e}")

    # ---------------------------------------------------------
    # PARTIE 2 : TEST DE LA CLASSE ADMIN (Fille)
    # ---------------------------------------------------------
    print("\n\n--- 3. Création d'un Admin manuel (Héritage) ---")
    # L'Admin prend les mêmes arguments que User + le grade
    a1 = Admin(
        pseudo="SuperProf", email="prof@ecole.com", mdp="root", grade="Moderateur"
    )

    print(f"✅ Admin créé : {a1.pseudo}")
    print(f"🔰 Grade (Spécifique Admin) : {a1.grade}")
    print(f"📅 Date création (Hérité de User) : {a1.created_at}")

    print("\n--- 4. Test de la Factory Admin (Static + Join) ---")
    try:
        # Test de la méthode qui fait le JOIN SQL
        a_bdd = Admin.get_admin_by_id(1)
        if a_bdd.id:
            print(f"✅ Admin récupéré : {a_bdd.pseudo} avec le grade {a_bdd.grade}")
        else:
            print("⚠️ Pas d'admin avec l'ID 1 trouvé.")
    except Exception as e:
        print(f"❌ Erreur BDD : {e}")

    # ---------------------------------------------------------
    # PARTIE 3 : VÉRIFICATION DU POLYMORPHISME / HÉRITAGE
    # ---------------------------------------------------------
    print("\n\n--- 5. Preuve de l'héritage (instanceof) ---")

    # Est-ce que a1 est un Admin ? OUI
    is_admin = isinstance(a1, Admin)
    # Est-ce que a1 est AUSSI un User ? OUI (car Admin hérite de User)
    is_user = isinstance(a1, User)

    print(f"L'objet a1 est-il un Admin ? {'OUI' if is_admin else 'NON'}")
    print(
        f"L'objet a1 est-il un User ?  {'OUI' if is_user else 'NON'} (C'est la magie de l'héritage !)"
    )


if __name__ == "__main__":
    main()
