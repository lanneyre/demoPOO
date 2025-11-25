<?php
class Genre extends Utils
{
    protected int|null $Genre_Id;
    protected string $Genre_Titre;
    protected string $Genre_Description;

    public function __construct($Genre_Id = null, $Genre_Titre = "", $Genre_Description = "")
    {
        $this->Genre_Id = $Genre_Id;
        $this->Genre_Titre = $Genre_Titre;
        $this->Genre_Description = $Genre_Description;
    }
}
