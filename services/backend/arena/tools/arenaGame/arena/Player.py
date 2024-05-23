
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
		

		except Exception as e:
			logger.error("error", e)
