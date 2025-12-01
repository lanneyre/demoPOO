import mysql.connector
from mysql.connector import Error
import bcrypt
from datetime import date


class User:
    # Propriété de CLASSE (équivalent au static $pdo)
    # Elle est partagée par toutes les instances
    _db_connection = None

    def __init__(
        self, id=None, pseudo="", email="", mdp="", created_at="", updated_at=""
    ):
        """
        CONSTRUCTEUR (__init__)
        Equivalent de public function __construct
        """
        self.id = id
        self.pseudo = pseudo
        self.email = email

        # Hashage du mot de passe (similaire à password_hash en PHP)
        # Note: bcrypt.hashpw attend des bytes, d'où le .encode()
        if mdp:
            salt = bcrypt.gensalt()
            self.mdp = bcrypt.hashpw(mdp.encode("utf-8"), salt)
        else:
            self.mdp = ""

        # Gestion des dates par défaut
        today = date.today().strftime("%Y-%m-%d")
        self.created_at = created_at if created_at else today
        self.updated_at = updated_at if updated_at else today

        # On s'assure que la connexion est prête (appel méthode de classe)
        User.get_db_connection()

    @classmethod
    def get_db_connection(cls):
        """
        MÉTHODE DE CLASSE (Singleton de connexion)
        Equivalent de public static function getPdo()
        On utilise @classmethod pour accéder à la variable de classe cls._db_connection
        """
        if cls._db_connection is None:
            config = {
                "user": "admin",
                "password": "Y@tta!6623",
                "host": "localhost",
                "database": "bddHeritage",
            }
            try:
                cls._db_connection = mysql.connector.connect(**config)
            except Error as e:
                print(f"Erreur !: {e}")

        return cls._db_connection

    # En Python, les getters/setters (__get/__set) ne sont pas utilisés de la même façon.
    # Les attributs sont publics par défaut. On accède direct via mon_user.pseudo.

    @classmethod
    def get_user_by_id(cls, user_id: int):
        """
        FACTORY (Méthode de classe)
        Equivalent de public static function getUserById()
        cls représente la classe 'User'.
        """
        cnx = cls.get_db_connection()
        cursor = cnx.cursor(
            dictionary=True
        )  # dictionary=True pour avoir un retour type assoc array

        sql = "SELECT * FROM user WHERE id = %s"
        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            print("L'utilisateur n'existe pas")
            return cls()  # Retourne un user vide
        else:
            # Retourne une nouvelle instance de User (ou de la classe enfant qui appelle)
            return cls(
                id=row["id"],
                pseudo=row["pseudo"],
                email=row["email"],
                mdp=row[
                    "mdp"
                ],  # Attention: ici on repasse le mdp déjà hashé, il faudrait adapter le constructeur
                created_at=row["created_at"],
                updated_at=row["updated_at"],
            )

    @classmethod
    def get_all(cls):
        """
        Equivalent de public static function getAll()
        """
        cnx = cls.get_db_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        cursor.close()

        users = []
        for u in rows:
            # On instancie un nouvel objet pour chaque ligne
            users.append(
                cls(id=u["id"], pseudo=u["pseudo"], email=u["email"], mdp=u["mdp"])
            )

        return users
