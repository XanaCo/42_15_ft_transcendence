import json

from channels.generic.websocket import WebsocketConsumer

# loggers
import logging
logger = logging.getLogger(__name__)

class Challenger(WebsocketConsumer):


	def connect(self):
		logger.debug("je passe ici")
		self.accept()
		self.send(text_data=json.dumps({"message": "Internet"}))

	async def disconnect(self, code):
		logger.debug("je m'en vais")
		pass

	def receive(self, text_data):
		try:
			# Essayer de charger le texte comme JSON
			data = json.loads(text_data)
		except json.JSONDecodeError:
			# Si une erreur de décodage se produit, gérer le cas où le texte n'est pas JSON valide
			# print("Erreur : Le texte reçu n'est pas un JSON valide")
			return
		msg = data.get('content')
		print("content :" + msg)
		responseData = {
			"nameA": "Pikachu",
			"nameB": "Bulbizarre",
			"hpA": "100",
			"hpB": "100",
			"hpMaxA": "100",
			"hpMaxB": "100",
			"lvlA": "5",
			"lvlB": "5",
			"att1": "Charge",
			"att1Pow": "Charge",
			"att1Type": "0",
			"att2": "Fouet lianes",
			"att2Pow": "Charge",
			"att2Type": "0",
			"att3": "",
			"att3Pow": "Charge",
			"att3Type": "0",
			"att4": "",
			"att4Pow": "Charge",
			"att4Type": "0",
			"xpRate": "40",
			"lastMoveA": "Charge",
			"lastMoveB": "Charge",
			"effA": "0",
			"effB": "0",
			"fastest": "0",
			"arenaType": "1",
		}
		self.send(text_data=json.dumps(responseData))

		# self.send(text_data=json.dumps({"message": msg}))


