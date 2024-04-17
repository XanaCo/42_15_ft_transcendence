import json

from channels.generic.websocket import WebsocketConsumer

# loggers
import logging
logger = logging.getLogger(__name__)

class Challenger(WebsocketConsumer):


	def connect(self):
		logger.debug("je passe ici")
		self.accept()

	async def disconnect(self, code):
		pass

	def receive(self, text_data):
		# try:
        # 	# Essayer de charger le texte comme JSON
        # 	data = json.loads(text_data)
    	# except json.JSONDecodeError:
    	#     # Si une erreur de décodage se produit, gérer le cas où le texte n'est pas JSON valide
    	#     print("Erreur : Le texte reçu n'est pas un JSON valide")
    	#     return

		logger.debug("je passe par recieve")
		# msg = json.loads(text_data)["message"]
		# if "key" in msg:
		# 	key_event = msg["key"]
		# 	if key_event in ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"]:
		# 		self.handle_arrow_key(key_event)

		# self.send(text_data=json.dumps({"message": msg}))
	# async def handle_arrow_key(self, key_event):
	# 	logger.error("Vous avez appuye sur la touche {key_event}")
	# 	self.send(text_data=json.dumps({"message": f"Vous avez appuye sur la touche {key_event}"}))

		# self.send(text_data=json.dumps({"message": msg}))
	# async def handle_arrow_key(self, key_event):
	# 	logger.error("Vous avez appuye sur la touche {key_event}")
	# 	self.send(text_data=json.dumps({"message": f"Vous avez appuye sur la touche {key_event}"}))
