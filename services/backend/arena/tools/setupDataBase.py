import os
import django

# Configuration de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arenaGame.settings")
django.setup()

# Importation des modèles Django
from arena.models import elem

# Fonction pour ajouter des données à la base de données
# def addData():
    # data1 = elem(name="flotte", attElemFlotte=100, attElemFeuille=50, attElemChaud=200, attElemBrise=100, attElemSable=200, attElemBagarre=100, attElemCaillou=200)
    # data1.save()

# Appel de la fonction pour ajouter des données
# if __name__ == "__main__":
    # addData()