<?php
class User
{
    public int $id;
    public string $nom;
    public string $prenom;
    public string $email;

    public function __construct($id = 42, $nom = "SMITH", $prenom = "John", $email = "noreply@ici.com")
    {
        $this->id = $id;
        $this->nom = $nom;
        $this->prenom = $prenom;
        $this->email = $email;
    }

    public function display()
    {
        return "" . $this->id . "\t" . $this->nom . "\t" . $this->prenom . "\t" . $this->email . "\n";
    }
}


// $u = new User();
// var_dump($u);
// $u->id = 22;
// $u->nom = "Tata";
// $u->prenom = "Yoyo";
// $u->email = "tata@yoyo.com";
// var_dump($u);

$u2 = new User(5, "truc 2", "machin");
echo ($u2->display());
