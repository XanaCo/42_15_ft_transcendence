from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Image

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

#############################################################################################################
#	API
#############################################################################################################

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ElemModelSerializer

class arenaAPI(APIView):
	serilizerClass = ElemModelSerializer