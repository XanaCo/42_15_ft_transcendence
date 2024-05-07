
from models import elem


# Création d'instances d'elem
def	addData():
	elem1 = elem.objects.create(name="Flotte", attElemFlotte=50, attElemFeuille=50, attElemChaud=200, attElemBrise=100, attElemSable=200, attElemBagarre=100, attElemCaillou=200)
	elem2 = elem.objects.create(name="Feuille", attElemFlotte=200, attElemFeuille=50, attElemChaud=50, attElemBrise=100, attElemSable=100, attElemBagarre=100, attElemCaillou=100)
	elem3 = elem.objects.create(name="Chaud", attElemFlotte=50, attElemFeuille=200, attElemChaud=50, attElemBrise=200, attElemSable=50, attElemBagarre=100, attElemCaillou=100)
	elem4 = elem.objects.create(name="Brise", attElemFlotte=100, attElemFeuille=100, attElemChaud=50, attElemBrise=50, attElemSable=200, attElemBagarre=100, attElemCaillou=50)
	elem5 = elem.objects.create(name="Sable", attElemFlotte=50, attElemFeuille=100, attElemChaud=200, attElemBrise=50, attElemSable=50, attElemBagarre=100, attElemCaillou=100)
	elem6 = elem.objects.create(name="Bagarre", attElemFlotte=100, attElemFeuille=100, attElemChaud=100, attElemBrise=100, attElemSable=100, attElemBagarre=50, attElemCaillou=100)
	elem7 = elem.objects.create(name="Caillou", attElemFlotte=50, attElemFeuille=100, attElemChaud=100, attElemBrise=200, attElemSable=100, attElemBagarre=100, attElemCaillou=50)

# Création d'instances d'attack
# attack1 = attack.objects.create(name="Goute", elem=elem1, power=50)
# attack2 = attack.objects.create(name="Attack2", elem=elem2, power=40)

# Création d'instances de species
# species1 = species.objects.create(name="Species1", elem=elem1, hp=100, at=80, de=60, sp=70)
# species2 = species.objects.create(name="Species2", elem=elem2, hp=120, at=70, de=50, sp=80)

