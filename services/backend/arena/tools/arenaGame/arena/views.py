from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Image, individual, elem, attack, species

# from arena import models

# import time

class Battle:
	turn = True

	def runBattle():
		print(Battle.turn)

def index(request):
	return HttpResponse("Hello from arena app")
# Create your views here.

# fill database
# def setupDB():
# 	elemFlote = models.Elem(attElemFlote = 100, attElemFeuille = 50, attElemChaud = 200, attElemBrise = 100, attElemSable = 200, attElemBagarre = 100, attElemCaillou = 200)
# 	elemFlote.save()
# 	elemFeuille = models.Elem(attElemFlote = 200, attElemFeuille = 100, attElemChaud = 50, attElemBrise = 100, attElemSable = 100, attElemBagarre = 100, attElemCaillou = 200)
# 	elemFeuille.save()
# 	elemChaud = models.Elem(attElemFlote = 50, attElemFeuille = 200, attElemChaud = 100, attElemBrise = 200, attElemSable = 100, attElemBagarre = 100, attElemCaillou = 50)
# 	elemChaud.save()


#############################################################################################################
#	BATTLE
#############################################################################################################

def getDamage(attackerLvl, attackerAtt, attackPower, defenderDef, cm):
	return (attackerLvl * 0.4 + 2) * attackerAtt * attackPower / defenderDef / 50 + 2 * cm

def getStat(base, iv, lvl):
	return (2 * base + iv) * lvl / 100 + 5

def getHpStat(base, iv, lvl):
	return (2 * base + iv) * lvl / 100 + lvl + 10

# background program
def runGames():
	# time.sleep(3)
	# setupDB()
	x = 0
	while True:
		x += 1

def testView(request):
	# Renvoie une réponse HTTP avec un message simple
	return HttpResponse("Bonjour, ceci est une vue Django !", content_type='text/plain')

def testImage(request):
	# return JsonResponse({'error': 'Internet'})
	newImg = Image.objects.create(image_field='jess.png')
	# return newImg.image_url
	return HttpResponse("img:", newImg.image_url)

def getMultiplyingFactor(attType, defType, type):
	return 1
	# case (attType)

def	damageCalculator(attacker, defender, attack):
	(((((lvl * 0.4 + 2) * attacker.at * attack.power) / defender.de) / 50) + 2) * getMultiplyingFactor(attacker.elem, defender.elem, attack.elem)


#############################################################################################################
#	API
#############################################################################################################

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404s
from .serializers import ElemModelSerializer

class arenaAPI(APIView):
	serilizerClass = ElemModelSerializer

#############################################################################################################
#	GENERATE POKEMON
#############################################################################################################

import random

def	generateIndividual():
	
	try:
		speBulbizarre = species.objects.get(name="Bulbizarre")
		name = "Individu_" + str(random.randint(1, 1000))
		species_instance = species.objects.order_by('?').first()  # Sélectionner une espèce au hasard
		lvl = random.randint(2, 3)
		iv_hp = random.randint(0, 6)
		iv_at = random.randint(0, 6)
		iv_sa = random.randint(0, 6)
		iv_de = random.randint(0, 6)
		iv_sd = random.randint(0, 6)
		iv_sp = random.randint(0, 6)
		hp = random.randint(1, 255)
		hp_max = getHpStat(speBulbizarre.hp)
		at = getStat(speBulbizarre.at, iv_at, lvl)
		sa = getStat(speBulbizarre.sa, iv_sa, lvl)
		de = getStat(speBulbizarre.de, iv_de, lvl)
		sd = getStat(speBulbizarre.sd, iv_sd, lvl)
		sp = getStat(speBulbizarre.sp, iv_sp, lvl)
		attack_instances = attack.objects.order_by('?')[:4]  # Sélectionner 4 attaques au hasard
	except species.DoesNotExist:
		# Si l'instance n'existe pas encore, vous pouvez créer une nouvelle instance
		# speBulbizarre = species.objects.create(name="Bulbizarre", elem=elemChaud, hp=45, at=49, sa=65, de=49, sd=65, sp=45)
		# speBulbizarre.save()
		print("Bulbizarre not set")

	# Créer l'individu avec les valeurs générées
	new_individual = individual.objects.create(
		name=name,
		species=species_instance,
		lvl=lvl,
		iv_hp=iv_hp,
		iv_at=iv_at,
		iv_sa=iv_sa,
		iv_de=iv_de,
		iv_sd=iv_sd,
		iv_sp=iv_sp,
		hp=hp,
		hp_max=hp_max,
		at=at,
		sa=sa,
		de=de,
		sd=sd,
		sp=sp,
		id_att_1=attack_instances[0],
		id_att_2=attack_instances[1],
		id_att_3=attack_instances[2],
		id_att_4=attack_instances[3]
	)


#############################################################################################################
#	
#############################################################################################################


