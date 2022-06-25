from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User  

from .models import * 

class UserSerializer(ModelSerializer):
	'''
		
	'''
	class Meta:
		model = User 
		fields = ('id','password','username','first_name','last_name','email')

class ProfileSerializer(ModelSerializer):
	class Meta:
		model = Profile  
		fields = '__all__'

class ProfileDetailSerializer(ModelSerializer):
	class Meta:
		model = Profile 
		fields = '__all__'
		depth = 1 

class ProjectSerializer(ModelSerializer):
	class Meta:
		model = Project 
		fields = ('title','timeline','image','author','created')
		depth = 2

class MyProjectsSerializer(ModelSerializer):
	class Meta:
		model = Project 
		fields = ('title','timeline','image','author','created')
		depth = 2

class TeamSerializer(ModelSerializer):
	class Meta:
		model = Team
		fields = '__all__'

class JobSerializer(ModelSerializer):
	class Meta:
		model = Job
		fields = '__all__'


class TransactionSerializer(ModelSerializer):
	class Meta:
		model = Transaction
		fields = '__all__'
		#depth = 2


class EventSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'

class QuestionSerializer(ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'
		depth = 1

class IdeaSerializer(ModelSerializer):
	class Meta:
		model = Idea 
		fields = '__all__'

class NewsSerializer(ModelSerializer):
	class Meta:
		model = News 
		fields = '__all__'

class AnnouncementSerializer(ModelSerializer):
	class Meta:
		model = Announcement 
		fields = '__all__'

		