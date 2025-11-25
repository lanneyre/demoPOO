<?php
require 'Employe.php';
require 'Technicien.php';

$employe = new Employe("Dupont", 30, 3000.00, "123-45-6789");
echo $employe->afficher() . PHP_EOL;
$employe->augmentation(5);
echo "Après augmentation de 5% :" . PHP_EOL;
echo $employe->afficher() . PHP_EOL;

$technicien = new Technicien("Martin", 28, 3200.00, "987-65-4321", "A");
echo $technicien->afficher() . PHP_EOL;

$technicien->augmentation(10);
echo "Après augmentation de 10% :" . PHP_EOL;
echo $technicien->afficher() . PHP_EOL;

$technicien->grade = "B";
echo "Après changement de grade à B :" . PHP_EOL;
echo $technicien->afficher() . PHP_EOL;
