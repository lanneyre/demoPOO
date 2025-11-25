<?php
class Categorie
{
    private int $id;
    private string $nom;
    private string $description;
    private string $image;

    public function __get($name)
    {
        return $this->$name;
    }

    public function __set($name, $value)
    {
        $this->$name = $value;
    }
}
