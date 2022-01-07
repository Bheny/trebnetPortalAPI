from rest_framework.serializers import ModelSerializer

from .models import * 

class ProjectSerializer(ModelSerializer):
	class Meta:
		model = Project 
		fields = '__all__'
		depth = 2
