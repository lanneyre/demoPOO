<?php
require_once("include/appTop.inc.php");

$g1 = new Genre(null, "test", "de la mort");
$pl = new Plateforme(null, "test", "plateforme");

$sqlGenre = $pdo->query("SELECT * FROM genre");
$genres = [];
while ($genre = $sqlGenre->fetch()) {
    $genres[] = new Genre($genre['Genre_Id'], $genre["Genre_Titre"], $genre["Genre_Description"]);
}


// $sqlplateforme = $pdo->query("SELECT * FROM plateforme");
// $plateformes = [];
// while ($plateforme = $sqlplateforme->fetch()) {
//     $plateformes[] = new Plateforme($plateforme['Plateforme_Id'], $plateforme["Plateforme_Nom"], $plateforme["Plateforme_Description"]);
// }

var_dump($g1->Genre_Titre);
// var_dump($plateformes);
