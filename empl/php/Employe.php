<?php
class Employe
{
    protected string $nom;
    protected int $age;
    protected float $salaire;
    protected string $NumSecu;

    public function __construct($nom, $age, $salaire, $NumSecu)
    {
        $this->nom = $nom;
        $this->age = $age;
        $this->salaire = $salaire;
        $this->NumSecu = $NumSecu;
    }

    public function __get($name): mixed
    {
        return $this->$name;
    }

    public function __set($name, $value): void
    {
        $this->$name = $value;
    }

    public function calculer_salaire(): float
    {
        return $this->salaire * 0.756;
    }

    public function augmentation(float $pourcentage): void
    {
        $this->salaire += $this->salaire * ($pourcentage / 100);
    }
    public function afficher(): string
    {
        return "Nom: {$this->nom}, Age: {$this->age}, Salaire Brut: {$this->salaire}, NumSecu: {$this->NumSecu}";
    }

    public function __toString(): string
    {
        return $this->afficher();
    }
}
