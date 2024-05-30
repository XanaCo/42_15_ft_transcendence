
from .models import Elem, Attack, Species, Individual, Player, Game

from .views import generateIndividual

from django.db import IntegrityError

# Création d'instances d'elem
def	addData():

#############################################################################################################
#	ELEM DATA
#############################################################################################################

	try:
		try:
			elemFlotte = Elem.objects.get(name="Flotte")
		except Elem.DoesNotExist:
			elemFlotte = Elem.objects.create(name="Flotte", attElemFlotte=50, attElemFeuille=50, attElemChaud=200, attElemBrise=100, attElemSable=200, attElemBagarre=100, attElemCaillou=200, attElemBanal)
			elemFlotte.save()
		try:
			elemFeuille = Elem.objects.get(name="Feuille")
		except Elem.DoesNotExist:
			elemFeuille = Elem.objects.create(name="Feuille", attElemFlotte=200, attElemFeuille=50, attElemChaud=50, attElemBrise=100, attElemSable=100, attElemBagarre=100, attElemCaillou=100, attElemBanal=100)
			elemFeuille.save()
		try:
			elemChaud = Elem.objects.get(name="Chaud")
		except Elem.DoesNotExist:
			elemChaud = Elem.objects.create(name="Chaud", attElemFlotte=50, attElemFeuille=200, attElemChaud=50, attElemBrise=200, attElemSable=50, attElemBagarre=100, attElemCaillou=100, attElemBanal=100)
			elemChaud.save()
		try:
			elemBrise = Elem.objects.get(name="Brise")
		except Elem.DoesNotExist:
			elemBrise = Elem.objects.create(name="Brise", attElemFlotte=100, attElemFeuille=100, attElemChaud=50, attElemBrise=50, attElemSable=200, attElemBagarre=100, attElemCaillou=50, attElemBanal=100)
			elemBrise.save()
		try:
			elemSable = Elem.objects.get(name="Sable")
		except Elem.DoesNotExist:
			elemSable = Elem.objects.create(name="Sable", attElemFlotte=50, attElemFeuille=100, attElemChaud=200, attElemBrise=50, attElemSable=50, attElemBagarre=100, attElemCaillou=100, attElemBanal=100)
			elemSable.save()
		try:
			elemBagarre = Elem.objects.get(name="Bagarre")
		except Elem.DoesNotExist:
			elemBagarre = Elem.objects.create(name="Bagarre", attElemFlotte=100, attElemFeuille=100, attElemChaud=100, attElemBrise=100, attElemSable=100, attElemBagarre=50, attElemCaillou=100, attElemBanal=200)
			elemBagarre.save()
		try:
			elemCaillou = Elem.objects.get(name="Caillou")
		except Elem.DoesNotExist:
			elemCaillou = Elem.objects.create(name="Caillou", attElemFlotte=50, attElemFeuille=100, attElemChaud=100, attElemBrise=200, attElemSable=100, attElemBagarre=100, attElemCaillou=50, attElemBanal=100)
			elemCaillou.save()
			
		try:
			elemBanal = Elem.objects.get(name="Banal")
		except Elem.DoesNotExist:
			elemBanal = Elem.objects.create(name="Banal", attElemFlotte=100, attElemFeuille=100, attElemChaud=100, attElemBrise=100, attElemSable=100, attElemBagarre=100, attElemCaillou=100, attElemBanal=50)
			elemBanal.save()

#############################################################################################################
#	ATTACK DATA
#############################################################################################################

		try:
			attBulle = Attack.objects.get(name="Bulle")
		except Attack.DoesNotExist:
			attBulle = Attack.objects.create(name="Bulle", elem=elemFlotte, power=40, variety=1)
			attBulle.save()

		try:
			attFeu = Attack.objects.get(name="Feu")
		except Attack.DoesNotExist:
			attFeu = Attack.objects.create(name="Feu", elem=elemChaud, power=40, variety=1)
			attFeu.save()

		try:
			attTige = Attack.objects.get(name="Tige")
		except Attack.DoesNotExist:
			attTige = Attack.objects.create(name="Tige", elem=elemFeuille, power=40, variety=0)
			attTige.save()

		try:
			attSouffle = Attack.objects.get(name="Souffle")
		except Attack.DoesNotExist:
			attSouffle = Attack.objects.create(name="Souffle", elem=elemBrise, power=40, variety=1)
			attSouffle.save()

		try:
			attTornado = Attack.objects.get(name="Tornado")
		except Attack.DoesNotExist:
			attTornado = Attack.objects.create(name="Tornado", elem=elemBrise, power=80, variety=1)
			attTornado.save()

