# import json

# from channels.generic.websocket import WebsocketConsumer

# # loggers
# import logging
# logger = logging.getLogger(__name__)

# class Challenger(WebsocketConsumer):


# 	async def connect(self):
# 		self.accept()

# 	async def disconnect(self, code):
# 		pass

# 	async def receive(self, text_data):
# 		msg = json.loads(text_data)["message"]
# 		if "key" in msg:
# 			key_event = msg["key"]
# 			if key_event in ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"]:
# 				self.handle_arrow_key(key_event)

# 		# self.send(text_data=json.dumps({"message": msg}))
# 	async def handle_arrow_key(self, key_event):
# 		logger.error("Vous avez appuye sur la touche {key_event}")
# 		self.send(text_data=json.dumps({"message": f"Vous avez appuye sur la touche {key_event}"}))
