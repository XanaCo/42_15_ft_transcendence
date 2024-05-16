
from .models import elem, attack, species, individual, player, game

from .views import generateIndividual

from django.db import IntegrityError

# Création d'instances d'elem
def	addData():

#############################################################################################################
#	ELEM DATA
#############################################################################################################

	try:
		try:
			elemFlotte = elem.objects.get(name="Flotte")
		except elem.DoesNotExist:
			elemFlotte = elem.objects.create(name="Flotte", attElemFlotte=50, attElemFeuille=50, attElemChaud=200, attElemBrise=100, attElemSable=200, attElemBagarre=100, attElemCaillou=200)
			elemFlotte.save()
		try:
			elemeFeuille = elem.objects.get(name="Feuille")
		except elem.DoesNotExist:
			elemeFeuille = elem.objects.create(name="Feuille", attElemFlotte=200, attElemFeuille=50, attElemChaud=50, attElemBrise=100, attElemSable=100, attElemBagarre=100, attElemCaillou=100)
			elemeFeuille.save()
		try:
			elemChaud = elem.objects.get(name="Chaud")
		except elem.DoesNotExist:
			elemChaud = elem.objects.create(name="Chaud", attElemFlotte=50, attElemFeuille=200, attElemChaud=50, attElemBrise=200, attElemSable=50, attElemBagarre=100, attElemCaillou=100)
			elemChaud.save()
		try:
			elemBrise = elem.objects.get(name="Brise")
		except elem.DoesNotExist:
			elemBrise = elem.objects.create(name="Brise", attElemFlotte=100, attElemFeuille=100, attElemChaud=50, attElemBrise=50, attElemSable=200, attElemBagarre=100, attElemCaillou=50)
			elemBrise.save()
		try:
			elemSable = elem.objects.get(name="Sable")
		except elem.DoesNotExist:
			elemSable = elem.objects.create(name="Sable", attElemFlotte=50, attElemFeuille=100, attElemChaud=200, attElemBrise=50, attElemSable=50, attElemBagarre=100, attElemCaillou=100)
			elemSable.save()
		try:
			elemBagarre = elem.objects.get(name="Bagarre")
		except elem.DoesNotExist:
			elemBagarre = elem.objects.create(name="Bagarre", attElemFlotte=100, attElemFeuille=100, attElemChaud=100, attElemBrise=100, attElemSable=100, attElemBagarre=50, attElemCaillou=100)
			elemBagarre.save()
		try:
			elemCaillou = elem.objects.get(name="Caillou")
		except elem.DoesNotExist:
			elemCaillou = elem.objects.create(name="Caillou", attElemFlotte=50, attElemFeuille=100, attElemChaud=100, attElemBrise=200, attElemSable=100, attElemBagarre=100, attElemCaillou=50)
			elemCaillou.save()

#############################################################################################################
#	ATTACK DATA
#############################################################################################################

		try:
			attBulle = attack.objects.get(name="Bulle")
		except attack.DoesNotExist:
			attBulle = attack.objects.create(name="Bulle", elem=elemFlotte, power=40)
			attBulle.save()

		try:
			attFeu = attack.objects.get(name="Feu")
		except attack.DoesNotExist:
			attFeu = attack.objects.create(name="Feu", elem=elemChaud, power=40)
			attFeu.save()

		try:
			attTig = attack.objects.get(name="Tige")
		except attack.DoesNotExist:
			attTig = attack.objects.create(name="Tige", elem=elemeFeuille, power=40)
			attTig.save()

#############################################################################################################
#	SPECIES DATA
#############################################################################################################

		species.objects.all().delete()

		try:
			speCarapuce = species.objects.get(name="Carapuce")
		except species.DoesNotExist:
			speCarapuce = species.objects.create(name="Carapuce", elem=elemFlotte, hp=44, at=48, sa=50, de=65, sd=64, sp=43)
			speCarapuce.save()

		try:
			speSalameche = species.objects.get(name="Salameche")
		except species.DoesNotExist:
			speSalameche = species.objects.create(name="Salameche", elem=elemChaud, hp=39, at=52, sa=60, de=43, sd=50, sp=65)
			speSalameche.save()

		try:
			speBulbizarre = species.objects.get(name="Bulbizarre")
		except species.DoesNotExist:
			speBulbizarre = species.objects.create(name="Bulbizarre", elem=elemChaud, hp=45, at=49, sa=65, de=49, sd=65, sp=45)
			speBulbizarre.save()


#############################################################################################################
#	INDIVIDUAL DATA
#############################################################################################################

		# individual.objects.all().delete()
		# try:
		# 	individual0 = individual.objects.get(id_ind=10)
		# except individual.DoesNotExist:
		# 	individual0 = individual.objects.create(id_ind=10, )

		bulbasaurA = generateIndividual()
		bulbasaurB = generateIndividual()

#############################################################################################################
#	PLAYER DATA
#############################################################################################################

		player.objects.all().delete()
		try:
			playerA = player.objects.get(idPlayer=10)
		except player.DoesNotExist:
			playerA = player.objects.create(idPlayer=10, isBot=False, idIndividual1=bulbasaurA, idIndividual2=None, idIndividual3=None, idIndividual4=None, idIndividual5=None, idIndividual6=None)
			playerA.save()

		try:
			playerB = player.objects.get(idPlayer=11)
		except player.DoesNotExist:
			playerB = player.objects.create(idPlayer=11, isBot=True, idIndividual1=bulbasaurB, idIndividual2=None, idIndividual3=None, idIndividual4=None, idIndividual5=None, idIndividual6=None)
			playerB.save()

#############################################################################################################
#	GAME DATA
#############################################################################################################




#############################################################################################################
#	OTHER
#############################################################################################################

	except IntegrityError as e:
		# Interceptez l'erreur d'intégrité (par exemple, une violation de contrainte d'unicité)
		print(f"Erreur d'intégrité lors de la création des éléments : {e}")
		# Vous pouvez journaliser l'erreur ou prendre d'autres mesures nécessaires
	except Exception as e:
		# Interceptez toute autre erreur imprévue
		print(f"Une erreur s'est produite lors de la création des éléments : {e}")
		# Vous pouvez journaliser l'erreur ou prendre d'autres mesures nécessaires

# Création d'instances d'attack
# attack1 = attack.objects.create(name="Goute", elem=elem1, power=50)
# attack2 = attack.objects.create(name="Attack2", elem=elem2, power=40)

# Création d'instances de species
# species1 = species.objects.create(name="Species1", elem=elem1, hp=100, at=80, de=60, sp=70)
# species2 = species.objects.create(name="Species2", elem=elem2, hp=120, at=70, de=50, sp=80)

