<?php
class Technicien extends Employe
{
    private string $grade;

    public function __construct($nom, $age, $salaire, $NumSecu, $grade)
    {
        parent::__construct($nom, $age, $salaire, $NumSecu);
        $this->grade = $grade;
    }

    public function __get($name): mixed
    {
        if ($name === 'grade') {
            return $this->grade;
        }
        return parent::__get($name);
    }

    public function __set($name, $value): void
    {
        if ($name === 'grade') {
            $this->grade = $value;
        } else {
            parent::__set($name, $value);
        }
    }

    public function prime(): int
    {
        return match ($this->grade) {
            'A' => 300,
            'B' => 200,
            'C' => 100,
            default => 0,
        };
    }

    public function calculer_salaire(): float
    {
        $salaire_base = parent::calculer_salaire();
        return $salaire_base + $this->prime();
    }

    public function afficher(): string
    {
        $info_parent = parent::afficher();
        return "{$info_parent}, Grade: {$this->grade}, prime: {$this->prime()}, Salaire Total: {$this->calculer_salaire()}";
    }
}
