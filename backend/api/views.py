#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .services import send_credits


class UserView(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()


class ProjectView(viewsets.ModelViewSet):
	serializer_class = ProjectSerializer
	queryset = Project.objects.all()


class ProfileView(viewsets.ModelViewSet):
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()


class ProfileDetailView(viewsets.ModelViewSet):
	"""


		Pass the profile ID to this URL ...
		/profile/detail/{profile_id}


	"""
	serializer_class = ProfileDetailSerializer
	queryset = Profile.objects.all()



class TeamView(viewsets.ModelViewSet):
	serializer_class = TeamSerializer
	queryset = Team.objects.all()

class JobView(viewsets.ModelViewSet):
	serializer_class = JobSerializer
	queryset = Job.objects.all()

# This view needs to check if the sender of the credits has the right priviledges to do so
# Also should allocate to the profiles of the accounts that have been specified.
# Subtraction of points from senders into the recievers too as well
class TransactionView(viewsets.ModelViewSet):
	"""
		A simple Viewset for listing or retrieving Transactions ..

		To Fetch Details

			/transaction/<id>/

			for example : To fetch item 13
			/transaction/13/

		To Update
			\t\tsend a formdata to using axios to the url
			/transaction/<id>/
	"""

	serializer_class = TransactionSerializer
	queryset = Transaction.objects.all()

	def create(self, request):
		serializer = TransactionSerializer(data=request.data)

		if serializer.is_valid():
			message = send_credits(int(request.data['amount']),request.data['sender'],request.data['reciever'])
			if message == "Successful":
				serializer.save()
				return Response(serializer.data)
			else:
				return Response({'message':message})

		return Response(serializer.errors)





class TransactionList(generics.ListCreateAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

	def list(self, request):
		#Note the use of ...
		queryset = self.get_queryset()
		serializer = TransactionSerializer(queryset, many=True)
		return Response(serializer.data)


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

class RankView(viewsets.ModelViewSet):
    serializer_class = RankSerializer
    queryset = Rank.objects.all()

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceRequestDetailView(viewsets.ModelViewSet):

    """


		Pass the profile ID to this URL ...
		/profile/detail/{profile_id}


	"""
    serializer_class = ServiceRequestDetailSerializer
    queryset = ServiceRequest.objects.all()

class NoteView(viewsets.ModelViewSet):
    serializer_class =  NoteSerializer
    queryset =  Note.objects.all()

class ServiceRequestView(viewsets.ModelViewSet):
    serializer_class =  ServiceRequestSerializer
    queryset =  ServiceRequest.objects.all()

class JobRequestView(viewsets.ModelViewSet):
    serializer_class = JobRequestSerializer
    queryset = JobRequest.objects.all()


