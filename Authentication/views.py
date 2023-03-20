from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import viewsets, generics, permissions, serializers, filters
from knox.models import AuthToken
from .models import PhoneBook
from rest_framework import status
from .serializers import *
from Profiles.models import Profile
from .services import send_sms
from Profiles.serializers import ProfileSerializer, ProfileDetailSerializer	
# Create your views here.

class SignUpAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer 

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		print("serializer is valid: ",serializer.is_valid())
		# serializer.is_valid(raise_exception=True)
		
		if serializer.is_valid():
			user = serializer.save() 
			token = AuthToken.objects.create(user)
			return Response({
				"users": UserSerializer(user, context=self.get_serializer_context()).data,
				"token": token[1]
			})
		else:
			return Response(serializer.errors)
	
		


class SignInAPI(generics.GenericAPIView):
	serializer_class = LoginSerializer 

	def post(self, request):
		serializer = self.get_serializer(data=request.data)
		print(serializer)
		serializer.is_valid(raise_exception=True)
		data = serializer.validated_data
		token = AuthToken.objects.create(data)[1]
		user = UserSerializer(data, context=self.get_serializer_context()).data
		user = {
			'id':user['id'],
			'username':user['username'],
			'email':user['email'],
		}
		profile = Profile.objects.get(user=user['id'])
		return Response({
			"user": user ,
			"profile": ProfileDetailSerializer(profile).data,
			"token": token
		})

class sendOtpViewSet(generics.GenericAPIView):
	"""
		This endpoints takes in the phone number , generates an otp and sends it to the number
	"""
	serializer_class = PhoneBookSerializer 

	def post(self, request):
		try:
			new_phone = request.data['phone']
			phone, created = PhoneBook.objects.get_or_create(phone=new_phone)
			print(phone)
			sent = send_sms(phone)
			print(dir(sent))
			return Response({'message':'sent'},status=status.HTTP_201_CREATED)
		except KeyError as e:
			message = "KeyError !!! "+str(e)
			return Response({'sent':message}, status=status.HTTP_200_OK)

class checkOtpViewSet(generics.GenericAPIView):
	"""
		This endpoints takes in the phone number , generates an otp and sends it to the number
	"""
	serializer_class = PhoneBookSerializer 

	def post(self, request):
		try:
			new_phone = request.data['phone']
			otp = request.data['otp']
			verified = PhoneBook.objects.get(phone=new_phone)
			if otp == verified.otp:
				verified = True 
			else: 
				verified = False
			return Response({'verified':verified},status=status.HTTP_201_CREATED)
		except KeyError as e:
			message = "KeyError !!! "+str(e)
			return Response({'sent':message}, status=status.HTTP_200_OK)
		# except PhoneBook.DoesNotExist:


# class PhoneBookViewSet(generics.GenericAPIView):
# 	serializer_class = PhoneBookSerializer
	
# 	def post(self, request):
# 		serializer = self.get_serializer(data=request.data)
# 		try:
# 			otp = request.data['otp']
# 			phone = request.data['phone']
# 			message = "There is a problem" 

# 			if phone and otp:  # checks if both phone and otp are being submitted
			
# 				registered_number = PhoneBook.objects.get(phone=phone, otp=otp)
# 				verified = True
# 				return Response({'verified':verified}, status=status.HTTP_200_OK)
# 			elif phone: # checks if only the phone is being submitted
# 				number = PhoneBook.objects.get(phone=phone)

# 				if number:
# 					#send response to the user if number already exists.
# 					data = {"message":phone+" already exists",'status':True}
# 				else:
# 					# save the new number
# 					data = {"message":phone+" saved",'status':True}
# 					serializer.save()
# 				return Response(data, status=status.HTTP_201_CREATED)
# 			else:
# 				print(phone) 
# 				# check if number exists
# 				number = PhoneBook.objects.get(phone=phone)
# 				#send otp to number 
# 				sent = send_sms(number.otp,number.phone)
# 				print(dir(sent))
# 				if sent:
# 					message = "otp sent"				

# 			return Response({'sent':message}, status=status.HTTP_200_OK)
# 		except KeyError as e:
# 			message = "KeyError !!! "+str(e)
# 			return Response({'sent':message}, status=status.HTTP_200_OK)

# 		except PhoneBook.DoesNotExist:
# 			verified = False
# 			return Response({'verified':verified}, status=status.HTTP_200_OK)

	

class UsernameAPI(generics.GenericAPIView):
	serializer_class = UsernameSerializer

	def post(self, request):
		serializer = UsernameSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		return Response({"status":"available"}) 
