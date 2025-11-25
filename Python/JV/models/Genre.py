# Fichier: models.py
from .database import db


class Genre(db.Model):
    __tablename__ = "genre"
    Genre_Id = db.Column(db.Integer, primary_key=True)
    Genre_Titre = db.Column(db.String(255), nullable=False)
    Genre_Description = db.Column(db.Text, nullable=False)

    # Relation : Un genre peut avoir plusieurs jeux
    jeux = db.relationship("Jeu", back_populates="genre")
