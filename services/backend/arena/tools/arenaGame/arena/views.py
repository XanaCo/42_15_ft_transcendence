# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Individual, Elem, Attack, Species, Game, Player

# from arena import models

# import time

def index(request):
	return HttpResponse("Hello from arena app")



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

# TO DO : mettre a jour les elems
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
#	API / SERIALIZERS
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
			newPokemon = Individual("Roucoul", random.randint(2, 4))

		elif (nbr > 5):
			newPokemon = Individual("Rattata", random.randint(2, 4))
		
		elif (nbr > 1):
			newPokemon = Individual("Nidoran^", random.randint(2, 4))
		
		else:
			newPokemon = Individual("Pikachu", random.randint(2, 4))
	
	except Species.DoesNotExist:
		print("Individual creation failed or species not set")
	return newPokemon

def generatePokemonZone2():
	try:
		nbr = random.randint(1, 100)
		if (nbr > 50):
		# spawn roucoul
			newPokemon = Individual("Roucoul", random.randint(5, 8))

		elif (nbr > 5):
			newPokemon = Individual("Rattata", random.randint(5, 8))
		
		elif (nbr > 1):
			newPokemon = Individual("Abra", random.randint(5, 8))
		
		else:
			newPokemon = Individual("Fantominus", random.randint(5, 8))
	
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
#	ENDPOINTS
#############################################################################################################

from .serializers import GameUserSerializer, GameMatchSerializer
import logging

logger = logging.getLogger(__name__)

# Mettre a jour toutes les variables d'ID

class GameUserAPI(APIView):
	def post(self, request):
		# logger.info(f'User ID: {user_id}')
		userSerializer = GameUserSerializer(data=request.data)
		if userSerializer.is_valid():
			userSerializer.save()
			return Response(userSerializer.data, status=status.HTTP_201_CREATED)
		return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, user_id=None):
		# logger.info(f'User ID: {user_id}')
		if user_id:
			try:
				user = Player.objects.get(idPlayer=user_id)
				userSerializer = GameUserSerializer(user)
				return Response(userSerializer.data, status=status.HTTP_200_OK)
			except Player.DoesNotExist:
				return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
		else:
			users = Player.objects.all()
			userSerializer = GameUserSerializer(users, many=True)
			return Response(userSerializer.data, status=status.HTTP_200_OK)
	
	def put(self, request, user_id=None):
		# logger.info(f'User ID: {user_id}')
		if not user_id:
			return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

		try:
			game_user = Player.objects.get(idPlayer=user_id)
		except Player.DoesNotExist:
			return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

		userSerializer = GameUserSerializer(game_user, data=request.data, partial=True)
		if userSerializer.is_valid():
			userSerializer.save()
			return Response(userSerializer.data, status=status.HTTP_200_OK)
		return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, user_id=None):
		# logger.info(f'Match ID: {match_id}')
		if not user_id:
			return Response({"error": "Player ID is required"}, status=status.HTTP_400_BAD_REQUEST)
		try:
			user = Player.objects.get(id=user_id)
		except Player.DoesNotExist:
			return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class GameMatchAPI(APIView):
	def post(self, request):
		# faire un embrachement pour savoir si on a un ou plusieurs joueur
		# logger.info(f'Match ID: {match_id}')
		player1 = request.data.get('player1')
		player2 = request.data.get('player2')

		try:
			userA, _ = Game.objects.get_or_create(idPlayer=player1.get("id"), userName=player1.get("username"))
			userB, _ = Game.objects.get_or_create(idPlayer=player2.get("id"), userName=player2.get("username"))
		except Game.DoesNotExist:
			return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
		match, created = Game.objects.get_or_create(
			idPlayerA=userA,
			idPlayerB=userB,
			#  un ou u=plusieurs joueurs ?
		)
		logger.info(f'Match: {match}')
		logger.info(f'Created: {created}')
		gameSerializer = GameMatchSerializer(match)
		logger.info(f'Match Serializer: {gameSerializer}')
		return Response(gameSerializer.data, status=status.HTTP_201_CREATED)

	def get(self, request, match_id=None):
		# logger.info(f'Match ID: {match_id}')
		if match_id:
			try:
				game = Game.objects.get(idGame=match_id)
				gameSerializer = GameMatchSerializer(game)
				return Response(gameSerializer.data, status=status.HTTP_200_OK)
			except Game.DoesNotExist:
				return Response({"error": "Match not found"}, status=status.HTTP_404_NOT_FOUND)

		else:
			games = Game.objects.all()
			gameSerializer = GameMatchSerializer(games, many=True)
			return Response(gameSerializer.data, status=status.HTTP_200_OK)

	def put(self, request, match_id=None):
		# logger.info(f'Match ID: {match_id}')
		if not match_id:
			return Response({"error: Match ID not found"}, status=status.HTTP_400_BAD_REQUEST)

		try:
			game = Game.objects.get(idGame=match_id)
		except Game.DoesNotExist:
			return Response({"error": "Match not found"}, status=status.HTTP_404_NOT_FOUND)
		
		gameSerializer = GameMatchSerializer(game, data=request.data, partial=True)
		if gameSerializer.is_valid():
			gameSerializer.save()
			return Response(gameSerializer.data, status=status.HTTP_200_OK)
		return Response(gameSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, match_id=None):
		# logger.info(f'Match ID: {match_id}')
		if not match_id:
			return Response({"error": "Match ID is required"}, status=status.HTTP_400_BAD_REQUEST)

		try:
			game = Game.objects.get(idGame=match_id)
		except Game.DoesNotExist:
			return Response({"error": "Match not found"}, status=status.HTTP_404_NOT_FOUND)

		game.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)