from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
import requests
import logging

from rest_framework import viewsets
from .forms import CustomUserCreationForm
from .models import CustomUser
from .serializers import CustomUserSerializer

logger = logging.getLogger(__name__)

class CustomUserViewSet(viewsets.ModelViewSet):
	serializer_class = CustomUserSerializer
	queryset = CustomUser.objects.all()

	def user_token(self, request, user_id):
		token_service_url = 'http://JWToken:8080/api/token/'
		try:
			token_response = requests.post(token_service_url, json={'user_id' : user_id})
			token_response.raise_for_status()
			user_token = token_response.json().get('token')
			return user_token
		except requests.exceptions.RequestException as e:
			print(f"Erreur lors de la connexion au service de génération de jetons : {e}")
			return None

	# @action(detail=False, methods=['get'])
	# def home(self, request):
	# 	users = CustomUser.objects.all()
	# 	serializer = CustomUserSerializer(users, many=True)
	# 	return Response(serializer.data)

	@action(detail=False, methods=['post'])
	def register(self, request):
		if request.method == 'POST':
			form = CustomUserCreationForm(request.POST, request.FILES)
			if form.is_valid():
				user = form.save(commit=False)
				user.is_online = True
				user.save()
				token = self.user_token(request, user.id)
				login(request, user)
				return Response({'success': True, 'token' : token},
					status=201)  # Utilisez le code de statut 201 pour indiquer que la ressource a été créée avec succès
			else:
				return Response(form.errors, status=400)  # Si le formulaire n'est pas valide, renvoyez les erreurs de validation avec le code de statut 400
		else:
			return Response({'error': 'Method not allowed'}, status=405)  # Si la méthode de requête n'est pas POST, renvoyez une erreur de méthode non autorisée avec le code de statut 405

	@action(detail=False, methods=['post'])
	def user_login(self, request):
		if request.method == 'POST':
			form = AuthenticationForm(request, request.POST)
			if form.is_valid():
				user = form.get_user()
				token = self.user_token(request, user.id)
				user.is_online = True
				user.save()
				login(request, user)
				return Response({'success': True, 'token' : token},
					status=201)
			else:
				return Response(form.errors, status=400)  # Si le formulaire n'est pas valide, renvoyez les erreurs de validation avec le code de statut 400
		else:
			return Response({'error': 'Method not allowed'}, status=405)  # Si la méthode de requête n'est pas POST, renvoyez une erreur de méthode non autorisée avec le code de statut 405

	@action(detail=False, methods=['post'])
	def user_logout(self, request):
		if request.method == 'POST':
			user = request.user
			token = request.headers.get('Authorization')
			token_service_url = 'http://JWToken:8080/api/token/'
			token_response = requests.get(token_service_url, headers={'Authorization' : token})
			data = token_response.json()
			user.is_online = False
			user.save()
			logout(request)
			return Response(data, status=200)
		else:
			return Response({'error': 'Method not allowed'}, status=405)  # Si la méthode de requête n'est pas POST, renvoyez une erreur de méthode non autorisée avec le code de statut 405



	# @action(detail=False, methods=['post'])
	# def edit_profile(self, request):
	# 	form = CustomProfileForm(request.data, instance=request.user)
	# 	if form.is_valid():
	# 		form.save()
	# 		return Response({'success': True}, status=201)
	# 	else:
	# 		return Response(form.errors, status=400)

	# @action(detail=False, methods=['post'])
	# def delete_account(self, request):
	# 	user = request.user
	# 	if not isinstance(user, AnonymousUser):
	# 		try:
	# 			user.delete()
	# 		except CustomUser.DoesNotExist:
	# 			return Response({'error': 'User not found'}, status=404)
	# 		logout(request)
	# 		return Response({'success': True}, status=200)
	# 	else:
	# 		return Response({'error': 'User not authenticated'}, status=401)

