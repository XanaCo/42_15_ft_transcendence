from rest_framework import serializers
from .models import elem, attack, species

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
		fields=['name', 'attElemFlotte', 'attElemFeuille', 'attElemChaud',
		'attElemBrise', 'attElemSable', 'attElemBagarre', 'attElemCaillou']
