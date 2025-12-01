<?php

/**
 * HÉRITAGE
 * La classe Admin 'étend' User.
 * Cela signifie qu'un Admin EST un User.
 * Il récupère automatiquement : $id, $pseudo, $email, getPdo(), etc.
 */
class admin extends user
{
    // Propriété spécifique à l'Admin (que User n'a pas)
    protected string $grade;

    /**
     * SURCHARGE DU CONSTRUCTEUR
     * On redéfinit le constructeur car l'Admin a une donnée en plus ($grade).
     */
    public function __construct($id = null, $pseudo = "", $email = "", $mdp = "", $grade = "", $created_at = "", $updated_at = "")
    {
        // 1. APPEL AU PARENT
        // On ne réécrit pas le code pour gérer l'id, le pseudo, le mot de passe...
        // On délègue ce travail au constructeur de la classe mère (User).
        parent::__construct($id, $pseudo, $email, $mdp, $created_at, $updated_at);
        // 2. SPÉCIFICITÉ
        // On gère uniquement ce qui est propre à l'Admin
        $this->grade = $grade;
    }

    /*
     * Encore une fois, la version commentée montre une méthode d'instance.
     * Elle obligerait à créer un objet admin vide avant de le remplir.
     */
    // public function getAdminById(int $id)
    // {
    //     $req = $this->pdo->prepare("SELECT * FROM admin JOIN user ON (user.id = admin.id_user) WHERE user.id = :id");
    //     $data = $req->execute(["id" => $id]);

    //     if ($req->rowCount() == 0) {
    //         echo "L'utilisateur n'existe pas";
    //     } else {
    //         $u = $req->fetch();
    //         $this->id = $u["id"];
    //         $this->pseudo = $u["pseudo"];
    //         $this->email = $u["email"];
    //         $this->mdp = $u["mdp"];
    //         $this->grade = $u["grade"];
    //         $this->created_at = $u["created_at"];
    //         $this->updated_at = $u["updated_at"];
    //     }
    // }


    /**
     * MÉTHODE STATIQUE
     * Récupération spécifique avec une JOINTURE SQL.
     * Notez que user::$pdo est accessible ici car il est 'protected' dans la classe mère.
     */
    public static function getAdminById(int $id): admin
    {
        user::getPdo();
        // La requête joint les deux tables car les infos sont réparties (User = infos de base, Admin = grade)
        $req = user::$pdo->prepare("SELECT * FROM admin JOIN user ON (user.id = admin.id_user) WHERE user.id = :id");
        $data = $req->execute(["id" => $id]);

        if ($req->rowCount() == 0) {
            echo "L'utilisateur n'existe pas";
            return new admin();
        } else {
            $u = $req->fetch();
            // On retourne un objet de type 'admin'
            // On passe toutes les infos au constructeur, y compris le 'grade' qui vient de la table admin
            return new admin(id: $u["id"], pseudo: $u["pseudo"], email: $u["email"], mdp: $u["mdp"], grade: $u['grade'], created_at: $u['created_at'], updated_at: $u['updated_at']);
        }
    }
}
