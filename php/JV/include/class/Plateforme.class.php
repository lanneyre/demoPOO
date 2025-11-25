<?php
class Plateforme extends Utils
{
    protected int|null $Plateforme_Id;
    protected string $Plateforme_Titre;
    protected string $Plateforme_Description;

    public function __construct($Plateforme_Id = null, $Plateforme_Titre = "", $Plateforme_Description = "")
    {
        $this->Plateforme_Id = $Plateforme_Id;
        $this->Plateforme_Titre = $Plateforme_Titre;
        $this->Plateforme_Description = $Plateforme_Description;
    }
}
