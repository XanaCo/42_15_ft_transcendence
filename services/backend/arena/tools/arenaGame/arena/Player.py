
import json
import logging

from channels.generic.websocket import WebsocketConsumer


# question pour alban

# comment je peux amener la classe game dans ma classe consumer ?
# 


logger = logging.getLogger(__name__)

class PlayerConsumer(WebsocketConsumer):

	def connect(self):
		self.accept()
		logger.info("Player connected")


	def disconnect(self, close_code):
		queryString = self.scope(['query_string'].decode())

	
	def receive(self, text_data):
		try:
			# cette variable contient l'input de la websocket
			text_data_json = json.loads(text_data)
			user_id = text_data_json.get("userID")
			# on peut acceder aux variables comme ca : id = text_data_json.get("userID")

			# trouver la bonne instance de Game

			# mettre a jour la bonne attaque
			
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
