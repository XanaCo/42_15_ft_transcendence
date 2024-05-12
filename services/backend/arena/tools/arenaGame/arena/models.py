from django.db import models

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
    id_ind = models.AutoField(primary_key=True)
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

class player(models.Model):
	idPlayer = models.IntegerField(primary_key=True)
	idIndividual1 = models.ForeignKey(individual, related_name='individual_1', on_delete=models.CASCADE)
	idIndividual2 = models.ForeignKey(individual, related_name='individual_2', on_delete=models.CASCADE)
	idIndividual3 = models.ForeignKey(individual, related_name='individual_3', on_delete=models.CASCADE)
	idIndividual4 = models.ForeignKey(individual, related_name='individual_4', on_delete=models.CASCADE)
	idIndividual5 = models.ForeignKey(individual, related_name='individual_5', on_delete=models.CASCADE)
	idIndividual6 = models.ForeignKey(individual, related_name='individual_6', on_delete=models.CASCADE)

class game(models.Model):
    id_game = models.AutoField(primary_key=True)
    id_player_a = models.ForeignKey(player, related_name='player_a_games', on_delete=models.CASCADE)
    id_player_b = models.ForeignKey(player, related_name='player_b_games', on_delete=models.CASCADE)

#############################################################################################################
#	IMAGE
#############################################################################################################
#	classe qui wrap des images

class Image(models.Model):
	image_field = models.ImageField(upload_to='jess.png')

	def image_url(self):
		return self.image_field.url
