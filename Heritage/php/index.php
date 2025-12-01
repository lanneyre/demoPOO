<?php

/**
 * Héritage (extends) : Évite de copier-coller du code. Admin n'a pas besoin de redéfinir $pseudo ou getPdo(), il les "hérite" de User.
 * Parent (parent::) : Permet d'appeler la logique de la classe mère avant d'ajouter la logique spécifique de l'enfant (très visible dans le __construct).
 * Static vs Instance :
 *  Utilisez Static (user::getUserById) quand vous n'avez pas encore d'objet et que vous voulez que la classe vous en crée un. C'est l'usine.
 *  Utilisez Instance (méthodes normales) quand vous voulez manipuler un objet qui existe déjà (ex: $monUser->changerMdp()).
 */


// 1. IMPORTATION DES CLASSES
// On inclut les fichiers de définition des classes pour pouvoir les utiliser.
// require_once est plus sûr : si le fichier manque, le script s'arrête.
require_once 'model/user.php';
require_once 'model/admin.php';

// Petite fonction utilitaire pour un affichage propre dans le navigateur
function debug($data)
{
    echo '<pre style="background-color: #f4f4f4; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">';
    print_r($data);
    echo '</pre>';
}

echo "<h1>Tests des classes User et Admin</h1>";
echo "<hr>";

// =========================================================
// PARTIE 1 : TEST DE LA CLASSE USER (La Mère)
// =========================================================

echo "<h2>1. Instanciation Manuelle d'un User</h2>";
echo "<p><i>Test du constructeur __construct(). On crée l'objet nous-mêmes.</i></p>";

// Création d'un nouvel objet (sans ID car c'est une création avant insertion BDD)
$u1 = new user(null, "Etudiant_Test", "test@ecole.com", "secret123");

// Affichage
echo "Pseudo : " . $u1->pseudo . "<br>";
echo "Email : " . $u1->email . "<br>";
// On vérifie que le mot de passe est bien haché
echo "Mot de passe (haché) : " . $u1->mdp . "<br>";

debug($u1);


echo "<h2>2. Récupération via Factory (Méthode Statique)</h2>";
echo "<p><i>Test de user::getUserById(). C'est la classe qui crée l'objet depuis la BDD.</i></p>";

// Notez l'utilisation de l'opérateur de résolution de portée (::)
// On n'utilise pas $u1->getUserById(), mais user::getUserById()
$userFromBdd = user::getUserById(1);

if ($userFromBdd->id) {
    echo "✅ Utilisateur trouvé en BDD !<br>";
    debug($userFromBdd);
} else {
    echo "⚠️ Utilisateur ID 1 non trouvé (Vérifiez votre BDD).<br>";
}


// =========================================================
// PARTIE 2 : TEST DE LA CLASSE ADMIN (La Fille)
// =========================================================

echo "<hr>";
echo "<h2>3. Instanciation Manuelle d'un Admin</h2>";
echo "<p><i>Test de l'héritage. Notez la propriété 'grade' en plus.</i></p>";

// Admin prend les mêmes arguments que User + le grade en 5ème position
$a1 = new admin(null, "SuperProf", "prof@ecole.com", "root", "Moderateur");

echo "Pseudo : " . $a1->pseudo . "<br>";
echo "<strong>Grade : " . $a1->grade . "</strong> (Propriété spécifique)<br>";

debug($a1);


echo "<h2>4. Récupération Admin via Factory (Jointure)</h2>";
echo "<p><i>Test de admin::getAdminById(). La requête SQL fait un JOIN pour tout remplir.</i></p>";

$adminFromBdd = admin::getAdminById(1);

if ($adminFromBdd->id) {
    echo "✅ Admin trouvé (ID: " . $adminFromBdd->id . ") avec le grade : " . $adminFromBdd->grade . "<br>";
    debug($adminFromBdd);
} else {
    echo "⚠️ Admin ID 1 non trouvé (Vérifiez votre BDD).<br>";
}


// =========================================================
// PARTIE 3 : PREUVE DE L'HÉRITAGE (Polymorphisme)
// =========================================================

echo "<hr>";
echo "<h2>5. Vérification des Types (instanceof)</h2>";

// On teste l'objet $a1 créé manuellement plus haut
echo "Analyse de l'objet <code>\$a1</code> :<br><br>";

// Est-ce que $a1 est un Admin ?
if ($a1 instanceof admin) {
    echo "✅ \$a1 est bien une instance de <strong>admin</strong>.<br>";
} else {
    echo "❌ \$a1 n'est pas un admin.<br>";
}

// Est-ce que $a1 est un User ? (C'est là que l'héritage est prouvé)
if ($a1 instanceof user) {
    echo "✅ \$a1 est AUSSI considéré comme une instance de <strong>user</strong> (car il en hérite).<br>";
} else {
    echo "❌ \$a1 n'est pas un user.<br>";
}
