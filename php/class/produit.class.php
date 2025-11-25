<?php
class Produit
{
    private int|null $id = null;
    private string $description;
    private float $prix;
    private string $nom;
    private array $images = [];
    private int $stock;
    private array $categories = [];

    public function __construct($id = null, $nom, $description, $prix, $stock = 0)
    {
        $this->nom = $nom;
        $this->id = $id;
        $this->description = $description;
        $this->prix = $prix;
        $this->stock = $stock;
    }

    public function getNom()
    {
        if ($this->id != null)
            return $this->nom;
        else
            return "erreur";
    }

    public function addImage(string $url)
    {
        $this->images[]  = $url;
    }

    public function addCategorie(Categorie $c)
    {
        $this->categories[]  = $c;
    }

    public function __get($name)
    {
        return $this->$name;
    }

    public function __set($name, $value)
    {
        $this->$name = $value;
    }
}