#############################################################################################################
#	SPECIES DATA
#############################################################################################################

		Species.objects.all().delete()

		try:
			speCarapuce = Species.objects.get(name="Carapuce")
		except Species.DoesNotExist:
			speCarapuce = Species.objects.create(name="Carapuce", elem=elemFlotte, hp=44, at=48, sa=50, de=65, sd=64, sp=43)
			speCarapuce.save()

		try:
			speCarabaffe = Species.objects.get(name="Carabaffe")
		except Species.DoesNotExist:
			speCarabaffe = Species.objects.create(name="Carabaffe", elem=elemFlotte, hp=59, at=63, sa=65, de=80, sd=80, sp=58)
			speCarabaffe.save()

		try:
			speTortank = Species.objects.get(name="Tortank")
		except Species.DoesNotExist:
			speTortank = Species.objects.create(name="Tortank", elem=elemFlotte, hp=79, at=83, sa=85, de=100, sd=105, sp=78)
			speTortank.save()

		try:
			speSalameche = Species.objects.get(name="Salameche")
		except Species.DoesNotExist:
			speSalameche = Species.objects.create(name="Salameche", elem=elemChaud, hp=39, at=52, sa=60, de=43, sd=50, sp=65)
			speSalameche.save()

		try:
			speReptincel = Species.objects.get(name="Reptincel")
		except Species.DoesNotExist:
			speReptincel = Species.objects.create(name="Reptincel", elem=elemChaud, hp=58, at=64, sa=80, de=58, sd=65, sp=80)
			speReptincel.save()

		try:
			speDracaufeu = Species.objects.get(name="Dracaufeu")
		except Species.DoesNotExist:
			speDracaufeu = Species.objects.create(name="Dracaufeu", elem=elemChaud, hp=78, at=84, sa=109, de=78, sd=85, sp=100)
			speDracaufeu.save()

		try:
			speBulbizarre = Species.objects.get(name="Bulbizarre")
		except Species.DoesNotExist:
			speBulbizarre = Species.objects.create(name="Bulbizarre", elem=elemFeuille, hp=45, at=49, sa=65, de=49, sd=65, sp=45)
			speBulbizarre.save()

		try:
			speHerbizarre = Species.objects.get(name="Herbizarre")
		except Species.DoesNotExist:
			speHerbizarre = Species.objects.create(name="Herbizarre", elem=elemFeuille, hp=60, at=62, sa=80, de=63, sd=80, sp=60)
			speHerbizarre.save()

		try:
			speFlobizarre = Species.objects.get(name="Flobizarre")
		except Species.DoesNotExist:
			speFlobizarre = Species.objects.create(name="Flobizarre", elem=elemFeuille, hp=80, at=82, sa=100, de=83, sd=100, sp=80)
			speFlobizarre.save()

		try:
			speRoucoul = Species.objects.get(name="Roucoul")
		except Species.DoesNotExist:
			speRoucoul = Species.objects.create(name="Roucoul", elem=elemBrise, hp=40, at=45, sa=35, de=40, sd=35, sp=56)
			speRoucoul.save()

		try:
			speRoucoups = Species.objects.get(name="Roucoups")
		except Species.DoesNotExist:
			speRoucoups = Species.objects.create(name="Roucoups", elem=elemBrise, hp=63, at=60, sa=50, de=55, sd=50, sp=71)
			speRoucoups.save()

		try:
			speRoucarnage = Species.objects.get(name="Roucarnage")
		except Species.DoesNotExist:
			speRoucarnage = Species.objects.create(name="Roucarnage", elem=elemBrise, hp=83, at=80, sa=70, de=75, sd=70, sp=101)
			speRoucarnage.save()

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

		Player.objects.all().delete()
		try:
			playerA = Player.objects.get(idPlayer=10)
		except Player.DoesNotExist:
			playerA = Player.objects.create(idPlayer=10, isBot=False, idIndividual1=bulbasaurA, idIndividual2=None, idIndividual3=None, idIndividual4=None, idIndividual5=None, idIndividual6=None)
			playerA.save()

		try:
			playerB = Player.objects.get(idPlayer=11)
		except Player.DoesNotExist:
			playerB = Player.objects.create(idPlayer=11, isBot=True, idIndividual1=bulbasaurB, idIndividual2=None, idIndividual3=None, idIndividual4=None, idIndividual5=None, idIndividual6=None)
			playerB.save()

#############################################################################################################
#	GAME DATA
#############################################################################################################

		Game.objects.all().delete()
		try:
			game1 = Game.objects.get(idGame=10)
		except Game.DoesNotExist:
			game1 = Game.objects.create(idGame=10, idPlayerA=playerA, idPlayerB=playerB, nbPlayer=2)
			game1.save()


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

