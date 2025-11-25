class User:
    id: int
    nom: str
    prenom: str
    email: str

    def __init__(self, id=42, nom="SMITH", prenom="John", email="noreply@ici.com"):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email

    def display(self):
        return (
            ""
            + str(self.id)
            + "\t"
            + self.nom
            + "\t"
            + self.prenom
            + "\t"
            + self.email
            + "\n"
        )


u = User(id=4, email="test@test.com")
print(u.display())
