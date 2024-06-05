
import asyncio
import json
import logging
import string
import random

from channels.generic.websocket import WebsocketConsumer

# TO DO : creer la classe GameInstance
from models import GameInstance

logger = logging.getLogger(__name__)

class PlayerConsumer(WebsocketConsumer):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.gameState = 0


	async def connect(self):
		await self.accept()
		logger.info("Player connected")
		self.gameState = await self.findLocalParty()

	async def disconnect(self, close_code):
		# a quoi sert chammel_layer ?
		# await self.chammel_layer.group_discard(self.gameState.group_name, self.channel_name)
		queryString = self.scope(['query_string'].decode())


#	Générer un nom de groupe unique
	async def generate_local_name(self, length=8):
		global group_names
		characters = string.ascii_letters + string.digits
		group_name = ''.join(random.choice(characters) for _ in range(length))  # Générer un nom aléatoire
		if (group_name in group_names):
			return await self.generate_local_name()  # Réessayer si le nom existe déjà
		else:
			group_names.append(group_name)
			return group_name


	async def findLocalParty(self):
		self.gameInstance = GameInstance()
		self.gameInstance.group_name = await self.generateLocalName()

		# Ajouter au groupe WebSocket
		await self.channel_layer.group_add(self.gameState.group_name, self.channel_name)

		# Envoyer un message indiquant que la partie est active
		await self.send(text_data=json.dumps({"party": "active"}))

		# Lancer la boucle de jeu
		asyncio.create_task(self.gameState.run_game_loop())


	async def receive(self, text_data):
		try:
			# cette variable contient l'input de la websocket
			text_data_json = json.loads(text_data)
			user_id = text_data_json.get("userID")
			# on peut acceder aux variables comme ca : id = text_data_json.get("userID")

			# trouver la bonne instance de Game

			# mettre a jour la bonne attaque

			# recuperer la variable du choix :
			# 0 a 3 pour les attaques
			# 4 a 9 pour les switchs
			# 10 pour la fuite
			# 11+ pour le choix de l'objet de l'inventaire
			
			# si je n'attends plus personne je met a jour les pv + pokemon actif

			# envoyer les donnees
			data = text_data_json.get("new")
			basejson = {
				"hpPokemonA": ,
				"hpPokemonB": ,
				"pokemonA": ,
				"pokemonB": ,
				"nbPokemonAliveA": ,
				"nbPokemonAliveB": ,
				"experienceA" ,
				"statutPokemonA": , # code binaire a 6 pokemon 12 ninaires ? present and alive
				"statutPokemonA": ,
				"LastAttackA": ,
				"LastAttackB": ,
				"fastest": ,
				"isLastAttackSuperEffectiveA": ,
				"isLastAttackSuperEffectiveB": ,
			}
			

			# serializer les donnees a envoyer
			response = json.dumps(basejson)
			# envoyer
			self.send(response)

		except json.JSONDecodeError as e:
			logger.error("Failed to decode JSON", exc_info=e)
			self.send(json.dumps({"error": "Invalid JSON format"}))

		except Exception as e:
			logger.error("An error occurred", exc_info=e)
			self.send(json.dumps({"error": "An unexpected error occurred"}))
