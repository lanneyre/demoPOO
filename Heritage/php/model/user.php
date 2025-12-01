<?php
class user
{
    // 1. VISIBILITÉ PROTECTED :
    // On utilise 'protected' au lieu de 'private'.
    // Cela permet aux classes enfants (comme Admin) d'accéder directement à ces propriétés.
    // C'est la base de l'héritage : partager les données avec la descendance.
    protected int|null $id;
    protected string $pseudo;
    protected string $email;
    protected string $mdp;
    protected string $created_at;
    protected string $updated_at;

    // 2. PROPRIÉTÉ STATIQUE :
    // $pdo appartient à la classe 'user' en général, pas à un utilisateur spécifique (Robert ou Sarah).
    // Tous les objets user partageront cette même connexion.
    protected static $pdo = null;

    /**
     * CONSTRUCTEUR
     * Il initialise l'objet. Notez que le hachage du mot de passe est fait ici.
     * (Attention : pour une vraie app, on sépare souvent la création depuis la BDD 
     * de la création d'un nouveau compte pour éviter de re-hacher un mot de passe déjà haché).
     */
    public function __construct($id = null, $pseudo = "", $email = "", $mdp = "", $created_at = "", $updated_at = "")
    {
        $this->id = $id;
        $this->pseudo = $pseudo;
        $this->email = $email;
        // Le hashage est automatique à l'instanciation
        $this->mdp = password_hash($mdp, PASSWORD_BCRYPT);

        // Gestion par défaut des dates si elles sont vides
        $this->created_at = $created_at ?: date("Y-m-d");
        $this->updated_at = $updated_at ?: date("Y-m-d");

        // On s'assure que la connexion BDD est prête
        user::getPdo();
    }

    /**
     * MÉTHODE STATIQUE (Singleton basique)
     * Pourquoi static ? Car on a besoin de la connexion AVANT même d'avoir un objet utilisateur.
     * On appelle user::getPdo() et non $this->getPdo().
     */
    public static function getPdo()
    {
        // Si $pdo est null, on crée la connexion (une seule fois pour toute l'application)
        if (user::$pdo == null) {
            $user = "admin";
            $pass = "Y@tta!6623";
            $host = "localhost";
            $dbname = "bddHeritage";
            try {
                user::$pdo = new PDO(
                    "mysql:host=$host;dbname=$dbname",
                    $user,
                    $pass
                );
            } catch (PDOException $e) {
                // s'il y a une erreur je la stocke dans ma variable
                echo "Erreur !: " . $e->getMessage() . "<br/>";
            }
        }
        return user::$pdo;
    }
    // 3. ENCAPSULATION / MAGIC METHODS
    // Permet d'accéder aux propriétés protected depuis l'extérieur comme si elles étaient public
    public function __get($name)
    {
        return $this->$name;
    }

    public function __set($name, $value)
    {
        $this->$name = $value;
    }

    /*
     * ---------------------------------------------------------
     * COMPARAISON PÉDAGOGIQUE : MÉTHODE D'OBJET vs DE CLASSE
     * ---------------------------------------------------------
     *
     * La méthode ci-dessous (commentée) est une méthode d'INSTANCE.
     * Pour l'utiliser, il faudrait faire :
     * $u = new User();      // On crée un objet vide inutilement
     * $u->getUserById(5);   // On demande à cet objet de se remplir
     * C'est moins logique et plus lourd.
     */
    // public function getUserById(int $id): void
    // {
    //     $req = $this->pdo->prepare("SELECT * FROM user WHERE id = :id");
    //     $data = $req->execute(["id" => $id]);

    //     if ($req->rowCount() == 0) {
    //         echo "L'utilisateur n'existe pas";
    //     } else {
    //         $u = $req->fetch();
    //         $this->id = $u["id"];
    //         $this->pseudo = $u["pseudo"];
    //         $this->email = $u["email"];
    //         $this->mdp = $u["mdp"];
    //         $this->created_at = $u["created_at"];
    //         $this->updated_at = $u["updated_at"];
    //     }
    // }


    /**
     * MÉTHODE STATIQUE
     * C'est la bonne approche. On demande à la CLASSE (le moule) de nous fabriquer un objet.
     * Usage : $monUser = user::getUserById(5);
     * Pas besoin d'instancier un objet vide au préalable.
     */
    public static function getUserById(int $id): user
    {
        user::getPdo(); // On s'assure que la connexion est là

        $req = user::$pdo->prepare("SELECT * FROM user WHERE id = :id");
        $data = $req->execute(["id" => $id]);

        if ($req->rowCount() == 0) {
            echo "L'utilisateur n'existe pas\n";
            // On retourne un user vide plutôt que null pour éviter des fatal errors
            return new user();
        } else {
            $u = $req->fetch();
            // RETOURNE UNE NOUVELLE INSTANCE
            // On utilise les arguments nommés (PHP 8) pour plus de clarté
            return new user(id: $u["id"], pseudo: $u["pseudo"], email: $u["email"], mdp: $u["mdp"], created_at: $u['created_at'], updated_at: $u['updated_at']);
        }
    }

    /**
     * Même logique : La classe nous fournit une liste d'objets.
     * Ce n'est pas le rôle d'un utilisateur unique de savoir lister tous les autres.
     */
    public static function getAll(): array
    {
        user::getPdo();

        $req = user::$pdo->query("SELECT * FROM user");
        $users = [];

        while ($u = $req->fetch()) {
            $users[] = new user(id: $u["id"], pseudo: $u["pseudo"], email: $u["email"], mdp: $u["mdp"]);;
        }

        return $users;
    }
}
