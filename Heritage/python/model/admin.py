# On importe la classe mère
from .user import User


class Admin(User):
    """
    HÉRITAGE
    Admin hérite de User (class Admin(User)).
    """

    def __init__(
        self,
        id=None,
        pseudo="",
        email="",
        mdp="",
        grade="",
        created_at="",
        updated_at="",
    ):
        """
        SURCHARGE DU CONSTRUCTEUR
        On doit explicitement appeler le constructeur du parent.
        """
        # 1. APPEL AU PARENT (Equivalent de parent::__construct)
        super().__init__(id, pseudo, email, mdp, created_at, updated_at)

        # 2. SPÉCIFICITÉ
        self.grade = grade

    @classmethod
    def get_admin_by_id(cls, admin_id: int):
        """
        FACTORY SPÉCIFIQUE
        Récupère les infos jointes et retourne un objet Admin.
        """
        cnx = cls.get_db_connection()  # On a accès à cette méthode grâce à l'héritage !
        cursor = cnx.cursor(dictionary=True)

        sql = "SELECT * FROM admin JOIN user ON (user.id = admin.id_user) WHERE user.id = %s"
        cursor.execute(sql, (admin_id,))

        row = cursor.fetchone()
        cursor.close()

        if row is None:
            print("L'utilisateur n'existe pas")
            return cls()  # Retourne un Admin vide
        else:
            # On retourne un objet de la classe courante (Admin)
            return cls(
                id=row["id"],
                pseudo=row["pseudo"],
                email=row["email"],
                mdp=row["mdp"],
                grade=row["grade"],  # Champ spécifique
                created_at=row["created_at"],
                updated_at=row["updated_at"],
            )
