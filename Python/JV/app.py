# Fichier: app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from include.config import DATABASE_URI, SECRET_KEY
from models import Jeu, Genre, Plateforme
from datetime import date
from flask_sqlalchemy import SQLAlchemy

# Initialisation de l'application Flask
app = Flask(__name__)

# Initialisation de l'objet SQLAlchemy (il sera lié à l'app Flask plus tard)
db = SQLAlchemy()

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Désactive les avertissements
app.config["SECRET_KEY"] = SECRET_KEY  # Nécessaire pour les 'flash messages'

# Liaison de l'ORM SQLAlchemy à notre application
db.init_app(app)

# --- ROUTE PRINCIPALE (remplace l'affichage de index.php) ---


@app.route("/")
def index():
    # Affichage des messages (équivalent de $msgKO / $msgOK)
    # Les messages sont récupérés dans le template index.html

    # Requêtes (équivalent de vos $queryJV, $queryGenre, $queryPlateforme)
    # L'ORM gère la jointure grâce à la relation 'genre' définie dans models.py
    try:
        jeux = db.session.query(Jeu).join(Genre).order_by(Jeu.Jeux_Titre).all()
        genres = db.session.query(Genre).order_by(Genre.Genre_Titre).all()
        plateformes = (
            db.session.query(Plateforme).order_by(Plateforme.Plateforme_Nom).all()
        )
    except Exception as e:
        flash(f"Erreur de connexion à la base de données: {e}", "danger")
        jeux = []
        genres = []
        plateformes = []

    return render_template(
        "index.html",
        jeux=jeux,
        genres=genres,
        plateformes_all=plateformes,  # Renommé pour éviter conflit dans le template
    )


# --- ROUTES DE TRAITEMENT (remplace traitements.php) ---


@app.route("/add", methods=["POST"])
def add_jeu():
    # Remplace la section "insert" de traitements.php
    try:
        # Récupération des données du formulaire
        nouveau_jeu = Jeu(
            Jeux_Titre=request.form.get("Jeux_Titre"),
            Jeux_Description=request.form.get("Jeux_Description"),
            Jeux_Prix=float(request.form.get("Jeux_Prix")),
            Jeux_DateSortie=date.fromisoformat(request.form.get("Jeux_DateSortie")),
            Jeux_PaysOrigine=request.form.get("Jeux_PaysOrigine"),
            Jeux_Connexion=request.form.get("Jeux_Connexion"),
            Jeux_Mode=request.form.get("Jeux_Mode"),
            Genre_Id=int(request.form.get("Genre_Id")),
        )

        # Récupération des plateformes (getlist gère les checkbox)
        plateformes_ids = request.form.getlist("Plateformes[]")
        if plateformes_ids:
            plateformes = (
                db.session.query(Plateforme)
                .filter(Plateforme.Plateforme_Id.in_(plateformes_ids))
                .all()
            )
            nouveau_jeu.plateformes = plateformes

        # Ajout à la session et commit
        db.session.add(nouveau_jeu)
        db.session.commit()

        flash("Jeu ajouté avec succès !", "success")

    except Exception as e:
        db.session.rollback()  # Annule les changements en cas d'erreur
        flash(f"Erreur lors de l'ajout du jeu: {e}", "danger")

    return redirect(url_for("index"))


@app.route("/update/<int:jeu_id>", methods=["POST"])
def update_jeu(jeu_id):
    # Remplace la section "update" de traitements.php
    try:
        jeu = db.session.query(Jeu).get_or_404(jeu_id)

        # Mise à jour des champs
        jeu.Jeux_Titre = request.form.get("Jeux_Titre")
        jeu.Jeux_Description = request.form.get("Jeux_Description")
        jeu.Jeux_Prix = float(request.form.get("Jeux_Prix"))
        jeu.Jeux_DateSortie = date.fromisoformat(request.form.get("Jeux_DateSortie"))
        jeu.Jeux_PaysOrigine = request.form.get("Jeux_PaysOrigine")
        jeu.Jeux_Connexion = request.form.get("Jeux_Connexion")
        jeu.Jeux_Mode = request.form.get("Jeux_Mode")
        jeu.Genre_Id = int(request.form.get("Genre_Id"))

        # Mise à jour des plateformes
        # (L'ORM est intelligent, on peut juste ré-assigner la liste)
        plateformes_ids = request.form.getlist("Plateformes[]")

        # C'est l'équivalent de votre "DELETE puis INSERT"
        jeu.plateformes.clear()  # Supprime les anciennes associations
        if plateformes_ids:
            plateformes = (
                db.session.query(Plateforme)
                .filter(Plateforme.Plateforme_Id.in_(plateformes_ids))
                .all()
            )
            jeu.plateformes = plateformes  # Ajoute les nouvelles

        db.session.commit()
        flash("Jeu modifié avec succès !", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Erreur lors de la modification du jeu: {e}", "danger")

    return redirect(url_for("index"))


@app.route("/delete/<int:jeu_id>", methods=["POST"])
def delete_jeu(jeu_id):
    # Remplace la section "delete" de traitements.php
    # Note : J'utilise POST pour la suppression (meilleure pratique que GET)
    # Le template html a été ajusté en conséquence.
    try:
        jeu = db.session.query(Jeu).get_or_404(jeu_id)

        # L'ORM gère la suppression des associations dans `jeuxplateforme`
        # grâce à la relation 'secondary' (pas besoin de le faire en deux étapes)
        db.session.delete(jeu)
        db.session.commit()

        flash("Jeu supprimé avec succès.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Erreur lors de la suppression: {e}", "danger")

    return redirect(url_for("index"))


# --- Point d'entrée pour lancer le serveur ---
if __name__ == "__main__":
    # Crée les tables si elles n'existent pas (basé sur models.py)
    # Ne modifie pas les tables existantes
    with app.app_context():
        db.create_all()

    app.run(debug=True)  # Lance le serveur en mode débogage
