from rest_framework import serializers
from .models import FriendRequest
from profiles.models import CustomUser
import base64 #maybe friends pp

class FriendRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = FriendRequest
		fields = '__all__'

class FriendsSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('user_id', 
				'profile_picture', 
				'username', 
				'first_name', 
				'last_name', 
				'is_online')
	
	def get_profile_picture_data(self, obj):
	# get binary data of image
		if obj.profile_picture:
			return base64.b64encode(obj.profile_picture.read()).decode('utf-8')
		else:
			return None


