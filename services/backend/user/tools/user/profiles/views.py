from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions, status
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import requests
import logging
import json

from rest_framework.views import APIView
from .forms import CustomUserCreationForm, CustomUserEditForm, CustomUserPasswordForm
from .models import CustomUser
from .serializers import CustomUserRegisterSerializer, CustomUsernameSerializer, CustomUserSerializer

from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
import random

logger = logging.getLogger(__name__)

def generate_random_digits(n=6):
	return "".join(map(str, random.sample(range(0, 10), n)))

def user_token(request, user_id):
	token_service_url = 'https://JWToken:4430/api/token/'
	try:
		token_response = requests.post(token_service_url, json={'user_id' : user_id}, verify=False)
		token_response.raise_for_status()
		user_token = token_response.json().get('token')
		return user_token
	except requests.exceptions.RequestException as e:
		print(f"Error token : {e}")
		return None

def create_userID_microservices(request, user_id, user_name):
	headers = {'Content-Type': 'application/json'}
	data = {"userID": user_id, "userName": user_name}

	logger.info('Creating user ID in microservices:')
	logger.info(data)
	logger.info(user_id)

	try:
		response = requests.post("https://game3d:4430/api/pong/", headers=headers, data=json.dumps(data), verify=False)
		response = requests.post("https://pokemap:4430/api/pokemap/", headers=headers, data=json.dumps(data), verify=False)
		#response = ADD OTHER MICROSERVICES LINKS HERE IF NEEDED
		return response
	except requests.exceptions.RequestException as e:
		print(f"Error creating user ID in microservices: {e}")
		return None

class JWTAuthentication(BaseAuthentication):
	def authenticate(self, request):
		auth_header = request.headers.get('Authorization')
		if not auth_header:
			return None

		token = auth_header.split(' ')[1]
		token_service_url = 'https://JWToken:4430/api/token/'
		try:
			token_response = requests.get(token_service_url, headers={'Authorization': auth_header}, verify=False)
			token_response.raise_for_status()
			valid = token_response.json().get('success')
			if valid is True:
				data = token_response.json().get('data')
				user_id = data.get('user_id')
				user = CustomUser.objects.get(user_id=user_id)
			return (user, token)
		except (requests.exceptions.RequestException, CustomUser.DoesNotExist, Exception):
			raise exceptions.AuthenticationFailed('Invalid token')


class AllCustomUserView(APIView):
	authentication_classes = [JWTAuthentication]
	def get(self, request, user_id=None):
		try:
			if user_id:
				user = get_object_or_404(CustomUser, user_id=user_id)
				serializer = CustomUserSerializer(user)
			else:
				users = CustomUser.objects.all()
				serializer = CustomUserSerializer(users, many=True)
			return (Response({'success': True, 'users': serializer.data}, status=status.HTTP_200_OK))
		except CustomUser.DoesNotExist:
			return Response({'error': 'User not found'}, status=status.HTTP_200_OK)

class CustomUserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		form = CustomUserCreationForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_online = 1
			user.save()
			token = user_token(request, user.user_id)
			if token is not None:
				logger.info('Token created')

				user_creation = create_userID_microservices(request, user.user_id, user.username)

				if user_creation is not None:
					login(request, user)
					return Response({'success': True, 'token' : token}, status=status.HTTP_201_CREATED)
				else:
					return Response({'error': 'API Error'}, status=status.HTTP_200_OK)
			else:
				return Response({'error': 'Error creating token'}, status=status.HTTP_200_OK)
		else:
			return Response(form.errors, status=status.HTTP_200_OK)

class CustomUserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			user = form.get_user()
			if user.is_2fa is True:
				verification_code = generate_random_digits()
				user.otp = verification_code
				user.otp_expiry_time = timezone.now() + timedelta(hours=1)
				user.save()
				send_mail(
					'Verification Code',
					f'Your verification code is: {user.otp}',
					'wilbanablo@gmail.com',
					[user.email],
					fail_silently=False,
				)
				return Response({'succes:': True, 'two_fa': True}, status=status.HTTP_200_OK)
			else:
				token = user_token(request, user.user_id)
				user.is_online = 1
				user.save()
				login(request, user)
				return Response({'success': True, 'token' : token, 'two_fa': False},
					status=201)
		else:
			return Response(form.errors, status=status.HTTP_200_OK)

class CustomUserVerify(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		otp = request.data.get('otp')
		try:
			user = CustomUser.objects.get(otp=otp)
			if (
				user.otp == otp and
				user.otp_expiry_time is not None and
				user.otp_expiry_time > timezone.now()
			):
				user.is_online = 1
				user.otp = ''
				user.otp_expiry_time = None
				token = user_token(request, user.user_id)
				user.save()
				login(request, user)
				return Response({'success': True, 'token' : token},
						status=201)
			else:
				return Response({'success': False, 'detail': 'Wrong code.'}, status=status.HTTP_200_OK)
		except CustomUser.DoesNotExist:
			return Response({'success': False}, status=status.HTTP_200_OK)


class CustomUserLogout(APIView):
	authentication_classes = [JWTAuthentication]
	def post(self, request):
		logger.debug(request)
		user = request.user
		try:
			user.is_online = 0
			user.save()
		except CustomUser.DoesNotExist:
			return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
		logout(request)
		return Response({'success': True, 'message': 'User logged out successfully'}, status=status.HTTP_200_OK)

class CustomUsernameView(APIView):
	authentication_classes = [JWTAuthentication]
	def get(self, request):
		serializer = CustomUsernameSerializer(request.user)
		return Response({'user': serializer.data, 'success': True}, status=status.HTTP_200_OK)

class CustomUserView(APIView):
	authentication_classes = [JWTAuthentication]
	def get(self, request):
		logger.info('User info')
		logger.info(request)
		logger.info(request.user)
		serializer = CustomUserSerializer(request.user)
		return Response({'user': serializer.data, 'success': True},status=status.HTTP_200_OK)

class CustomUserEditView(APIView):
	authentication_classes = [JWTAuthentication]
	parser_classes = (MultiPartParser, FormParser,)
	def post(self, request):
		form = CustomUserEditForm(request.data, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			return Response({'success': True}, status=status.HTTP_201_CREATED)
		else:
			return Response(form.errors, status=status.HTTP_200_OK)

class CustomUserPasswordView(APIView):
	authentication_classes = [JWTAuthentication]
	def post(self, request):
		form = CustomUserPasswordForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return Response({'success': True}, status=status.HTTP_201_CREATED)
		else:
			return Response(form.errors, status=status.HTTP_200_OK)


class CustomUserStatusView(APIView):
	def put(self, request):
		try:
			logger.info(request.data)
			user = get_object_or_404(CustomUser, user_id=request.data.get('user_id'))
			user.is_online = request.data.get('status')
			user.save()
			return Response({'success': True}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({'error': str(e)}, status=status.HTTP_200_OK)

