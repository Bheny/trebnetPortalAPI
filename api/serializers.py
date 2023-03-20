from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(ModelSerializer):
	'''

	'''
	class Meta:
		model = User
		fields = ('id','password','username','first_name','last_name','email')

class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =('username',)


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


class RankSerializer(ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    user = SimpleUserSerializer()
    rank = RankSerializer()
    class Meta:
        model = Profile
        fields = ('id','image','location','balance','user','rank')


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

### Service Request serializers
class ServiceRequestSerializer(ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

class ServiceRequestDetailSerializer(ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        depth = 1

### Ends all affairs with service requests

class JobRequestSerializer(ModelSerializer):
    class Meta:
        model = JobRequest
        fields = '__all__'

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
