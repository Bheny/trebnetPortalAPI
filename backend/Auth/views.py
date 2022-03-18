from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .forms import UserRegisterForm
from django.contrib.auth.models import User, auth
from.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.middleware import csrf

@api_view(['GET'])
def getCSRFToken(request):
	csrftoken = csrf.get_token(request)
	return JsonResponse({'csrfToken':csrftoken})

@api_view(['POST'])
def register(request):
	'''
		Creating the user accounts
		Required data include 

		username, email, password1, password2

	'''
	form = UserRegisterForm()
	try:
		if request.method == 'POST':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				form.save()
				return JsonResponse({ 'success':'Username created for {}'.format(username)}, safe=False)
			else:
				return JsonResponse({'errors':form.errors }, safe=False)	
	except Exception as e:
		print(e)
		return JsonResponse({'message':'Form reset'}, safe=False)


#@csrf_exempt
@api_view(['POST'])
def login(request):
	'''
		The Login route only takes post data using Form Data.

		It uses the fields:
		     Username or email 
		     password 

		returns user data in json form when validated 
		else returns a response with key 'message'.
	'''
	if request.method == "POST":
		username = request.POST.get('username') 
		password = request.POST.get('password')
		print(username, password)
		new_user = auth.authenticate(username=username, password=password)
		print(new_user)
		if new_user is not None:
			auth.login(request, new_user)
			user = new_user
			serializer = UserSerializer(new_user)
			return JsonResponse({'user':serializer.data}, safe=False)
		return JsonResponse({'message':"user does not exist"}, safe=False)


def logout(request):
	user = request.user
	auth.logout(request)
	return JsonResponse({'message':'{} logged out sucessfully'.format(user)}, safe=False)

