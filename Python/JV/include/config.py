# Fichier: config.py

# Récupérez les identifiants de votre fichier config.php
USER = "jvpython"
PASS = "jeuxvideo"
HOST = "localhost"
DBNAME = "jeuxvideo"

# Flask et SQLAlchemy préfèrent une chaîne de connexion unique (URI)
# Assurez-vous d'avoir un connecteur comme 'mysql-connector-python' (d'où le "mysql+mysqlconnector")
DATABASE_URI = f"mysql+mysqlconnector://{USER}:{PASS}@{HOST}/{DBNAME}"

# Clé secrète pour Flask (nécessaire pour les messages flash, etc.)
SECRET_KEY = "une_cle_secrete_tres_aleatoire"
