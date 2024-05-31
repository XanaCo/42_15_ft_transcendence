from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Image, Individual, Elem, Attack, Species

# from arena import models

# import time

def index(request):
	return HttpResponse("Hello from arena app")

#############################################################################################################
#	BATTLE
#############################################################################################################

def getStat(base, iv, lvl):
	return (2 * base + iv * 7) * lvl / 100 + 5

def getHpStat(base, iv, lvl):
	return (2 * base + iv * 7) * lvl / 100 + lvl + 10

# background program
# def runGames():
# 	# time.sleep(3)
# 	# setupDB()
# 	x = 0
# 	while True:
# 		x += 1

def testView(request):
	# Renvoie une réponse HTTP avec un message simple
	return HttpResponse("Bonjour, ceci est une vue Django !", content_type='text/plain')

def testImage(request):
	# return JsonResponse({'error': 'Internet'})
	newImg = Image.objects.create(image_field='jess.png')
	# return newImg.image_url
	return HttpResponse("img:", newImg.image_url)

def getMultiplyingFactor(attType, defType, type):

	if attType.name == type.name:
		multiFactor = 1.5
	else:
		multiFactor = 1
	match defType.name:
		case "Flotte":
			multiFactor *= type.attElemFlotte
		case "Feuille":
			multiFactor *= type.attElemFeuille
		case "Chaud":
			multiFactor *= type.attElemChaud
		case "Brise":
			multiFactor *= type.attElemBrise
		case "Sable":
			multiFactor *= type.attElemSable
		case "Bagarre":
			multiFactor *= type.attElemBagarre
		case "Caillou":
			multiFactor *= type.attElemCaillou
	return multiFactor / 100

def	damageCalculator(attacker, defender, attack):
	(((((attacker.lvl * 0.4 + 2) * attacker.at * attack.power) / defender.de) / 50) + 2) * getMultiplyingFactor(attacker.elem, defender.elem, attack.elem)

# TO DO : ajouter les taux de capture sur les pokemons
def canItakeThisOne(hp, hp_max, lvl, rate):
	return ((1 - (hp / hp_max)) * rate + (random.randint(0, 20) - lvl) / 50 > 1)


# TO DO : ameliorer cette formule
def giveMeExpPlease(lvlDead, lvlAlive, rate):
	lvlDead * 8 * (3 - rate) + lvlAlive - lvlDead


#############################################################################################################
#	API
#############################################################################################################

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404s
from .serializers import ElemModelSerializer

class arenaAPI(APIView):
	serilizerClass = ElemModelSerializer

#############################################################################################################
#	GENERATE POKEMON
#############################################################################################################

import random

# V2
def generatePokemonZone1():
	try:
		nbr = random.randint(1, 100)
		if (nbr > 50):
		# spawn roucoul
			newPokemon = Individual("roucoul", random.randint(2, 4))

		elif (nbr > 5):
			newPokemon = Individual("rattata", random.randint(2, 4))
		
		elif (nbr > 1):
			newPokemon = Individual("nidoran^", random.randint(2, 4))
		
		else:
			newPokemon = Individual("pikachu", random.randint(2, 4))
	
	except Species.DoesNotExist:
		print("Individual creation failed or species not set")
	return newPokemon



# V1 obsolete
# def	generateIndividual():
	
# 	try:
# 		# 1% de chance de trouver un truc tres style
# 		# 5% de chance de trouver un truc style
# 		# 44% de chance de trouver de la merde 1
# 		# 50% de chance de trouver de la merde 2
# 		speBulbizarre = Species.objects.get(name="Bulbizarre")
# 		name = "Individu_" + str(random.randint(1, 1000))
# 		species_instance = Species.objects.order_by('?').first()  # Sélectionner une espèce au hasard
# 		lvl = random.randint(2, 3)
# 		iv_hp = random.randint(0, 6)
# 		iv_at = random.randint(0, 6)
# 		iv_sa = random.randint(0, 6)
# 		iv_de = random.randint(0, 6)
# 		iv_sd = random.randint(0, 6)
# 		iv_sp = random.randint(0, 6)
# 		# wtf hp ?
# 		hp = random.randint(1, 255)
# 		hp_max = getHpStat(speBulbizarre.hp)
# 		at = getStat(speBulbizarre.at, iv_at, lvl)
# 		sa = getStat(speBulbizarre.sa, iv_sa, lvl)
# 		de = getStat(speBulbizarre.de, iv_de, lvl)
# 		sd = getStat(speBulbizarre.sd, iv_sd, lvl)
# 		sp = getStat(speBulbizarre.sp, iv_sp, lvl)
# 		attack_instances = Attack.objects.order_by('?')[:4]  # Sélectionner 4 attaques au hasard
# 	except Species.DoesNotExist:
# 		# Si l'instance n'existe pas encore, vous pouvez créer une nouvelle instance
# 		# speBulbizarre = species.objects.create(name="Bulbizarre", elem=elemChaud, hp=45, at=49, sa=65, de=49, sd=65, sp=45)
# 		# speBulbizarre.save()
# 		print("Bulbizarre not set")

# 	# Créer l'individu avec les valeurs générées
# 	new_individual = Individual.objects.create(
# 		name=name,
# 		species=species_instance,
# 		lvl=lvl,
# 		iv_hp=iv_hp,
# 		iv_at=iv_at,
# 		iv_sa=iv_sa,
# 		iv_de=iv_de,
# 		iv_sd=iv_sd,
# 		iv_sp=iv_sp,
# 		hp=hp,
# 		hp_max=hp_max,
# 		at=at,
# 		sa=sa,
# 		de=de,
# 		sd=sd,
# 		sp=sp,
# 		id_att_1=attack_instances[0],
# 		id_att_2=attack_instances[1],
# 		id_att_3=attack_instances[2],
# 		id_att_4=attack_instances[3]
# 	)
# 	return new_individual


#############################################################################################################
#	
#############################################################################################################


