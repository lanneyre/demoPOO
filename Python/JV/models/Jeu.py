from .database import db


# Table d'association pour la relation Many-to-Many entre 'jeux' et 'plateforme'
# C'est l'équivalent de votre table `jeuxplateforme`
jeux_plateforme_table = db.Table(
    "jeuxplateforme",
    db.Column("Jeux_Id", db.Integer, db.ForeignKey("jeux.Jeux_Id"), primary_key=True),
    db.Column(
        "Plateforme_Id",
        db.Integer,
        db.ForeignKey("plateforme.Plateforme_Id"),
        primary_key=True,
    ),
)


class Jeu(db.Model):
    __tablename__ = "jeux"
    Jeux_Id = db.Column(db.Integer, primary_key=True)
    Jeux_Titre = db.Column(db.String(255), nullable=False)
    Jeux_Description = db.Column(db.Text, nullable=False)
    Jeux_Prix = db.Column(db.Float, nullable=False)
    Jeux_DateSortie = db.Column(db.Date, nullable=False)
    Jeux_PaysOrigine = db.Column(db.String(255), nullable=False)
    Jeux_Connexion = db.Column(db.String(255), nullable=False)
    Jeux_Mode = db.Column(db.String(255), nullable=False)

    # Clé étrangère vers Genre
    Genre_Id = db.Column(db.Integer, db.ForeignKey("genre.Genre_Id"), nullable=False)

    # Relation : Un jeu appartient à un genre
    genre = db.relationship("Genre", back_populates="jeux")

    # Relation Many-to-Many : Un jeu peut être sur plusieurs plateformes
    plateformes = db.relationship(
        "Plateforme",
        secondary=jeux_plateforme_table,
        backref="jeux",  # Permet de faire plateforme.jeux
    )
