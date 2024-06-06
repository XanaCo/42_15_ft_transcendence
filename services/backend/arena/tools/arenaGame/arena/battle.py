import json

from channels.generic.websocket import WebsocketConsumer

from .models import Game

# loggers
import logging
logger = logging.getLogger(__name__)

class Challenger(WebsocketConsumer):

	waitingA = True
	waitingB = False

	game = None

	def connect(self):
		logger.debug("je passe ici")
		try:
			self.game = Game.objects.get(idGame=10)
			self.accept()
		except Game.DoesNotExist:
			print("Player with idPlayer=1 does not exist")
		self.send(text_data=json.dumps({"message": "Internet"}))

	async def disconnect(self, code):
		logger.debug("je m'en vais")
		pass

	def performAttack(self):
		print("Performing an attack")
		# Add the code to perform an attack
	
	def runAway(self):
		print("Running away")
		# Add the code to run away
	
	def changePokemon(self):
		print("Changing Pokemon")
		# Add the code to change Pokemon
	
	def useItem(self):
		print("Using an item from the inventory")
		# Add the code to use an item

	# recup l'id du joueur et le matchId
	def receive(self, text_data):
		try:
			# Essayer de charger le texte comme JSON
			data = json.loads(text_data)
		except json.JSONDecodeError:
			# Si une erreur de décodage se produit, gérer le cas où le texte n'est pas JSON valide
			# print("Erreur : Le texte reçu n'est pas un JSON valide")
			return
		
		action = data.get('content')
		# Convert action to integer if it's a string
		if isinstance(action, str) and action.isdigit():
			action = int(action)
		# Check the value of action and perform actions accordingly
		if 0 <= action <= 3:
			self.performAttack()
		elif action == 4:
			self.runAway()
		elif 5 <= action <= 10:
			self.changePokemon()
		elif action >= 11:
			self.useItem()
		else:
			print("Invalid action")

		print("content :" + action)
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


