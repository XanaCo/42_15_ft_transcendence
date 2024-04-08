from django.shortcuts import render
from django.http import HttpResponse

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
