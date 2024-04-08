import json

from channels.generic.websocket import WebsocketConsumer

class Challenger(WebsocketConsumer):
	def connect(self, close_code):
		self.accept()

	def disconnect(self, code):
		pass

	def receive(self, text_data):

		msg = json.loads(text_data)["message"]
		if "key" in msg:
			key_event = msg["key"]
			if key_event in ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"]:
				self.handle_arrow_key(key_event)
	
		# self.send(text_data=json.dumps({"message": msg}))
	def handle_arrow_key(self, key_event):
		self.send(text_data=json.dumps({"message": f"Vous avez appuye sur la touche {key_event}"}))
	

