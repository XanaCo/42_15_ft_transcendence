from django.db import models

# USER MODEL
class GameUser(models.Model):
	userID = models.IntegerField(unique=True)
	userName = models.CharField(max_length=100, unique=True)
	gamesWon = models.IntegerField(default=0)
	gamesLost = models.IntegerField(default=0)
	gamesPlayed = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.userName}'


# GAME SETTINGS MODEL
class GameSettings(models.Model):
	SCENE_CHOICES = {
		"P": "Playground",
		"C": "Cornfield",
		"D": "Dorm",
	}

	SCORE_CHOICES = {
		7: "7",
		11: "11",
		17: "17",
	}

	TYPE_CHOICES = {
		0: "0",
		1: "1",
		2: "2",
	}

	user = models.ForeignKey(GameUser, on_delete=models.CASCADE)
	scene = models.CharField(max_length=100, choices=SCENE_CHOICES, default="Cornfield")
	ball = models.IntegerField(choices=TYPE_CHOICES, default=1)
	paddle = models.IntegerField(choices=TYPE_CHOICES, default=1)
	table = models.IntegerField(choices=TYPE_CHOICES, default=1)
	score = models.IntegerField(choices=SCORE_CHOICES, default=11)
	powerups = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.user.userName}\'s settings'

class GameMatch(models.Model):
	GAME = {
		0: "not_started",
		1: "playing",
		2: "finished",
	}

	player1 = models.ForeignKey(GameUser, on_delete=models.PROTECT, related_name='matches_as_player1')
	player2 = models.ForeignKey(GameUser, on_delete=models.PROTECT, related_name='matches_as_player2')
	player1_score = models.IntegerField(default=0)
	player2_score = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=GAME, default=0)

	def __str__(self):
		if player1 == None or player2 == None:
			return f'Match {self.id}: Players not set or deleted'
		return f'Match {self.id}: {self.player1.userName} vs {self.player2.userName}, {self.status}'
