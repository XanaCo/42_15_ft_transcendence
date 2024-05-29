from django.db import models
import random

#############################################################################################################
#	CLASSIC DATA TO BATTLE
#############################################################################################################

class elem(models.Model):
	name = models.CharField(primary_key=True, max_length=255)
	attElemFlotte = models.IntegerField()
	attElemFeuille = models.IntegerField()
	attElemChaud = models.IntegerField()
	attElemBrise = models.IntegerField()
	attElemSable = models.IntegerField()
	attElemBagarre = models.IntegerField()
	attElemCaillou = models.IntegerField()

class attack(models.Model):
	name = models.CharField(primary_key=True, max_length=255)
	elem = models.ForeignKey(elem, on_delete=models.CASCADE)
	power = models.IntegerField()
	variety = models.IntegerField()
	# 0 -> physique
	# 1 -> special

class species(models.Model):
	name = models.CharField(primary_key=True, max_length=255)
	elem = models.ForeignKey(elem, on_delete=models.CASCADE)
	hp = models.IntegerField(default=0, null=True)
	at = models.IntegerField(default=0, null=True)
	sa = models.IntegerField(default=0, null=True)
	de = models.IntegerField(default=0, null=True)
	sd = models.IntegerField(default=0, null=True)
	sp = models.IntegerField(default=0, null=True)

class individual(models.Model):
	id_ind = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	species = models.ForeignKey(species, on_delete=models.CASCADE)
	lvl = models.IntegerField()
	iv_hp = models.IntegerField()
	iv_at = models.IntegerField()
	iv_sa = models.IntegerField()
	iv_de = models.IntegerField()
	iv_sd = models.IntegerField()
	iv_sp = models.IntegerField()
	hp = models.IntegerField()
	hp_max = models.IntegerField()
	at = models.IntegerField()
	sa = models.IntegerField()
	de = models.IntegerField()
	sd = models.IntegerField()
	sp = models.IntegerField()
	id_att_1 = models.ForeignKey(attack, related_name='attack_individual_set_1', on_delete=models.CASCADE)
	id_att_2 = models.ForeignKey(attack, related_name='attack_individual_set_2', on_delete=models.CASCADE)
	id_att_3 = models.ForeignKey(attack, related_name='attack_individual_set_3', on_delete=models.CASCADE)
	id_att_4 = models.ForeignKey(attack, related_name='attack_individual_set_4', on_delete=models.CASCADE)

#	bot attack
	def	attackSelection(self):
		while (1):
			randNbr = random.randint(0,3)
			if (randNbr == 0 and self.id_att_1 is not None):
				return self.id_att_1
			if (randNbr == 1 and self.id_att_2 is not None):
				return self.id_att_2
			if (randNbr == 2 and self.id_att_3 is not None):
				return self.id_att_3
			if (randNbr == 3 and self.id_att_4 is not None):
				return self.id_att_4
	
	def	lvlUp(self):
		self.lvl += 1
		hp += self.getHpStat(self.species.hp, self.iv_hp, self.lvl) - hp_max
		hp_max = self.getHpStat(self.species.hp, self.iv_hp, self.lvl)
		at = self.getStat(self.species.at, self.iv_at, self.lvl)
		sa = self.getStat(self.species.sa, self.iv_sa, self.lvl)
		de = self.getStat(self.species.de, self.iv_de, self.lvl)
		sd = self.getStat(self.species.sd, self.iv_sd, self.lvl)
		sp = self.getStat(self.species.sp, self.iv_sp, self.lvl)
		self.save()

class player(models.Model):
	idPlayer = models.IntegerField(primary_key=True)
	isBot = models.BooleanField(default=False)
	idIndividual1 = models.ForeignKey(individual, related_name='individual_1', on_delete=models.CASCADE, null=True)
	idIndividual2 = models.ForeignKey(individual, related_name='individual_2', on_delete=models.CASCADE, null=True)
	idIndividual3 = models.ForeignKey(individual, related_name='individual_3', on_delete=models.CASCADE, null=True)
	idIndividual4 = models.ForeignKey(individual, related_name='individual_4', on_delete=models.CASCADE, null=True)
	idIndividual5 = models.ForeignKey(individual, related_name='individual_5', on_delete=models.CASCADE, null=True)
	idIndividual6 = models.ForeignKey(individual, related_name='individual_6', on_delete=models.CASCADE, null=True)
	def restoreAllIndividual(self):
		individuals = [
			self.idIndividual1, self.idIndividual2, self.idIndividual3,
			self.idIndividual4, self.idIndividual5, self.idIndividual6
		]
		for individual in individuals:
			if individual is not None:
				individual.hp = individual.hp_max
				individual.save()


class game(models.Model):
	idGame = models.IntegerField(primary_key=True)
	idPlayerA = models.ForeignKey(player, related_name='player_a_games', on_delete=models.CASCADE)
	idPlayerB = models.ForeignKey(player, related_name='player_b_games', on_delete=models.CASCADE)
	nbPlayer = models.IntegerField(default=2)
	nbAttackWeAreWaitingFor = models.IntegerField(default=nbPlayer)

	# set attack A
	attackA = models.ForeignKey(attack, related_name="attack_a", on_delete=models.CASCADE, null=True)
	# set attack B
	attackB = models.ForeignKey(attack, related_name="attack_b", on_delete=models.CASCADE, null=True)


	def	updateAttackA(self, attackA):
		# update attack
		self.attackA = attackA
		self.nbAttackWeAreWaitingFor -= 1
		# si on est pret on lance l'attaque
		if (self.nbAttackWeAreWaitingFor == 0):
			self.individualsAttack(self)
		print("A")

	def	updateAttackB(self, attackB):
		# update attack
		self.attackB = attackB
		self.nbAttackWeAreWaitingFor -= 1
		# si on est pret on lance l'attaque
		if (self.nbAttackWeAreWaitingFor == 0):
			self.individualsAttack(self)
		print("B")

	def individualsAttack(self):
		print(self.idPlayerA, self.idPlayerB, self.attackA, self.attackB)
		
		# mettre en mode attente du choix d'attaque
		self.nbAttackWeAreWaitingFor = self.nbPlayer


#############################################################################################################
#	IMAGE
#############################################################################################################
#	classe qui wrap des images

class Image(models.Model):
	image_field = models.ImageField(upload_to='jess.png')

	def image_url(self):
		return self.image_field.url
