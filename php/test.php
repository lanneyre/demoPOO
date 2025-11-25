<?php

require("class/categorie.class.php");
require("class/produit.class.php");

$c1 = new Categorie();
$c1->nom = "Catégorie 1";
$c1->description = "J'ai pas envie de me prendre la tête";
$c2 = new Categorie();
$c2->nom = "Catégorie 2";
$c2->description = "J'ai pas envie de me prendre la tête une deuxième fois";

$p = new Produit(id: 1, nom: "test", description: "description du test", prix: 42.1);
$p->addImage("http://localhost/monimage.png");
$p->addImage("http://localhost/monimage2.png");

$p->addCategorie($c1);
$p->addCategorie($c2);
var_dump($p->categories);
