#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import * 
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@api_view(['POST'])
@csrf_exempt
def send_credits(request):
	print(dir(request.POST),request.POST)
	#senderId = request.POST
	#recieverId = request.POST.get('reciever')

	return Response()

class UserView(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()


class ProjectView(viewsets.ModelViewSet):
	serializer_class = ProjectSerializer
	queryset = Project.objects.all() 


class ProfileView(viewsets.ModelViewSet):
	serializer_class = ProfileSerializer  
	queryset = Profile.objects.all()

class TeamView(viewsets.ModelViewSet):
	serializer_class = TeamSerializer  
	queryset = Team.objects.all()

class JobView(viewsets.ModelViewSet):
	serializer_class = JobSerializer  
	queryset = Job.objects.all()

class TransactionView(viewsets.ModelViewSet):
	serializer_class = TransactionSerializer  
	queryset = Transaction.objects.all()

class EventView(viewsets.ModelViewSet):
	serializer_class = EventSerializer  
	queryset = Event.objects.all()

class QuestionView(viewsets.ModelViewSet):
	serializer_class = QuestionSerializer  
	queryset = Question.objects.all()

class IdeaView(viewsets.ModelViewSet):
	serializer_class = IdeaSerializer  
	queryset = Idea.objects.all()

class NewsView(viewsets.ModelViewSet):
	serializer_class = NewsSerializer  
	queryset = News.objects.all()

class AnnouncementView(viewsets.ModelViewSet):
	serializer_class = AnnouncementSerializer  
	queryset = Announcement.objects.all()
