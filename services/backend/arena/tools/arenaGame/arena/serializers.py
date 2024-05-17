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
		fields = '__all__'

class AttackSerializer(serializers.ModelSerializer):
	name = serializers.CharField(read_only = True)
	elem = serializers.PrimaryKeyRelatedField(queryset=elem.objects.all())
	power = serializers.PrimaryKeyRelatedField(queryset=attack.objects.all())
	class Meta:
		model = attack
		fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
	name = serializers.CharField(read_only=True)
	elem = serializers.PrimaryKeyRelatedField(queryset=elem.objects.all())
	hp = serializers.IntegerField(read_only=True)
	at = serializers.IntegerField(read_only=True)
	sa = serializers.IntegerField(read_only=True)
	de = serializers.IntegerField(read_only=True)
	sd = serializers.IntegerField(read_only=True)
	sp = serializers.IntegerField(read_only=True)
	class Meta:
		model = species
		fields = '__all__'

class IndividualSerializer(serializers.ModelSerializer):
	id_ind = serializers.IntegerField(read_only=True)
	name = serializers.CharField(read_only=True)
	species = serializers.PrimaryKeyRelatedField(queryset=species.objects.all())
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
	id_att_1 = serializers.PrimaryKeyRelatedField(queryset=attack.objects.all())
	id_att_2 = serializers.PrimaryKeyRelatedField(queryset=attack.objects.all())
	id_att_3 = serializers.PrimaryKeyRelatedField(queryset=attack.objects.all())
	id_att_4 = serializers.PrimaryKeyRelatedField(queryset=attack.objects.all())
	class Meta:
		model = individual
		fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
	idPlayer = serializers.IntegerField(read_only=True)
	isBot = serializers.BooleanField(read_only=True)
	idIndividual1 = serializers.PrimaryKeyRelatedField(queryset=individual.objects.all())
	idIndividual2 = serializers.PrimaryKeyRelatedField(queryset=individual.objects.all())
	idIndividual3 = serializers.PrimaryKeyRelatedField(queryset=individual.objects.all())
	idIndividual4 = serializers.PrimaryKeyRelatedField(queryset=individual.objects.all())
	idIndividual5 = serializers.PrimaryKeyRelatedField(queryset=individual.objects.all())
	idIndividual6 = serializers.PrimaryKeyRelatedField(queryset=individual.objects.all())
	class Meta:
		model = player
		fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
	idGame = serializers.IntegerField(read_only=True)
	idPlayerA = serializers.PrimaryKeyRelatedField(queryset=player.objects.all())
	idPlayerB = serializers.PrimaryKeyRelatedField(queryset=player.objects.all())
	nbPlayer = serializers.IntegerField(read_only=True)
	nbAttackWeAreWaitingFor = serializers.IntegerField(read_only=True)
	attackA = serializers.PrimaryKeyRelatedField(queryset=attack.objects.all())
	attackB = serializers.PrimaryKeyRelatedField(queryset=attack.objects.all())
	class Meta:
		model = game
		fields = '__all__'

