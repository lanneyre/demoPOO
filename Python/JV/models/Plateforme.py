# Fichier: models.py


from .database import db


class Plateforme(db.Model):
    __tablename__ = "plateforme"
    Plateforme_Id = db.Column(db.Integer, primary_key=True)
    Plateforme_Nom = db.Column(db.String(255), nullable=False)
    Plateforme_Description = db.Column(db.Text, nullable=False)
