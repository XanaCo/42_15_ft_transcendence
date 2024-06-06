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
		self.send(text_data=json.dumps({"message": msg}))
