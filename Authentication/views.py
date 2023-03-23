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
from Notifications.services import send_notification
from Class.models import Class
from Ranks.models import Rank
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from .server import *

class PasswordResetView(APIView):
    def post(self, request, user_id, token):
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        if password != confirm_password:
            return Response({'status': 'error', 'message': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(id=user_id).first()
        if user and PasswordResetTokenGenerator().check_token(user, token):
            try:
                user.set_password(password)
                user.save()
                return Response({'status': 'success'})
            except ValidationError as e:
                return Response({'status': 'error', 'message': e.message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': 'error', 'message': 'Invalid user or token'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordRecoveryView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            token = PasswordResetTokenGenerator().make_token(user)
            reset_link = f"{settings.BASE_URL}/password-reset/{user.id}/{token}"
            subject = 'Password Recovery'
            message = f'Click on the link below to reset your password:\n{reset_link}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send(subject, message,  recipient_list)
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error', 'message': 'User with that email not found'})

class SignUpAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer 

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		print("serializer is valid: ",serializer.is_valid())
		# serializer.is_valid(raise_exception=True)
		rank, created = Rank.objects.get_or_create(title="Associate", active=True)

		if serializer.is_valid():
			user = serializer.save() 
			send_verification_email(user)
			class_data = serializer.validated_data['class_title']
			print(dir(Class))
			c = Class.objects.get(title__iexact=class_data)
			
			profile = Profile.objects.create(user=user, rank=rank, Class=c)

			
			message = "Profile Created, You are now an Associate of the Rebel Ranks"
			send_notification(message, profile)
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
		print("this:", serializer)
		serializer.is_valid(raise_exception=True)
		data = serializer.validated_data
		#Before you log them in check if the re quested class exists.
		class_name = request.data['class_title']
		try:
			class_data = Class.objects.get(title=class_name)
			profile = Profile.objects.filter(user=user['id']).filter(Class__title=class_name)[0]
			token = AuthToken.objects.create(data)[1]
			user = UserSerializer(data, context=self.get_serializer_context()).data
			user = {
			'id':user['id'],
			'username':user['username'],
			'email':user['email'],
			}
			
			return Response({
			"user": user ,
			"profile": ProfileDetailSerializer(profile).data,
			"token": token
			})

		except Class.DoesNotExist:
			return Response({'data':'User account with this Profile does not exist'}, status=status.HTTP_400_BAD_REQUEST)
		
		

		
		
		
		
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

class verify_email(generics.GenericAPIView):
	serializer_class = EmailVerificationTokenSerializer 

	def get_object(self, token):
		try:
			token = EmailVerificationToken.objects.get(token=token)
		except EmailVerificationToken.DoesNotExist:
			raise Http404
		

	def get(self, request, token):
		# token = request.data['token']
		 # Get the verification token
		try:
			token_obj = EmailVerificationToken.objects.get(token=token)
		except EmailVerificationToken.DoesNotExist:
			# Return an error response if the token is invalid or expired
			return 'Invalid or expired token'

		# Verify the user's email address
		user = token_obj.user
		user.is_active = True
		user.save()

		# Delete the verification token only if the user is made active
		if user.is_active:
			token_obj.delete()

		# Return a success response
		response = 'Your email address has been verified'

		return Response({'data':response})



