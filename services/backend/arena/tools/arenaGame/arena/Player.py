
import json
import logging

from channels.generic.websocket import WebsocketConsumer


logger = logging.getLogger(__name__)

class PlayerConsumer(WebsocketConsumer):

	def connect(self):
		self.accept()


	def disconnect(self, close_code):
		queryString = self.scope(['query_string'].decode())

	
	def receive(self, text_data):
		try:
			# cette variable contient l'input de la websocket
			text_data_json = json.loads(text_data)
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
			}
			


			# serializer les donnees a envoyer

			# envoyer

			if instance.is_valid():
				json_data2 = json.dumps(instance.data)
				self.send(json_data2)

		except Exception as e:
			logger.error("error", e)
