from django.db import models

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
	hp = models.IntegerField()
	at = models.IntegerField()
	de = models.IntegerField()
	sp = models.IntegerField()

# class individual(models.Model):
# 	idInd = models.IntegerField(primary_key=True)
# 	name = models.CharField(max_length=255)
# 	idSpecies = models.ForeignKey(species, on_delete=models.CASCADE)
# 	lvl = models.IntegerField()
# 	ivHp = models.IntegerField()
# 	ivAt = models.IntegerField()
# 	ivDe = models.IntegerField()
# 	ivSp = models.IntegerField()
# 	hp = models.IntegerField()
# 	hpMax = models.IntegerField()
# 	at = models.IntegerField()
# 	de = models.IntegerField()
# 	sp = models.IntegerField()
# 	idAtt1 = models.ForeignKey(attack, on_delete=models.CASCADE)
# 	# idAtt2 = models.ForeignKey(attack, on_delete=models.CASCADE)
# 	# idAtt3 = models.ForeignKey(attack, on_delete=models.CASCADE)
# 	# idAtt4 = models.ForeignKey(attack, on_delete=models.CASCADE)

# class player(models.Model):
# 	idPlayer = models.IntegerField(primary_key=True)
# 	idIndividual1 = models.ForeignKey(individual, on_delete=models.CASCADE)
	# idIndividual2 = models.ForeignKey(individual, on_delete=models.CASCADE)
	# idIndividual3 = models.ForeignKey(individual, on_delete=models.CASCADE)
	# idIndividual4 = models.ForeignKey(individual, on_delete=models.CASCADE)
	# idIndividual5 = models.ForeignKey(individual, on_delete=models.CASCADE)
	# idIndividual6 = models.ForeignKey(individual, on_delete=models.CASCADE)






#	classe qui wrap des images

class Image(models.Model):
	image_field = models.ImageField(upload_to='jess.png')

	def image_url(self):
		return self.image_field.url
