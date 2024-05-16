from rest_framework import serializers
from .models import elem, attack, species, individual, player, game

class ElemModelSerializer(serializers.ModelSerializer):

	name = serializers.IntegerField(read_only=True)
	attElemFlotte = serializers.IntegerField(read_only=True)
	attElemFeuille = serializers.IntegerField(read_only=True)
	attElemChaud = serializers.IntegerField(read_only=True)
	attElemBrise = serializers.IntegerField(read_only=True)
	attElemSable = serializers.IntegerField(read_only=True)
	attElemBagarre = serializers.IntegerField(read_only=True)
	attElemCaillou = serializers.IntegerField(read_only=True)

	class Meta:
		model = elem
		fields=['name', 'attElemFlotte', 'attElemFeuille', 'attElemChaud',
		'attElemBrise', 'attElemSable', 'attElemBagarre', 'attElemCaillou']

class AttackSerializer(serializers.ModelSerializer):
	name = serializers.CharField(read_only = True)
	elem = serializers.ForeignKey(read_only = True)
	power = serializers.IntegerField(read_only = True)
	class Meta:
		model = attack
		fields = ['attackID', 'name', 'elem', 'power']

class SpeciesSerializer(serializers.ModelSerializer):
	name = serializers.CharField(read_only=True)
	elem = serializers.ForeignKey(read_only=True)
	hp = serializers.IntegerField(read_only=True)
	at = serializers.IntegerField(read_only=True)
	sa = serializers.IntegerField(read_only=True)
	de = serializers.IntegerField(read_only=True)
	sd = serializers.IntegerField(read_only=True)
	sp = serializers.IntegerField(read_only=True)
	class Meta:
		model = species
		fields = ["speciesID", 'name', 'elem', 'hp', 'at', 'sa', 'de', 'sd', 'sp']

class IndividualSerializer(serializers.ModelSerializer):
	id_ind = serializers.AutoField(read_only=True)
	name = serializers.CharField(read_only=True)
	species = serializers.ForeignKey(read_only=True)
	lvl = serializers.IntegerField(read_only=True)
	iv_hp = serializers.IntegerField(read_only=True)
	iv_at = serializers.IntegerField(read_only=True)
	iv_sa = serializers.IntegerField(read_only=True)
	iv_de = serializers.IntegerField(read_only=True)
	iv_sd = serializers.IntegerField(read_only=True)
	iv_sp = serializers.IntegerField(read_only=True)
	hp = serializers.IntegerField(read_only=True)
	hp_max = serializers.IntegerField(read_only=True)
	at = serializers.IntegerField(read_only=True)
	sa = serializers.IntegerField(read_only=True)
	de = serializers.IntegerField(read_only=True)
	sd = serializers.IntegerField(read_only=True)
	sp = serializers.IntegerField(read_only=True)
	id_att_1 = serializers.ForeignKey(read_only=True)
	id_att_2 = serializers.ForeignKey(read_only=True)
	id_att_3 = serializers.ForeignKey(read_only=True)
	id_att_4 = serializers.ForeignKey(read_only=True)
	class Meta:
		model = individual
		fields = ['id_ind', 'name', 'species', 'lvl', 'iv_hp', 'iv_at', 'iv_sa', 'iv_de', 'iv_sd', 'hp', 'hp_max', 'at', 'sa', 'de', 'sd', 'sp', 'id_att_1', 'id_att_2', 'id_att_3', 'id_att_4']

class PlayerSerializer(serializers.ModelSerializer):
	idPlayer = serializers.IntegerField(read_only=True)
	isBot = serializers.BooleanField(read_only=True)
	idIndividual1 = serializers.ForeignKey(read_only=True)
	idIndividual2 = serializers.ForeignKey(read_only=True)
	idIndividual3 = serializers.ForeignKey(read_only=True)
	idIndividual4 = serializers.ForeignKey(read_only=True)
	idIndividual5 = serializers.ForeignKey(read_only=True)
	idIndividual6 = serializers.ForeignKey(read_only=True)
	class Meta:
		model = player
		fields = ['idPlayer', 'isBot', 'idIndividual1', 'idIndividual2', 'idIndividual3', 'idIndividual4', 'idIndividual5', 'idIndividual6']

class GameSerializer(serializers.ModelSerializer):
	idGame = serializers.AutoField(read_only=True)
	idPlayerA = serializers.ForeignKey(read_only=True)
	idPlayerB = serializers.ForeignKey(read_only=True)
	nbPlayer = serializers.IntegerField(read_only=True)
	nbAttackWeAreWaitingFor = serializers.IntegerField(read_only=True)
	attackA = serializers.ForeignKey(read_only=True)
	attackB = serializers.ForeignKey(read_only=True)
	class Meta:
		model = game
		fields = ['idGame', 'idPlayerA', 'idPlayerB', 'nbPlayer', 'nbAttackWeAreWaitingFor', 'attackA', 'attackB']

