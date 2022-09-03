from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from django.http import JsonResponse
from .forms import UserRegisterForm
from django.contrib.auth.models import User, auth
from.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.middleware import csrf
from knox.models import AuthToken 
from rest_framework.response import Response 
from .serializers import UserSerializer, RegisterSerializer , LoginSerializer 

class SignUpAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer 

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save() 
		token = AuthToken.objects.create(user)
		return Response({
			"users": UserSerializer(user, context=self.get_serializer_context()).data,
			"token": token[1]
		})


class SignInAPI(generics.GenericAPIView):
	serializer_class = LoginSerializer 

	def post(self, request):
		serializer = self.get_serializer(data=request.data)
		print(serializer)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data
		return Response({
			"user": UserSerializer(user, context=self.get_serializer_context()).data,
			"token": AuthToken.objects.create(user)[1]
		})

def logout(request):
	user = request.user
	auth.logout(request)
	return JsonResponse({'message':'{} logged out sucessfully'.format(user)}, safe=False)

