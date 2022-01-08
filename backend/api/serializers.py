from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User  

from .models import * 

class ProfileSerializer(ModelSerializer):
	class Meta:
		model = Profile  
		fields = '__all__'

class ProjectSerializer(ModelSerializer):
	class Meta:
		model = Project 
		fields = ('title','timeline','image','author','created')
		depth = 2
